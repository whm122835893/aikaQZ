<template>
  <uni-view class="padding" style="padding-top: 12px;">
    <uni-view style="display: flex; flex-wrap: wrap;">
      <uni-view v-for="g in goods" :key="g.title" class="item" data-nav-to="/pages/market/details">
        <uni-image style="width: 106px; height: 106px; border-radius: 8px;">
          <div :style="`background-image: url(&quot;${g.image}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div>
          <img :src="g.image" draggable="false" />
        </uni-image>
        <uni-view style="width: 106px; margin-top: 6px; font-size: 11px; color: rgb(51, 51, 51); line-height: 1.4; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">{{ g.title }}</uni-view>
        <uni-view style="font-size: 12px; color: rgb(229, 77, 66); margin-top: 2px;">¥{{ g.price }}</uni-view>
      </uni-view>
    </uni-view>
    <uni-view style="margin: 16px 4px 0; font-size: 12px; color: rgb(153, 153, 153); line-height: 1.9;">
      卡鉴是 ICARD 爱卡平台为数字藏品提供的鉴证档案，链上编号与持有信息一一可查。<br />
      源站此页需要藏品编号参数并渲染证书画布，克隆版以藏品网格形式呈现。
    </uni-view>
  </uni-view>
</template>

<script setup>
import { GOODS } from '@/mock/data'

// 源站为canvas 证书页（依赖藏品编号参数），无参时是空壳；
// 这里复用页面自带的 .item 三列栅格类展示藏品网格。
const goods = GOODS.slice(0, 6)
</script>