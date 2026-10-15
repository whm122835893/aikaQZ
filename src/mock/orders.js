/**
 * 订单数据（三类订单页共用）
 *
 * 覆盖：首发订单 / 常规交易 / 求购订单 / 委托订单 / 盲盒订单，
 * 每单带type + status 两个维度，页面按当前 Tab 组合过滤。
 */

export const ORDER_TYPES = ['首发订单', '常规交易', '求购订单', '委托订单', '盲盒订单']

/** 统一的 status 词表，三类页面各自取用其中一部分 */
export const UNPAID = '待付款'
export const PAID = '已支付'
export const CLOSED = '已关闭'
export const CANCELED = '订单取消'
export const DONE = '已成交'
export const SOLD = '已售出'
export const BIDDING = '求购中'
export const SHIPPED = '待发货'
export const RECEIVED = '已收货'

const NAMES = [
  '艾卡德·星际远征', '艾卡德·国潮之光', '像素方块·典藏', '山海经·灵兽录',
  '赛博机甲·Genesis', '敦煌飞天·限量', '未来城市·夜景', '春山可望·系列一',
  '山海经·神兽册', '星际拾荒者', '幻境花园', '机械纪元·Genesis X',
  '青绿千里·宋画', '夏日花火', '神兽现世·贰'
]

/** [type, status, price, time] */
const SEED = [
  ['首发订单', UNPAID, 19.0, '2026-09-18 10:10'],
  ['首发订单', PAID, 88.0, '2026-09-17 15:32'],
  ['首发订单', PAID, 128.0, '2026-09-15 09:05'],
  ['首发订单', CANCELED, 19.0, '2026-09-12 20:41'],
  ['首发订单', PAID, 66.0, '2026-09-10 14:20'],
  ['首发订单', UNPAID, 39.0, '2026-09-08 11:11'],

  ['常规交易', UNPAID, 45.0, '2026-09-19 08:44'],
  ['常规交易', PAID, 120.0, '2026-09-18 19:03'],
  ['常规交易', PAID, 268.0, '2026-09-16 16:48'],
  ['常规交易', CLOSED, 45.0, '2026-09-14 13:27'],
  ['常规交易', SHIPPED, 88.0, '2026-09-11 10:02'],
  ['常规交易', PAID, 156.0, '2026-09-06 17:39'],

  ['求购订单', BIDDING, 30.0, '2026-09-19 12:00'],
  ['求购订单', BIDDING, 52.0, '2026-09-18 12:00'],
  ['求购订单', DONE, 30.0, '2026-09-13 21:15'],
  ['求购订单', CLOSED, 52.0, '2026-09-09 09:26'],
  ['求购订单', DONE, 75.0, '2026-09-02 18:40'],

  ['委托订单', BIDDING, 66.0, '2026-09-19 09:30'],
  ['委托订单', SOLD, 66.0, '2026-09-07 22:18'],
  ['委托订单', CLOSED, 41.0, '2026-09-04 14:52'],
  ['委托订单', DONE, 98.0, '2026-08-28 10:07'],

  ['盲盒订单', PAID, 25.0, '2026-09-19 16:20'],
  ['盲盒订单', PAID, 25.0, '2026-09-15 16:20'],
  ['盲盒订单', CANCELED, 25.0, '2026-09-11 16:20'],
  ['盲盒订单', RECEIVED, 35.0, '2026-09-01 16:20']
]

export const ORDERS = SEED.map((s, i) => {
  const [type, status, price, time] = s
  const n = i % NAMES.length
  return {
    id: 10000 + i,
    no: 'IC' + String(20260900000 + i * 137),
    type,
    status,
    name: NAMES[n],
    token: 1000 + ((i * 37) % 9000),
    price: price.toFixed(2),
    time,
    qty: (i % 3) + 1
  }
})

/** 按 type + status 列表过滤；statuses 为空表示全部 */
export function pickOrders(type, statuses) {
  const want = Array.isArray(statuses) ? statuses.filter(Boolean) : []
  return ORDERS.filter((o) => {
    if (type && o.type !== type) return false
    if (!want.length) return true
    return want.includes(o.status)
  })
}
/* ===== 实物订单（PhysicalOrderList 页专用）=====
   源站该页为纯静态空壳（只有 tab 骨架 + 「暂无数据」占位），
   这里补 12 条演示数据，覆盖 购买 / 托管 / 寄售 三类 × 四种状态。 */
export const PHYSICAL = ['实物购买', '实物托管', '实物寄售']

const P_NAMES = [
  '爱卡·盲盒公仔（限量版）',
  'ICARD 金属会员徽章',
  '山海经·神兽册页册',
  '赛博机甲 Genesis |Ver.2',
  '国潮之美·非遗折扇',
  '像素方块·典藏套装',
  '爱卡联名·帆布托特包',
  '文卡德·星际远征手办'
]
const P_SPEC = ['标准版', '典藏版', '豪华版', '编号版']

const P_SEED = [
  ['实物购买', UNPAID, 299, '2026-09-19 10:24'],
  ['实物购买', PAID, 599, '2026-09-18 15:02'],
  ['实物购买', PAID, 1299, '2026-09-15 09:41'],
  ['实物购买', CANCELED, 199, '2026-09-11 20:18'],
  ['实物托管', PAID, 88, '2026-09-17 11:35'],
  ['实物托管', UNPAID, 158, '2026-09-16 08:50'],
  ['实物托管', PAID, 268, '2026-09-08 17:20'],
  ['实物寄售', PAID, 328, '2026-09-14 14:12'],
  ['实物寄售', SOLD, 688, '2026-09-06 10:05'],
  ['实物寄售', PAID, 128, '2026-09-02 19:30'],
  ['实物寄售', CANCELED, 458, '2026-08-29 13:44'],
  ['实物托管', CANCELED, 118, '2026-08-22 16:08']
]

export const PHYSICAL_ORDERS = P_SEED.map((s, i) => {
  const [type, status, price, time] = s
  return {
    id: 20000 + i,
    no: 'IC' + String(20260910000 + i * 211),
    type,
    status,
    name: P_NAMES[i % P_NAMES.length],
    spec: P_SPEC[i % P_SPEC.length],
    image: '/static/images/goods/' + ((i % 6) + 1) + '.jpg',
    price: price.toFixed(2),
    time,
    qty: (i % 2) + 1
  }
})

/** 实物订单页：主 tab（全部/购买/托管/寄售）× 子 tab（全部/待付款/已支付/订单取消）双向过滤 */
export function pickPhysical(type, statuses) {
  const want = Array.isArray(statuses) ? statuses.filter(Boolean) : []
  return PHYSICAL_ORDERS.filter((o) => {
    if (type && type !== '全部' && o.type !== type) return false
    if (!want.length) return true
    return want.includes(o.status)
  })
}
