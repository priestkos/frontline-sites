// Measures each page in headless Chrome over CDP. No dependencies: Node's global
// WebSocket plus the DevTools HTTP endpoint.
import { spawn } from 'node:child_process';
import {existsSync, mkdtempSync, readdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

function findChrome() {
  const direct = [
    process.env.CHROME_BIN,
    '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser',
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
    'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
    'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  ].filter(Boolean);
  for (const c of direct) if (existsSync(c)) return c;
  // Browser download caches (puppeteer / playwright), found without hardcoding a home path.
  const roots = [
    process.env.USERPROFILE && join(process.env.USERPROFILE, '.cache', 'puppeteer', 'chrome'),
    process.env.HOME && join(process.env.HOME, '.cache', 'puppeteer', 'chrome'),
    process.env.LOCALAPPDATA && join(process.env.LOCALAPPDATA, 'ms-playwright'),
  ].filter(Boolean);
  const subs = [
    'chrome-win64/chrome.exe', 'chrome-win32/chrome.exe',
    'chrome-linux64/chrome', 'chrome-linux/chrome',
    'chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing',
  ];
  for (const root of roots) {
    if (!existsSync(root)) continue;
    for (const entry of readdirSync(root)) {
      for (const sub of subs) {
        const p = join(root, entry, sub);
        if (existsSync(p)) return p;
      }
    }
  }
  return 'google-chrome';
}
const CHROME = findChrome();
const PORT = 9333;
const urls = process.argv.slice(2);

const profile = mkdtempSync(join(tmpdir(), 'cdp-'));
const chrome = spawn(CHROME, [
  '--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
  '--disable-extensions', '--hide-scrollbars', `--remote-debugging-port=${PORT}`,
  `--user-data-dir=${profile}`, 'about:blank',
], { stdio: 'ignore' });

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function endpoint() {
  for (let i = 0; i < 60; i++) {
    try {
      const r = await fetch(`http://127.0.0.1:${PORT}/json/list`);
      const list = await r.json();
      const page = list.find((t) => t.type === 'page');
      if (page?.webSocketDebuggerUrl) return page.webSocketDebuggerUrl;
    } catch { /* not up yet */ }
    await sleep(250);
  }
  throw new Error('devtools endpoint never came up');
}

const MEASURE = `(() => {
  const de = document.documentElement;
  const vis = (el) => { const s = getComputedStyle(el); return s.opacity !== '0' && s.visibility !== 'hidden'; };
  const charts = [...document.querySelectorAll('svg.chart-svg, svg.cs')].map((s) => {
    const r = s.getBoundingClientRect();
    return { w: Math.round(r.width), h: Math.round(r.height), paths: s.querySelectorAll('path').length };
  });
  const riseHidden = [...document.querySelectorAll('.rise')].filter((e) => !vis(e)).length;
  const blocks = [...document.querySelectorAll('.panel, .pan, .plate, .sec')];
  return JSON.stringify({
    title: document.title,
    h1: (document.querySelector('h1') || {}).textContent || null,
    overflowX: de.scrollWidth > innerWidth + 1,
    scrollW: de.scrollWidth, innerW: innerWidth, scrollH: de.scrollHeight,
    textChars: (document.body.innerText || '').length,
    headings: document.querySelectorAll('h1,h2,h3,h4').length,
    tables: document.querySelectorAll('table').length,
    svg: document.querySelectorAll('svg').length,
    canvas: document.querySelectorAll('canvas').length,
    canvasPainted: [...document.querySelectorAll('canvas')].map((c) => {
      try { const d = c.getContext('2d').getImageData(0, 0, Math.min(60, c.width), Math.min(60, c.height)).data;
        let lit = 0; for (let i = 3; i < d.length; i += 4) if (d[i] > 0) lit++; return lit; } catch (e) { return -1; }
    }),
    charts,
    riseHidden,
    blocksWithHeight: blocks.filter((b) => b.getBoundingClientRect().height > 40).length,
    blocksTotal: blocks.length,
    animatedPath: [...document.querySelectorAll('path[style*="stroke-dashoffset"]')].length
  });
})()`;

function rpc(ws, id, method, params = {}) {
  return new Promise((resolve) => {
    const onMsg = (ev) => {
      let m; try { m = JSON.parse(ev.data); } catch { return; }
      if (m.id === id) { ws.removeEventListener('message', onMsg); resolve(m); }
    };
    ws.addEventListener('message', onMsg);
    ws.send(JSON.stringify({ id, method, params }));
  });
}

const ws = new WebSocket(await endpoint());
await new Promise((res) => ws.addEventListener('open', res));

let id = 1;
await rpc(ws, id++, 'Page.enable');
await rpc(ws, id++, 'Runtime.enable');
const problems = [];
ws.addEventListener('message', (ev) => {
  let m; try { m = JSON.parse(ev.data); } catch { return; }
  if (m.method === 'Runtime.exceptionThrown') {
    problems.push('EXCEPTION ' + (m.params?.exceptionDetails?.text || '') + ' ' +
      (m.params?.exceptionDetails?.exception?.description || '').split('\n')[0]);
  }
  if (m.method === 'Runtime.consoleAPICalled' && ['error', 'warning'].includes(m.params.type)) {
    problems.push(m.params.type.toUpperCase() + ' ' + m.params.args.map((a) => a.value ?? a.description).join(' '));
  }
});

for (const url of urls) {
  const label = url.split('/').slice(-2).join('/');
  const nav = await rpc(ws, id++, 'Page.navigate', { url });
  await sleep(3800);
  const res = await rpc(ws, id++, 'Runtime.evaluate', {
    expression: MEASURE, returnByValue: true, awaitPromise: false,
  });
  let data = null;
  try { data = JSON.parse(res.result?.result?.value ?? 'null'); } catch { data = null; }
  console.log('\n=== ' + label);
  console.log(JSON.stringify(data, null, 1));
}

console.log('\n=== JS problems seen: ' + problems.length);
problems.slice(0, 14).forEach((p) => console.log('  ' + p));
ws.close();
chrome.kill();
process.exit(0);
