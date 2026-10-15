/**
 * 轻量交互基建
 *
 * 源站 74 个页面全是抓来的静态快照，没有脚本。这里补三件事：
 * 1. 登录态（localStorage），供登录 / 注册 / 昵称 / 安全密码等页面共用；
 * 2. Toast 提示，替代源站调用 uni.showToast 的行为；
 * 3. 手机号 / 密码 / 验证码的表单校验规则，登录与注册共用同一套。
 */
import { ref } from 'vue'

const LS_KEY = 'icard_auth'

function read() {
  try {
    return JSON.parse(localStorage.getItem(LS_KEY)) || null
  } catch {
    return null
  }
}

/** 当前登录用户，未登录为 null */
export const authUser = ref(read())

/** 是否已登录 */
export function isLogin() {
  return !!authUser.value
}

export function signIn(user) {
  authUser.value = user
  try {
    localStorage.setItem(LS_KEY, JSON.stringify(user))
  } catch { /* 隐私模式下写入失败时仅保留内存态 */ }
}

export function signOut() {
  authUser.value = null
  try {
    localStorage.removeItem(LS_KEY)
  } catch { /* 同上 */ }
}

/* ---------------------------------- Toast --------------------------------- */

let toastTimer = null

/** 顶部居中浮层提示，2 秒后自动消失 */
export function toast(text, ms = 2000) {
  let el = document.getElementById('__ic_toast__')
  if (!el) {
    el = document.createElement('div')
    el.id = '__ic_toast__'
    Object.assign(el.style, {
      position: 'fixed',
      left: '50%',
      top: '45%',
      transform: 'translate(-50%, -50%)',
      maxWidth: '78%',
      padding: '12px 20px',
      borderRadius: '10px',
      background: 'rgba(0,0,0,.82)',
      color: '#fff',
      fontSize: '14px',
      lineHeight: '20px',
      textAlign: 'center',
      zIndex: '99999',
      pointerEvents: 'none',
      backdropFilter: 'blur(6px)',
      transition: 'opacity .2s'
    })
    document.body.appendChild(el)
  }
  el.textContent = text
  el.style.opacity = '1'
  if (toastTimer) clearTimeout(toastTimer)
  toastTimer = setTimeout(() => { el.style.opacity = '0' }, ms)
}

/* --------------------------------- 校验规则 -------------------------------- */

export const PHONE_RE = /^1[3-9]\d{9}$/
export const PWD_MIN = 6

export function checkPhone(v) {
  const s = (v || '').trim()
  if (!s) return '请输入手机号'
  if (!/^\d+$/.test(s)) return '手机号只能包含数字'
  if (s.length !== 11) return '手机号需为 11 位'
  if (!PHONE_RE.test(s)) return '手机号格式不正确'
  return ''
}

export function checkPassword(v) {
  const s = v || ''
  if (!s) return '请输入密码'
  if (s.length < PWD_MIN) return `密码至少 ${PWD_MIN} 位`
  return ''
}

export function checkCode(v) {
  const s = (v || '').trim()
  if (!s) return '请输入验证码'
  if (!/^\d{6}$/.test(s)) return '验证码为 6 位数字'
  return ''
}

/** 登录 / 注册共用的演示账号（不校验真实后端） */
export const DEMO_PHONE = '13800138000'
export const DEMO_CODE = '123456'
export const DEMO_PWD = '123456'