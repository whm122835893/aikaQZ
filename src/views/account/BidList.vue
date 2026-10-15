<template>
  <uni-view data-v-857ee3e0 class="padding-lr">
    <uni-scroll-view data-v-857ee3e0 class="nav">
      <div class="uni-scroll-view">
        <div class="uni-scroll-view" style="overflow: auto hidden;">
          <div class="uni-scroll-view-content">
            <uni-view data-v-857ee3e0
              v-for="(t, i) in tabs"
              :key="t"
              :data-id="i"
              class="cu-item text-gray flex-sub"
              :class="tab === i ? 'text-bold text-black text-lg' : ''"
              @click="tab = i"
            > {{ t }} </uni-view>
          </div>
        </div>
      </div>
    </uni-scroll-view>

    <uni-view data-v-857ee3e0 class="list margin-top-sm padding-bottom">
      <uni-view data-v-857ee3e0
        v-for="o in rows"
        :key="o.id"
        class="bid-item padding-sm radius bg-grey margin-bottom-sm"
        @click="go(o)"
      >
        <uni-view data-v-857ee3e0 class="flex align-center justify-between">
          <uni-view data-v-857ee3e0 class="over bid-name"> {{ o.name }} </uni-view>
          <uni-view data-v-857ee3e0 class="bid-status" :class="statusClass(o.status)"> {{ o.status }} </uni-view>
        </uni-view>
        <uni-view data-v-857ee3e0 class="flex align-center justify-between margin-top-sm">
          <uni-view data-v-857ee3e0 class="text-sm text-gray"> 单号 {{ o.no }} · #{{ o.token }} </uni-view>
          <uni-view data-v-857ee3e0 class="text-sm text-gray"> {{ o.time }} </uni-view>
        </uni-view>
        <uni-view data-v-857ee3e0 class="margin-top-xs bid-price">
          ￥{{ o.price }}
          <uni-text data-v-857ee3e0 class="text-sm text-gray"><span>x{{ o.qty }}</span></uni-text>
        </uni-view>
      </uni-view>

      <uni-view data-v-857ee3e0 v-if="!rows.length" class="flex align-center justify-center" style="height: 50vh;">
        <uni-view data-v-857ee3e0 class="text-center">
          <uni-image data-v-857ee3e0 style="width: 90px; height: 80px;">
            <div style="background-image: url(&quot;/static/images/empty1.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
            <img src="/static/images/empty1.png" draggable="false"></uni-image>
          <uni-view data-v-857ee3e0 class="text-grey margin-top-xs"> 暂无数据 </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
import { computed, ref } from 'vue'
import { pickOrders, BIDDING, DONE, CLOSED, SOLD } from '@/mock/orders'
import { toast } from '@/utils/interact'

const tabs = ['全部', BIDDING, DONE, CLOSED, SOLD]
const tab = ref(0)

const statusMap = {
  全部: [],
  求购中: [BIDDING],
  已成交: [DONE],
  已关闭: [CLOSED],
  已售出: [SOLD]
}

const rows = computed(() => {
  const st = tabs[tab.value]
  const pool = statusMap[st] || []
  // pool 为空数组代表「全部」
  const a = pool.length ? pickOrders('求购订单', pool) : pickOrders('求购订单')
  const b = pool.length ? pickOrders('委托订单', pool) : pickOrders('委托订单')
  return a.concat(b)
})

function statusClass(s) {
  if (s === BIDDING) return 'st-open'
  if (s === CLOSED) return 'st-closed'
  return 'st-done'
}

function go(o) {
  toast('求购单 ' + o.no + ' · ' + o.name)
}
</script>