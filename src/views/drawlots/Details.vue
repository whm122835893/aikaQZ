<template>
  <uni-view data-v-4ef1aa35="" class="detail-page"><uni-view data-v-4ef1aa35="" class="page-bg"></uni-view><uni-view data-v-4ef1aa35="" class="hero-watermark-wrap" style="top: 12px;"><uni-image data-v-4ef1aa35="" class="hero-watermark"><div style="background-image: url(&quot;/static/images/login/2.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/images/login/2.png" draggable="false"></uni-image></uni-view><uni-view data-v-4ef1aa35="" class="page-header" style="padding-top: 12px;"><uni-view data-v-4ef1aa35="" class="header-back"><uni-text data-v-4ef1aa35="" class="cuIcon-back"><span></span></uni-text></uni-view><uni-view data-v-4ef1aa35="" class="header-title">抽签</uni-view><uni-view data-v-4ef1aa35="" class="header-placeholder"></uni-view></uni-view><uni-scroll-view data-v-4ef1aa35="" class="page-scroll" style="top: 50px; height: calc(100vh - 50px - 0 - env(safe-area-inset-bottom));"><div class="uni-scroll-view"><div class="uni-scroll-view" style="overflow: hidden auto;"><div class="uni-scroll-view-content"><uni-view data-v-4ef1aa35="" class="hero-block"><uni-view data-v-4ef1aa35="" class="hero-stage"><uni-view data-v-4ef1aa35="" class="hero-cover-wrap"><uni-image class="hero-cover"><div :style="bgImg(act.img)"></div><img :src="act.img" draggable="false"></uni-image></uni-view><uni-view data-v-4ef1aa35="" class="hero-pedestal-wrap"><uni-image data-v-4ef1aa35="" class="hero-pedestal" style="height: 144px;"><div style="background-image: url(&quot;/static/images/integral/newicon/1.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/images/integral/newicon/1.png" draggable="false"></uni-image><uni-view data-v-4ef1aa35="" class="hero-title-row"><uni-view data-v-4ef1aa35="" class="hero-title-inner"><uni-image data-v-4ef1aa35="" class="hero-deco-img" style="width: 314px;"><div style="background-image: url(&quot;/static/images/integral/newicon/6.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/images/integral/newicon/6.png" draggable="false"></uni-image><uni-text class="hero-title"><span>{{ act.title }}</span></uni-text></uni-view></uni-view></uni-view></uni-view></uni-view><uni-view data-v-4ef1aa35="" class="section-card"><uni-view data-v-4ef1aa35="" class="section-head"><uni-image data-v-4ef1aa35="" class="section-title-img" style="width: 74px;"><div style="background-image: url(&quot;/static/images/integral/newicon/5.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/images/integral/newicon/5.png" draggable="false"></uni-image></uni-view><uni-view data-v-4ef1aa35="" class="flow-panel"><uni-view data-v-4ef1aa35="" class="flow-track"><uni-view data-v-4ef1aa35="" class="flow-track-line"></uni-view><uni-view data-v-4ef1aa35="" class="flow-track-progress" style="width: 12.6%;"></uni-view><uni-view data-v-4ef1aa35="" class="flow-steps"><uni-view data-v-4ef1aa35="" class="flow-step"><uni-view data-v-4ef1aa35="" class="flow-dot">1</uni-view><uni-view data-v-4ef1aa35="" class="flow-label">抽签中</uni-view><uni-view class="flow-time">{{ act.t1 }}</uni-view></uni-view><uni-view data-v-4ef1aa35="" class="flow-step"><uni-view data-v-4ef1aa35="" class="flow-dot">2</uni-view><uni-view data-v-4ef1aa35="" class="flow-label">开签中</uni-view><uni-view class="flow-time">{{ act.t2 }}</uni-view></uni-view><uni-view data-v-4ef1aa35="" class="flow-step"><uni-view data-v-4ef1aa35="" class="flow-dot">3</uni-view><uni-view data-v-4ef1aa35="" class="flow-label">公示时间</uni-view><uni-view class="flow-time">{{ act.t3 }}</uni-view></uni-view></uni-view></uni-view></uni-view></uni-view><uni-view data-v-4ef1aa35="" class="section-card"><uni-view data-v-4ef1aa35="" class="section-head"><uni-image data-v-4ef1aa35="" class="section-title-img" style="width: 74px;"><div style="background-image: url(&quot;/static/images/integral/newicon/4.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/images/integral/newicon/4.png" draggable="false"></uni-image></uni-view><uni-view v-if="!pool.length" class="section-empty">暂无奖池藏品</uni-view><uni-view v-else class="pool-grid"><uni-view v-for="(g, i) in pool" :key="i" class="pool-item"><uni-image class="pool-item-img"><div :style="bgImg(g.img)"></div><img :src="g.img" draggable="false"></uni-image><uni-text class="pool-item-num">{{ i + 1 }}号</uni-text></uni-view></uni-view></uni-view><uni-view data-v-4ef1aa35="" class="section-card"><uni-view data-v-4ef1aa35="" class="section-head"><uni-image data-v-4ef1aa35="" class="section-title-img" style="width: 90px;"><div style="background-image: url(&quot;/static/images/integral/newicon/3.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/images/integral/newicon/3.png" draggable="false"></uni-image><uni-text data-v-4ef1aa35="" class="section-status"><span>未开始</span></uni-text></uni-view><uni-view v-if="!code" class="section-empty" @click="genCode"> 暂未抽签，点击生成抽签码 </uni-view><uni-view v-else class="lot-code-box" @click="copyCode"><uni-text class="lot-code">{{ code }}</uni-text><uni-text class="lot-code-tip">点击复制</uni-text></uni-view></uni-view><uni-view data-v-4ef1aa35="" class="bottom-spacer"></uni-view><uni-view class="lot-action-bar" data-v-4ef1aa35=""><uni-view class="lot-action-btn ghost" @click="router.back()">返回</uni-view><uni-view class="lot-action-btn primary" @click="genCode">{{ code ? '重新抽签' : '立即抽签' }}</uni-view></uni-view></div></div></div></uni-scroll-view></uni-view>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { toast, isLogin } from '@/utils/interact'

const route = useRoute()
const router = useRouter()

const ACTS = {
  a1: {
    title: '《艾卡德-学习》限量抽签',
    img: '/upload/861bfe33d903a1fc7808f503e302b14e77f07ce1.png',
    t1: '2026-10-08 10:00', t2: '2026-10-09 20:00', t3: '2026-10-10 12:00',
    progress: 34,
    pool: [
      { img: '/upload/861bfe33d903a1fc7808f503e302b14e77f07ce1.png' },
      { img: '/upload/a78f2138480a3638e085dee9e4f3e693265faa7a.jpg' },
      { img: '/upload/4a5cec899296b7a17ff7277dfcaeafa51f7673f8.png' },
      { img: '/upload/194d693b5e364b79c16bb647807972341d4e5744.png' },
      { img: '/upload/2fa0e35b68000d5aa6a869c4513d4f537ef5eaf0.png' },
      { img: '/upload/45c0ec9b95b85006375bdfe673239b0752cca05c.png' }
    ]
  },
  a2: {
    title: '《国潮之光》首发抽签',
    img: '/upload/a78f2138480a3638e085dee9e4f3e693265faa7a.jpg',
    t1: '2026-10-06 10:00', t2: '2026-10-08 20:00', t3: '2026-10-09 12:00',
    progress: 72,
    pool: [
      { img: '/upload/a78f2138480a3638e085dee9e4f3e693265faa7a.jpg' },
      { img: '/upload/a18237a80fad69667669015f27a189561f47d47f.jpg' },
      { img: '/upload/f6746c2b2cf5254376c8958f1bc8780955ae168c.png' },
      { img: '/upload/87f1615abb555956911f888aea806b7403685231.jpg' }
    ]
  },
  a3: {
    title: '《像素方块》社区抽签',
    img: '/upload/4a5cec899296b7a17ff7277dfcaeafa51f7673f8.png',
    t1: '待开启', t2: '待开启', t3: '待开启',
    progress: 0,
    pool: [{ img: '/upload/4a5cec899296b7a17ff7277dfcaeafa51f7673f8.png' }]
  }
}

const id = String(route.query.id || 'a1')
const act = ACTS[id] || ACTS.a1
const pool = ref(act.pool)
const code = ref('')

function bgImg(url) {
  return {
    backgroundImage: 'url(' + url + ')',
    backgroundPosition: 'center center',
    backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat'
  }
}

function genCode() {
  if (!isLogin()) return toast('请先登录')
  if (act.progress === 0) return toast('活动尚未开始')
  if (code.value) return toast('已生成过抽签码')
  const n = String(Math.floor(100000 + Math.random() * 900000))
  code.value = 'LQ-' + n.slice(0, 3) + '-' + n.slice(3)
  toast('抽签码已生成：' + code.value)
}

async function copyCode() {
  try {
    await navigator.clipboard.writeText(code.value)
    toast('抽签码已复制')
  } catch {
    toast('复制失败，请手动记录')
  }
}
</script>
