/**
 *本地演示数据
 *
 * 全部内容均从抓取到的真实页面快照里抽取（公告页10 条、首页商品 7 件），
 * 图片地址也已改写为本地 public 目录下的副本，不依赖源站。
 *
 * 存在的意义：源站有 15 个页面的内容依赖登录态、URL 参数（?id=）或第三方
 * iframe，无参访问时是空壳。这些数据用于把它们填成可浏览状态，
 * 便于查看版式，不代表源站真实业务数据。
 */

/** 公告列表 —— 来自 pages/notification/notification 的 10 张notice-card */
export const NOTICES = [
  {
    "publisher": "爱卡ICARD官方公告",
    "avatar": "/static/22.jpg",
    "time": "2026/10/06 22:52:08",
    "tag": "运营公告",
    "tagStyle": "background-color: rgb(255, 224, 240); color: rgb(207, 61, 127);",
    "title": "【爱卡试运营晚安公告】 致ICARD爱卡全体用户",
    "images": []
  },
  {
    "publisher": "爱卡ICARD官方公告",
    "avatar": "/static/22.jpg",
    "time": "2026/10/06 21:44:47",
    "tag": "合成公告",
    "tagStyle": "background-color: rgb(255, 234, 222); color: rgb(255, 106, 0);",
    "title": "【爱卡合成公告】iCard爱卡平台奶奶有道理系列藏品《慢行致远》合成活动来袭！",
    "images": [
      "/upload/fde3e9210841133dc8ad445ba020d08a81303a06.png"
    ]
  },
  {
    "publisher": "爱卡ICARD官方公告",
    "avatar": "/static/22.jpg",
    "time": "2026/10/06 21:07:05",
    "tag": "寄售公告",
    "tagStyle": "background-color: rgb(240, 226, 252); color: rgb(124, 75, 181);",
    "title": "【爱卡寄售公告】iCard奶奶有道理系列藏品《花香碟自来》寄售调整公告",
    "images": [
      "/upload/fde3e9210841133dc8ad445ba020d08a81303a06.png"
    ]
  },
  {
    "publisher": "爱卡ICARD官方公告",
    "avatar": "/static/22.jpg",
    "time": "2026/10/06 19:38:15",
    "tag": "运营公告",
    "tagStyle": "background-color: rgb(255, 224, 240); color: rgb(207, 61, 127);",
    "title": "【爱卡运营公告】ICARD爱卡注册开户福利第三弹！",
    "images": [
      "/upload/861bfe33d903a1fc7808f503e302b14e77f07ce1.png"
    ]
  },
  {
    "publisher": "爱卡ICARD官方公告",
    "avatar": "/static/22.jpg",
    "time": "2026/10/06 19:21:01",
    "tag": "寄售公告",
    "tagStyle": "background-color: rgb(240, 226, 252); color: rgb(124, 75, 181);",
    "title": "【爱卡寄售公告】iCard爱卡皮影生肖系列藏品《运粮鼠》寄售公告",
    "images": [
      "/upload/3df504960e882648dc0b96be33fadf1aeb059ec4.jpg"
    ]
  },
  {
    "publisher": "爱卡ICARD官方公告",
    "avatar": "/static/22.jpg",
    "time": "2026/10/06 17:48:00",
    "tag": "空投公告",
    "tagStyle": "background-color: rgb(232, 255, 226); color: rgb(94, 174, 52);",
    "title": "【爱卡空投公告】关于iCard爱卡平台首期转发活动奖励空投公告",
    "images": [
      "/upload/d731d68eb467f51988152a9d94b98ce960e266de.png"
    ]
  },
  {
    "publisher": "爱卡ICARD官方公告",
    "avatar": "/static/22.jpg",
    "time": "2026/10/06 16:23:27",
    "tag": "合成公告",
    "tagStyle": "background-color: rgb(255, 234, 222); color: rgb(255, 106, 0);",
    "title": "【爱卡合成公告】皮影生肖系列藏品《运粮鼠》合成活动来袭！",
    "images": []
  },
  {
    "publisher": "爱卡ICARD官方公告",
    "avatar": "/static/22.jpg",
    "time": "2026/10/06 14:19:30",
    "tag": "寄售公告",
    "tagStyle": "background-color: rgb(240, 226, 252); color: rgb(124, 75, 181);",
    "title": "【爱卡寄售公告】iCard爱卡奶奶有道理系列藏品《花香蝶自来》寄售公告",
    "images": [
      "/upload/fde3e9210841133dc8ad445ba020d08a81303a06.png"
    ]
  },
  {
    "publisher": "爱卡ICARD官方公告",
    "avatar": "/static/22.jpg",
    "time": "2026/10/06 11:40:30",
    "tag": "寄售公告",
    "tagStyle": "background-color: rgb(240, 226, 252); color: rgb(124, 75, 181);",
    "title": "【爱卡寄售公告】iCard爱卡平台系列藏品《艾卡德-学习》寄售公告",
    "images": [
      "/upload/861bfe33d903a1fc7808f503e302b14e77f07ce1.png"
    ]
  },
  {
    "publisher": "爱卡ICARD官方公告",
    "avatar": "/static/22.jpg",
    "time": "2026/10/06 09:57:35",
    "tag": "合成公告",
    "tagStyle": "background-color: rgb(255, 234, 222); color: rgb(255, 106, 0);",
    "title": "【爱卡合成公告】藏品《艾卡德-学习》限量分解活动来袭！",
    "images": []
  }
]

/** 首页商品 —— 来自 pages/home/home 的 7 张 waterfall-item */
export const GOODS = [
  {
    "title": "ICARD联名高端定制手机壳iPhone",
    "price": "19.9",
    "image": "/upload/f6746c2b2cf5254376c8958f1bc8780955ae168c.png"
  },
  {
    "title": "坐姿宇航员看书太空人大型装饰摆件潮流单品",
    "price": "199",
    "image": "/upload/c7d5b6506317d71aefb74c98ef2d7219e116d772.jpg"
  },
  {
    "title": "三角洲行动手办模型盲盒六一儿童节礼物",
    "price": "99",
    "image": "/upload/87f1615abb555956911f888aea806b7403685231.jpg"
  },
  {
    "title": "潮玩积木TOPTOY兔破未来半解剖拼装",
    "price": "199",
    "image": "/upload/ab284b9f1c4cac8eec22e8c9a30cf62ed9bac28d.png"
  },
  {
    "title": "ICARD潮流时尚联名手办高端定制款",
    "price": "199",
    "image": "/upload/45c0ec9b95b85006375bdfe673239b0752cca05c.png"
  },
  {
    "title": "一飞冲天齐天大圣孙悟空摆件装饰手办模型",
    "price": "99",
    "image": "/upload/3cdf6d1069191c8eb66b0185572abe9fa4ceb934.jpg"
  },
  {
    "title": "哆啦盲盒摆件玩具手办公仔潮玩礼物周边",
    "price": "99",
    "image": "/upload/a78f2138480a3638e085dee9e4f3e693265faa7a.jpg"
  }
]

/** 公告详情页正文模板：按公告序号取一条，缺省用第一条 */
export function getNotice(index = 0) {
  return NOTICES[index % NOTICES.length]
}

/** 公告正文 HTML（详情页与公告列表共用） */
export function buildNoticeBody(index = 0) {
  const n = getNotice(index)
  const imgs = n.images
    .map((src) => `<p style="text-align:center;"><img src="${src}" style="max-width:100%;" /></p>`)
    .join('')
  return `
    <p style="font-size: 15px; line-height: 1.9; color: rgb(51, 51, 51); text-indent: 2em;">
      ${n.title}
    </p>
    <p style="font-size: 14px; line-height: 2; color: rgb(102, 102, 102); text-indent: 2em;">
      尊敬的ICARD爱卡用户：<br />
      为持续提升平台体验，iCard 爱卡平台现就本次事项说明如下。本公告自发布之日起生效，
      平台将在客户端与官网同步公示。如有疑问，请联系官方客服。
    </p>
    ${imgs}
    <p style="font-size: 13px; line-height: 1.9; color: rgb(153, 153, 153);">
      特此公告。<br />
      ICARD爱卡官方<br />
      ${n.time}
    </p>
  `.trim()
}

/** 藏品详情（用于 market/details 等页面的展示位） */
export const GOODS_DETAIL = {
  name: GOODS[0].title,
  cover: GOODS[0].image,
  price: GOODS[0].price,
  issued: 1000,
  circulating: 386,
  creator: 'ICARD爱卡官方',
  brand: 'iCard 爱卡平台',
  intro:
    '本藏品为 ICARD 爱卡平台发行的数字版权品，采用区块链技术存证，' +
    '每一份均拥有独立唯一的链上编号，可溯源、不可篡改。',
  notice: [
    '本商品中包含的数字版权品为虚拟数字商品，而非实物。',
    '本商品一经售出，不支持退换，请谨慎购买。',
    '数字版权品的所有权转移以平台登记记录为准。'
  ]
}

/** 钱包概览（pages/wallet/wallet） */
export const WALLET = {
  balance: '1,286.50',
  income: '342.80',
  frozen: '0.00',
  points: 1,
  address: '0x7a3c...9f21'
}

/** 演示账号（pages/account/account 未登录态替换用） */
export const DEMO_USER = {
  nickname: '爱卡体验官',
  phone: '138****8888',
  level: '普通会员'
}

/** 合成 / 置换结果（pages/colorfulMix/result、pages/mix/result） */
export const SYNTH_RESULT = {
  cover: GOODS[1].image,
  name: GOODS[1].title,
  sub: '合成成功',
  serialNo: 'NO.20261007-0001'
}

/** 求购 / 委托表单的默认填充（pages/market/submitBegBuy、pages/entrust/entrust） */
export const FORM_DEFAULTS = {
  goodsName: GOODS[2].title,
  goodsCover: GOODS[2].image,
  price: GOODS[2].price,
  count: 1,
  serviceFee: '5%'
}
