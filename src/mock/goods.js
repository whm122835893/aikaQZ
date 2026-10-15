/**
 * 市场藏品共享数据
 *
 * Market.vue 与 Details.vue / GoodsDetails.vue 共用同一份藏品数据，
 * 这样从列表点进详情时，两边展示的名称、价格、成交数据是一致的。
 */

export const GOODS = [
  {
    id: 'g001', name: '国潮之光', img: '/upload/a78f2138480a3638e085dee9e4f3e693265faa7a.jpg',
    issued: 1000, circ: 960, floor: 156.0, vol: 52, fav: true,
    author: 'ICARD原创', series: '奶奶有道理系列', desc: '以国潮元素重构的经典IP藏品，全系列限量发行。',
    holder: 86, listed: 12, bids: 8
  },
  {
    id: 'g002', name: '像素方块', img: '/upload/4a5cec899296b7a17ff7277dfcaeafa51f7673f8.png',
    issued: 1500, circ: 1400, floor: 210.0, vol: 48, fav: true,
    author: '像素工坊', series: '方块宇宙', desc: '8-bit 复古风格，每一枚方块都是独一无二的编号。',
    holder: 92, listed: 6, bids: 15
  },
  {
    id: 'g003', name: '潮流限定', img: '/upload/a78f2138480a3638e085dee9e4f3e693265faa7a.jpg',
    issued: 2000, circ: 1900, floor: 128.0, vol: 35, fav: true,
    author: 'ICARD联名', series: '潮流联名', desc: '潮流跨界联名款，含限量编号与专属铭牌。',
    holder: 79, listed: 18, bids: 11
  },
  {
    id: 'g004', name: '雪山牦牛', img: '/upload/194d693b5e364b79c16bb647807972341d4e5744.png',
    issued: 2500, circ: 2400, floor: 76.8, vol: 18, fav: true,
    author: '高原计划', series: '秘境系列', desc: '取自青藏高原的雪域意象，配以手工上色工艺。',
    holder: 68, listed: 21, bids: 6
  },
  {
    id: 'g005', name: '运粮鼠', img: '/upload/c7d5b6506317d71aefb74c98ef2d7219e116d772.jpg',
    issued: 3000, circ: 3000, floor: null, vol: 1, fav: true,
    author: 'ICARD原创', series: '动物寓言', desc: '以寓言为底本的生肖系列作品，全额流通。',
    holder: 54, listed: 0, bids: 3
  },
  {
    id: 'g006', name: '萌宠日常', img: '/upload/eac7b7d495b9f1a16d1a6cdc9142feb9db7d197f.png',
    issued: 4500, circ: 3900, floor: 31.5, vol: 8, fav: false,
    author: '萌宠工坊', series: '日常记录', desc: '记录普通生活的温暖瞬间，适合作为入门藏品。',
    holder: 47, listed: 14, bids: 5
  },
  {
    id: 'g007', name: '藏獒卫士', img: '/upload/014670993c94be10445946388f2b610062dfa5b4.png',
    issued: 5000, circ: 4200, floor: 24.6, vol: 6, fav: false,
    author: '高原计划', series: '秘境系列', desc: '高原守护者的设计与传说故事结合。',
    holder: 43, listed: 11, bids: 4
  },
  {
    id: 'g008', name: '街头涂鸦王', img: '/upload/45c0ec9b95b85006375bdfe673239b0752cca05c.png',
    issued: 6000, circ: 5800, floor: 58.0, vol: 21, fav: true,
    author: '街头艺术', series: '城市涂鸦', desc: '把街头涂鸦搬上链，每一枚都有独立编号。',
    holder: 71, listed: 26, bids: 9
  },
  {
    id: 'g009', name: '机甲武士', img: '/upload/a18237a80fad69667669015f27a189561f47d47f.jpg',
    issued: 7000, circ: 6900, floor: 88.0, vol: 16, fav: true,
    author: '重工机械', series: '未来纪元', desc: '重型机甲设定，关节处采用可动结构设计。',
    holder: 64, listed: 19, bids: 7
  },
  {
    id: 'g010', name: '星际指挥官', img: '/upload/f6746c2b2cf5254376c8958f1bc8780955ae168c.png',
    issued: 8000, circ: 7600, floor: 36.5, vol: 12, fav: true,
    author: '深空工作室', series: '星际纪元', desc: '星际巡航指挥官的形象设计与角色档案。',
    holder: 58, listed: 16, bids: 10
  },
  {
    id: 'g011', name: '青铜面具', img: '/upload/2fa0e35b68000d5aa6a869c4513d4f537ef5eaf0.png',
    issued: 9000, circ: 8600, floor: 42.0, vol: 14, fav: true,
    author: '青铜纪', series: '文明遗存', desc: '取材于青铜器纹样，附赠编号证书。',
    holder: 61, listed: 13, bids: 12
  },
  {
    id: 'g012', name: '拳击小子001', img: '/upload/a2ff31cdf75776b14e0874c6ac449ac18d54536e.png',
    issued: 12000, circ: 500, floor: null, vol: 0, fav: true,
    author: 'ICARD原创', series: '运动系列', desc: '首发编号藏品，后续发行量待揭晓。',
    holder: 12, listed: 0, bids: 0
  },
  {
    id: 'g013', name: '齐天大圣', img: '/upload/d81c74c15ff10ecb194c79b63c56987c8b89f038.png',
    issued: 12000, circ: 9000, floor: null, vol: 9, fav: false,
    author: '西游纪', series: '东方神话', desc: '取自东方神话中的经典形象重塑。',
    holder: 38, listed: 4, bids: 6
  },
  {
    id: 'g014', name: '深海猎人', img: '/upload/ab284b9f1c4cac8eec22e8c9a30cf62ed9bac28d.png',
    issued: 15000, circ: 3200, floor: null, vol: 3, fav: false,
    author: '深空工作室', series: '海洋纪元', desc: '深海探险者系列首章。',
    holder: 26, listed: 2, bids: 2
  },
  {
    id: 'g015', name: '未来港湾', img: '/upload/fde3e9210841133dc8ad445ba020d08a81303a06.png',
    issued: 22000, circ: 15500, floor: 15.2, vol: 13, fav: true,
    author: '深空工作室', series: '未来纪元', desc: '悬浮于云端的城市群落设定集。',
    holder: 52, listed: 24, bids: 8
  },
  {
    id: 'g016', name: '花样蝶自来', img: '/upload/87f1615abb555956911f888aea806b7403685231.jpg',
    issued: 20000, circ: 20000, floor: 12.8, vol: 4, fav: false,
    author: 'ICARD原创', series: '奶奶有道理系列', desc: '全额流通的系列作品，适合低门槛入手。',
    holder: 45, listed: 9, bids: 5
  },
  {
    id: 'g017', name: '机械纪元', img: '/upload/3df504960e882648dc0b96be33fadf1aeb059ec4.jpg',
    issued: 40000, circ: 21000, floor: 8.5, vol: 26, fav: false,
    author: '重工机械', series: '未来纪元', desc: '机械文明兴衰史的宏大叙事。',
    holder: 34, listed: 28, bids: 7
  },
  {
    id: 'g018', name: '国风仕女', img: '/upload/9927ec172e23d48dc113f6d091ff42a8c2d7be8b.png',
    issued: 35000, circ: 30000, floor: 6.6, vol: 9, fav: false,
    author: '青铜纪', series: '东方美学', desc: '传统工笔与现代审美的结合。',
    holder: 31, listed: 17, bids: 4
  },
  {
    id: 'g019', name: '艾卡德-学习', img: '/upload/861bfe33d903a1fc7808f503e302b14e77f07ce1.png',
    issued: 50000, circ: 8890, floor: null, vol: 0, fav: true,
    author: 'ICARD原创', series: '艾卡德系列', desc: '平台早期作品，流通量低于发行量。',
    holder: 19, listed: 0, bids: 0
  },
  {
    id: 'g020', name: '未来机甲', img: '/upload/3cdf6d1069191c8eb66b0185572abe9fa4ceb934.jpg',
    issued: 30000, circ: 12000, floor: null, vol: 7, fav: false,
    author: '重工机械', series: '未来纪元', desc: '通用型机甲的量产版设定。',
    holder: 29, listed: 6, bids: 3
  },
  {
    id: 'g021', name: '山海经卷', img: '/upload/a78f2138480a3638e085dee9e4f3e693265faa7a.jpg',
    issued: 60000, circ: 28000, floor: 3.8, vol: 31, fav: false,
    author: '青铜纪', series: '东方神话', desc: '按山海经顺序逐一成卷的系列企划。',
    holder: 25, listed: 30, bids: 6
  },
  {
    id: 'g022', name: '艾卡德-战斗', img: '/upload/861bfe33d903a1fc7808f503e302b14e77f07ce1.png',
    issued: 26000, circ: 13400, floor: null, vol: 5, fav: false,
    author: 'ICARD原创', series: '艾卡德系列', desc: '艾卡德系列的战斗形态衍生作品。',
    holder: 22, listed: 3, bids: 2
  }
]

/** 挂单（出售）流水，价格带围绕地板价波动 */
export const MAKING_LIST = (g) => {
  if (g.floor == null) return []
  const rows = []
  for (let i = 0; i < Math.min(g.listed, 8); i++) {
    rows.push({
      no: String(1000 + i * 37),
      price: +(g.floor * (1 + i * 0.06)).toFixed(2),
      owner: 'user_' + (100 + ((i * 7) % 60)),
      time: '2026-10-0' + ((i % 7) + 1) + ' 12:0' + (i % 10)
    })
  }
  return rows
}

/** 求购单 */
export const BID_LIST = (g) => {
  if (g.floor == null) return []
  const rows = []
  for (let i = 0; i < Math.min(g.bids, 6); i++) {
    rows.push({
      no: String(2000 + i * 53),
      price: +(g.floor * (1 - i * 0.04)).toFixed(2),
      owner: 'user_' + (200 + ((i * 13) % 70)),
      amount: 1 + (i % 3)
    })
  }
  return rows
}

/** 相关公告 */
export const RELATED_NOTICES = [
  { title: '【爱卡合成公告】iCard奶奶有道理系列藏品《慢行致远》合成活动来袭！', time: '2026/10/06 21:44', tag: '合成公告' },
  { title: '【爱卡寄售公告】iCard奶奶有道理系列藏品《花香碟自来》寄售调整公告', time: '2026/10/06 19:38', tag: '寄售公告' },
  { title: '【爱卡试运营晚安公告】 致ICARD爱卡全体用户', time: '2026/10/06 22:52', tag: '运营公告' }
]

/** 按 id 取藏品；缺省返回第一件 */
export function getGoods(id) {
  if (!id) return GOODS[0]
  const key = String(id).replace(/^#?/, '')
  return GOODS.find((g) => g.id === key || g.id.replace('g', '') === key) || GOODS[0]
}