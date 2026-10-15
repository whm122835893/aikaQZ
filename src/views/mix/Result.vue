<template>
  <uni-view data-v-a9d517da="" class="container"><uni-view data-v-a9d517da="" class="pro_img"><uni-image data-v-a9d517da="" class="img"><div :style="`background-image: url(&quot;${result.cover}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div><img :src="result.cover" draggable="false" /></uni-image></uni-view><uni-view data-v-a9d517da="" class="title" style="margin-top: 15px;"> {{ result.name }} </uni-view><uni-view data-v-a9d517da="" class="padding"><uni-view data-v-a9d517da="" class="bg-grey round cu-btn lg flex align-center justify-center" data-nav-back> 确定 </uni-view></uni-view></uni-view>
</template>

<script setup>
import { SYNTH_RESULT } from '@/mock/data'

// 与合成结果同构，源站依赖置换接口返回的参数渲染。
const result = SYNTH_RESULT
</script>