/**
 * 全站点击导航规则表
 *
 * 站点里74 个页面组件都是抓取来的静态 HTML，没有 @click / <a>，
 * 因此统一用「事件委托 + 选择器映射」的方式补上跳转能力。
 *
 * 规则匹配方式：从点击目标向上逐层找祖先，
 * 每层先看 data-nav-to 显式属性 → 再看返回键 → 再看下面这张表，
 * 因此「越靠近点击处的元素优先级越高」。
 */

/** 这些区域自带处理逻辑（TabBar 切换、导航栏返回），一律不拦截 */
export const IGNORE_SELECTORS = [
  '.uni-page-head',   // PageHead.vue 自己处理返回
  '.tabbar',
  '.tabbaritem'
]

/** 命中即 router.back() */
export const BACK_SELECTORS = [
  '.back-btn',
  '.header-back',
  '.nav-back',
  '.cuIcon-back',
  '.cuIcon-backfill',
  '.action.back'
]

/**
 * 按可见文案派生的路由表。
 * 之所以用文案而不是 nth-child，是因为静态快照里同一class 出现多次，
 * 只有文案能区分「首发 / 市场 / 求购 / 委托」这类并列入口。
 *
 * 文案里的空格、全角空格都已剔除，匹配前会统一压缩。
 */
export const LOGOUT_LABEL = '退出登录'

const TEXT_ROUTES = [
  // 我的页 —— 订单四宫格
  ['首发', '/pages/account/orderList'],
  ['市场', '/pages/account/marketOrderList'],
  ['求购', '/pages/account/bidList'],
  ['委托', '/pages/entrust/entrust'],

  // 我的页 —— 设置列表
  ['账号安全', '/pages/account/safePass'],
  ['我的钱包', '/pages/wallet/wallet'],
  ['我的收藏', '/pages/account/other'],
  ['收藏记录', '/pages/account/open'],
  ['关于平台', '/pages/account/about'],
  ['我的地址', '/pages/address/address'],

  // 命中即登出（值用自身作为标记，由 nav/index.js 走特殊分支）
  [LOGOUT_LABEL, LOGOUT_LABEL]
]

/** 长文案优先，避免「我的钱包」被短词「钱包」抢先命中 */
const TEXT_ROUTES_LONGEST_FIRST = TEXT_ROUTES.slice().sort((a, b) => b[0].length - a[0].length)

const text2route = (node) => {
  const raw = (node.innerText || node.textContent || '').trim()
  if (!raw) return null
  // 单元格文案可能带空格、换行或夹杂图标文本，先压缩再比对
  const norm = raw.replace(/\s+/g, '')
  if (!norm) return null
  // 第一轮：完全相等
  for (const [label, to] of TEXT_ROUTES) {
    if (norm === label) return to
  }
  // 第二轮：包含匹配（父节点会把图标/副标题文案一起算进来）
  for (const [label, to] of TEXT_ROUTES_LONGEST_FIRST) {
    if (label.length >= 3 && norm.includes(label)) return to
  }
  return null
}

/**
 * 选择器 → 路由。数组顺序即同层优先级。
 * to 也可以是 (node) => string | null，用于动态判定。
 */
export const NAV_RULES = [
  // 首页：商品瀑布流卡片 → 藏品详情（含挂单列表、快捷购买）
  { sel: '.waterfall-item', to: (node) => '/pages/market/details?id=' + (node.getAttribute('data-id') || '') },

  // 首页：公告轮播条 → 公告详情
  { sel: '.notice-swiper-item', to: '/pages/notification/details' },

  // 市场：列表行 / 表格行 → 藏品详情
  { sel: '.market-table-row', to: (node) => '/pages/market/details?id=' + (node.getAttribute('data-id') || '') },
  { sel: '.market-list-thumb', to: (node) => { const row = node.closest('.market-table-row'); return '/pages/market/details?id=' + (row && row.getAttribute('data-id') || '') } },
  { sel: '.grid-card', to: (node) => '/pages/market/details?id=' + (node.getAttribute('data-id') || '') },

  // 公告：公告卡片 → 公告详情
  { sel: '.notice-card', to: '/pages/notification/details' },

  // 我的页：订单四宫格 + 设置列表（按文案分发）
  { sel: '.trade-item', to: text2route },
  { sel: '.trade-all', to: '/pages/account/orderList' },
  { sel: '.menu-item', to: text2route },

  // 详情类页面里的相关条目
  { sel: '.relative-notice-item', to: '/pages/notification/details' },
  { sel: '.consign-item', to: '/pages/market/sale' }
]

/**
 * 未接入跳转的已知入口，保留记录以便后续接数据后补上。
 *
 * - .quick-card（合成页 4 个纯图入口，源站快照里没有文案，无法判断目标）
 * - .activity-card（精彩合成活动卡，目标依赖活动 ID）
 * - 首页 banner / swiper（运营位，跳转目标由后台配置）
 * - market 详情页的「寄售 / 求购 / 委托」按钮（需要藏品 ID 与登录态）
 */
export const UNMAPPED_NOTE = [
  '.quick-card',       // 活动页入口，已改用 data-nav-to 显式声明
  '.activity-card',    // 活动卡片，源站无明确目标路由
  '.swiper-item',      // 轮播项，需结合运营配置才能确定目标
  '.category-tab',     // 市场页子 Tab，已改为页内 v-model 筛选
  '.sub-tag-chip'      // 市场页推荐标签，已改为页内筛选
]