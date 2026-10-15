<template>
  <uni-view data-v-67ad99a6 class="padding">
    <uni-view v-if="rows.length" data-v-67ad99a6>
      <uni-view
        v-for="o in rows"
        :key="o.id"
        data-v-67ad99a6
        class="mix-record-item"
        @click="openDetail(o)"
      >
        <uni-view data-v-67ad99a6 class="mix-record-head">
          <uni-text data-v-67ad99a6 class="mix-record-time"><span>{{ o.time }}</span></uni-text>
          <uni-text data-v-67ad99a6 class="mix-record-state"><span>{{ o.state }}</span></uni-text>
        </uni-view>
        <uni-view data-v-67ad99a6 class="mix-record-body">
          <uni-image data-v-67ad99a6 class="mix-record-img">
            <div :style="`background-image: url(&quot;${o.image}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div>
            <img :src="o.image" alt="" draggable="false" />
          </uni-image>
          <uni-view data-v-67ad99a6 class="mix-record-info">
            <uni-view data-v-67ad99a6 class="mix-record-name">{{ o.name }}</uni-view>
            <uni-view data-v-67ad99a6 class="mix-record-from">消耗 {{ o.from.length }} 份合成</uni-view>
          </uni-view>
          <uni-view data-v-67ad99a6 class="mix-record-token">#{{ o.token }}</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view
      v-else
      data-v-4d930ea0
      data-v-67ad99a6
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

    <!-- 合成详情弹层 -->
    <uni-view data-v-67ad99a6 class="cu-modal bottom-modal" :class="{ show: !!detail }">
      <uni-view data-v-67ad99a6 class="cu-dialog bg-white mix-sheet">
        <uni-view data-v-67ad99a6 class="mix-sheet-title">合成详情</uni-view>
        <uni-view v-if="detail" data-v-67ad99a6 class="mix-sheet-body">
          <uni-view data-v-67ad99a6 class="mix-sheet-line">合成获得：{{ detail.name }}</uni-view>
          <uni-view data-v-67ad99a6 class="mix-sheet-label">消耗材料</uni-view>
          <uni-view
            v-for="(m, i) in detail.from"
            :key="i"
            data-v-67ad99a6
            class="mix-sheet-mat"
          >{{ m }}</uni-view>
          <uni-view data-v-67ad99a6 class="mix-row"><uni-text data-v-67ad99a6><span>链上编号</span></uni-text><uni-text data-v-67ad99a6 class="mix-row-v"><span>#{{ detail.token }}</span></uni-text></uni-view>
          <uni-view data-v-67ad99a6 class="mix-row"><uni-text data-v-67ad99a6><span>状态</span></uni-text><uni-text data-v-67ad99a6 class="mix-row-v"><span>{{ detail.state }}</span></uni-text></uni-view>
          <uni-view data-v-67ad99a6 class="mix-row"><uni-text data-v-67ad99a6><span>时间</span></uni-text><uni-text data-v-67ad99a6 class="mix-row-v"><span>{{ detail.time }}</span></uni-text></uni-view>
        </uni-view>
        <uni-view data-v-67ad99a6 class="mix-sheet-footer">
          <uni-view data-v-67ad99a6 class="mix-sheet-btn" @click="detail = null">关闭</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
/**
 * 合成记录（mix/Records）
 * 源站只有一层 .padding + 永久「暂无数据」，没有任何数据与事件。
 * 克隆版补齐：6 条合成记录 + 详情弹层（展开消耗材料清单）。
 */
import { ref } from 'vue'
import { GOODS } from '@/mock/goods'

const SEED = [
  ['2026-10-08 21:14', '已到账', 2],
  ['2026-10-02 15:37', '已到账', 4],
  ['2026-09-26 11:08', '合成中', 1],
  ['2026-09-18 19:52', '已到账', 3],
  ['2026-09-09 10:21', '已到账', 5],
  ['2026-08-31 16:44', '合成中', 0]
]

const rows = ref(
  SEED.map(([time, state, gi], i) => {
    const g = GOODS[gi % GOODS.length]
    const from = [
      `${GOODS[(gi + 1) % GOODS.length].name} #${1000 + i * 7}`,
      `${GOODS[(gi + 2) % GOODS.length].name} #${1100 + i * 7}`
    ]
    return {
      id: 60000 + i,
      name: g.name,
      image: g.img,
      token: 2000 + i * 31,
      time,
      state,
      from
    }
  })
)

const detail = ref(null)

function openDetail(o) {
  detail.value = o
}
</script>