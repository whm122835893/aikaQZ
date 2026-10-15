#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PhysicalGoodsDetails.vue —— 价格/标题 -- 换成真实数据 + 立即购买弹层"""
import io

P = 'src/views/market/PhysicalGoodsDetails.vue'
old = io.open(P, encoding='utf-8').read()
V = 'data-v-f24de0b0=""'

tpl = '''<template>
  <uni-view ''' + V + ''' class="physical-page">
    <uni-view ''' + V + ''' class="page-header" style="padding-top: 12px;">
      <uni-view ''' + V + ''' class="header-back"><uni-text ''' + V + ''' class="cuIcon-back"><span></span></uni-text></uni-view>
      <uni-view ''' + V + ''' class="header-title">商品详情</uni-view>
      <uni-view ''' + V + ''' class="header-placeholder"></uni-view>
    </uni-view>

    <uni-scroll-view ''' + V + ''' class="page-scroll" style="top: 50px; height: calc(-110px + 100vh);">
      <div class="uni-scroll-view">
        <div class="uni-scroll-view" style="overflow: hidden auto;">
          <div class="uni-scroll-view-content">
            <uni-swiper ''' + V + ''' class="goods-swiper">
              <div class="uni-swiper-wrapper">
                <div class="uni-swiper-slides">
                  <div class="uni-swiper-slide-frame" style="width: 100%; height: 100%; transform: translate(0%, 0px) translateZ(0px);">
                    <uni-swiper-item ''' + V + ''' style="position: absolute; width: 100%; height: 100%; transform: translate(0%, 0px) translateZ(0px);">
                      <uni-image ''' + V + ''' class="goods-banner">
                        <div style="background-image: url(&quot;/static/images/index/icon/bg.png&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;"></div>
                        <img src="/static/images/index/icon/bg.png" draggable="false"></uni-image>
                    </uni-swiper-item>
                  </div>
                </div>
                <div class="uni-swiper-dots uni-swiper-dots-horizontal">
                  <div class="uni-swiper-dot uni-swiper-dot-active" style="background: rgb(255, 255, 255);"></div>
                </div>
              </div>
            </uni-swiper>

            <uni-view ''' + V + ''' class="price-block">
              <uni-view ''' + V + ''' class="price-row">
                <uni-text ''' + V + ''' class="price-symbol"><span>¥</span></uni-text>
                <uni-text ''' + V + ''' class="price-current"><span>{{ p.price }}</span></uni-text>
              </uni-view>
              <uni-view ''' + V + ''' class="goods-title">{{ p.name }}</uni-view>
              <uni-view ''' + V + ''' class="service-tags">包邮 · 7天无理由 · 现货速发</uni-view>
            </uni-view>

            <uni-view ''' + V + ''' class="section-card section-detail">
              <uni-view ''' + V + ''' class="section-head">
                <uni-view ''' + V + ''' class="section-bar"></uni-view>
                <uni-text ''' + V + ''' class="section-title"><span>商品详情</span></uni-text>
              </uni-view>
              <uni-view ''' + V + ''' class="detail-empty">{{ p.desc }}</uni-view>
            </uni-view>

            <uni-view ''' + V + ''' class="section-card section-detail">
              <uni-view ''' + V + ''' class="section-head">
                <uni-view ''' + V + ''' class="section-bar"></uni-view>
                <uni-text ''' + V + ''' class="section-title"><span>规格参数</span></uni-text>
              </uni-view>
              <uni-view ''' + V + ''' class="spec-row">
                <uni-text ''' + V + ''' class="spec-label"><span>发货地</span></uni-text>
                <uni-text ''' + V + ''' class="spec-value"><span>{{ p.place }}</span></uni-text>
              </uni-view>
              <uni-view ''' + V + ''' class="spec-row">
                <uni-text ''' + V + ''' class="spec-label"><span>库存</span></uni-text>
                <uni-text ''' + V + ''' class="spec-value"><span>{{ p.stock }} 件</span></uni-text>
              </uni-view>
              <uni-view ''' + V + ''' class="spec-row">
                <uni-text ''' + V + ''' class="spec-label"><span>品牌</span></uni-text>
                <uni-text ''' + V + ''' class="spec-value"><span>{{ p.brand }}</span></uni-text>
              </uni-view>
            </uni-view>

            <uni-view ''' + V + ''' class="bottom-spacer"></uni-view>
          </div>
        </div>
      </div>
    </uni-scroll-view>

    <uni-view ''' + V + ''' class="bottom-bar">
      <uni-view ''' + V + ''' class="bottom-left">
        <uni-view ''' + V + ''' class="bottom-price">
          <uni-text ''' + V + ''' class="bottom-price-symbol"><span>¥</span></uni-text>
          <uni-text ''' + V + ''' class="bottom-price-num"><span>{{ p.price }}</span></uni-text>
        </uni-view>
      </uni-view>
      <uni-view ''' + V + ''' class="buy-btn" @click="openBuy">立即购买</uni-view>
    </uni-view>

    <uni-view ''' + V + ''' class="cu-modal bottom-modal" :class="{ show: sheet }">
      <uni-view ''' + V + ''' class="cu-dialog bg-white text-left padding radius">
        <uni-view ''' + V + ''' class="text-center text-bold text-lg">确认订单</uni-view>
        <uni-view ''' + V + ''' class="text-center margin-top">
          <uni-view ''' + V + ''' class="text-lg text-bold"> {{ p.name }} </uni-view>
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
            <uni-view ''' + V + ''' class="text-xl" style="width: 150px;">￥ {{ total }}</uni-view>
            <uni-view ''' + V + ''' class="cu-btn lg btn-action-yellow radius" style="width: 150px;" @click="submit">立即购买</uni-view>
          </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { isLogin, toast } from '@/utils/interact'

const route = useRoute()
const router = useRouter()

/** 演示商品库，id 对应市场里的藏品编号 */
const SHOP = {
  p1: { name: '艾卡德实体典藏册', price: '299.00', stock: 88, brand: 'ICARD', place: '浙江杭州', desc: '限量 500 册精装典藏，含编号卡片与实体证书。' },
  p2: { name: '数字藏品实体周边·徽章', price: '129.00', stock: 320, brand: 'ICARD', place: '广东深圳', desc: '金属珐琅徽章，单枚直径 40mm，附独立编号。' },
  p3: { name: '国潮系列丝巾', price: '199.00', stock: 156, brand: '国潮之光', place: '江苏苏州', desc: '桑蚕丝 16 姆米，原创手绘纹样，附防尘袋。' }
}

const key = String(route.query.id || 'p1')
const p = SHOP[key] || SHOP.p1

const sheet = ref(false)
const qty = ref(1)
const total = computed(() => (Number(p.price) * qty.value).toFixed(2))

function openBuy() {
  if (!isLogin()) {
    toast('请先登录')
    setTimeout(() => router.replace('/pages/login/login'), 800)
    return
  }
  sheet.value = true
}

function submit() {
  toast('下单成功：' + p.name + ' x' + qty.value + ' ￥' + total.value)
  sheet.value = false
  qty.value = 1
}
</script>
'''

io.open(P, 'w', encoding='utf-8').write(tpl)
print('PhysicalGoodsDetails rewritten %d -> %d' % (len(old), len(tpl)))