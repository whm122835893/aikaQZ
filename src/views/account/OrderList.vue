<template>
  <uni-view data-v-38529c3e class="order-page">
    <uni-view data-v-38529c3e class="page-bg"></uni-view>
    <uni-view data-v-38529c3e class="hero-watermark-wrap" style="top: 12px;">
      <uni-image data-v-38529c3e class="hero-watermark">
        <div style="background-image: url(&quot;/static/images/login/2.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div>
        <img src="/static/images/login/2.png" draggable="false"></uni-image>
    </uni-view>

    <uni-view data-v-38529c3e class="order-sticky-header" style="padding-top: 24px;">
      <uni-view data-v-38529c3e class="header">
        <uni-view data-v-38529c3e class="back-btn"><uni-text data-v-38529c3e class="cuIcon-back"><span></span></uni-text></uni-view>
        <uni-view data-v-38529c3e class="page-title">我的订单</uni-view>
        <uni-view data-v-38529c3e class="header-placeholder"></uni-view>
      </uni-view>

      <uni-scroll-view data-v-38529c3e class="tab-bar-scroll">
        <div class="uni-scroll-view">
          <div class="uni-scroll-view" style="overflow: auto hidden;">
            <div class="uni-scroll-view-content">
              <uni-view data-v-38529c3e class="tab-bar-inner">
                <uni-view data-v-38529c3e
                  v-for="t in topTabs"
                  :id="'top-tab-' + t.id"
                  :key="t.id"
                  class="tab-item"
                  :class="{ active: top === t.id }"
                  @click="setTop(t.id)"
                >
                  <uni-text data-v-38529c3e><span>{{ t.label }}</span></uni-text>
                  <uni-view data-v-38529c3e class="tab-line"></uni-view>
                </uni-view>
              </uni-view>
            </div>
          </div>
        </div>
      </uni-scroll-view>

      <uni-scroll-view data-v-38529c3e class="sub-tab-bar-scroll">
        <div class="uni-scroll-view">
          <div class="uni-scroll-view" style="overflow: auto hidden;">
            <div class="uni-scroll-view-content">
              <uni-view data-v-38529c3e class="sub-tab-capsule-wrap">
                <uni-view data-v-38529c3e class="sub-tab-capsule">
                  <uni-view data-v-38529c3e
                    v-for="(st, i) in subTabs"
                    :id="'sub-tab-' + i"
                    :key="st"
                    class="sub-tab-item"
                    :class="{ active: sub === i }"
                    @click="sub = i"
                  >
                    <uni-text data-v-38529c3e><span>{{ st }}</span></uni-text>
                  </uni-view>
                </uni-view>
              </uni-view>
            </div>
          </div>
        </div>
      </uni-scroll-view>
    </uni-view>

    <uni-scroll-view data-v-38529c3e class="order-scroll-body" style="top: 162px; height: 650px;">
      <div class="uni-scroll-view">
        <div class="uni-scroll-view" style="overflow: hidden auto;">
          <div class="uni-scroll-view-content">
            <div class="uni-scroll-view-refresher" style="background-color: transparent; height: 0px;">
              <uni-view data-v-38529c3e class="refresher-slot" style="height: 54px; min-height: 54px;">
                <uni-image data-v-38529c3e class="refresher-slot__icon" style="width: 36px; height: 36px;">
                  <div style="background-image: url(&quot;/static/icard.gif&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div>
                  <img src="/static/icard.gif" draggable="false"></uni-image>
              </uni-view>
            </div>

            <uni-view data-v-38529c3e class="order-list-wrap">
              <uni-view data-v-38529c3e class="order-list">
                <uni-view data-v-38529c3e v-for="o in rows" :key="o.id" class="order-item" @click="openDetail(o)">
                  <uni-view data-v-38529c3e class="order-item-head">
                    <uni-text data-v-38529c3e class="order-item-no"><span>订单编号：{{ o.no }}</span></uni-text>
                    <uni-text data-v-38529c3e class="order-item-status" :class="statusClass(o.status)"><span>{{ o.status }}</span></uni-text>
                  </uni-view>
                  <uni-view data-v-38529c3e class="order-item-body">
                    <uni-view data-v-38529c3e class="order-thumb" :style="bgImg(goodsOf(o))"></uni-view>
                    <uni-view data-v-38529c3e class="order-info">
                      <uni-view data-v-38529c3e class="over order-name">{{ o.name }}</uni-view>
                      <uni-view data-v-38529c3e class="order-token">#{{ o.token }} · 数量 {{ o.qty }}</uni-view>
                      <uni-view data-v-38529c3e class="order-time">{{ o.time }}</uni-view>
                    </uni-view>
                    <uni-view data-v-38529c3e class="order-price">
                      ￥<uni-text data-v-38529c3e class="text-xl text-bold"><span>{{ o.price }}</span></uni-text>
                    </uni-view>
                  </uni-view>
                </uni-view>
              </uni-view>

              <uni-view data-v-38529c3e v-if="!rows.length" class="flex align-center justify-center" style="height: 50vh;">
                <uni-view data-v-38529c3e class="text-center">
                  <uni-image data-v-38529c3e style="width: 90px; height: 80px;">
                    <div style="background-image: url(&quot;/static/images/empty1.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
                    <img src="/static/images/empty1.png" draggable="false"></uni-image>
                  <uni-view data-v-38529c3e class="text-grey margin-top-xs"> 暂无数据 </uni-view>
                </uni-view>
              </uni-view>
            </uni-view>
          </div>
        </div>
      </div>
    </uni-scroll-view>

    <uni-view data-v-38529c3e class="cu-modal bottom-modal" :class="{ show: !!detail }">
      <uni-view data-v-38529c3e class="cu-dialog bg-white">
        <uni-view data-v-38529c3e class="padding text-left" @click="detail = null">
          <uni-view data-v-38529c3e class="flex align-center justify-between">
            <uni-view data-v-38529c3e class="text-grey"> 订单编号: {{ detail ? detail.no : '' }} </uni-view>
            <uni-text data-v-38529c3e class="cuIcon-close"><span></span></uni-text>
          </uni-view>

          <uni-view data-v-38529c3e class="flex align-center justify-between margin-top-sm">
            <uni-view data-v-38529c3e class="flex align-center">
              <uni-view data-v-38529c3e class="radius order-thumb" :style="bgImg(goodsOf(detail))"></uni-view>
              <uni-view data-v-38529c3e class="margin-left padding-top">
                <uni-view data-v-38529c3e class="over text-lg">{{ detail ? detail.name : '' }}</uni-view>
                <uni-view data-v-38529c3e class="margin-top-xl text-black"> ￥{{ detail ? detail.price : '0.00' }} </uni-view>
              </uni-view>
            </uni-view>
          </uni-view>

          <uni-view data-v-38529c3e class="flex align-center justify-between margin-top">
            <uni-view data-v-38529c3e class="text-grey"> 接收人区块链地址 </uni-view>
            <uni-view data-v-38529c3e class="text-black">{{ detail ? detail.token : 0 }}</uni-view>
          </uni-view>

          <uni-view data-v-38529c3e class="margin-top-xl flex align-center justify-center" @click="goPay">
            <uni-view data-v-38529c3e class="cu-btn lg btn-action-yellow radius pay-btn">{{ actionText }}</uni-view>
          </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
import { computed, ref } from 'vue'
import { pickOrders, UNPAID, PAID, CANCELED } from '@/mock/orders'
import { GOODS } from '@/mock/goods'
import { toast } from '@/utils/interact'

/** 主 Tab：id 对应源站 top-tab-N 的 N */
const topTabs = [
  { id: 1, label: '首发订单' },
  { id: 2, label: '常规交易' },
  { id: 4, label: '求购订单' },
  { id: 7, label: '委托订单' },
  { id: 3, label: '盲盒订单' }
]

const top = ref(1)
const sub = ref(0)
const detail = ref(null)

const subTabs = computed(() => ['全部', UNPAID, PAID, CANCELED])

const statusMap = {
  待付款: [UNPAID],
  已支付: [PAID],
  订单取消: [CANCELED],
  已关闭: [],
  已成交: [],
  已售出: [],
  求购中: [],
  待发货: [UNPAID],
  已收货: [PAID]
}

const rows = computed(() => {
  const t = topTabs.find((x) => x.id === top.value)
  const st = subTabs.value[sub.value]
  if (st === '全部') return pickOrders(t.label)
  const pool = statusMap[st]
  if (!pool || !pool.length) return []
  return pickOrders(t.label, pool)
})

const actionText = computed(() => (detail.value && detail.value.status === UNPAID ? '去支付' : '关闭'))

function bgImg(url) {
  if (!url) return {}
  return { backgroundImage: 'url(' + url + ')', backgroundPosition: 'center center', backgroundSize: 'cover', backgroundRepeat: 'no-repeat' }
}

function goodsOf(o) {
  if (!o) return ''
  const i = (o.token % GOODS.length + GOODS.length) % GOODS.length
  return GOODS[i].img
}

function statusClass(s) {
  if (s === UNPAID) return 'st-unpaid'
  if (s === CANCELED || s === '已关闭') return 'st-closed'
  return 'st-paid'
}

function setTop(id) {
  if (top.value === id) return
  top.value = id
  sub.value = 0
}

function openDetail(o) {
  detail.value = o
}

function goPay() {
  if (!detail.value) return
  if (detail.value.status !== UNPAID) {
    detail.value = null
    return
  }
  toast('已跳转收银台（演示环境不真实扣款）')
  detail.value = null
}
</script>