<script setup>
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const tabs = [
  { label: '首页', path: '/pages/home/home', icon: '/static/images/tabbar/1.png', active: '/static/images/tabbar/2.png' },
  { label: '合成', path: '/pages/colorfulMix/colorfulMix', icon: '/static/images/tabbar/9.png', active: '/static/images/tabbar/10.png' },
  { label: '市场', path: '/pages/market/market', icon: '/static/images/tabbar/3.png', active: '/static/images/tabbar/4.png' },
  { label: '公告', path: '/pages/notification/notification', icon: '/static/images/tabbar/11.png', active: '/static/images/tabbar/12.png' },
  { label: '我的', path: '/pages/account/account', icon: '/static/images/tabbar/7.png', active: '/static/images/tabbar/8.png' }
]

const router = useRouter()
const route = useRoute()

const isActive = (t) => route.path === t.path
const icon = (t) => (isActive(t) ? t.active : t.icon)
const bg = (t) => ({
  backgroundImage: `url("${icon(t)}")`,
  backgroundPosition: '0% 0%',
  backgroundSize: '100% 100%',
  backgroundRepeat: 'no-repeat'
})
const go = (t) => router.replace(t.path)
</script>

<template>
  <uni-view data-v-53a1042a="" class="box box1">
    <uni-view data-v-53a1042a="">
      <uni-view data-v-53a1042a="" class="tabbar">
        <uni-view
          v-for="t in tabs"
          :key="t.path"
          data-v-53a1042a=""
          class="tabbaritem"
          @click="go(t)"
        >
          <uni-image data-v-53a1042a="" style="width: 24px; height: 24px;">
            <div :style="bg(t)"></div>
            <img :src="icon(t)" draggable="false" />
          </uni-image>
          <uni-view data-v-53a1042a="" :class="['name', { oname: isActive(t) }]">{{ t.label }}</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>
