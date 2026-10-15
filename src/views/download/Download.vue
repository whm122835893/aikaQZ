<template>
  <uni-view data-v-0b05f8fb="" class="download-page">
    <uni-image data-v-0b05f8fb="" class="page-bg">
      <div style="background-image: url(&quot;/static/images/invite/bg.png&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;"></div>
      <img src="/static/images/invite/bg.png" draggable="false"></uni-image>

    <uni-view data-v-0b05f8fb="" class="page-content" style="padding-top: 0px;">
      <uni-view data-v-0b05f8fb="" class="back-btn"><uni-text data-v-0b05f8fb="" class="cuIcon-back"><span></span></uni-text></uni-view>

      <uni-view data-v-0b05f8fb="" class="brand-wrap">
        <uni-image data-v-0b05f8fb="" class="brand-img" style="height: 170px;">
          <div style="background-image: url(&quot;/static/images/invite/top.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
          <img src="/static/images/invite/top.png" draggable="false"></uni-image>
      </uni-view>

      <uni-view data-v-0b05f8fb="" class="download-btns">
        <uni-view data-v-0b05f8fb="" class="dl-card" @click="pick('H5')">
          <uni-image data-v-0b05f8fb="" class="download-btn" style="height: 70px;">
            <div style="background-image: url(&quot;/static/images/invite/6.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
            <img src="/static/images/invite/6.png" draggable="false"></uni-image>
          <uni-view data-v-0b05f8fb="" class="dl-name">网页版</uni-view>
          <uni-view data-v-0b05f8fb="" class="dl-desc">浏览器直接访问，无需安装</uni-view>
        </uni-view>
        <uni-view data-v-0b05f8fb="" class="dl-card" @click="pick('App')">
          <uni-image data-v-0b05f8fb="" class="download-btn" style="height: 70px;">
            <div style="background-image: url(&quot;/static/images/invite/7.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
            <img src="/static/images/invite/7.png" draggable="false"></uni-image>
          <uni-view data-v-0b05f8fb="" class="dl-name">App 客户端</uni-view>
          <uni-view data-v-0b05f8fb="" class="dl-desc">iOS / Android 均可下载</uni-view>
        </uni-view>
      </uni-view>

      <uni-view data-v-0b05f8fb="" v-if="qrText" class="qr-box">
        <uni-view data-v-0b05f8fb="" class="qr-fake big">{{ qrText }}</uni-view>
        <uni-view data-v-0b05f8fb="" class="qr-tip">扫码下载 {{ picked }}</uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
import { computed, ref } from 'vue'
import { toast } from '@/utils/interact'

const picked = ref('')
const qrText = computed(() => picked.value)

function pick(platform) {
  picked.value = platform
  toast('正在准备' + platform + '安装包（演示环境不提供真实下载）')
}
</script>
