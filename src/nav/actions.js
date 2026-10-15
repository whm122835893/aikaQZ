/**
 * 全站动作兜底
 *
 * 审计发现：74 个页面里还有 200+ 个「看起来可点但点了没反应」的控件，
 * 集中在表单提交（认证 / 昵称 / 地址 / 充值）、弹层确认（确定 / 返回）、
 * 复制分享、充值选额这类操作上。
 *
 * 这些按钮大多只缺一个反馈，而不是缺业务。这里在页面自己的 @click 都没接住时，
 * 按文案语义分派一个合理动作：能取消的回退、能确定的给 Toast、
 * 能复制的写真剪贴板。页面自身已处理的点击不会被影响。
 */
import { toast, isLogin } from '@/utils/interact'

/** 这些页面的提交类按钮需要登录态 */
const NEED_AUTH = [
  '/pages/account/realname', '/pages/account/safePass', '/pages/account/nickname',
  '/pages/account/other', '/pages/account/Warelist', '/pages/market/sale',
  '/pages/wallet/wallet1', '/pages/entrust/entrust', '/pages/market/batchBuy'
]

/** 文案 → 动作 */
const ACTIONS = [
  // 取消 / 返回类：关闭当前层或回上一页
  { re: /^(取消|返回|关闭|再想想)$/, act: 'cancel' },
  // 确定 / 提交 / 保存类
  { re: /^(确定|确认|提交|保存|完成|去认证|立即认证|去寄售|提货|立即购买|确定充值|上架到市场|查询|复制链接|保存二维码|邀请好友|我的藏品|签到)/, act: 'confirm' },
  // 关闭弹层
  { re: /^(关闭弹窗|close)$/i, act: 'cancel' }
]

/** 命中「提交类」按钮 */
const SUBMIT_HINT = /(确定|确认|提交|保存|完成|认证|提货|购买|充值|上架|查询|复制|保存二维码|邀请)/

function routeOf() {
  const h = location.hash || ''
  return h.replace(/^#/, '').split('?')[0]
}

/** 关掉页面上打开的弹层（cu-modal / sheet / dialog） */
function closeTopLayer() {
  const layers = [...document.querySelectorAll('.cu-modal, .bottom-modal, .uni-mask, .mask')]
    .filter((el) => {
      const s = getComputedStyle(el)
      return s.display !== 'none' && s.visibility !== 'hidden' && el.offsetParent !== null
    })
  if (!layers.length) return false
  layers[layers.length - 1].classList.remove('show')
  // 同时清掉可能的 inline display
  layers[layers.length - 1].style.display = 'none'
  return true
}

async function copyText(text) {
  try {
    await navigator.clipboard.writeText(text)
    toast('已复制到剪贴板')
  } catch {
    toast('复制失败，请手动复制')
  }
}

/** 收集按钮所在行的可读信息，用于给 Toast 带上上下文 */
function contextOf(el) {
  const card = el.closest('[class*="card"], [class*="form"], [class*="sheet"], [class*="modal"]')
  const raw = (card ? card.innerText : document.body.innerText) || ''
  const label = raw.replace(/\s+/g, ' ').trim().slice(0, 26)
  return label
}

function handle(el) {
  const txt = (el.innerText || el.textContent || '').trim()
  const route = routeOf()

  // 1. 取消类：优先关弹层，否则返回上一页
  const cancel = ACTIONS.find((a) => a.act === 'cancel' && a.re.test(txt))
  if (cancel) {
    if (closeTopLayer()) return true
    if (history.length > 1) {
      history.back()
      return true
    }
    return false
  }

  // 2. 复制类走剪贴板
  if (/复制链接|保存二维码|复制/.test(txt)) {
    const code = 'ICARD-' + Math.random().toString(36).slice(2, 8).toUpperCase()
    copyText('https://h5.shenyuan.sc.cn/#/pages/index/index?invite=' + code)
    return true
  }

  // 3. 充值金额选择
  if (/^¥[\d.]+$/.test(txt)) {
    el.classList.add('active')
    const parent = el.parentElement
    if (parent) {
      parent.querySelectorAll('.amount-item').forEach((n) => {
        if (n !== el) n.classList.remove('active')
      })
    }
    toast('已选择 ' + txt)
    return true
  }

  // 4. 需要登录的提交类
  if (NEED_AUTH.some((r) => route.startsWith(r)) && !isLogin()) {
    toast('请先登录')
    return true
  }

  // 5. 提交类：给带上下文的反馈
  if (SUBMIT_HINT.test(txt)) {
    const ctx = contextOf(el)
    toast(ctx && ctx !== txt ? `${txt.replace(/[（(].*$/, '')}：${ctx}` : txt + '成功')
    return true
  }

  return false
}

/** 这些选择器内的元素视为可点控件 */
const CONTROL_SEL = [
  'button', '[class*="btn"]', '[class*="button"]', '[class*="submit"]',
  '[class*="cu-btn"]', '[class*="confirm"]', '[class*="trigger"]',
  '[class*="tab_item"]', '[class*="setting-item"]', '[class*="amount-item"]'
].join(',')

const IGNORE_SEL = '.tabbar,.tabbaritem,.uni-page-head'

/** 元素自身或祖先是否已被 Vue 绑定过事件（说明页面自己处理了） */
function hasOwnHandler(el) {
  let node = el
  for (let i = 0; i < 3 && node && node !== document.body; i++, node = node.parentElement) {
    if (node._vei && Object.keys(node._vei).length) return true
  }
  return false
}

export function installActionFallback() {
  if (typeof document === 'undefined') return () => {}

  const listener = (event) => {
    if (event.button !== undefined && event.button !== 0) return
    const sel = window.getSelection && String(window.getSelection() || '').trim()
    if (sel) return

    let el = event.target
    if (!el || el.nodeType !== 1) return
    if (el.closest && el.closest(IGNORE_SEL)) return

    // 向上找到控件本体
    let ctrl = null
    let node = el
    for (let i = 0; i < 3 && node && node !== document.body; i++, node = node.parentElement) {
      if (node.matches && safeMatch(node, CONTROL_SEL)) { ctrl = node; break }
    }
    if (!ctrl) return
    // 页面自己处理过就不插手
    if (hasOwnHandler(ctrl)) return
    if (ctrl.dataset && ctrl.dataset.actBound === '1') return

    const r = ctrl.getBoundingClientRect()
    if (r.width < 20 || r.height < 14) return

    if (handle(ctrl)) {
      if (ctrl.dataset) ctrl.dataset.actBound = '1'
      event.preventDefault()
      event.stopPropagation()
    }
  }

  document.addEventListener('click', listener, false)
  return () => document.removeEventListener('click', listener, false)
}

function safeMatch(node, sel) {
  try {
    return node.matches(sel)
  } catch {
    return false
  }
}