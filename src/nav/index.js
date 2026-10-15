import { IGNORE_SELECTORS, BACK_SELECTORS, NAV_RULES, LOGOUT_LABEL } from './rules'
import { signOut, toast } from '../utils/interact'

const BACK = Symbol('router.back')
const LOGOUT = Symbol('router.logout')
const MAX_DEPTH = 8

/** 命中任一选择器则该元素及其子树不参与拦截 */
const isIgnored = (node) =>
  IGNORE_SELECTORS.some((sel) => typeof node.matches === 'function' && node.matches(sel))

const safeMatch = (node, sel) => {
  try {
    return typeof node.matches === 'function' && node.matches(sel)
  } catch {
    return false
  }
}

/**
 * 从点击目标向上逐层回溯，返回 { kind: 'back' } 或目标路由路径。
 * 找不到则返回 null，表示这次点击不该被拦截。
 */
function resolveTarget(target) {
  let node = target

  for (let depth = 0; depth < MAX_DEPTH; depth++) {
    if (!node || node.nodeType !== 1) break
    if (node === document.body) break
    if (isIgnored(node)) return null

    // 1. 显式声明优先
    const explicit = node.getAttribute && node.getAttribute('data-nav-to')
    if (explicit) return explicit

    const explicitBack = node.getAttribute && node.getAttribute('data-nav-back')
    if (explicitBack !== null && explicitBack !== undefined) return BACK

    // 2. 返回键
    if (BACK_SELECTORS.some((sel) => safeMatch(node, sel))) return BACK

    // 3. 映射表
    for (const rule of NAV_RULES) {
      if (!safeMatch(node, rule.sel)) continue
      const to = typeof rule.to === 'function' ? rule.to(node) : rule.to
      if (to === LOGOUT_LABEL) return LOGOUT
      if (to) return to
    }

    node = node.parentElement
  }

  return null
}

/**
 * 安装全局点击导航。返回卸载函数。
 * 用捕获阶段监听，确保比页面内部处理更早生效，同时对未处理的点击零侵入。
 */
export function installNavDelegation(router) {
  if (typeof document === 'undefined') return () => {}

  const handler = (event) => {
    // 只响应左键 / 触摸
    if (event.button !== undefined && event.button !== 0) return
    // 文本选中的拖拽不触发跳转
    if (typeof window.getSelection === 'function') {
      const sel = window.getSelection()
      if (sel && String(sel).trim().length > 0) return
    }

    const target = resolveTarget(event.target)
    if (!target) return

    if (typeof event.preventDefault === 'function') event.preventDefault()
    if (typeof event.stopPropagation === 'function') event.stopPropagation()

    if (target === BACK) {
      router.back()
      return
    }

    if (target === LOGOUT) {
      signOut()
      toast('已退出登录')
      router.replace('/pages/home/home')
      return
    }

    const current = router.currentRoute.value
    if (current && current.fullPath === target) return
    router.push(target)
  }

  document.addEventListener('click', handler, true)

  return () => document.removeEventListener('click', handler, true)
}