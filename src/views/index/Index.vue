<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const sec = ref(1)

let timer = null

function enter() {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
  router.replace('/pages/home/home')
}

onMounted(() => {
  timer = setInterval(() => {
    sec.value -= 1
    if (sec.value <= 0) enter()
  }, 1000)
})

// 关键：离开启动页必须清定时器，否则它会在 1s 后把当前页面弹回首页
onUnmounted(() => {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
})
</script>

<template>
  <uni-view data-v-667f0804="" class="launch-page"><uni-image data-v-667f0804="" class="launch-bg"><div style="background-image: url(&quot;/static/images/index/index/dow.png&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;"></div><img src="/static/images/index/index/dow.png" draggable="false"></uni-image><uni-view data-v-667f0804="" class="countdown-wrap" style="top: 12px;" @click="enter"><uni-text data-v-667f0804="" class="countdown-text"><span>{{ sec }}s 跳过</span></uni-text></uni-view></uni-view>
</template>
