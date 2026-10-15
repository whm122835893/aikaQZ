/** 全量 SFC 体检：parse + compileTemplate + compileScript */
import { readFileSync, readdirSync, statSync } from 'node:fs'
import { join } from 'node:path'
import { createRequire } from 'node:module'

const require = createRequire(import.meta.url)
const sfc = require('../node_modules/.pnpm/@vue+compiler-sfc@3.5.43/node_modules/@vue/compiler-sfc/dist/compiler-sfc.cjs.js')

function walk(dir, out = []) {
  for (const n of readdirSync(dir)) {
    const p = join(dir, n)
    if (statSync(p).isDirectory()) walk(p, out)
    else if (p.endsWith('.vue')) out.push(p)
  }
  return out
}

const files = walk('src/views').sort()
const bad = []

for (const p of files) {
  const src = readFileSync(p, 'utf-8')
  let res = null
  try {
    res = sfc.parse(src, { filename: p })
  } catch (e) {
    bad.push([p, 'parse: ' + String(e).slice(0, 300)])
    continue
  }
  // 3.5.x 的 parse 返回 { descriptor, errors }
  const d = res.descriptor || res
  const errs = [...(res.errors || []), ...(d.errors || [])]
  if (!d.template) errs.push('template missing')
  else {
    try {
      const r = sfc.compileTemplate({ source: d.template.content, filename: p, id: 'x' })
      errs.push(...(r.errors || []))
    } catch (e) { errs.push('compileTemplate: ' + String(e).slice(0, 300)) }
  }
  if (d.scriptSetup) {
    try { sfc.compileScript(d, { id: 'x' }) }
    catch (e) { errs.push('compileScript: ' + String(e).slice(0, 300)) }
  }
  if (errs.length) bad.push([p, errs.map(String).join(' | ').slice(0, 400)])
}

console.log('scanned ' + files.length + ' files')
if (bad.length) {
  console.log('BROKEN ' + bad.length + ':')
  for (const [p, e] of bad) console.log(' - ' + p + ' => ' + e)
  process.exit(1)
}
console.log('all SFC OK')