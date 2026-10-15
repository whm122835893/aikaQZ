# ICARD 爱卡 H5 — 站点克隆项目

对 <https://h5.shenyuan.sc.cn>（**ICARD 爱卡**，uni-app 构建的数字藏品 + 实物商城 H5）的完整前端克隆。

> 这是一个**独立项目**，与其它工程无任何耦合，可单独运行。

## 快速开始

```bash
cd /workspace/icard-clone
pnpm install
pnpm dev          # http://localhost:5173/
```

构建产物：

```bash
pnpm build        # 输出到 dist/
pnpm preview
```

## 路由对照

URL 结构保留原站的 hash 路由（`#/pages/xxx/yyy`），共 **75 条路由**（原站提取 74 条 + 根路径重定向）。

| 底部 Tab | 路由 | 说明 |
|---|---|---|
| 首页 | `/#/pages/home/home` | 搜索 / banner / 公告轮播 / 分类 Tab / 商品瀑布流 |
| 活动 | `/#/pages/colorfulMix/colorfulMix` | 抽签、积分商城、转盘、签到、精彩合成 |
| 市场 | `/#/pages/market/market` | 活动市场 / 自由市场 / 我的关注、专辑筛选、行情列表 |
| 公告 | `/#/pages/notification/notification` | 公告分类筛选 + 列表 |
| 我的 | `/#/pages/account/account` | 订单、钱包、收藏、地址、账号安全 |

启动页 `#/pages/index/index`（1s 倒计时后自动进入首页）。

### 完整趋势路由清单（74 条）

| 模块 | 页面 |
|---|---|
| index | index（启动页） |
| home | home |
| colorfulMix | colorfulMix、community、group、icardGame、records、result |
| market | market、details、goodsDetails、physicalGoodsDetails、sale、saleResult、Consignment、batchBuy、bidDetail、cardMap、createOrder、submitBegBuy |
| notification | notification、details |
| Announcement | Announcement（消息）、details、list |
| account | account、orderList、marketOrderList、physicalOrderList、bidList、saleList、order、Warelist、blindbox、invite、InviteRankingList、nickname、realname、safePass、open、about、privacy、service、community、increase、other、otheruser、user |
| address | address、add |
| wallet | wallet、wallet1、thirdWallet |
| invite | invite、list |
| integral | details、Get、records |
| drawlots | drawlots、details |
| drawPrize | drawPrize |
| mix | mix、details、records、result |
| login | login、register、forget |
| common | emptyPage |
| community / download / entrust / Transformation / webview | community、download、entrust、Transformation、Policy、webview2 |

## 目录结构

```
icard-clone/
├── public/                 # 静态资源，与源站路径 1:1 保持一致
│   ├── static/             # 源站 /static 全量镜像（图片 / tabbar 图标 / 字体）
│   ├── upload/             # 源站运营上传图片（横幅、藏品封面、商品图）
│   └── assets/             # 自定义字库 new.TTF / tabs.ttf
├── src/
│   ├── App.vue             # uni-app 页面骨架 + 全局导航
│   ├── main.js
│   ├── router/index.js     # 75 条路由
│   ├── components/
│   │   ├── TabBar.vue      # 底部 5 Tab（含选中态图标切换）
│   │   └── PageHead.vue    # 顶部 uni 导航栏（按页注入标题）
│   ├── data/pageHeads.js   # 各页导航栏标题映射
│   ├── nav/
│   │   ├── rules.js        # 点击导航映射表（选择器 → 路由）+ 文案路由表 + 登出标记
│   │   ├── index.js        # 事件委托安装器 installNavDelegation()
│   │   └── actions.js      # 全局动作兜底 installActionFallback()：给无逻辑的可点元素派发动作
│   ├── utils/interact.js   # 登录态（localStorage）、Toast、手机号/密码/验证码校验
│   ├── mock/
│   │   ├── data.js         # 演示数据（公告10 条 / 钱包 / 表单默认值）
│   │   ├── goods.js        # 22 条藏品（列表与详情共用），含挂单/求购流水生成器
│   │   └── orders.js       # 24 条订单，覆盖首发/常规/求购/委托/盲盒 × 5 种状态
│   ├── styles/site.css     # 源站全量样式（uni 框架 + 业务 scoped 样式）+ 运行时补丁
│   └── views/              # 75 个页面组件（按原 pages 目录分模块）
├── scripts/
│   ├── inject_script.py    # 向快照页注入 <script setup> 的结构化工具
│   ├── make_singlefile.py  # 单文件 HTML 打包后处理
│   ├── sfc-check.mjs       # 全量 SFC 体检（parse + compileTemplate + compileScript）
│   └── patch_*.py          # 各页交互补强的补丁脚本（可重放）
├── vite.config.js
└── vite.config.singlefile.js
```

## 交互与数据

页面组件是从源站抓下来的静态 HTML，本身不带任何 `@click`。为了让克隆版能真正点得动，加了**三层**机制：

### 第1 层：全局点击导航（`src/nav/`）

- `rules.js` 是核心映射表，规则形如「CSS 选择器 → 路由」。命中方式是从点击目标向上逐层回溯，**越靠近点击处的元素优先级越高**。
- 文案路由表 `TEXT_ROUTES` 用可见文案区分同名class 的并列入口（首发 / 市场 / 求购 / 委托），采用「先完全相等、再包含匹配」两轮策略，且长文案优先（避免「我的钱包」被短词抢占）。
- `LOGOUT_LABEL = '退出登录'` 命中后走特殊分支：`signOut()` 清 `localStorage['icard_auth']` → Toast → `router.replace('/pages/home/home')`。
- 单个元素想覆盖默认行为时，直接加 `data-nav-to="/pages/xxx/yyy"` 或 `data-nav-back`，无需改 JS。
- `App.vue` 的 `onMounted` 调用 `installNavDelegation(router)`，捕获阶段监听；`.uni-page-head`、`.tabbar`、`.tabbaritem` 在忽略名单里。

| 来源 | 选择器 | 目标 |
|---|---|---|
| 首页 | `.waterfall-item` | `/pages/market/details` |
| 首页 | `.notice-swiper-item` | `/pages/notification/details` |
| 市场 | `.market-table-row` / `.market-list-thumb` | `/pages/market/details` |
| 公告 | `.notice-card` | `/pages/notification/details` |
| 我的 | `.trade-item` | 按文案分发 orderList / marketOrderList / bidList / entrust |
| 我的 | `.menu-item` | 按文案分发 safePass / wallet / other / open / about / address；「退出登录」走登出分支 |
| 合成页 | `.quick-card` `.feature-card` | 用 `data-nav-to` 显式声明目标 |
| 各类详情页 | `.back-btn` `.header-back` `.nav-back` `.cuIcon-back` | `router.back()` |

### 第 2 层：全局动作兜底（`src/nav/actions.js`）

`installActionFallback()` 给「可点但无逻辑」的控件派发动作，用 `_vei` 检测页面是否已自行处理，避免抢handler：

- 取消 / 关闭类 → 关闭顶层弹层或 `history.back()`
- 复制类 → `navigator.clipboard.writeText()`
- `^¥[\d.]+$` →切换充值档位高亮
- 需登录页（`/pages/account/realname`、`safePass`、`wallet1`、`entrust`、`batchBuy` 等）→ 未登录时 Toast「请先登录」
- 提交类文案（`确定|确认|提交|保存|完成|认证|提货|购买|充值|上架|查询|复制`）→ 带上下文 Toast

### 第 3 层：页面内`<script setup>`

关键业务页已完全重写为响应式组件，数据来自 `src/mock/`：

| 页面 | 已实现能力 |
|---|---|
| `login/Login`、`Register`、`Forget` | 手机号 / 密码 / 验证码 / 邀请码表单，60秒倒计时，两次密码一致性校验，登录态写入 `localStorage['icard_auth']` |
| `market/Market` | 22 条藏品、3 子 Tab × 4 标签 × 2 排序、关键词搜索、行 → 详情跳转 |
| `market/Details` | 藏品实况、挂单 / 求购 / 委托三个子列表、相关公告、4 个底部操作 + 2 个弹层、收藏切换、金额联动 |
| `market/GoodsDetails` | 藏品实况、寄售（收益试算）/ 转赠（接收人）/ 购买（数量增减）三个弹层、收藏、底部操作条 |
| `market/PhysicalGoodsDetails` | 3 条演示商品、规格参数表、数量选择、下单 |
| `market/BidDetail` | 价格与数量联动、支付方式切换、金额试算（已清零源站遗留的 5 处 `NaN`） |
| `account/OrderList` | 5 个主 Tab × 4 个子 Tab 双向过滤，24 条订单，点行开详情弹层，待付款可去支付 |
| `account/MarketOrderList` | 3 个状态 Tab 切换 |
| `account/BidList` | 5 个状态 Tab 切换（求购 + 委托单合并展示） |
| `account/Other` | 持有/ 售出 × 藏品 / 盲盒 双层 Tab、藏品抽屉、批量寄售（费用试算）、合成结果弹层 |
| `account/User` | 昵称 / 手机 / 钱包地址真实值，昵称弹层可改，地址可复制 |
| `account/Privacy` | 设置操作密码（6 位数字 + 一致性校验）、找回密码跳转 |
| `account/Increase` | 转赠查询：编号真实化、地址与价格输入、查询结果卡（含服务费与到账试算） |
| `account/Invite` | 邀请码由 `--` 改为 `IC+手机号后 6 位`、二维码占位、复制邀请码 / 链接、分享海报弹层、邀请记录 |
| `wallet/Wallet1` | 6 档充值（满 100 送 10、满 200 送 30）、3 种支付方式、余额实时累加 |
| `notification/Notification` | 9 个分类 Tab 响应式过滤、关键词搜索 + 一键清空、公告卡进详情 |
| `drawPrize/DrawPrize` | 抽 1 次 / 十连 / 点机器抽奖，6 奖品加权随机、中奖弹窗、抽奖记录 |
| `drawlots/Drawlots` / `Details` | 3 个活动（2 进行中 / 1 未开始）、奖池网格、三步时间、抽签码生成与复制、进度条 |
| `download/Download` | 网页版 / App 两个下载入口，点击后出二维码占位 |
| `colorfulMix/ColorfulMix` | 4 个入口全部可跳（补齐缺失的 `data-nav-to`）、活动卡跳合成记录 |

### 关键技术点

- **原生 `input` 不能用 `v-model`**：Vue 会把它编译成 `onUpdate:modelValue`（组件事件），原生 input 只发 `input` 事件。必须写 `:value="phone" @input="set('phone', $event.target.value)"`。
- **重写快照页必须保留 `data-v` 作用域属性**：`site.css` 里所有业务样式都带 `[data-v-xxxxxxxx]`（Vue scoped 编译产物）。若重写模板时把这些属性删掉，该页所有布局/配色会**静默失效**——页面变成纯文本无样式，且不报任何错。`scripts/fix_scope_attr.py` 可从原始快照 `crawl4/*.html` 反查每页真实scope id 并批量补回。
  ```bash
  python3 scripts/fix_scope_attr.py   # 补回缺失的 data-v
  ```
- **新增样式必须带作用域前缀**：`.order-item` / `.empty-box` / `.info-value` 这类通用类名若不带 `[data-v-x]` 会全局污染所有页面。补丁区所有选择器一律写成 `.foo[data-v-xxxxxxxx]`。
- **不要复用快照里的「骨架占位符」类名**：`.item-placeholder` 在源站被定义为 `{width:calc((100%-20px)/3); height:0; padding:0; visibility:hidden}`——它是骨架屏的隐形占位块。复用它做卡片会让内容直接消失（元素存在但 `getBoundingClientRect` 可见性为 false，Playwright 报 `element is not visible`）。必须另起类名。
- **必须全局隐藏 `uni-page-head`**：它是 uni-app 运行时自动注入的原生导航栏（`position:fixed; height:44px; z-index:998;` 黑底）。克隆版 75 个页面全部自带自定义 `.header`，这个原生顶栏会压住页面顶部并**拦截点击**（表现为顶部 Tab / 按钮点不动）。源站靠 `navigationStyle:custom` 隐藏，克隆版等效处理：
  ```css
  uni-page-head { display: none !important; }
  ```
- **空壳页排查方法**：`grep -c '<script'` 为 0 的页面就是纯静态快照壳，表现为「Tab 点不动 + 永远暂无数据」。
- **「疑似无反应」不等于 bug —— 判断 Tab 要看列表内容变化，不能只看 URL**：全站点击审计（`audit_all.py`，198 次点击）会用「URL 变了 / 弹层开了」判定是否有反应，但 Tab 切换两者都不变，会被误记。正确判定是比对点击前后**列表 innerText 是否变化**。实测结论：
  | 页面 | Tab 数 | 结论 |
  |---|---|---|
  | `bidList` / `orderList` / `physicalOrderList` / `saleList` | 4–5 | 全部生效，条数随 Tab 变化（如 9→3→2→1） |
  | `marketOrderList` | 3 | 生效；列表类名是 `.list > uni-view`（不是 `.order-item`），写错选择器会误判为「0 条」 |
  | `order` 的 `.tab_item` | 1 | 它是**页面标题**不是 Tab，误报 |
  | `InviteRankingList` 的 `.rank-row` | 10 | 排行榜行本就不可点，误报 |
  | `notification` 的 `.action-btn` | 1 | 是搜索图标，绑定了 `focusSearch`，有 toast，误报 |
- **跨页传参用 `sessionStorage`**：`Details`（寄售）→ `Sale`（填售价）→ `SaleResult`（结果）这条链路，中间页无法靠 vue-router query 拿到藏品（源站快照就是空壳，`￥` 和 `#` 后面什么都没有）。约定两个 key：`icard_sale_goods`（藏品信息）、`icard_sale_result`（成交信息），读取时全部用 `try/catch` 包裹并留兜底数据，保证直接打开结果页也不空白。
- **样式配色必须与页面主题一致**（源站是**浅色**主题，不是深色）：全局兜底是 `uni-page-body{background:#fff!important}`，深色页面靠 `body.pages-xxx` 单独覆盖。踩过的坑：
  | 类| colorui 原值 | 问题 | 修正 |
  |---|---|---|---|
  | `.bg-grey` | `#343861` 深蓝底白字 | 浅色页面上深蓝卡片突兀 | `#f7f8fa` + 深色文字 |
  | `.info-value` | `rgba(255,255,255,.55)` 白字 | 白底上完全不可见 | `#8e8e8e` |
  | `.own-meta` / `.setting-value` | 白字 | 同上 | `#999` / `#8e8e8e` |
  | `.text-white` | `#fff` | 浅色 Tab 上不可读 | 按页覆盖为 `#333` |
  | 订单卡片（自加） | 深色半透明白底 | 压在浅色渐变上看不清 | 白色半透+深色文字 |
- **底部fixed 条必须对齐作用域属性**：快照里`.page-body` 带 `[data-v-xxxxxx]{z-index:3}`，权重高于普通类名。新加的底部条要么继承该`data-v` 属性，要么用 `[data-v-xxxxxx]` 选择器提权重，否则会被正文盖住、点击被拦截。
- **SFC 结构**：`scripts/inject_script.py` 统一保证 `<template>…</template>` 在前、`<script setup>` 在后。`script` 若被追加到 `</template>` 之后会被模板解析器整段吞掉（表现为 `descriptor.scriptSetup` 长度为 0）。
- **全量体检**：`node scripts/sfc-check.mjs` 对 75 个 SFC 逐个跑 `parse + compileTemplate + compileScript`，是改页面后必过的关卡。

> 注：`@vue/compiler-sfc` 3.5.x 的 `parse()` 返回 `{ descriptor, errors }` 而非 descriptor 本身，体检脚本里已按新版结构取。

### 单文件产物的移动端验证

`icard-clone.html` 需在微信内置浏览器实测（Chromium 桌面端无法暴露问题）。验证脚本用Playwright 模拟微信 UA + `file://` 协议：

```bash
# 微信 UA 下逐页渲染 + 节点数/横向溢出检查
python3 wx_all.py       # 76 页，0 渲染异常 / 0 JS 异常
# 对比度审计：找出「浅色文字压在浅色底」的不可读元素
python3 audit_light.py  # 启发式，需配合截图人工核验（半透明叠加会误报）
```

判空阈值参考：`#app` 节点数 ≥ 12、`documentElement.scrollWidth ≤ 392`、可见文本 ≥ 4 字符。`index/index` 启动页节点数天然偏低（1s后自动跳首页），属正常。

### 关于「空壳」页面

源站有 15 条路由的内容依赖登录态、URL 参数（`?id=`）或第三方 iframe，无参访问时就是空盒子——这部分**版式是忠实还原的**，空是因为拿不到数据。为了能浏览，用 `src/mock/` 里的演示数据把它们填上了：

| 页面 | 填充内容 |
|---|---|
| `notification/Details`、`Announcement/Details` | 标题、发布方、时间、正文 HTML、相关推荐（支持 `?n=2` 切换第 n 条） |
| `Announcement/List` | 10 条公告列表（源站此路由本身无实现） |
| `wallet/Wallet` | 汇付 / 易宝两张钱包卡（文案烤在背景图里）+ 资产概览 |
| `wallet/ThirdWallet` | 汇付 iframe 换成说明卡 |
| `market/CreateOrder` | 订单卡片、藏品信息、编号分配、底部结算栏 |
| `market/SubmitBegBuy`、`entrust/Entrust` | 求购 / 委托表单与费用试算 |
| `colorfulMix/Result`、`mix/Result` | 合成 / 置换结果图与名称 |
| `market/CardMap` | 复用页面自带 `.item` 三列栅格展示藏品网格 |
| `account/PhysicalOrderList` | 12 条实物订单 + 双层 Tab（全部/购买/托管/寄售 × 全部/待付款/已支付/订单取消）+ 详情弹层 |
| `account/Warelist` | 6 条云仓可提货藏品 + 详情（链上编号列表）+ 批量寄售（收益/服务费试算）+ 提货（地址/备注） |
| `account/SaleList` | 4 类售出 Tab 过滤 + 10 条售出记录 + 详情弹层（含服务费与实收） |
| `account/Open` | 8 条开盒记录按月分组 + 筛选（全部记录 / 只看传说）+ 详情弹层 |
| `account/Order` | 4 状态 Tab + 7 条提货订单 + 详情弹层 + 提醒发货 / 查看物流 |
| `mix/Records`、`colorfulMix/Records` | 各 6 条合成记录 + 详情弹层（展开消耗材料清单） |
| `integral/Records` | 7 条积分兑换记录 + 详情弹层（含物流） |
| `address/Address` | 3 条收货地址 + 设为默认 / 编辑 / 删除 + 底部跳新增页 |
| `invite/List` | 2 Tab（分享中 / 分享成功）+ 8 条邀请记录 + 详情弹层 |
| `account/InviteRankingList` | 10 条排行榜数据，当前用户高亮 + 我的排名 |
| `webview/Policy`、`webview/Webview2` | 隐私政策正文、第三方通道未接入说明 |
| `account/Community` | 公众号二维码与说明 |

填充原则：**只用页面原有的 class 与 `data-v`，尽量不新增全局 class**；必须新增时集中在 `site.css` 末尾的补丁区，并注明原因（如作用域权重）。`mix/records`（正确的「暂无数据」空态）与 `index/index`（启动页倒计时）保持原样。

## 克隆原理（为什么能做到高保真）

源站是 uni-app 产物，页面样式分散在运行时注入的 `<style>` 里，DOM 使用 `<uni-view>` / `<uni-image>` 等自定义元素。本项目采用 **结构快照 + 原样式表复用** 的方式，而非人工重写 UI：

1. **路由表提取**：从 `index.js` 中的 `pages/*/*` 字符串集合还原出 74 条路由。
2. **登录绕过**：通过 patch `history.replaceState / uni.redirectTo`，阻止未登录时的登录页重定向，从而采集到全部受限页面的真实 DOM。
3. **结构快照**：Playwright 以 iPhone 6/7/8 视口（375×812）逐路由导出 `uni-page` 的完整 outerHTML，包含原始 class、`data-v-xxxxxx` scoped 标识和全部内联样式。
4. **样式采集**：遍历所有路由，聚合运行时注入的 `<style>` 内容，与 `index.css`（uni 框架基础样式）合并为 `site.css`。
5. **代码生成**：脚本把 HTML 快照切掉重复的 tabbar 片段，直接包成 Vue SFC 的 `<template>`，保持类名与内联样式原样。
6. **运行时补齐**：补齐 uni-app 运行时才注入的部分（`uni-page-head / uni-image / uni-input` 骨架、`--window-left` 等系统变量），并在 Vite 里设置 `whitespace: 'preserve'`（保留换行，避免文本排版被压缩）与 `transformAssetUrls: false`（资源走 public 路径）。
7. **资源本地化**：静态图片、SVG、tabbar 图标、TTF 字库、外链 cuIcon 图标字体全部下载到 `public/`，路径与源站一致。

## 已知限制

- **数据是本地 mock**：`src/mock/goods.js`（22 条藏品）、`src/mock/orders.js`（24 条订单）、`src/mock/data.js`（10 条公告）为演示数据，钱包余额等为写死值。源站接口是 `api.shenyuan.sc.cn/{32位hash}` 的混淆端点，未逆向，接真实数据需自行替换。
- **演示账号**：手机号 `13800138000`、验证码 `123456`、密码 `123456`。登录态存`localStorage['icard_auth']`，退出登录会清除。
- **未接入的交互**：首页 Banner / swiper 等运营位跳转目标由后台配置，克隆版保持静态；真实支付、真实文件下载、真实二维码生成均以Toast 提示代替。
- **字体体积**：`public/assets/*.ttf` 合计约 19MB（源站同样如此，是其首屏偏慢的主因）。生产环境建议抽取子集。
- **静态托管的 403**：源站根路径直接访问返回 OSS 403，正常入口为 `/index.html`，本项目不受影响。
- **源站 3 张 CSS 背景图 404**：`/static/images/login/bg.png`、`/static/images/mix/item.png`、`/static/images/mix/open.png` 在源站自身即返回 404，克隆版保持一致未做补图。

## 验证

```bash
node scripts/sfc-check.mjs    # 全量 75 个 SFC 体检：parse + compileTemplate + compileScript
pnpm build# 产物构建
pnpm preview                              # 本地预览（默认 4173）
```

浏览器端回归（Playwright，375×812 视口）覆盖：登录/注册/找回/登出全流程、订单三页 Tab 过滤与详情弹层、市场详情四子列表、抽奖单发/十连、抽签活动与抽签码、充值档位与余额累加、邀请码与海报、隐私密码设置、公告分类与搜索、收藏页双层 Tab、实物下单、活动页入口跳转—— **38 项断言全部通过，全站 75 页点击冒烟 0 个 JS 异常**。

## 单文件版（`icard-clone.html`）

用 `vite-plugin-singlefile` 把全部 JS / CSS 内联进**一个 HTML**，双击即可用浏览器打开，无需起服务器。

```bash
pnpm exec vite build --config vite.config.singlefile.js   # 生成 dist/index.html（已内联 JS/CSS）
python3 scripts/make_singlefile.py                       # 资源前缀改写为源站绝对 URL
```

成品在仓库根目录 `icard-clone.html`（约 918KB）。

### 资源策略
| 资源 | 处理方式 | 说明 |
|---|---|---|
| JS / CSS | 全部内联 | 75 个页面 + mock 数据 + 导航逻辑打包进单文件，离线可运行 |
| 图标字体 `uni`/`unibtn`/`unimapbtn`/`weui` | base64 内联 | 返回键、Tab 图标、按钮图标正常显示 |
| 图片 `/static/`、`/upload/`、`/img/`、`/assets/` | 改写为源站绝对 URL | 需联网显示（不内联以避免 42MB 资源撑爆单文件） |
| 文本字体 `new`/`tabs` | 走源站，失败降级 | `file://` 下因浏览器跨域策略降级为系统 sans-serif，仅字形微调，不影响布局与图标 |

### 说明
若需要完全离线（连图片也内嵌）或连文本字体都精确还原，可把 `public/` 资源改成 base64 内联，代价是单文件体积涨到几十 MB。
