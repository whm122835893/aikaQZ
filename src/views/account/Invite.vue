<template>
  <uni-view data-v-6098179e="" class="invite-page">
    <uni-view data-v-6098179e="" class="hero-wrap">
      <uni-image data-v-6098179e="" class="hero-bg" style="height: 810px;">
        <div style="background-image: url(&quot;/static/images/invite/icon/3.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
        <img src="/static/images/invite/icon/3.png" draggable="false"></uni-image>
    </uni-view>

    <uni-view data-v-6098179e="" class="header" style="padding-top: 24px;">
      <uni-view data-v-6098179e="" class="back-btn"><uni-text data-v-6098179e="" class="cuIcon-back"><span></span></uni-text></uni-view>
      <uni-view data-v-6098179e="" class="page-title">邀请好友</uni-view>
      <uni-view data-v-6098179e="" class="header-placeholder"></uni-view>
    </uni-view>

    <uni-view data-v-6098179e="" class="invite-body">
      <uni-view data-v-6098179e="" class="top-content">
        <uni-view data-v-6098179e="" class="code-card">
          <uni-view data-v-6098179e="" class="code-left">
            <uni-view data-v-6098179e="" class="code-label">我的邀请码</uni-view>
            <uni-view data-v-6098179e="" class="code-row">
              <uni-text data-v-6098179e="" class="code-value"><span>{{ myCode }}</span></uni-text>
              <uni-image data-v-6098179e="" class="copy-icon" @click="copyText(myCode, '邀请码已复制')">
                <div style="background-image: url(&quot;/static/images/invite/icon/2.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div>
                <img src="/static/images/invite/icon/2.png" draggable="false"></uni-image>
            </uni-view>
            <uni-view data-v-6098179e="" class="code-desc">邀请好友注册，一起收藏热爱</uni-view>
          </uni-view>
          <uni-view data-v-6098179e="" class="code-divider"></uni-view>
          <uni-view data-v-6098179e="" class="code-right">
            <uni-view data-v-6098179e="" class="qr-wrap">
              <uni-view data-v-6098179e="" class="qr-fake">{{ qrText }}</uni-view>
              <uni-view data-v-6098179e="" class="qr-hit" @click="copyText(inviteLink, '邀请链接已复制')"></uni-view>
            </uni-view>
            <uni-view data-v-6098179e="" class="qr-label">扫码加入</uni-view>
          </uni-view>
        </uni-view>
      </uni-view>

      <uni-view data-v-6098179e="" class="action-btns">
        <uni-view data-v-6098179e="" class="btn-share" @click="poster = true">
          <uni-image data-v-6098179e="" class="btn-icon">
            <div style="background-image: url(&quot;/static/images/invite/icon/4.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div>
            <img src="/static/images/invite/icon/4.png" draggable="false"></uni-image>
          <uni-text data-v-6098179e=""><span>分享邀请海报</span></uni-text>
        </uni-view>
        <uni-view data-v-6098179e="" class="btn-copy-link" @click="copyText(inviteLink, '邀请链接已复制')">
          <uni-image data-v-6098179e="" class="btn-icon btn-icon-dark">
            <div style="background-image: url(&quot;/static/images/invite/icon/1.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div>
            <img src="/static/images/invite/icon/1.png" draggable="false"></uni-image>
          <uni-text data-v-6098179e=""><span>复制链接</span></uni-text>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-scroll-view data-v-6098179e="" class="invite-scroll-body">
      <div class="uni-scroll-view">
        <div class="uni-scroll-view" style="overflow: hidden auto;">
          <div class="uni-scroll-view-content">
            <uni-view data-v-6098179e="" class="record-card">
              <uni-view data-v-6098179e="" class="record-title">邀请记录</uni-view>
              <uni-view v-if="!records.length" data-v-6098179e="" class="record-empty">
                <uni-view data-v-6098179e="" class="empty-text">暂无邀请记录</uni-view>
              </uni-view>
              <uni-view v-for="r in records" v-else data-v-6098179e="" :key="r.phone" class="record-item">
                <uni-text data-v-6098179e="" class="record-phone"><span>{{ maskPhone(r.phone) }}</span></uni-text>
                <uni-text data-v-6098179e="" class="record-time"><span>{{ r.time }}</span></uni-text>
                <uni-text data-v-6098179e="" class="record-reward"><span>+{{ r.reward }} 积分</span></uni-text>
              </uni-view>
            </uni-view>
            <uni-view data-v-6098179e="" class="page-bottom-space"></uni-view>
          </div>
        </div>
      </div>
    </uni-scroll-view>

    <uni-view data-v-6098179e="" class="cu-modal" :class="{ show: poster }">
      <uni-view data-v-6098179e="" class="cu-dialog poster-dialog">
        <uni-view data-v-6098179e="" id="htmlCanvas" class="poster-box">
          <uni-image data-v-6098179e="" class="poster-bg" style="height: 396px;">
            <div style="background-image: url(&quot;/static/images/invite/1.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
            <img src="/static/images/invite/1.png" draggable="false"></uni-image>
          <uni-view data-v-6098179e="" class="poster-content">
            <uni-view data-v-6098179e="" class="poster-code-label">我的邀请码</uni-view>
            <uni-view data-v-6098179e="" class="poster-code">{{ myCode }}</uni-view>
            <uni-view data-v-6098179e="" class="poster-qr-wrap">
              <uni-view data-v-6098179e="" class="qr-fake big">{{ qrText }}</uni-view>
            </uni-view>
            <uni-view data-v-6098179e="" class="poster-tip">扫码加入，一起收藏热爱</uni-view>
          </uni-view>
        </uni-view>
        <uni-view data-v-6098179e="" class="poster-save" @click="closePoster">截图保存</uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
import { computed, ref } from 'vue'
import { authUser, toast } from '@/utils/interact'

const poster = ref(false)

/** 演示用：邀请记录初始为空，可通过邀请链接进入后再由外部注入 */
const records = ref([])

const myCode = computed(() => {
  const phone = (authUser.value && authUser.value.phone) || '13800138000'
  return 'IC' + phone.slice(-6)
})

const inviteLink = computed(() => 'https://h5.shenyuan.sc.cn/#/pages/login/register?code=' + myCode.value)

/** 演示环境没有二维码库，用邀请码渲染成方块占位，语义等价 */
const qrText = computed(() => myCode.value)

function maskPhone(p) {
  return p.slice(0, 3) + '****' + p.slice(-4)
}

async function copyText(text, okTip) {
  if (!text) return toast('内容为空')
  try {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      await navigator.clipboard.writeText(text)
    }
  } catch {
    /* file:// 下 clipboard 不可用，降级为提示 */
  }
  toast(okTip + '：' + text)
}

function closePoster() {
  poster.value = false
  toast('演示环境无法直接保存图片，请截图保存')
}
</script>
