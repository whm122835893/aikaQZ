<template>
  <uni-view data-v-58d8ffe2="" class="detail-page">
    <uni-view data-v-58d8ffe2="" class="page-header" style="padding-top: 12px;">
      <uni-view data-v-58d8ffe2="" class="header-back"><uni-text data-v-58d8ffe2="" class="cuIcon-back"><span></span></uni-text></uni-view>
      <uni-view data-v-58d8ffe2="" class="header-title">藏品详情</uni-view>
      <uni-view data-v-58d8ffe2="" class="header-fav" @click="faved = !faved">
        <uni-text data-v-58d8ffe2="" class="cuIcon-star" :class="{ 'cuIcon-starfill faved': faved }"><span></span></uni-text>
      </uni-view>
    </uni-view>

    <uni-view data-v-58d8ffe2="" class="hero-section">
      <uni-image data-v-58d8ffe2="" class="hero-bg" style="height: 384px;">
        <div style="background-image: url(&quot;/static/images/market/icon/bg.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
        <img src="/static/images/market/icon/bg.png" draggable="false"></uni-image>
      <uni-view data-v-58d8ffe2="" class="hero-watermark-wrap" style="top: 12px;">
        <uni-image data-v-58d8ffe2="" class="hero-watermark">
          <div style="background-image: url(&quot;/static/images/login/2.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div>
          <img src="/static/images/login/2.png" draggable="false"></uni-image>
      </uni-view>
      <uni-view data-v-58d8ffe2="" class="hero-podium-wrap">
        <uni-view data-v-58d8ffe2="" class="hero-cover-stage">
          <uni-image data-v-58d8ffe2="" class="hero-cover hero-cover-3d" :style="bgImg(g.img)">
            <div :style="bgImg(g.img)"></div>
          </uni-image>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view data-v-58d8ffe2="" class="page-body">
      <uni-view data-v-58d8ffe2="" id="header-anchor" class="info-card">
        <uni-view data-v-58d8ffe2="" class="info-title"> {{ g.name }} </uni-view>
        <uni-view data-v-58d8ffe2="" class="info-capsules">
          <uni-view data-v-58d8ffe2="" class="info-capsule">
            <uni-view data-v-58d8ffe2="" class="capsule-label">发行</uni-view>
            <uni-view data-v-58d8ffe2="" class="capsule-value">{{ g.issued }}份</uni-view>
          </uni-view>
          <uni-view data-v-58d8ffe2="" class="info-capsule">
            <uni-view data-v-58d8ffe2="" class="capsule-label">流通</uni-view>
            <uni-view data-v-58d8ffe2="" class="capsule-value">{{ g.circ }}份</uni-view>
          </uni-view>
          <uni-view data-v-58d8ffe2="" class="info-capsule">
            <uni-view data-v-58d8ffe2="" class="capsule-label">地板价</uni-view>
            <uni-view data-v-58d8ffe2="" class="capsule-value">{{ floorText }}</uni-view>
          </uni-view>
        </uni-view>
        <uni-view data-v-58d8ffe2="" class="meta-list">
          <uni-view data-v-58d8ffe2="" class="meta-row">
            <uni-text data-v-58d8ffe2="" class="meta-label"><span>藏品编号</span></uni-text>
            <uni-view data-v-58d8ffe2="" class="meta-right"><uni-text data-v-58d8ffe2="" class="meta-value"><span>#{{ g.id }}</span></uni-text></uni-view>
          </uni-view>
          <uni-view data-v-58d8ffe2="" class="meta-row">
            <uni-text data-v-58d8ffe2="" class="meta-label"><span>创作者</span></uni-text>
            <uni-view data-v-58d8ffe2="" class="meta-right">
              <uni-image data-v-58d8ffe2="" class="brand-row-avatar">
                <div style="background-image: url(&quot;/static/images/invite/top1.png&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;"></div>
                <img src="/static/images/invite/top1.png" draggable="false"></uni-image>
              <uni-text data-v-58d8ffe2="" class="brand-row-name"><span>{{ g.author }}</span></uni-text>
            </uni-view>
          </uni-view>
          <uni-view data-v-58d8ffe2="" class="meta-row">
            <uni-text data-v-58d8ffe2="" class="meta-label"><span>品牌方</span></uni-text>
            <uni-view data-v-58d8ffe2="" class="meta-right">
              <uni-image data-v-58d8ffe2="" class="brand-row-avatar">
                <div style="background-image: url(&quot;/static/images/invite/top1.png&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;"></div>
                <img src="/static/images/invite/top1.png" draggable="false"></uni-image>
              <uni-text data-v-58d8ffe2="" class="brand-row-name"><span>{{ g.series }}</span></uni-text>
            </uni-view>
          </uni-view>
          <uni-view data-v-58d8ffe2="" class="meta-row">
            <uni-text data-v-58d8ffe2="" class="meta-label"><span>持有者</span></uni-text>
            <uni-view data-v-58d8ffe2="" class="meta-right"><uni-text data-v-58d8ffe2="" class="meta-value"><span>{{ g.holder }} 人</span></uni-text></uni-view>
          </uni-view>
        </uni-view>
      </uni-view>

      <uni-view data-v-58d8ffe2="" class="detail-section">
        <uni-view data-v-58d8ffe2="" class="notice-card">
          <uni-view data-v-58d8ffe2="" class="notice-card-title">藏品介绍</uni-view>
          <uni-view data-v-58d8ffe2="" class="notice-card-text">{{ g.desc }}</uni-view>
        </uni-view>
        <uni-view data-v-58d8ffe2="" class="notice-card">
          <uni-view data-v-58d8ffe2="" class="notice-card-title">购买须知</uni-view>
          <uni-view data-v-58d8ffe2="" class="notice-card-text">数字藏品一经售出不支持退换，请仔细核对规格；成交后可在「我的订单」查看交易记录。</uni-view>
        </uni-view>
      </uni-view>

      <uni-view data-v-58d8ffe2="" class="bottom-spacer"></uni-view>
    </uni-view>

    <!-- 寄售弹层 -->
    <uni-view data-v-58d8ffe2="" class="cu-modal bottom-modal sell-modal" :class="{ show: sheet === 'sell' }">
      <uni-view data-v-58d8ffe2="" class="cu-dialog sell-sheet">
        <uni-view data-v-58d8ffe2="" class="sell-sheet-title">寄售</uni-view>
        <uni-view data-v-58d8ffe2="" class="sell-sheet-body">
          <uni-view data-v-58d8ffe2="" class="sell-field-label">寄售价格</uni-view>
          <uni-view data-v-58d8ffe2="" class="sell-field-input">
            <uni-input data-v-58d8ffe2="">
              <div class="uni-input-wrapper">
                <div class="uni-input-placeholder sell-input-placeholder">请输入价格</div>
                <input class="uni-input-input" :value="sellPrice" @input="onSellPrice($event.target.value)" />
              </div>
            </uni-input>
          </uni-view>
          <uni-view data-v-58d8ffe2="" class="sell-fee-row">
            <uni-view data-v-58d8ffe2="" class="sell-fee-label">预计收益</uni-view>
            <uni-view data-v-58d8ffe2="" class="sell-fee-value"> {{ sellNet }} </uni-view>
          </uni-view>
          <uni-view data-v-58d8ffe2="" class="sell-fee-row">
            <uni-view data-v-58d8ffe2="" class="sell-fee-label">服务费(5%)</uni-view>
            <uni-view data-v-58d8ffe2="" class="sell-fee-value"> {{ sellFee }} </uni-view>
          </uni-view>
        </uni-view>
        <uni-view data-v-58d8ffe2="" class="sell-sheet-footer">
          <uni-view data-v-58d8ffe2="" class="sheet-btn outline" @click="sheet = ''">返回</uni-view>
          <uni-view data-v-58d8ffe2="" class="sheet-btn primary" @click="submitSell">寄售</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <!-- 转赠弹层 -->
    <uni-view data-v-58d8ffe2="" class="cu-modal" :class="{ show: sheet === 'gift' }">
      <uni-view data-v-58d8ffe2="" class="cu-dialog text-left padding radius">
        <uni-view data-v-58d8ffe2="" class="text-center text-bold text-lg"> 转赠好友 </uni-view>
        <uni-view data-v-58d8ffe2="" class="margin-top">
          <uni-view data-v-58d8ffe2=""> 待转赠藏品信息： </uni-view>
          <uni-view data-v-58d8ffe2="" class="padding-sm margin-top radius bg-gray"> {{ g.name }} #{{ g.id }} </uni-view>
        </uni-view>
        <uni-view data-v-58d8ffe2="" class="margin-top">
          <uni-view data-v-58d8ffe2=""> 接收人账号 </uni-view>
          <uni-view data-v-58d8ffe2="" class="padding-sm margin-top radius bg-gray">
            <uni-input data-v-58d8ffe2="">
              <div class="uni-input-wrapper">
                <div class="uni-input-placeholder text-df">请输入接收人账号</div>
                <input class="uni-input-input" :value="giftTo" @input="giftTo = $event.target.value" />
              </div>
            </uni-input>
          </uni-view>
        </uni-view>
        <uni-view data-v-58d8ffe2="" class="margin-top">
          <uni-view data-v-58d8ffe2="" class="flex">
            <uni-view data-v-58d8ffe2="" class="cu-btn lg margin-right bg-gray flex-sub radius" @click="sheet = ''"> 返回 </uni-view>
            <uni-view data-v-58d8ffe2="" class="cu-btn lg btn-action-yellow flex-sub radius" @click="submitGift"> 确认转赠 </uni-view>
          </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <!-- 购买弹层 -->
    <uni-view data-v-58d8ffe2="" class="cu-modal bottom-modal" :class="{ show: sheet === 'buy' }">
      <uni-view data-v-58d8ffe2="" class="cu-dialog bg-white text-left padding radius">
        <uni-view data-v-58d8ffe2="" class="text-center text-bold text-lg">请选择购买数量</uni-view>
        <uni-view data-v-58d8ffe2="" class="text-center margin-top">
          <uni-image data-v-58d8ffe2="" class="radius" style="width: 100px; height: 100px;" :style="bgImg(g.img)">
            <div :style="bgImg(g.img)"></div>
          </uni-image>
          <uni-view data-v-58d8ffe2="" class="text-lg text-bold"> {{ g.name }} </uni-view>
        </uni-view>
        <uni-view data-v-58d8ffe2="" class="flex padding-lr-xl align-center margin-top justify-between">
          <uni-view data-v-58d8ffe2="" class="btn-action-yellow text-xl flex align-center justify-center radius" style="width: 40px; height: 40px;" @click="qty = qty > 1 ? qty - 1 : 1">
            <uni-text data-v-58d8ffe2="" class="cuIcon-move"><span></span></uni-text>
          </uni-view>
          <uni-view data-v-58d8ffe2="" class="flex-sub text-center text-xl text-bold"> {{ qty }} </uni-view>
          <uni-view data-v-58d8ffe2="" class="btn-action-yellow text-xl flex align-center justify-center radius" style="width: 40px; height: 40px;" @click="qty = qty + 1">
            <uni-text data-v-58d8ffe2="" class="cuIcon-add"><span></span></uni-text>
          </uni-view>
        </uni-view>
        <uni-view data-v-58d8ffe2="" class="padding margin-top">
          <uni-view data-v-58d8ffe2="" class="flex align-center justify-between">
            <uni-view data-v-58d8ffe2="" class="text-xl" style="width: 150px;">￥ {{ buyTotal }}</uni-view>
            <uni-view data-v-58d8ffe2="" class="cu-btn lg btn-action-yellow radius" style="width: 150px;" @click="submitBuy">立即购买</uni-view>
          </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <!-- 底部操作条 -->
    <uni-view data-v-58d8ffe2="" class="gd-bottom-bar">
      <uni-view data-v-58d8ffe2="" class="gd-bar-btn plain" @click="open('gift')"> 转赠 </uni-view>
      <uni-view data-v-58d8ffe2="" class="gd-bar-btn plain" @click="open('sell')"> 寄售 </uni-view>
      <uni-view data-v-58d8ffe2="" class="gd-bar-btn primary" @click="open('buy')"> 立即购买 </uni-view>
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
  sellPrice.value = String(v).replace(/[^\d.]/g, '').slice(0, 10)
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
