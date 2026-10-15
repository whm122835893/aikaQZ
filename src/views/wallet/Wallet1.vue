<template>
  <uni-view data-v-21f9d0aa="" class="wallet-page" style="padding-top: 0px;">
    <uni-view data-v-21f9d0aa="" class="header">
      <uni-view data-v-21f9d0aa="" class="back-btn"><uni-text data-v-21f9d0aa="" class="cuIcon-back"><span></span></uni-text></uni-view>
      <uni-view data-v-21f9d0aa="" class="page-title">我的钱包</uni-view>
      <uni-view data-v-21f9d0aa="" class="header-placeholder"></uni-view>
    </uni-view>

    <uni-view data-v-21f9d0aa="" class="balance-card">
      <uni-view data-v-21f9d0aa="" class="balance-label">当前余额（元）</uni-view>
      <uni-view data-v-21f9d0aa="" class="balance-value">{{ balance }}</uni-view>
    </uni-view>

    <uni-view data-v-21f9d0aa="" class="section-card">
      <uni-view data-v-21f9d0aa="" class="section-title">选择充值金额</uni-view>
      <uni-view data-v-21f9d0aa="" class="amount-grid">
        <uni-view v-for="a in AMOUNTS" :key="a" data-v-21f9d0aa="" class="amount-item"
          :class="{ active: picked === a }" @click="choose(a)">
          <uni-view data-v-21f9d0aa="" class="amount-money">¥{{ money(a) }}</uni-view>
          <uni-view v-if="bonus(a)" data-v-21f9d0aa="" class="amount-bonus">送 ¥{{ bonus(a) }}</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view data-v-21f9d0aa="" class="section-card">
      <uni-view data-v-21f9d0aa="" class="section-title">支付方式</uni-view>
      <uni-view data-v-21f9d0aa="" class="pay-list">
        <uni-view v-for="(p, i) in PAYS" :key="p" data-v-21f9d0aa="" class="pay-item"
          :class="{ active: pay === i }" @click="pay = i">
          <uni-text data-v-21f9d0aa="" :class="['cuIcon-' + p.icon, 'pay-icon']"><span></span></uni-text>
          <uni-view data-v-21f9d0aa="" class="pay-name">{{ p.name }}</uni-view>
          <uni-text data-v-21f9d0aa="" class="cuIcon-check pay-check"><span></span></uni-text>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view data-v-21f9d0aa="" class="bottom-bar">
      <uni-view data-v-21f9d0aa="" class="bottom-btn" @click="doRecharge">确定充值 ¥{{ money(picked) }}</uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { authUser, isLogin, toast } from '@/utils/interact'

const router = useRouter()

/** 档位（分），展示时格式化为元 */
const AMOUNTS = [8, 18, 38, 68, 128, 288]
const PAYS = [
  { name: '微信支付', icon: 'weixin' },
  { name: '支付宝', icon: 'zhifubao' },
  { name: '余额支付', icon: 'wallet' }
]

const picked = ref(8)
const pay = ref(0)
const paid = ref(0)

const balance = computed(() => (Number(pick(paid.value)) || 0).toFixed(2))

function pick(v) {
  const n = Number(v)
  return Number.isFinite(n) && n > 0 ? n : 8
}

function money(v) {
  return pick(v).toFixed(2)
}

/** 满 100 送 10，满 200 送 30 */
function bonus(v) {
  const n = pick(v)
  if (n >= 200) return 30
  if (n >= 100) return 10
  return 0
}

function choose(v) {
  picked.value = pick(v)
}

function doRecharge() {
  if (!isLogin()) {
    toast('请先登录')
    setTimeout(() => router.replace('/pages/login/login'), 800)
    return
  }
  const amt = pick(picked.value)
  paid.value = paid.value + amt
  toast('充值成功 ¥' + money(amt) + '，余额 ' + balance.value)
  picked.value = AMOUNTS[0]
}
</script>
