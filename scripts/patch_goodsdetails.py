#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GoodsDetails.vue —— 空壳页补全：真实藏品 + 寄售/转赠/购买三个弹层"""
import io

P = 'src/views/market/GoodsDetails.vue'
old = io.open(P, encoding='utf-8').read()
V = 'data-v-58d8ffe2=""'

tpl = '''<template>
  <uni-view ''' + V + ''' class="detail-page">
    <uni-view ''' + V + ''' class="page-header" style="padding-top: 12px;">
      <uni-view ''' + V + ''' class="header-back"><uni-text ''' + V + ''' class="cuIcon-back"><span></span></uni-text></uni-view>
      <uni-view ''' + V + ''' class="header-title">藏品详情</uni-view>
      <uni-view ''' + V + ''' class="header-fav" @click="faved = !faved">
        <uni-text ''' + V + ''' class="cuIcon-star" :class="{ 'cuIcon-starfill faved': faved }"><span></span></uni-text>
      </uni-view>
    </uni-view>

    <uni-view ''' + V + ''' class="hero-section">
      <uni-image ''' + V + ''' class="hero-bg" style="height: 384px;">
        <div style="background-image: url(&quot;/static/images/market/icon/bg.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
        <img src="/static/images/market/icon/bg.png" draggable="false"></uni-image>
      <uni-view ''' + V + ''' class="hero-watermark-wrap" style="top: 12px;">
        <uni-image ''' + V + ''' class="hero-watermark">
          <div style="background-image: url(&quot;/static/images/login/2.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div>
          <img src="/static/images/login/2.png" draggable="false"></uni-image>
      </uni-view>
      <uni-view ''' + V + ''' class="hero-podium-wrap">
        <uni-view ''' + V + ''' class="hero-cover-stage">
          <uni-image ''' + V + ''' class="hero-cover hero-cover-3d" :style="bgImg(g.img)">
            <div :style="bgImg(g.img)"></div>
          </uni-image>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view ''' + V + ''' class="page-body">
      <uni-view ''' + V + ''' id="header-anchor" class="info-card">
        <uni-view ''' + V + ''' class="info-title"> {{ g.name }} </uni-view>
        <uni-view ''' + V + ''' class="info-capsules">
          <uni-view ''' + V + ''' class="info-capsule">
            <uni-view ''' + V + ''' class="capsule-label">发行</uni-view>
            <uni-view ''' + V + ''' class="capsule-value">{{ g.issued }}份</uni-view>
          </uni-view>
          <uni-view ''' + V + ''' class="info-capsule">
            <uni-view ''' + V + ''' class="capsule-label">流通</uni-view>
            <uni-view ''' + V + ''' class="capsule-value">{{ g.circ }}份</uni-view>
          </uni-view>
          <uni-view ''' + V + ''' class="info-capsule">
            <uni-view ''' + V + ''' class="capsule-label">地板价</uni-view>
            <uni-view ''' + V + ''' class="capsule-value">{{ floorText }}</uni-view>
          </uni-view>
        </uni-view>
        <uni-view ''' + V + ''' class="meta-list">
          <uni-view ''' + V + ''' class="meta-row">
            <uni-text ''' + V + ''' class="meta-label"><span>藏品编号</span></uni-text>
            <uni-view ''' + V + ''' class="meta-right"><uni-text ''' + V + ''' class="meta-value"><span>#{{ g.id }}</span></uni-text></uni-view>
          </uni-view>
          <uni-view ''' + V + ''' class="meta-row">
            <uni-text ''' + V + ''' class="meta-label"><span>创作者</span></uni-text>
            <uni-view ''' + V + ''' class="meta-right">
              <uni-image ''' + V + ''' class="brand-row-avatar">
                <div style="background-image: url(&quot;/static/images/invite/top1.png&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;"></div>
                <img src="/static/images/invite/top1.png" draggable="false"></uni-image>
              <uni-text ''' + V + ''' class="brand-row-name"><span>{{ g.author }}</span></uni-text>
            </uni-view>
          </uni-view>
          <uni-view ''' + V + ''' class="meta-row">
            <uni-text ''' + V + ''' class="meta-label"><span>品牌方</span></uni-text>
            <uni-view ''' + V + ''' class="meta-right">
              <uni-image ''' + V + ''' class="brand-row-avatar">
                <div style="background-image: url(&quot;/static/images/invite/top1.png&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;"></div>
                <img src="/static/images/invite/top1.png" draggable="false"></uni-image>
              <uni-text ''' + V + ''' class="brand-row-name"><span>{{ g.series }}</span></uni-text>
            </uni-view>
          </uni-view>
          <uni-view ''' + V + ''' class="meta-row">
            <uni-text ''' + V + ''' class="meta-label"><span>持有者</span></uni-text>
            <uni-view ''' + V + ''' class="meta-right"><uni-text ''' + V + ''' class="meta-value"><span>{{ g.holder }} 人</span></uni-text></uni-view>
          </uni-view>
        </uni-view>
      </uni-view>

      <uni-view ''' + V + ''' class="detail-section">
        <uni-view ''' + V + ''' class="notice-card">
          <uni-view ''' + V + ''' class="notice-card-title">藏品介绍</uni-view>
          <uni-view ''' + V + ''' class="notice-card-text">{{ g.desc }}</uni-view>
        </uni-view>
        <uni-view ''' + V + ''' class="notice-card">
          <uni-view ''' + V + ''' class="notice-card-title">购买须知</uni-view>
          <uni-view ''' + V + ''' class="notice-card-text">数字藏品一经售出不支持退换，请仔细核对规格；成交后可在「我的订单」查看交易记录。</uni-view>
        </uni-view>
      </uni-view>

      <uni-view ''' + V + ''' class="bottom-spacer"></uni-view>
    </uni-view>

    <!-- 寄售弹层 -->
    <uni-view ''' + V + ''' class="cu-modal bottom-modal sell-modal" :class="{ show: sheet === 'sell' }">
      <uni-view ''' + V + ''' class="cu-dialog sell-sheet">
        <uni-view ''' + V + ''' class="sell-sheet-title">寄售</uni-view>
        <uni-view ''' + V + ''' class="sell-sheet-body">
          <uni-view ''' + V + ''' class="sell-field-label">寄售价格</uni-view>
          <uni-view ''' + V + ''' class="sell-field-input">
            <uni-input ''' + V + '''>
              <div class="uni-input-wrapper">
                <div class="uni-input-placeholder sell-input-placeholder">请输入价格</div>
                <input class="uni-input-input" :value="sellPrice" @input="onSellPrice($event.target.value)" />
              </div>
            </uni-input>
          </uni-view>
          <uni-view ''' + V + ''' class="sell-fee-row">
            <uni-view ''' + V + ''' class="sell-fee-label">预计收益</uni-view>
            <uni-view ''' + V + ''' class="sell-fee-value"> {{ sellNet }} </uni-view>
          </uni-view>
          <uni-view ''' + V + ''' class="sell-fee-row">
            <uni-view ''' + V + ''' class="sell-fee-label">服务费(5%)</uni-view>
            <uni-view ''' + V + ''' class="sell-fee-value"> {{ sellFee }} </uni-view>
          </uni-view>
        </uni-view>
        <uni-view ''' + V + ''' class="sell-sheet-footer">
          <uni-view ''' + V + ''' class="sheet-btn outline" @click="sheet = ''">返回</uni-view>
          <uni-view ''' + V + ''' class="sheet-btn primary" @click="submitSell">寄售</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <!-- 转赠弹层 -->
    <uni-view ''' + V + ''' class="cu-modal" :class="{ show: sheet === 'gift' }">
      <uni-view ''' + V + ''' class="cu-dialog text-left padding radius">
        <uni-view ''' + V + ''' class="text-center text-bold text-lg"> 转赠好友 </uni-view>
        <uni-view ''' + V + ''' class="margin-top">
          <uni-view ''' + V + '''> 待转赠藏品信息： </uni-view>
          <uni-view ''' + V + ''' class="padding-sm margin-top radius bg-gray"> {{ g.name }} #{{ g.id }} </uni-view>
        </uni-view>
        <uni-view ''' + V + ''' class="margin-top">
          <uni-view ''' + V + '''> 接收人账号 </uni-view>
          <uni-view ''' + V + ''' class="padding-sm margin-top radius bg-gray">
            <uni-input ''' + V + '''>
              <div class="uni-input-wrapper">
                <div class="uni-input-placeholder text-df">请输入接收人账号</div>
                <input class="uni-input-input" :value="giftTo" @input="giftTo = $event.target.value" />
              </div>
            </uni-input>
          </uni-view>
        </uni-view>
        <uni-view ''' + V + ''' class="margin-top">
          <uni-view ''' + V + ''' class="flex">
            <uni-view ''' + V + ''' class="cu-btn lg margin-right bg-gray flex-sub radius" @click="sheet = ''"> 返回 </uni-view>
            <uni-view ''' + V + ''' class="cu-btn lg btn-action-yellow flex-sub radius" @click="submitGift"> 确认转赠 </uni-view>
          </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <!-- 购买弹层 -->
    <uni-view ''' + V + ''' class="cu-modal bottom-modal" :class="{ show: sheet === 'buy' }">
      <uni-view ''' + V + ''' class="cu-dialog bg-white text-left padding radius">
        <uni-view ''' + V + ''' class="text-center text-bold text-lg">请选择购买数量</uni-view>
        <uni-view ''' + V + ''' class="text-center margin-top">
          <uni-image ''' + V + ''' class="radius" style="width: 100px; height: 100px;" :style="bgImg(g.img)">
            <div :style="bgImg(g.img)"></div>
          </uni-image>
          <uni-view ''' + V + ''' class="text-lg text-bold"> {{ g.name }} </uni-view>
        </uni-view>
        <uni-view ''' + V + ''' class="flex padding-lr-xl align-center margin-top justify-between">
          <uni-view ''' + V + ''' class="btn-action-yellow text-xl flex align-center justify-center radius" style="width: 40px; height: 40px;" @click="qty = qty > 1 ? qty - 1 : 1">
            <uni-text ''' + V + ''' class="cuIcon-move"><span></span></uni-text>
          </uni-view>
          <uni-view ''' + V + ''' class="flex-sub text-center text-xl text-bold"> {{ qty }} </uni-view>
          <uni-view ''' + V + ''' class="btn-action-yellow text-xl flex align-center justify-center radius" style="width: 40px; height: 40px;" @click="qty = qty + 1">
            <uni-text ''' + V + ''' class="cuIcon-add"><span></span></uni-text>
          </uni-view>
        </uni-view>
        <uni-view ''' + V + ''' class="padding margin-top">
          <uni-view ''' + V + ''' class="flex align-center justify-between">
            <uni-view ''' + V + ''' class="text-xl" style="width: 150px;">￥ {{ buyTotal }}</uni-view>
            <uni-view ''' + V + ''' class="cu-btn lg btn-action-yellow radius" style="width: 150px;" @click="submitBuy">立即购买</uni-view>
          </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <!-- 底部操作条 -->
    <uni-view ''' + V + ''' class="gd-bottom-bar">
      <uni-view ''' + V + ''' class="gd-bar-btn plain" @click="open('gift')"> 转赠 </uni-view>
      <uni-view ''' + V + ''' class="gd-bar-btn plain" @click="open('sell')"> 寄售 </uni-view>
      <uni-view ''' + V + ''' class="gd-bar-btn primary" @click="open('buy')"> 立即购买 </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getGoods } from '@/mock/goods'
import { isLogin, toast } from '@/utils/interact'

const route = useRoute()
const router = useRouter()
const g = getGoods(route.query.id)

const faved = ref(false)
const sheet = ref('')
const qty = ref(1)
const sellPrice = ref(String(g.floor || 10))
const giftTo = ref('')

const floorText = computed(() => (g.floor == null ? '--' : '￥' + g.floor))
const buyTotal = computed(() => ((g.floor || 10) * qty.value).toFixed(2))
const sellFee = computed(() => '￥ ' + (Number(sellPrice.value || 0) * 0.05).toFixed(2))
const sellNet = computed(() => '￥ ' + (Number(sellPrice.value || 0) * 0.95).toFixed(2))

function bgImg(url) {
  if (!url) return {}
  return { backgroundImage: 'url(' + url + ')', backgroundPosition: 'center center', backgroundSize: 'cover', backgroundRepeat: 'no-repeat' }
}

function onSellPrice(v) {
  sellPrice.value = String(v).replace(/[^\\d.]/g, '').slice(0, 10)
}

function open(k) {
  if (!isLogin()) return toast('请先登录')
  sheet.value = k
}

function submitSell() {
  const p = Number(sellPrice.value)
  if (!(p > 0)) return toast('请输入正确的寄售价格')
  toast('已提交寄售：' + g.name + ' ￥' + p.toFixed(2))
  sheet.value = ''
}

function submitGift() {
  if (!giftTo.value.trim()) return toast('请输入接收人账号')
  toast('已向 ' + giftTo.value.trim() + ' 发起转赠')
  sheet.value = ''
  giftTo.value = ''
}

function submitBuy() {
  toast('购买成功：' + g.name + ' x' + qty.value + ' ￥' + buyTotal.value)
  sheet.value = ''
  qty.value = 1
}
</script>
'''

io.open(P, 'w', encoding='utf-8').write(tpl)
print('GoodsDetails rewritten %d -> %d' % (len(old), len(tpl)))