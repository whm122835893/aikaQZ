<template>
  <uni-view data-v-5aae308f class="page">
    <uni-view data-v-5aae308f class="cu-bar flex justify-between align-center" style="width: 100%; height: 25px;">
      <uni-view data-v-5aae308f class="action bg-white round padding justify-start" style="width: 25px; height: 25px; position: relative; z-index: 10;">
        <uni-view data-v-5aae308f class="back-btn">
          <uni-text data-v-5aae308f class="cuIcon-back text-black"><span></span></uni-text>
        </uni-view>
      </uni-view>
      <uni-view data-v-5aae308f class="text-black text-xl flex-sub text-center" style="margin-left: -15%; font-family: new; font-weight: 500; font-size: 16px;">寄售记录</uni-view>
    </uni-view>

    <uni-view data-v-5aae308f class="content padding">
      <uni-view v-if="rows.length" data-v-5aae308f class="consign-record-list">
        <uni-view v-for="r in rows" :key="r.id" data-v-5aae308f class="consign-record-item">
          <uni-view data-v-5aae308f>
            <uni-view data-v-5aae308f class="consign-record-name">{{ r.name }}</uni-view>
            <uni-view data-v-5aae308f class="consign-record-time">{{ r.time }}</uni-view>
          </uni-view>
          <uni-view data-v-5aae308f class="consign-record-price">寄售￥{{ r.price }}</uni-view>
        </uni-view>
      </uni-view>

      <uni-view v-else data-v-5aae308f class="consign-record-empty">暂无寄售记录</uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
/**
 * 寄售记录页 /pages/market/Consignment
 * 源站为纯静态空壳：只有 1 条写死的 name / 寄售￥985，无数据源、无交互。
 * 克隆版补齐 6 条寄售记录（名称 + 时间 + 金额）。
 */
import { ref } from 'vue'
import { GOODS } from '@/mock/goods'

const rows = ref(
  GOODS.slice(0, 6).map((g, i) => ({
    id: g.id,
    name: g.name,
    price: Number(g.floor || 188).toFixed(0),
    time: `2026-09-${String(16 - i * 2).padStart(2, '0')} 05:06:30`
  }))
)
</script>
