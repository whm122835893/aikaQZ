<template>
  <uni-view data-v-7144ea85 class="padding-lr text-white">
    <uni-scroll-view data-v-7144ea85 class="nav">
      <div class="uni-scroll-view">
        <div class="uni-scroll-view" style="overflow: auto hidden;">
          <div class="uni-scroll-view-content">
            <uni-view data-v-7144ea85
              v-for="(t, i) in tabs"
              :key="t.label"
              :data-id="i"
              class="cu-item text-gray flex-sub"
              :class="tab === i ? 'text-bold text-white' : ''"
              @click="tab = i"
            >
              {{ t.label }}
              <uni-view data-v-7144ea85 class="line"></uni-view>
            </uni-view>
          </div>
        </div>
      </div>
    </uni-scroll-view>

    <uni-view data-v-7144ea85 class="list">
      <uni-view data-v-7144ea85
        v-for="o in rows"
        :key="o.id"
        class="item padding-sm radius bg-grey margin-bottom-sm"
        @click="go(o)"
      >
        <uni-view data-v-7144ea85 class="text-sm text-right" :class="o.status === UNPAID ? 'text-orange' : ''">
          {{ o.status }}
        </uni-view>
        <uni-view data-v-7144ea85 class="flex align-center">
          <uni-view data-v-7144ea85 style="width: 210px;">
            <uni-view data-v-7144ea85 class="over"> {{ o.name }} </uni-view>
            <uni-view data-v-7144ea85 class="flex align-center margin-top-sm">
              <uni-view data-v-7144ea85 class="round bg-orange flex align-center justify-center text-black" style="width: 20px; height: 20px;">
                <uni-text data-v-7144ea85 class="cuIcon-cardboardfill"><span></span></uni-text>
              </uni-view>
              <uni-view data-v-7144ea85 class="text-black bg-orange padding-lr-sm flex align-center justify-center" style="height: 15px; margin-left: -2px; position: relative; z-index: 0; border-radius: 5px;">
                #{{ o.token }}
              </uni-view>
            </uni-view>
            <uni-view data-v-7144ea85 class="margin-top-xs">
              <uni-text data-v-7144ea85><span>￥</span></uni-text>
              <uni-text data-v-7144ea85 class="text-xl text-bold" style="font-family: new;"><span>{{ o.price }}</span></uni-text>
            </uni-view>
            <uni-view data-v-7144ea85 class="text-right text-sm text-gray"> {{ o.time }} </uni-view>
          </uni-view>
        </uni-view>
      </uni-view>

      <uni-view data-v-7144ea85 v-if="!rows.length" class="empty-box"> 暂无数据 </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
import { computed, ref } from 'vue'
import { pickOrders, UNPAID, PAID, CLOSED, CANCELED, SHIPPED } from '@/mock/orders'
import { toast } from '@/utils/interact'

/* 「已关闭」Tab 需要同时容纳「已关闭」和「订单取消」两种终态，
   否则常规交易里唯一的关闭单（状态是 订单取消）会查不到，Tab 显示为空。 */
const tabs = [
  { label: UNPAID, statuses: [UNPAID] },
  { label: PAID, statuses: [PAID, SHIPPED] },
  { label: CLOSED, statuses: [CLOSED, CANCELED] }
]
const tab = ref(0)

/** 只取常规交易这一类订单 */
const rows = computed(() => pickOrders('常规交易', tabs[tab.value].statuses))

function go(o) {
  if (o.status === UNPAID) {
    toast('订单 ' + o.no + ' 待支付，演示环境不真实扣款')
    return
  }
  toast('订单 ' + o.no + ' · ' + o.name)
}
</script>