<template>
  <uni-view data-v-4ca01c7d class="sale-page">
    <uni-view data-v-4ca01c7d class="header margin-lr">
      <uni-view data-v-4ca01c7d class="back-btn"><uni-text data-v-4ca01c7d class="cuIcon-back"><span></span></uni-text></uni-view>
      <uni-view data-v-4ca01c7d class="page-title">售出记录</uni-view>
      <uni-view data-v-4ca01c7d class="header-placeholder"></uni-view>
    </uni-view>

    <uni-view data-v-4ca01c7d class="tab-bar">
      <uni-view
        v-for="(t, i) in tabs"
        :key="t"
        data-v-4ca01c7d
        class="tab-item"
        :class="{ active: tab === i }"
        @click="tab = i"
      >
        <uni-text data-v-4ca01c7d><span>{{ t }}</span></uni-text>
        <uni-view data-v-4ca01c7d class="tab-line"></uni-view>
      </uni-view>
    </uni-view>

    <uni-view v-if="rows.length" data-v-4ca01c7d class="sale-list">
      <uni-view
        v-for="o in rows"
        :key="o.id"
        data-v-4ca01c7d
        class="sale-item"
        @click="openDetail(o)"
      >
        <uni-view data-v-4ca01c7d class="sale-head">
          <uni-text data-v-4ca01c7d class="sale-no"><span>单号 {{ o.no }}</span></uni-text>
          <uni-text data-v-4ca01c7d class="sale-status" :class="statusClass(o.status)"><span>{{ o.status }}</span></uni-text>
        </uni-view>

        <uni-view data-v-4ca01c7d class="sale-body">
          <uni-image data-v-4ca01c7d class="sale-thumb">
            <div :style="`background-image: url(&quot;${o.image}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div>
            <img :src="o.image" alt="" draggable="false" />
          </uni-image>
          <uni-view data-v-4ca01c7d class="sale-info">
            <uni-view data-v-4ca01c7d class="sale-name over">{{ o.name }}</uni-view>
            <uni-view data-v-4ca01c7d class="sale-token">#{{ o.token }} · x{{ o.qty }}</uni-view>
            <uni-view data-v-4ca01c7d class="sale-time">{{ o.time }}</uni-view>
          </uni-view>
          <uni-view data-v-4ca01c7d class="sale-right">
            <uni-view data-v-4ca01c7d class="sale-price">¥{{ o.price }}</uni-view>
            <uni-view data-v-4ca01c7d class="sale-fee">实收 ¥{{ o.net }}</uni-view>
          </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view
      v-else
      data-v-4d930ea0
      data-v-4ca01c7d
      class="flex align-center justify-center"
      style="height: 50vh;"
    >
      <uni-view data-v-4d930ea0 class="text-center">
        <uni-image data-v-4d930ea0 style="width: 90px; height: 80px;">
          <div style="background-image: url(&quot;/static/images/empty1.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
          <img src="/static/images/empty1.png" alt="" draggable="false" />
        </uni-image>
        <uni-view data-v-4d930ea0 class="text-grey margin-top-xs"> 暂无数据 </uni-view>
      </uni-view>
    </uni-view>

    <!-- 售出详情弹层 -->
    <uni-view data-v-4ca01c7d class="cu-modal bottom-modal" :class="{ show: !!detail }">
      <uni-view data-v-4ca01c7d class="cu-dialog bg-white sale-sheet">
        <uni-view data-v-4ca01c7d class="sale-sheet-title">售出详情</uni-view>
        <uni-view v-if="detail" data-v-4ca01c7d class="sale-sheet-body">
          <uni-view data-v-4ca01c7d class="sale-row"><uni-text data-v-4ca01c7d><span>单号</span></uni-text><uni-text data-v-4ca01c7d class="sale-row-v"><span>{{ detail.no }}</span></uni-text></uni-view>
          <uni-view data-v-4ca01c7d class="sale-row"><uni-text data-v-4ca01c7d><span>藏品</span></uni-text><uni-text data-v-4ca01c7d class="sale-row-v"><span>{{ detail.name }}</span></uni-text></uni-view>
          <uni-view data-v-4ca01c7d class="sale-row"><uni-text data-v-4ca01c7d><span>编号</span></uni-text><uni-text data-v-4ca01c7d class="sale-row-v"><span>#{{ detail.token }} × {{ detail.qty }}</span></uni-text></uni-view>
          <uni-view data-v-4ca01c7d class="sale-row"><uni-text data-v-4ca01c7d><span>类型</span></uni-text><uni-text data-v-4ca01c7d class="sale-row-v"><span>{{ detail.type }}</span></uni-text></uni-view>
          <uni-view data-v-4ca01c7d class="sale-row"><uni-text data-v-4ca01c7d><span>成交价</span></uni-text><uni-text data-v-4ca01c7d class="sale-row-v strong"><span>¥{{ detail.price }}</span></uni-text></uni-view>
          <uni-view data-v-4ca01c7d class="sale-row"><uni-text data-v-4ca01c7d><span>服务费(5%)</span></uni-text><uni-text data-v-4ca01c7d class="sale-row-v"><span>¥{{ detail.fee }}</span></uni-text></uni-view>
          <uni-view data-v-4ca01c7d class="sale-row"><uni-text data-v-4ca01c7d><span>实收</span></uni-text><uni-text data-v-4ca01c7d class="sale-row-v strong"><span>¥{{ detail.net }}</span></uni-text></uni-view>
          <uni-view data-v-4ca01c7d class="sale-row"><uni-text data-v-4ca01c7d><span>成交时间</span></uni-text><uni-text data-v-4ca01c7d class="sale-row-v"><span>{{ detail.time }}</span></uni-text></uni-view>
        </uni-view>
        <uni-view data-v-4ca01c7d class="sale-sheet-footer">
          <uni-view data-v-4ca01c7d class="sale-sheet-btn" @click="detail = null">关闭</uni-view>
          <uni-view data-v-4ca01c7d class="sale-sheet-btn primary" @click="reset">重新寄售</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
/**
 * 售出记录
 * 源站该页是纯静态空壳：4 个 Tab 只有第一个带 .active，没有数据、没有切换逻辑。
 * 克隆版补齐：4 类售出（数藏 / 秒转 / 实物 / 已售出）Tab 过滤 + 10 条演示数据 + 详情弹层。
 */
import { computed, ref } from 'vue'
import { GOODS } from '@/mock/goods'
import { toast } from '@/utils/interact'

const tabs = ['数藏售出', '秒转售出', '实物售出', '已售出']
const tab = ref(0)
const detail = ref(null)

const SOLD = '已售出'
const DEAL = '已成交'

/** 10 条售出记录：覆盖 4 类 Tab × 已成交/已售出两种状态 */
const SEED = [
  ['数藏售出', DEAL, 168, '2026-09-19 14:22', 2],
  ['数藏售出', DEAL, 320, '2026-09-17 10:08', 1],
  ['数藏售出', SOLD, 88, '2026-09-14 19:46', 3],
  ['数藏售出', DEAL, 520, '2026-09-10 09:15', 1],
  ['秒转售出', SOLD, 45, '2026-09-19 08:31', 5],
  ['秒转售出', DEAL, 99, '2026-09-16 21:02', 2],
  ['秒转售出', SOLD, 210, '2026-09-12 16:40', 1],
  ['实物售出', DEAL, 599, '2026-09-18 11:27', 1],
  ['实物售出', SOLD, 1299, '2026-09-09 13:55', 1],
  ['已售出', SOLD, 666, '2026-09-05 15:10', 4]
]

const ALL = SEED.map((s, i) => {
  const [type, status, price, time, qty] = s
  const g = GOODS[i % GOODS.length]
  const fee = (price * qty * 0.05).toFixed(2)
  return {
    id: 30000 + i,
    no: 'IC' + String(20260890000 + i * 173),
    type,
    status,
    name: g.name,
    image: g.img,
    token: 1000 + i * 47,
    price: (price * qty).toFixed(2),
    fee,
    net: (price * qty * 0.95).toFixed(2),
    time,
    qty
  }
})

/** 「已售出」Tab 是全局状态筛选，其余按类型筛选 */
const rows = computed(() => {
  const t = tabs[tab.value]
  if (t === '已售出') return ALL.filter((o) => o.status === SOLD)
  return ALL.filter((o) => o.type === t)
})

function statusClass(s) {
  return s === DEAL ? 'st-done' : 'st-sold'
}


function openDetail(o) {
  detail.value = o
}

function reset() {
  const o = detail.value
  detail.value = null
  toast(`${o.name} 已重新上架寄售`)
}
</script>