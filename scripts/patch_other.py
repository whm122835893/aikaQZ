#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Other.vue —— 我的收藏：持有/售出 Tab + 藏品/盲盒二级Tab + 列表 + 批量寄售弹层 + 合成结果弹层"""
import io

P = 'src/views/account/Other.vue'
old = io.open(P, encoding='utf-8').read()
V = 'data-v-6f58a460=""'

tpl = '''<template>
  <uni-view ''' + V + ''' class="container" style="min-height: 100vh;">
    <uni-view ''' + V + ''' class="cu-bar flex justify-between align-center pos" style="width: 100%; height: 25px;">
      <uni-view ''' + V + ''' class="action round padding justify-start" style="width: 25px; height: 25px; position: relative; z-index: 10;">
        <uni-view ''' + V + ''' class=""><uni-text ''' + V + ''' class="cuIcon-back text-white"><span></span></uni-text></uni-view>
      </uni-view>
      <uni-view ''' + V + ''' class="text-white text-xl flex-sub text-center" style="margin-left: -15%; font-family: new; font-weight: 500; font-size: 16px;">我的收藏</uni-view>
    </uni-view>

    <uni-view ''' + V + ''' class="flex align-end padding" style="height: 200px; background: url(&quot;../../static/images/index/abg.png&quot;) center center / 100% 100%;">
      <uni-view ''' + V + ''' class="flex align-center">
        <uni-view ''' + V + ''' style="width: 62px; height: 62px;">
          <uni-image ''' + V + ''' class="round margin-bottom-sm" style="width: 62px; height: 62px; border: 2px solid rgb(255, 255, 255);">
            <div style="background-image: url(&quot;/static/images/user/logo.jpg&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;"></div>
            <img src="/static/images/user/logo.jpg" draggable="false"></uni-image>
        </uni-view>
        <uni-view ''' + V + ''' class="margin-left-lg">
          <uni-view ''' + V + ''' class="over text-lg text-white" style="max-width: 150px; font-weight: 600; font-size: 18px;"> {{ uname }} </uni-view>
          <uni-view ''' + V + ''' class="text-sm text-grey margin-top-xs"> 登录后可查看你的数字版权品 </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view ''' + V + ''' class="padding" style="border-radius: 20px 20px 0px 0px; min-height: calc(-200px + 100vh);">
      <uni-view ''' + V + ''' class="top_bar">
        <uni-view ''' + V + ''' class="flex align-start justify-start" style="overflow-x: scroll; font-size: 14px; font-weight: 600;">
          <uni-view v-for="(t, i) in mainTabs" :key="t" ''' + V + ''' class="text-lg text-center padding-lr padding-bottom-sm" :class="main === i ? 'text-black text-bold' : 'text-gray'" @click="setMain(i)">
            {{ t }} <uni-view ''' + V + ''' class="line2"></uni-view>
          </uni-view>
        </uni-view>
      </uni-view>

      <uni-view ''' + V + ''' class="flex justify-between align-center" style="width: 100%; padding: 5px; font-weight: 600; font-size: 13px;">
        <uni-view ''' + V + '''>
          <uni-view ''' + V + ''' class="flex align-start bg-gray2 round">
            <uni-view v-for="(t, i) in subTabs" :key="t" ''' + V + ''' class="padding-xs flex align-center padding-lr-xs" :class="sub === i ? 'bg-white round text-change-blue cust-padding' : ''" @click="sub = i">
              <uni-view ''' + V + ''' class="over padding-lr-xs" style="transition: 0.3s;"> {{ t }} </uni-view>
            </uni-view>
          </uni-view>
        </uni-view>
        <uni-view ''' + V + ''' class="flex">
          <uni-view ''' + V + ''' class="flex align-center" @click="openSell">
            <uni-text ''' + V + ''' class="cuIcon-round" style="font-size: 15px; margin-top: 2px;"><span></span></uni-text>
            <uni-view ''' + V + ''' class="margin-left-xs"> 可合成 </uni-view>
          </uni-view>
          <uni-view ''' + V + ''' class="margin-left" @click="toSearch">
            <uni-text ''' + V + ''' class="cuIcon-search text-bold"><span></span></uni-text>
          </uni-view>
        </uni-view>
      </uni-view>

      <uni-view ''' + V + ''' class="margin-top flex flex-wrap own-list">
        <uni-view v-for="g in rows" :key="g.id" ''' + V + ''' class="own-item" @click="openDetail(g)">
          <uni-view ''' + V + ''' class="own-thumb" :style="bgImg(g.img)"></uni-view>
          <uni-view ''' + V + ''' class="own-name">{{ g.name }}</uni-view>
          <uni-view ''' + V + ''' class="own-meta">#{{ g.id }} · 剩 {{ g.circ }} </uni-view>
        </uni-view>
      </uni-view>

      <uni-view v-if="!rows.length" ''' + V + ''' class="flex align-center justify-center" style="height: 50vh;">
        <uni-view class="text-center">
          <uni-image style="width: 90px; height: 80px;">
            <div style="background-image: url(&quot;/static/images/empty1.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
            <img src="/static/images/empty1.png" draggable="false"></uni-image>
          <uni-view class="text-grey margin-top-xs"> 暂无数据 </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <!-- 藏品详情抽屉 -->
    <uni-view ''' + V + ''' class="cu-modal bottom-modal" :class="{ show: !!detail }">
      <uni-view ''' + V + ''' class="cu-dialog bg-white" style="border-radius: 19px 19px 0px 0px;">
        <uni-view ''' + V + ''' class="padding-sm text-left" @click="detail = null">
          <uni-view ''' + V + ''' class="flex align-center justify-between margin-top-sm">
            <uni-view ''' + V + ''' class="flex align-center">
              <uni-view ''' + V + ''' class="margin-left">
                <uni-view ''' + V + ''' class="over text-lg" style="font-weight: 500; font-size: 18px; color: rgb(34, 34, 34);"> {{ detail ? detail.name : '' }} </uni-view>
                <uni-view ''' + V + ''' class="text-sm text-grey" style="font-weight: 400; font-size: 11px; color: rgb(102, 102, 102); margin-top: 5px;">持有: {{ detail ? detail.circ : 0 }} 个</uni-view>
              </uni-view>
            </uni-view>
            <uni-image ''' + V + ''' style="width: 24px; height: 24px;">
              <div style="background-image: url(&quot;/static/images/user/close.png&quot;); background-position: 0% 0%; background-size: 100% 100%; background-repeat: no-repeat;"></div>
              <img src="/static/images/user/close.png" draggable="false"></uni-image>
          </uni-view>
          <uni-view ''' + V + ''' class="margin-top-sm flex">
            <uni-view ''' + V + ''' class="cu-btn lg bg-gray radius margin-right flex-sub" @click="detail = null"> 返回 </uni-view>
            <uni-view ''' + V + ''' class="cu-btn lg btn-action-yellow radius flex-sub" @click="openSell"> 寄售 </uni-view>
          </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <!-- 批量寄售 -->
    <uni-view ''' + V + ''' class="cu-modal" :class="{ show: sheet === 'sell' }">
      <uni-view ''' + V + ''' class="cu-dialog bg-white text-left padding radius">
        <uni-view ''' + V + ''' class="text-center text-bold text-lg">批量寄售</uni-view>
        <uni-view ''' + V + ''' class="margin-top">
          <uni-view ''' + V + '''>寄售价格</uni-view>
          <uni-view ''' + V + ''' class="padding-sm margin-top radius bg-gray">
            <uni-input ''' + V + '''>
              <div class="uni-input-wrapper">
                <div class="uni-input-placeholder text-df">请输入价格</div>
                <input maxlength="140" class="uni-input-input" :value="price" @input="onPrice($event.target.value)" />
              </div>
            </uni-input>
          </uni-view>
        </uni-view>
        <uni-view ''' + V + ''' class="margin-top flex align-center justify-between">
          <uni-view ''' + V + ''' class="text-grey">预计收益</uni-view>
          <uni-view ''' + V + ''' class="text-bold">￥ {{ net }}</uni-view>
        </uni-view>
        <uni-view ''' + V + ''' class="margin-top-sm flex align-center justify-between">
          <uni-view ''' + V + ''' class="text-grey">服务费(5%)</uni-view>
          <uni-view ''' + V + ''' class="text-bold">￥ {{ fee }}</uni-view>
        </uni-view>
        <uni-view ''' + V + ''' class="padding margin-top">
          <uni-view ''' + V + ''' class="flex">
            <uni-view ''' + V + ''' class="cu-btn lg bg-gray radius margin-right flex-sub" @click="sheet = ''">返回</uni-view>
            <uni-view ''' + V + ''' class="cu-btn lg bg-gradual-grey radius flex-sub" @click="submitSell">寄售</uni-view>
          </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <!-- 合成结果 -->
    <uni-view ''' + V + ''' class="cu-modal" :class="{ show: sheet === 'mix' }">
      <uni-view ''' + V + ''' class="cu-dialog bg-white">
        <uni-view ''' + V + ''' class="padding">
          <uni-view ''' + V + '''>开启结果</uni-view>
          <uni-view ''' + V + ''' class="margin-top">
            <uni-view ''' + V + ''' class="radius" style="width: 150px; height: 150px;" :style="bgImg(mixImg)">
              <div :style="bgImg(mixImg)"></div>
            </uni-view>
          </uni-view>
          <uni-view ''' + V + ''' class="margin-top-sm"> {{ mixName }} </uni-view>
          <uni-view ''' + V + ''' class="flex margin-top">
            <uni-view ''' + V + ''' class="cu-btn round margin-lr-xl lg flex-sub bg-black text-green" @click="sheet = ''">确定</uni-view>
          </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view ''' + V + ''' style="height: 80px;"></uni-view>
  </uni-view>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { GOODS } from '@/mock/goods'
import { authUser, isLogin, toast } from '@/utils/interact'

const router = useRouter()

const mainTabs = ['持有资产', '售出资产']
const subTabs = ['藏品', '盲盒']
const main = ref(0)
const sub = ref(0)

const sheet = ref('')
const detail = ref(null)
const price = ref('')

const uname = computed(() => {
  const u = authUser.value
  return u ? u.name || 'ICARD用户' + String(u.phone || '').slice(-4) : '未登录'
})

/** 演示数据：前 6 条作持有，后 6 条作售出；盲盒 Tab 走收藏数靠前的 4 条 */
const rows = computed(() => {
  const pool = main.value === 0 ? GOODS.slice(0, 6) : GOODS.slice(6, 12)
  if (sub.value === 1) return pool.slice(0, 4)
  return pool
})

const fee = computed(() => (Number(price.value || 0) * 0.05).toFixed(2))
const net = computed(() => (Number(price.value || 0) * 0.95).toFixed(2))

const mixImg = computed(() => (detail.value ? detail.value.img : GOODS[0].img))
const mixName = computed(() => (detail.value ? detail.value.name : GOODS[0].name))

function bgImg(url) {
  if (!url) return {}
  return { backgroundImage: 'url(' + url + ')', backgroundPosition: 'center center', backgroundSize: 'cover', backgroundRepeat: 'no-repeat' }
}

function setMain(i) {
  main.value = i
  sub.value = 0
}

function openDetail(g) {
  detail.value = g
}

function onPrice(v) {
  price.value = String(v).replace(/[^\\d.]/g, '').slice(0, 10)
}

function openSell() {
  if (!isLogin()) return toast('请先登录')
  detail.value = null
  sheet.value = 'sell'
}

function submitSell() {
  const p = Number(price.value)
  if (!(p > 0)) return toast('请输入寄售价格')
  toast('已提交批量寄售，单价￥' + p.toFixed(2))
  sheet.value = ''
  price.value = ''
}

function toSearch() {
  router.push('/pages/market/market')
}

/** 顶部「可合成」：从选中藏品里开一个结果 */
const mixEntry = ref('')
function openMix() {
  if (!isLogin()) return toast('请先登录')
  if (!rows.value.length) return toast('暂无可合成的藏品')
  mixEntry.value = rows.value[0].name
  detail.value = rows.value[0]
  sheet.value = 'mix'
}
</script>
'''

io.open(P, 'w', encoding='utf-8').write(tpl)
print('Other rewritten %d -> %d' % (len(old), len(tpl)))