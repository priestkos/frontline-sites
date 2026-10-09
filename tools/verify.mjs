// Verifies both sites: un-hides every tab panel, forces reveals, measures chart
// geometry and canvas paint coverage, captures a hero screenshot. CDP over Node's
// global WebSocket, no dependencies.
import { spawn } from 'node:child_process';
import { mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const CHROME = process.env.CHROME_BIN || [
  '/usr/bin/google-chrome', '/usr/bin/chromium',
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
].find((p) => { try { return require('node:fs').existsSync(p); } catch { return false; } }) || 'google-chrome';
const PORT = 9334;
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const profile = mkdtempSync(join(tmpdir(), 'cdp2-'));
const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', '--no-first-run',
  '--hide-scrollbars', `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`,
  '--window-size=1440,900', 'about:blank'], { stdio: 'ignore' });

async function wsUrl() {
  for (let i = 0; i < 80; i++) {
    try {
      const list = await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json();
      const p = list.find((t) => t.type === 'page');
      if (p?.webSocketDebuggerUrl) return p.webSocketDebuggerUrl;
    } catch {}
    await sleep(250);
  }
  throw new Error('no devtools endpoint');
}

const PREP = `(() => {
  document.querySelectorAll('[hidden]').forEach(e => e.removeAttribute('hidden'));
  document.querySelectorAll('.rise').forEach(e => e.classList.add('in'));
  return 1; })()`;

const MEASURE = `(() => {
  const de = document.documentElement;
  const charts = [...document.querySelectorAll('svg.chart-svg, svg.cs')].slice(0, 6).map((s) => {
    const r = s.getBoundingClientRect();
    const paths = [...s.querySelectorAll('path')].map(p => Math.round(p.getBoundingClientRect().width));
    return { w: Math.round(r.width), h: Math.round(r.height), paths, widest: Math.max(0, ...paths) };
  });
  const canvasPaint = [...document.querySelectorAll('canvas')].map((c) => {
    let lit = 0;
    try {
      const ctx = c.getContext('2d');
      for (let i = 1; i <= 4; i++) for (let j = 1; j <= 4; j++) {
        const x = Math.max(0, Math.floor(c.width * i / 5) - 20), y = Math.max(0, Math.floor(c.height * j / 5) - 20);
        const d = ctx.getImageData(x, y, 40, 40).data;
        for (let k = 3; k < d.length; k += 4) if (d[k] > 0) lit++;
      }
    } catch (e) { return { err: String(e) }; }
    return { w: c.width, h: c.height, litPixels: lit };
  });
  const hiddenLeft = [...document.querySelectorAll('.rise')]
    .filter(e => getComputedStyle(e).opacity === '0').length;
  return JSON.stringify({
    title: document.title,
    overflowX: de.scrollWidth > innerWidth + 1,
    scrollW: de.scrollWidth, innerW: innerWidth, scrollH: de.scrollHeight,
    textChars: (document.body.innerText || '').length,
    headings: document.querySelectorAll('h1,h2,h3,h4').length,
    tables: document.querySelectorAll('table').length,
    tableRows: document.querySelectorAll('table tr').length,
    codeBlocks: document.querySelectorAll('pre').length,
    svg: document.querySelectorAll('svg').length,
    charts, canvasPaint, hiddenLeft
  });
})()`;

const ws = new WebSocket(await wsUrl());
await new Promise((r) => ws.addEventListener('open', r));
let id = 1;
const rpc = (method, params = {}) => new Promise((resolve) => {
  const myId = id++;
  const on = (ev) => { let m; try { m = JSON.parse(ev.data); } catch { return; }
    if (m.id === myId) { ws.removeEventListener('message', on); resolve(m); } };
  ws.addEventListener('message', on);
  ws.send(JSON.stringify({ id: myId, method, params }));
});
await rpc('Page.enable'); await rpc('Runtime.enable');
const problems = [];
ws.addEventListener('message', (ev) => {
  let m; try { m = JSON.parse(ev.data); } catch { return; }
  if (m.method === 'Runtime.exceptionThrown') problems.push('EXCEPTION ' + (m.params?.exceptionDetails?.text || ''));
  if (m.method === 'Runtime.consoleAPICalled' && m.params.type === 'error')
    problems.push('CONSOLE ' + m.params.args.map((a) => a.value ?? a.description).join(' '));
});

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const targets = ['woodblock-codex', 'plotting-table']
  .map((d) => [pathToFileURL(join(REPO, d, 'index.html')).href, join(REPO, d, 'preview.png')]);
for (const [url, shot] of targets) {
  await rpc('Page.navigate', { url });
  await sleep(3400);
  await rpc('Runtime.evaluate', { expression: PREP, returnByValue: true });
  await sleep(1400);                       // let counters + chart animations run
  const r = await rpc('Runtime.evaluate', { expression: MEASURE, returnByValue: true });
  let data = null; try { data = JSON.parse(r.result?.result?.value ?? 'null'); } catch {}
  console.log('\n=== ' + url.split('/').slice(-2)[0]);
  console.log(JSON.stringify(data, null, 1));
  const cap = await rpc('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
  if (cap.result?.data) { writeFileSync(shot, Buffer.from(cap.result.data, 'base64')); console.log('screenshot -> ' + shot); }
}
console.log('\nJS problems: ' + problems.length); problems.slice(0, 10).forEach((p) => console.log('  ' + p));
ws.close(); chrome.kill(); process.exit(0);
