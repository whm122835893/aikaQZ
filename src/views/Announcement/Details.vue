<template>
  <uni-view data-v-12ee4397="" class="padding container"><uni-view data-v-12ee4397="" class="radius padding-tb"><uni-view data-v-12ee4397="" class="text-lg text-bold" style="font-weight: 500; font-size: 18px; color: rgb(51, 51, 51);"> {{ notice.title }} </uni-view><uni-view data-v-12ee4397="" class="margin-top-sm text-sm text-gray" style="font-weight: 400; font-size: 12px; color: rgb(153, 153, 153);"> {{ notice.publisher }}　{{ notice.time }} </uni-view></uni-view><uni-view data-v-12ee4397="" class="radius bg-white"><uni-view data-v-12ee4397="" class="vhtml margin-top" v-html="body"></uni-view></uni-view><uni-view data-v-12ee4397="" class="radius bg-white margin-top-sm"><uni-view data-v-12ee4397="" class="cu-bar flex justify-between"><uni-view data-v-12ee4397="" class="action round padding justify-start" style="width: 25px; height: 25px;" data-nav-back><uni-view data-v-12ee4397=""><uni-text data-v-12ee4397="" class="cuIcon-back text-black"><span></span></uni-text></uni-view></uni-view><uni-view data-v-12ee4397="" class="text-bold" style="font-size: 15px; color: rgb(51, 51, 51);">icard爱卡</uni-view><uni-view data-v-12ee4397="" style="width: 25px;"></uni-view></uni-view><uni-view data-v-12ee4397="" class="margin-top-sm text-sm text-gray" style="font-weight: 400; font-size: 12px; color: rgb(153, 153, 153);">收藏每一份热爱</uni-view></uni-view></uni-view>
</template>

<script setup>
import { computed } from 'vue'
import { getNotice, buildNoticeBody } from '@/mock/data'

// 与 notification/details 同源，源站同样依赖 ?id=，此处默认取第一条公告。
const n = Number(new URLSearchParams(location.hash.split('?')[1] || '').get('n') || 0) || 0
const notice = getNotice(n)
const body = computed(() => buildNoticeBody(n))
</script>