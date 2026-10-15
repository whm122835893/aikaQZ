<template>
  <uni-view data-v-ddd8370c="" class="lottery-page"><uni-image data-v-ddd8370c="" class="page-bg" style="height: 812px;"><div style="background-image: url(&quot;/static/images/notice/bg.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/images/notice/bg.png" draggable="false"></uni-image><uni-view data-v-ddd8370c="" class="lottery-header" style="padding-top: 8px; background: transparent;"><uni-view data-v-ddd8370c="" class="back-btn"><uni-text data-v-ddd8370c="" class="cuIcon-back"><span></span></uni-text></uni-view><uni-text data-v-ddd8370c="" class="header-title"><span>幸运抽奖</span></uni-text><uni-view data-v-ddd8370c="" class="header-right"><uni-text class="header-link" @click="showRules"><span>规则</span></uni-text><uni-text class="header-link" @click="showHistory"><span>记录</span></uni-text></uni-view></uni-view><uni-scroll-view data-v-ddd8370c="" class="page-scroll" style="height: 812px;"><div class="uni-scroll-view"><div class="uni-scroll-view" style="overflow: hidden auto;"><div class="uni-scroll-view-content"><uni-view data-v-ddd8370c="" class="page-inner"><uni-view data-v-ddd8370c="" class="header-space" style="height: 124px;"></uni-view><uni-view data-v-ddd8370c="" class="machine-section"><uni-view data-v-ddd8370c="" class="machine-window"><uni-image class="machine-img machine-clickable" style="height: 384px;" @click="draw(1)"><div style="background-image: url(&quot;/static/images/notice/mine.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/images/notice/mine.png" draggable="false"></uni-image><uni-view data-v-ddd8370c="" class="action-dock"><uni-view data-v-ddd8370c="" class="action-btn-img" :class="{disabled: drawing}" @click="draw(1)"><uni-image data-v-ddd8370c="" class="action-btn-pic" style="height: 44px;"><div style="background-image: url(&quot;/static/images/notice/2.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/images/notice/2.png" draggable="false"></uni-image></uni-view><uni-view data-v-ddd8370c="" class="action-btn-img" :class="{disabled: drawing}" @click="draw(10)"><uni-image data-v-ddd8370c="" class="action-btn-pic" style="height: 42px;"><div style="background-image: url(&quot;/static/images/notice/3.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/images/notice/3.png" draggable="false"></uni-image></uni-view></uni-view></uni-view></uni-view><uni-view data-v-ddd8370c="" class="info-card prize-card"><uni-view data-v-ddd8370c="" class="prize-head"><uni-text data-v-ddd8370c="" class="prize-diamond"><span>✦</span></uni-text><uni-text data-v-ddd8370c="" class="prize-head-text"><span>奖品列表</span></uni-text><uni-text data-v-ddd8370c="" class="prize-diamond"><span>✦</span></uni-text></uni-view><uni-view v-if="!prizes.length" class="empty-block prize-empty"><uni-text class="empty-text"><span>暂无奖品信息</span></uni-text></uni-view><uni-view v-else class="prize-list"><uni-view v-for="(p, i) in prizes" :key="i" class="prize-row"><uni-image class="prize-row-icon"><div :style="bgImg(p.icon)"></div><img :src="p.icon" draggable="false"></uni-image><uni-text class="prize-row-name">{{ p.name }}</uni-text><uni-text class="prize-row-prob">概率 {{ p.prob }}%</uni-text><uni-text class="prize-row-stock">库存 {{ p.stock }}</uni-text></uni-view></uni-view></uni-view></uni-view></div></div></div></uni-scroll-view><uni-view class="cu-modal" :class="{show: result}"><uni-view data-v-ddd8370c="" class="cu-dialog"><uni-view data-v-ddd8370c="" class="flex justify-around align-center"><uni-view data-v-ddd8370c=""><uni-image data-v-ddd8370c="" style="width: 127px; height: 115px;"><div style="background-image: url(&quot;/static/drawprize/gift.png&quot;); background-position: 0% 0%; background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/drawprize/gift.png" draggable="false"></uni-image></uni-view><uni-view data-v-ddd8370c="" style="margin-top: -50px;"><uni-image data-v-ddd8370c="" style="width: 29px; height: 28px;"><div style="background-image: url(&quot;/static/drawprize/close.png&quot;); background-position: 0% 0%; background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/drawprize/close.png" draggable="false"></uni-image></uni-view></uni-view><uni-view data-v-ddd8370c="" class="cu-dialog-content" style="margin: -25px auto 0px; z-index: 5; position: relative;"><uni-view data-v-ddd8370c="" class="flex justify-center align-center flex-direction"><uni-view data-v-ddd8370c="" class="flex justify-start align-start margin-top"><uni-image data-v-ddd8370c="" style="width: 177px; height: 32px; margin-left: -20%;"><div style="background-image: url(&quot;/static/drawprize/mtitle.png&quot;); background-position: 0% 0%; background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/drawprize/mtitle.png" draggable="false"></uni-image></uni-view><uni-view data-v-ddd8370c="" class="padding-lr margin-top pbox" style="width: 100%;"></uni-view><uni-view data-v-ddd8370c="" class="flex margin-top" style="position: absolute; bottom: 0px; transform: translateY(-15px);"><uni-view class="cu-btn bbg" @click="closeResult">确认</uni-view></uni-view></uni-view></uni-view></uni-view></uni-view></uni-view>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { toast, isLogin } from '@/utils/interact'

const router = useRouter()

const prizes = ref([])
const drawing = ref(false)
const result = ref(null)
const resultText = ref('')
const history = ref([])

/** 生成 background-image 样式 */
function bgImg(url) {
  return {
    backgroundImage: 'url(' + url + ')',
    backgroundPosition: 'center center',
    backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat'
  }
}

/** 奖品池：按概率加权随机 */
const POOL = [
  { name: '国潮之光', icon: '/upload/a78f2138480a3638e085dee9e4f3e693265faa7a.jpg', prob: 1, stock: 3, weight: 5 },
  { name: '像素方块', icon: '/upload/4a5cec899296b7a17ff7277dfcaeafa51f7673f8.png', prob: 3, weight: 12 },
  { name: '机甲武士', icon: '/upload/a18237a80fad69667669015f27a189561f47d47f.jpg', prob: 6, weight: 20 },
  { name: '星际指挥官', icon: '/upload/f6746c2b2cf5254376c8958f1bc8780955ae168c.png', prob: 10, weight: 28 },
  { name: '青铜面具', icon: '/upload/2fa0e35b68000d5aa6a869c4513d4f537ef5eaf0.png', prob: 16, weight: 20 },
  { name: '积分券 100', icon: '/static/images/integral/1.png', prob: 20, weight: 15 }
]

const totalWeight = POOL.reduce((s, p) => s + p.weight, 0)

function roll() {
  let r = Math.random() * totalWeight
  for (const p of POOL) {
    r -= p.weight
    if (r <= 0) return p
  }
  return POOL[POOL.length - 1]
}

function draw(times) {
  if (drawing.value) return
  if (!isLogin()) return toast('请先登录')

  drawing.value = true
  toast(times === 1 ? '抽奖中...' : '十连抽奖中...')

  setTimeout(() => {
    const got = []
    for (let i = 0; i < times; i++) got.push(roll())

    got.forEach((p) => {
      const hit = prizes.value.find((x) => x.name === p.name)
      if (hit) {
        hit.stock -= 1
      } else {
        prizes.value.push({ ...p })
      }
    })

    history.value.unshift(...got.map((p) => ({ name: p.name, time: nowText() })))

    resultText.value = times === 1
      ? '恭喜获得：' + got[0].name
      : '恭喜获得：' + got.map((p) => p.name).join('、')
    result.value = got
    drawing.value = false
  }, 900)
}

function closeResult() {
  result.value = null
}

function showRules() {
  toast('每消耗 1 次机会抽 1 枚，奖品概率见下方列表')
}

function showHistory() {
  toast(history.value.length ? '已抽 ' + history.value.length + ' 次' : '还没有抽奖记录')
}

function nowText() {
  const d = new Date()
  const p = (n) => String(n).padStart(2, '0')
  return d.getFullYear() + '/' + p(d.getMonth() + 1) + '/' + p(d.getDate()) + ' ' + p(d.getHours()) + ':' + p(d.getMinutes())
}
</script>
