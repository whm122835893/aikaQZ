<template>
  <uni-view data-v-ba03fd20="" class="container"><uni-view data-v-ba03fd20="" class="pro_img"><uni-image data-v-ba03fd20="" class="img"><div :style="`background-image: url(&quot;${result.cover}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div><img :src="result.cover" draggable="false" /></uni-image></uni-view><uni-view data-v-ba03fd20="" class="title" style="margin-top: 15px;"> {{ result.name }} </uni-view><uni-view data-v-ba03fd20="" class="padding"><uni-view data-v-ba03fd20="" class="bg-grey lg cu-btn round flex align-center justify-center" data-nav-back> 确定 </uni-view></uni-view></uni-view>
</template>

<script setup>
import { SYNTH_RESULT } from '@/mock/data'

// 源站此页由合成接口返回结果后渲染，图片与标题都是空插值；这里用演示数据填充。
const result = SYNTH_RESULT
</script>