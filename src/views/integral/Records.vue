<template>
  <uni-view data-v-0d9c109e class="records-page" style="padding-top: 0px;">
    <uni-view data-v-0d9c109e class="header">
      <uni-view data-v-0d9c109e class="back-btn"><uni-text data-v-0d9c109e class="cuIcon-back"><span></span></uni-text></uni-view>
      <uni-view data-v-0d9c109e class="page-title">兑换记录</uni-view>
      <uni-view data-v-0d9c109e class="header-placeholder"></uni-view>
    </uni-view>

    <uni-view v-if="rows.length" data-v-0d9c109e class="padding">
      <uni-view
        v-for="o in rows"
        :key="o.id"
        data-v-0d9c109e
        class="ex-item"
        @click="openDetail(o)"
      >
        <uni-view data-v-0d9c109e class="ex-head">
          <uni-text data-v-0d9c109e class="ex-no"><span>单号 {{ o.no }}</span></uni-text>
          <uni-text data-v-0d9c109e class="ex-state" :class="stateClass(o.state)"><span>{{ o.state }}</span></uni-text>
        </uni-view>
        <uni-view data-v-0d9c109e class="ex-body">
          <uni-image data-v-0d9c109e class="ex-thumb">
            <div :style="`background-image: url(&quot;${o.image}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div>
            <img :src="o.image" alt="" draggable="false" />
          </uni-image>
          <uni-view data-v-0d9c109e class="ex-info">
            <uni-view data-v-0d9c109e class="ex-name">{{ o.name }}</uni-view>
            <uni-view data-v-0d9c109e class="ex-cost">消耗 {{ o.cost }} 积分</uni-view>
            <uni-view data-v-0d9c109e class="ex-time">{{ o.time }}</uni-view>
          </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view
      v-else
      data-v-4d930ea0
      data-v-0d9c109e
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

    <!-- 兑换详情弹层 -->
    <uni-view data-v-0d9c109e class="cu-modal bottom-modal" :class="{ show: !!detail }">
      <uni-view data-v-0d9c109e class="cu-dialog bg-white ex-sheet">
        <uni-view data-v-0d9c109e class="ex-sheet-title">兑换详情</uni-view>
        <uni-view v-if="detail" data-v-0d9c109e class="ex-sheet-body">
          <uni-view data-v-0d9c109e class="ex-row"><uni-text data-v-0d9c109e><span>单号</span></uni-text><uni-text data-v-0d9c109e class="ex-row-v"><span>{{ detail.no }}</span></uni-text></uni-view>
          <uni-view data-v-0d9c109e class="ex-row"><uni-text data-v-0d9c109e><span>商品</span></uni-text><uni-text data-v-0d9c109e class="ex-row-v"><span>{{ detail.name }}</span></uni-text></uni-view>
          <uni-view data-v-0d9c109e class="ex-row"><uni-text data-v-0d9c109e><span>积分</span></uni-text><uni-text data-v-0d9c109e class="ex-row-v strong"><span>{{ detail.cost }} 分</span></uni-text></uni-view>
          <uni-view data-v-0d9c109e class="ex-row"><uni-text data-v-0d9c109e><span>状态</span></uni-text><uni-text data-v-0d9c109e class="ex-row-v"><span>{{ detail.state }}</span></uni-text></uni-view>
          <uni-view data-v-0d9c109e class="ex-row"><uni-text data-v-0d9c109e><span>兑换时间</span></uni-text><uni-text data-v-0d9c109e class="ex-row-v"><span>{{ detail.time }}</span></uni-text></uni-view>
          <uni-view data-v-0d9c109e class="ex-row"><uni-text data-v-0d9c109e><span>物流</span></uni-text><uni-text data-v-0d9c109e class="ex-row-v"><span>{{ detail.state === '已发货' ? '中通快递 ZT3092817465 · 运输中' : '暂未发货' }}</span></uni-text></uni-view>
        </uni-view>
        <uni-view data-v-0d9c109e class="ex-sheet-footer">
          <uni-view data-v-0d9c109e class="ex-sheet-btn" @click="detail = null">关闭</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
/**
 * 兑换记录（integral/Records）
 * 源站只有 header + 永久「暂无数据」，无任何数据与事件。
 * 克隆版补齐：7 条积分兑换记录 + 详情弹层。
 */
import { ref } from 'vue'
import { GOODS } from '@/mock/goods'

const DONE = '已完成'
const SHIPPED = '已发货'
const WAIT = '待发货'

const SEED = [
  [SHIPPED, 1200, '2026-10-09 09:12', 2],
  [WAIT, 800, '2026-10-06 14:38', 0],
  [DONE, 3200, '2026-09-28 20:05', 1],
  [DONE, 560, '2026-09-20 11:47', 3],
  [DONE, 2100, '2026-09-11 16:22', 4],
  [DONE, 980, '2026-09-02 10:09', 5],
  [DONE, 4500, '2026-08-24 18:51', 6]
]

const rows = ref(
  SEED.map(([state, cost, time, gi], i) => {
    const g = GOODS[gi % GOODS.length]
    return {
      id: 70000 + i,
      no: 'EX' + String(20260860000 + i * 149),
      name: g.name + ' 限定周边',
      image: g.img,
      cost,
      state,
      time
    }
  })
)

const detail = ref(null)

function stateClass(s) {
  if (s === DONE) return 'st-done'
  if (s === SHIPPED) return 'st-ship'
  return 'st-wait'
}

function openDetail(o) {
  detail.value = o
}
</script>