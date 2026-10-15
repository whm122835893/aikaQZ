<template>
  <uni-view data-v-31c76ef9="" class="padding container"><uni-view data-v-31c76ef9="" class="radius padding-bottom"><uni-view data-v-31c76ef9="" class="text-lg text-bold" style="font-weight: 800; font-size: 18px; color: rgb(51, 51, 51);"> {{ notice.title }} </uni-view><uni-view data-v-31c76ef9="" class="margin-top-sm text-sm text-gray" style="font-weight: 400; font-size: 12px; color: rgb(153, 153, 153);"> {{ notice.publisher }}　{{ notice.time }} </uni-view></uni-view><uni-view data-v-31c76ef9="" class="radius bg-white"><uni-view data-v-31c76ef9="" class="vhtml margin-top" v-html="body"></uni-view></uni-view><uni-image data-v-31c76ef9="" class="notice-footer-img" style="height: 516px;"><div style="background-image: url(&quot;/static/not.jpg&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/not.jpg" draggable="false"></uni-image><uni-view data-v-31c76ef9="" class="related-section"><uni-view data-v-31c76ef9="" class="related-title">相关推荐</uni-view><uni-view data-v-31c76ef9="" class="related-grid"><uni-view data-v-31c76ef9="" class="related-item" v-for="g in goods" :key="g.title" data-nav-to="/pages/market/details"><uni-image data-v-31c76ef9="" class="related-cover"><div :style="`background-image: url(&quot;${g.image}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div><img :src="g.image" draggable="false" /></uni-image><uni-view data-v-31c76ef9="" class="related-name">{{ g.title }}</uni-view></uni-view></uni-view></uni-view></uni-view>
</template>

<script setup>
import { computed } from 'vue'
import { getNotice, buildNoticeBody, GOODS } from '@/mock/data'

// 源站此页靠 URL 上的 ?id= 取公告，无参访问时标题、时间、正文都是空插值。
// 这里默认取公告列表第一条，并按需切换；?n=2 可看第2 条。
const n = Number(new URLSearchParams(location.hash.split('?')[1] || '').get('n') || 0) || 0
const notice = getNotice(n)
const body = computed(() => buildNoticeBody(n))
const goods = GOODS.slice(0, 3)
</script>