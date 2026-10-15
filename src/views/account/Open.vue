<template>
  <uni-view data-v-440f64a3 class="page">
    <uni-view data-v-440f64a3 class="cu-bar flex justify-between align-center" style="width: 100%; height: 25px;">
      <uni-view data-v-440f64a3 class="action bg-white round padding justify-start" style="width: 25px; height: 25px; position: relative; z-index: 10;">
        <uni-view data-v-440f64a3 class="  "><uni-text data-v-440f64a3 class="cuIcon-back text-black"><span></span></uni-text></uni-view>
      </uni-view>
      <uni-view data-v-440f64a3 class="text-black text-xl flex-sub text-center" style="font-family: new; font-weight: 500; font-size: 16px; margin-left: 12%;">开盒记录</uni-view>
      <uni-view data-v-440f64a3 class="fer-btn text-center" style="position: relative; margin-right: 10px;">
        <uni-view data-v-440f64a3 class="top-btn text-center" @click="toggleFilter">
          {{ filterLabel }} <uni-text data-v-440f64a3 class="cuIcon-triangleupfill"><span></span></uni-text>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view data-v-440f64a3 class="content">
      <uni-view v-for="grp in grouped" :key="grp.month" data-v-440f64a3 class="content-month">
        <uni-view data-v-440f64a3 class="content-time">{{ grp.month }}</uni-view>
        <uni-view
          v-for="o in grp.list"
          :key="o.id"
          data-v-440f64a3
          class="content-item flex justify-between align-center padding"
          @click="openDetail(o)"
        >
          <uni-view data-v-440f64a3 class="item-left flex">
            <uni-view data-v-440f64a3 class="item-img" :style="`background-image: url(&quot;${o.image}&quot;); background-size: cover; background-position: center center;`"></uni-view>
            <uni-view data-v-440f64a3 class="item-content margin-left">
              <uni-view data-v-440f64a3 class="open-name">{{ o.name }}</uni-view>
              <uni-view data-v-440f64a3 class="margin-top-sm open-time">{{ o.time }}</uni-view>
            </uni-view>
          </uni-view>
          <uni-view data-v-440f64a3 class="cuIcon-right"></uni-view>
        </uni-view>
      </uni-view>

      <uni-view
        v-if="!grouped.length"
        data-v-4d930ea0
        data-v-440f64a3
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

    <!-- 开盒详情弹层 -->
    <uni-view data-v-440f64a3 class="cu-modal bottom-modal" :class="{ show: !!detail }">
      <uni-view data-v-440f64a3 class="cu-dialog bg-white open-sheet">
        <uni-view data-v-440f64a3 class="open-sheet-title">开盒详情</uni-view>
        <uni-view v-if="detail" data-v-440f64a3 class="open-sheet-body">
          <uni-image data-v-440f64a3 class="open-sheet-img">
            <div :style="`background-image: url(&quot;${detail.image}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div>
            <img :src="detail.image" alt="" draggable="false" />
          </uni-image>
          <uni-view data-v-440f64a3 class="open-sheet-name">{{ detail.name }}</uni-view>
          <uni-view data-v-440f64a3 class="open-row"><uni-text data-v-440f64a3><span>盲盒</span></uni-text><uni-text data-v-440f64a3 class="open-row-v"><span>{{ detail.box }}</span></uni-text></uni-view>
          <uni-view data-v-440f64a3 class="open-row"><uni-text data-v-440f64a3><span>编号</span></uni-text><uni-text data-v-440f64a3 class="open-row-v"><span>#{{ detail.token }}</span></uni-text></uni-view>
          <uni-view data-v-440f64a3 class="open-row"><uni-text data-v-440f64a3><span>稀有度</span></uni-text><uni-text data-v-440f64a3 class="open-row-v rare"><span>{{ detail.rare }}</span></uni-text></uni-view>
          <uni-view data-v-440f64a3 class="open-row"><uni-text data-v-440f64a3><span>开盒时间</span></uni-text><uni-text data-v-440f64a3 class="open-row-v"><span>{{ detail.time }}</span></uni-text></uni-view>
        </uni-view>
        <uni-view data-v-440f64a3 class="open-sheet-footer">
          <uni-view data-v-440f64a3 class="open-sheet-btn" @click="detail = null">关闭</uni-view>
          <uni-view data-v-440f64a3 class="open-sheet-btn primary" :data-nav-to="'/pages/market/market'">去市场看看</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
/**
 * 开盒记录
 * 源站该页是抓取时的原始单条占位：标题写死 "name"、时间是 2024-10-28、.item-img 是空灰块，
 * 顶部「全部记录」筛选项也没有任何事件。克隆版补齐：真实藏品图与名称、
 * 按月分组、筛选切换（全部记录 / 只看传说）、点击进入开盒详情。
 */
import { computed, ref } from 'vue'
import { GOODS } from '@/mock/goods'

const RARE = ['普通', '稀有', '史诗', '传说']

const ALL = [
  ['2026年10月', 0, '2026-10-08 20:35:33'],
  ['2026年10月', 2, '2026-10-03 11:12:07'],
  ['2026年10月', 5, '2026-10-01 09:48:51'],
  ['2026年9月', 1, '2026-09-27 21:04:16'],
  ['2026年9月', 3, '2026-09-22 15:33:40'],
  ['2026年9月', 7, '2026-09-15 10:20:08'],
  ['2026年8月', 4, '2026-08-30 19:57:22'],
  ['2026年8月', 6, '2026-08-18 13:05:44']
]

const RECORDS = ALL.map(([month, gi, time], i) => {
  const g = GOODS[gi % GOODS.length]
  return {
    id: 40000 + i,
    month,
    name: g.name,
    image: g.img,
    box: `${g.series}盲盒`,
    token: 1000 + i * 53,
    rare: RARE[i % 4],
    time
  }
})

const onlyRare = ref(false)
const detail = ref(null)

const filterLabel = computed(() => (onlyRare.value ? '只看传说' : '全部记录'))

const filtered = computed(() => (onlyRare.value ? RECORDS.filter((r) => r.rare === '传说') : RECORDS))

const grouped = computed(() => {
  const map = new Map()
  for (const r of filtered.value) {
    if (!map.has(r.month)) map.set(r.month, [])
    map.get(r.month).push(r)
  }
  return [...map.entries()].map(([month, list]) => ({ month, list }))
})

function toggleFilter() {
  onlyRare.value = !onlyRare.value
}


function openDetail(o) {
  detail.value = o
}

</script>