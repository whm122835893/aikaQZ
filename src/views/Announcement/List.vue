<template>
  <uni-view style="min-height: 100vh; background-color: #f5f6f8; padding: 10px 12px 20px; box-sizing: border-box;">
    <uni-view
      v-for="(item, i) in NOTICES"
      :key="i"
      style="background: #fff; border-radius: 10px; padding: 12px; margin-bottom: 10px;"
      :data-nav-to="`/pages/Announcement/details?n=${i}`"
    >
      <uni-view style="display: flex; align-items: center;">
        <uni-image style="width: 32px; height: 32px; border-radius: 50%; flex-shrink: 0;">
          <div :style="`background-image: url(&quot;${item.avatar}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div>
          <img :src="item.avatar" draggable="false" />
        </uni-image>
        <uni-view style="flex: 1; min-width: 0; margin-left: 10px;">
          <uni-view style="font-size: 13px; color: rgb(51, 51, 51);">{{ item.publisher }}</uni-view>
          <uni-view style="font-size: 11px; color: rgb(153, 153, 153); margin-top: 2px;">{{ item.time }}</uni-view>
        </uni-view>
        <uni-text class="cu-tag2 radius sm" :style="item.tagStyle + 'font-size: 11px;'">
          <span>{{ item.tag }}</span>
        </uni-text>
      </uni-view>
      <uni-view style="margin-top: 10px; font-size: 14px; line-height: 1.6; color: rgb(51, 51, 51); font-weight: 600;">{{ item.title }}</uni-view>
      <uni-view v-if="item.images.length" style="margin-top: 10px; display: flex; gap: 8px;">
        <uni-image v-for="(img, k) in item.images" :key="k" style="width: 80px; height: 80px; border-radius: 6px; flex-shrink: 0;">
          <div :style="`background-image: url(&quot;${img}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div>
          <img :src="img" draggable="false" />
        </uni-image>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
import { NOTICES } from '@/mock/data'

// 源站这条路由抓取时渲染为 0 节点（无对应页面实现），这里按公告列表补齐，
// 便于查看；视觉沿用通知页公告卡的白底圆角风格，用内联样式实现，不改动全局 CSS。
</script>