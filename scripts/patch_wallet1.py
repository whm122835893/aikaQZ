#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wallet1.vue —— 充值页补多档位 + 档位选择联动 + 底部按钮可用"""
import io

P = 'src/views/wallet/Wallet1.vue'
old = io.open(P, encoding='utf-8').read()
V = 'data-v-21f9d0aa=""'

tpl = '''<template>
  <uni-view ''' + V + ''' class="wallet-page" style="padding-top: 0px;">
    <uni-view ''' + V + ''' class="header">
      <uni-view ''' + V + ''' class="back-btn"><uni-text ''' + V + ''' class="cuIcon-back"><span></span></uni-text></uni-view>
      <uni-view ''' + V + ''' class="page-title">我的钱包</uni-view>
      <uni-view ''' + V + ''' class="header-placeholder"></uni-view>
    </uni-view>

    <uni-view ''' + V + ''' class="balance-card">
      <uni-view ''' + V + ''' class="balance-label">当前余额（元）</uni-view>
      <uni-view ''' + V + ''' class="balance-value">{{ balance }}</uni-view>
    </uni-view>

    <uni-view ''' + V + ''' class="section-card">
      <uni-view ''' + V + ''' class="section-title">选择充值金额</uni-view>
      <uni-view ''' + V + ''' class="amount-grid">
        <uni-view v-for="a in AMOUNTS" :key="a" ''' + V + ''' class="amount-item"
          :class="{ active: picked === a }" @click="choose(a)">
          <uni-view ''' + V + ''' class="amount-money">¥{{ money(a) }}</uni-view>
          <uni-view v-if="bonus(a)" ''' + V + ''' class="amount-bonus">送 ¥{{ bonus(a) }}</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view ''' + V + ''' class="section-card">
      <uni-view ''' + V + ''' class="section-title">支付方式</uni-view>
      <uni-view ''' + V + ''' class="pay-list">
        <uni-view v-for="(p, i) in PAYS" :key="p" ''' + V + ''' class="pay-item"
          :class="{ active: pay === i }" @click="pay = i">
          <uni-text ''' + V + ''' :class="['cuIcon-' + p.icon, 'pay-icon']"><span></span></uni-text>
          <uni-view ''' + V + ''' class="pay-name">{{ p.name }}</uni-view>
          <uni-text ''' + V + ''' class="cuIcon-check pay-check"><span></span></uni-text>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view ''' + V + ''' class="bottom-bar">
      <uni-view ''' + V + ''' class="bottom-btn" @click="doRecharge">确定充值 ¥{{ money(picked) }}</uni-view>
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
'''

io.open(P, 'w', encoding='utf-8').write(tpl)
print('Wallet1 rewritten %d -> %d' % (len(old), len(tpl)))