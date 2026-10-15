<template>
  <uni-view data-v-0fe5be2c="" class="drawlots-page"><uni-view data-v-0fe5be2c="" class="page-bg"></uni-view><uni-view data-v-0fe5be2c="" class="hero-watermark-wrap" style="top: 12px;"><uni-image data-v-0fe5be2c="" class="hero-watermark"><div style="background-image: url(&quot;/static/images/login/2.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/images/login/2.png" draggable="false"></uni-image></uni-view><uni-view data-v-0fe5be2c="" class="drawlots-sticky-header" style="padding-top: 24px;"><uni-view data-v-0fe5be2c="" class="header"><uni-view data-v-0fe5be2c="" class="back-btn"><uni-text data-v-0fe5be2c="" class="cuIcon-back"><span></span></uni-text></uni-view><uni-view data-v-0fe5be2c="" class="page-title">抽签活动</uni-view><uni-view data-v-0fe5be2c="" class="header-placeholder"></uni-view></uni-view><uni-view data-v-0fe5be2c="" class="hero-banner-wrap"><uni-image data-v-0fe5be2c="" class="hero-banner" style="height: 270px;"><div style="background-image: url(&quot;/static/images/integral/icon/1.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/images/integral/icon/1.png" draggable="false"></uni-image></uni-view></uni-view><uni-scroll-view data-v-0fe5be2c="" class="drawlots-scroll-body" style="top: 334px; height: 478px;"><div class="uni-scroll-view"><div class="uni-scroll-view" style="overflow: hidden auto;"><div class="uni-scroll-view-content"><div class="uni-scroll-view-refresher" style="background-color: transparent; height: 0px;"><uni-view data-v-a0f2fc02="" data-v-0fe5be2c="" class="refresher-slot" style="height: 54px; min-height: 54px;"><uni-image data-v-a0f2fc02="" class="refresher-slot__icon" style="width: 36px; height: 36px;"><div style="background-image: url(&quot;/static/icard.gif&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/icard.gif" draggable="false"></uni-image></uni-view></div><uni-view data-v-0fe5be2c="" class="content-wrap"><uni-view data-v-0fe5be2c="" class="section-card"><uni-view data-v-0fe5be2c="" class="section-header"><uni-view data-v-0fe5be2c="" class="section-title">精选抽签活动</uni-view><uni-view data-v-0fe5be2c="" class="section-sub">参与抽签，赢取惊喜好礼</uni-view></uni-view><uni-view v-for="a in acts" :key="a.id" class="lot-card" @click="open(a)"><uni-image class="lot-card-cover"><div :style="bgImg(a.img)"></div><img :src="a.img" draggable="false"></uni-image><uni-view class="lot-card-body"><uni-text class="lot-card-title">{{ a.title }}</uni-text><uni-text class="lot-card-desc">{{ a.desc }}</uni-text><uni-view class="lot-card-meta"><uni-text class="lot-card-pool">奖池 {{ a.pool }} 件</uni-text><uni-text class="lot-card-status" :class="a.state">{{ a.stateText }}</uni-text></uni-view></uni-view></uni-view><uni-view v-if="!acts.length" class="empty-wrap"><uni-view data-v-0fe5be2c="" class="empty-title">暂无其他活动</uni-view><uni-view data-v-0fe5be2c="" class="empty-sub">更多精彩，敬请期待</uni-view></uni-view></uni-view></uni-view><uni-view data-v-0fe5be2c="" class="page-bottom-space"></uni-view></div></div></div></uni-scroll-view></uni-view>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { toast } from '@/utils/interact'

const router = useRouter()

const acts = ref([
  {
    id: 'a1',
    title: '《艾卡德-学习》限量抽签',
    desc: '参与抽签即有机会获得限量编号藏品',
    img: '/upload/861bfe33d903a1fc7808f503e302b14e77f07ce1.png',
    pool: 30, state: 'open', stateText: '抽签中'
  },
  {
    id: 'a2',
    title: '《国潮之光》首发抽签',
    desc: '首发藏品抽签，签码随机生成',
    img: '/upload/a78f2138480a3638e085dee9e4f3e693265faa7a.jpg',
    pool: 100, state: 'open', stateText: '抽签中'
  },
  {
    id: 'a3',
    title: '《像素方块》社区抽签',
    desc: '仅限社区成员参与，明日开签',
    img: '/upload/4a5cec899296b7a17ff7277dfcaeafa51f7673f8.png',
    pool: 50, state: 'soon', stateText: '未开始'
  }
])

function bgImg(url) {
  return {
    backgroundImage: 'url(' + url + ')',
    backgroundPosition: 'center center',
    backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat'
  }
}

function open(a) {
  if (a.state === 'soon') return toast('活动尚未开始')
  router.push({ path: '/pages/drawlots/details', query: { id: a.id } })
}
</script>
