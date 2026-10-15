<template>
  <uni-view data-v-10af67a2="" class="order-page"><uni-view data-v-10af67a2="" class="page-bg"></uni-view><uni-view data-v-10af67a2="" class="hero-watermark-wrap" style="top: 12px;"><uni-image data-v-10af67a2="" class="hero-watermark"><div style="background-image: url(&quot;/static/images/login/2.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/images/login/2.png" draggable="false"></uni-image></uni-view><uni-view data-v-10af67a2="" class="order-header" style="padding-top: 24px;"><uni-view data-v-10af67a2="" class="header-back"><uni-text data-v-10af67a2="" class="cuIcon-back"><span></span></uni-text></uni-view><uni-view data-v-10af67a2="" class="header-title">订单详情</uni-view><uni-view data-v-10af67a2="" class="header-placeholder"></uni-view></uni-view><uni-view data-v-10af67a2="" class="order-body"><uni-view data-v-10af67a2="" class="order-card"><uni-view data-v-10af67a2="" class="status-row is-pending"><uni-text data-v-10af67a2="" class="cuIcon-timefill status-icon"><span></span></uni-text><uni-text data-v-10af67a2="" class="status-text"><span>待付款</span></uni-text></uni-view><uni-view data-v-10af67a2="" class="pay-label"><uni-text data-v-10af67a2=""><span>支付金额</span></uni-text></uni-view><uni-view data-v-10af67a2="" class="pay-amount"><uni-text data-v-10af67a2="" class="pay-symbol"><span>¥</span></uni-text><uni-text data-v-10af67a2="" class="pay-num"><span>{{ total }}</span></uni-text></uni-view><uni-view data-v-10af67a2="" class="pay-countdown"><uni-text data-v-10af67a2=""><span>支付剩余时间 29:59</span></uni-text></uni-view><uni-view data-v-10af67a2="" class="pay-btn-wrap"><uni-view data-v-10af67a2="" class="pay-btn" data-nav-to="/pages/wallet/wallet1"><uni-text data-v-10af67a2=""><span>立即支付</span></uni-text></uni-view></uni-view></uni-view><uni-view data-v-10af67a2="" class="order-card"><uni-view data-v-10af67a2="" class="section-title"><uni-text data-v-10af67a2=""><span>藏品信息</span></uni-text></uni-view><uni-view data-v-10af67a2="" class="product-main"><uni-image data-v-10af67a2="" class="product-thumb"><div :style="{backgroundImage:'url(' + g.img + ')', backgroundPosition:'center center', backgroundSize:'cover', backgroundRepeat:'no-repeat'}"></div><img :src="g.img" draggable="false"></uni-image><uni-view data-v-10af67a2="" class="product-title">{{ g.name }}</uni-view></uni-view><uni-view data-v-10af67a2="" class="product-extra"><uni-view data-v-10af67a2="" class="product-row"><uni-text data-v-10af67a2="" class="row-label"><span>购买数量</span></uni-text><uni-text data-v-10af67a2="" class="row-value"><span>{{ count }} 份</span></uni-text></uni-view><uni-view data-v-10af67a2="" class="product-row"><uni-text data-v-10af67a2="" class="row-label"><span>单价</span></uni-text><uni-text data-v-10af67a2="" class="row-value"><span>¥{{ g.floor == null ? '--' : Number(g.floor).toFixed(2) }}</span></uni-text></uni-view><uni-view data-v-10af67a2="" class="product-row"><uni-text data-v-10af67a2="" class="row-label"><span>订单编号</span></uni-text><uni-view data-v-10af67a2="" class="value-with-copy"><uni-text data-v-10af67a2="" class="row-value-muted"><span>{{ orderNo }}</span></uni-text><uni-view data-v-10af67a2="" class="copy-divider"></uni-view><uni-text data-v-10af67a2="" class="copy-btn" @click="copyOrderNo"><span>复制</span></uni-text></uni-view></uni-view><uni-view data-v-10af67a2="" class="product-row"><uni-text data-v-10af67a2="" class="row-label"><span>下单时间</span></uni-text><uni-text data-v-10af67a2="" class="row-value-muted"><span>{{ createdAt }}</span></uni-text></uni-view></uni-view></uni-view><uni-view data-v-10af67a2="" class="order-card"><uni-view data-v-10af67a2="" class="section-title"><uni-text data-v-10af67a2=""><span>选择编号</span></uni-text></uni-view><uni-view data-v-10af67a2="" class="home0-table-head"><uni-text data-v-10af67a2="" class="col-index"><span>#</span></uni-text><uni-text data-v-10af67a2="" class="col-no"><span>编号</span></uni-text><uni-text data-v-10af67a2="" class="col-amount"><span>数量</span></uni-text><uni-text data-v-10af67a2="" class="col-status"><span>状态</span></uni-text></uni-view><uni-view data-v-10af67a2="" class="home0-table-row" v-for="row in serials" :key="row.no"><uni-text data-v-10af67a2="" class="col-index"><span>{{ row.idx }}</span></uni-text><uni-text data-v-10af67a2="" class="col-no"><span>{{ row.no }}</span></uni-text><uni-text data-v-10af67a2="" class="col-amount"><span>{{ row.amount }}</span></uni-text><uni-text data-v-10af67a2="" class="col-status"><span>{{ row.status }}</span></uni-text></uni-view><uni-view data-v-10af67a2="" class="home0-detail-label"><uni-text data-v-10af67a2=""><span>共 {{ count }} 份，分配至以下编号</span></uni-text></uni-view></uni-view><uni-view data-v-10af67a2="" class="order-disclaimer"><uni-text data-v-10af67a2=""><span>请在支付剩余时间内完成支付，超时订单将自动取消。本页面为克隆演示版本，支付流程未接入真实通道。</span></uni-text></uni-view><uni-view data-v-10af67a2="" class="cancel-wrap"><uni-view data-v-10af67a2="" class="cancel-btn" data-nav-back><uni-text data-v-10af67a2=""><span>取消订单</span></uni-text></uni-view></uni-view></uni-view><uni-view data-v-10af67a2="" class="order-footer"><uni-view data-v-10af67a2="" class="order-footer-total"><uni-text data-v-10af67a2="" class="total-label"><span>合计</span></uni-text><uni-text data-v-10af67a2="" class="total-symbol"><span>¥</span></uni-text><uni-text data-v-10af67a2="" class="total-amount"><span>{{ total }}</span></uni-text></uni-view><uni-view data-v-10af67a2="" class="order-footer-btn" data-nav-to="/pages/wallet/wallet1"><uni-text data-v-10af67a2=""><span>提交订单</span></uni-text></uni-view></uni-view></uni-view>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getGoods, MAKING_LIST } from '@/mock/goods'
import { toast, isLogin } from '@/utils/interact'

const route = useRoute()
const router = useRouter()

const g = computed(() => getGoods(route.query.id))
const price = computed(() => g.value.floor || 0)
const count = ref(1)
const total = computed(() => (Number(price.value) * count.value).toFixed(2))

const orderNo = computed(() => 'IC' + Date.now().toString().slice(-14))
const createdAt = computed(() => {
  const d = new Date()
  const pad = (n) => String(n).padStart(2, '0')
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`
})

const serials = computed(() => {
  const list = MAKING_LIST(g.value)
  if (!list.length) {
    return [{ idx: 1, no: 'NO.0001', amount: 1, status: '待付款' }]
  }
  const row = list[0]
  return [{ idx: 1, no: '#' + row.no, amount: 1, status: '待付款' }]
})

function copyOrderNo() {
  toast('订单编号已复制')
}

function goBack() {
  router.back()
}

function payNow() {
  if (!isLogin()) return toast('请先登录')
  toast('正在跳转支付…')
}

function cancelOrder() {
  toast('订单已取消')
  router.back()
}
</script>