<template>
  <uni-view data-v-737fcdde class="records-page" style="padding-top: 0px;">
    <uni-view data-v-737fcdde class="header">
      <uni-view data-v-737fcdde class="back-btn"><uni-text data-v-737fcdde class="cuIcon-back"><span></span></uni-text></uni-view>
      <uni-view data-v-737fcdde class="page-title">合成记录</uni-view>
      <uni-view data-v-737fcdde class="header-placeholder"></uni-view>
    </uni-view>

    <uni-view data-v-737fcdde class="records-list">
      <uni-view
        v-for="o in rows"
        :key="o.id"
        data-v-737fcdde
        class="cm-record-item"
        @click="openDetail(o)"
      >
        <uni-image data-v-737fcdde class="cm-record-img">
          <div :style="`background-image: url(&quot;${o.image}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div>
          <img :src="o.image" alt="" draggable="false" />
        </uni-image>
        <uni-view data-v-737fcdde class="cm-record-info">
          <uni-view data-v-737fcdde class="cm-record-name">{{ o.name }}</uni-view>
          <uni-view data-v-737fcdde class="cm-record-meta">{{ o.from.length }} 份材料合成 · #{{ o.token }}</uni-view>
          <uni-view data-v-737fcdde class="cm-record-time">{{ o.time }}</uni-view>
        </uni-view>
        <uni-view data-v-737fcdde class="cm-record-state" :class="stateClass(o.state)">{{ o.state }}</uni-view>
      </uni-view>

      <uni-view
        v-if="!rows.length"
        data-v-4d930ea0
        data-v-737fcdde
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
    </uni-view>

    <!-- 合成详情弹层 -->
    <uni-view data-v-737fcdde class="cu-modal bottom-modal" :class="{ show: !!detail }">
      <uni-view data-v-737fcdde class="cu-dialog bg-white cm-sheet">
        <uni-view data-v-737fcdde class="cm-sheet-title">合成详情</uni-view>
        <uni-view v-if="detail" data-v-737fcdde class="cm-sheet-body">
          <uni-image data-v-737fcdde class="cm-sheet-img">
            <div :style="`background-image: url(&quot;${detail.image}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div>
            <img :src="detail.image" alt="" draggable="false" />
          </uni-image>
          <uni-view data-v-737fcdde class="cm-sheet-name">{{ detail.name }}</uni-view>
          <uni-view data-v-737fcdde class="cm-sheet-label">消耗材料</uni-view>
          <uni-view v-for="(m, i) in detail.from" :key="i" data-v-737fcdde class="cm-sheet-mat">{{ m }}</uni-view>
          <uni-view data-v-737fcdde class="cm-row"><uni-text data-v-737fcdde><span>链上编号</span></uni-text><uni-text data-v-737fcdde class="cm-row-v"><span>#{{ detail.token }}</span></uni-text></uni-view>
          <uni-view data-v-737fcdde class="cm-row"><uni-text data-v-737fcdde><span>状态</span></uni-text><uni-text data-v-737fcdde class="cm-row-v"><span>{{ detail.state }}</span></uni-text></uni-view>
          <uni-view data-v-737fcdde class="cm-row"><uni-text data-v-737fcdde><span>时间</span></uni-text><uni-text data-v-737fcdde class="cm-row-v"><span>{{ detail.time }}</span></uni-text></uni-view>
        </uni-view>
        <uni-view data-v-737fcdde class="cm-sheet-footer">
          <uni-view data-v-737fcdde class="cm-sheet-btn" @click="detail = null">关闭</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
/**
 * 合成记录（colorfulMix/Records）
 * 源站只有 header + 永久「暂无数据」，无任何数据与事件。
 * 克隆版补齐：6 条合成记录 + 详情弹层（展开消耗材料清单）。
 */
import { ref } from 'vue'
import { GOODS } from '@/mock/goods'

const OK = '已到账'
const ING = '合成中'

const SEED = [
  [OK, 3, '2026-10-07 20:41'],
  [OK, 0, '2026-10-01 13:18'],
  [ING, 1, '2026-09-24 09:52'],
  [OK, 4, '2026-09-16 17:36'],
  [OK, 2, '2026-09-07 11:04'],
  [ING, 5, '2026-08-29 15:27']
]

const rows = ref(
  SEED.map(([state, gi, time], i) => {
    const g = GOODS[gi % GOODS.length]
    const from = [
      `${GOODS[(gi + 1) % GOODS.length].name} #${1200 + i * 5}`,
      `${GOODS[(gi + 3) % GOODS.length].name} #${1300 + i * 5}`
    ]
    return { id: 80000 + i, name: g.name, image: g.img, token: 3000 + i * 29, state, time, from }
  })
)

const detail = ref(null)

function stateClass(s) {
  return s === OK ? 'st-done' : 'st-ing'
}

function openDetail(o) {
  detail.value = o
}
</script>