<template>
  <uni-view data-v-359aa7e0="" class="container" style="padding-top: 0px;">
    <uni-view data-v-359aa7e0="">
      <uni-view data-v-359aa7e0="" class="header margin-lr">
        <uni-view data-v-359aa7e0="" class="back-btn"><uni-text data-v-359aa7e0="" class="cuIcon-back"><span></span></uni-text></uni-view>
        <uni-view data-v-359aa7e0="" class="page-title">个人信息</uni-view>
        <uni-view data-v-359aa7e0="" class="header-placeholder"></uni-view>
      </uni-view>

      <uni-view data-v-359aa7e0="" class="radius-change-radius padding-sm">
        <uni-view data-v-359aa7e0="" class="bg-white radius-change-radius">
          <uni-view data-v-359aa7e0="" class="borderBottom flex margin-bottom-sm align-center padding-tb justify-between padding-lr-sm" style="border-radius: 6px;">
            <uni-view data-v-359aa7e0="" class="flex align-center"><uni-view data-v-359aa7e0="" class="margin-left-sm title">头像</uni-view></uni-view>
            <uni-view data-v-359aa7e0="" class="flex align-center text-grey">
              <uni-image data-v-359aa7e0="" class="avatar-img">
                <div style="background-image: url(&quot;/static/images/user/logo.jpg&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;"></div>
                <img src="/static/images/user/logo.jpg" draggable="false"></uni-image>
              <uni-text data-v-359aa7e0="" class="cuIcon-right" @click="pickAvatar"><span></span></uni-text>
            </uni-view>
          </uni-view>

          <uni-view data-v-359aa7e0="" class="flex margin-bottom-sm align-center justify-between padding-lr-sm padding-tb borderBottom" style="border-radius: 6px;" @click="sheet = true">
            <uni-view data-v-359aa7e0="" class="flex align-center"><uni-view data-v-359aa7e0="" class="margin-left-sm title">昵称</uni-view></uni-view>
            <uni-view data-v-359aa7e0="" class="flex align-center text-grey">
              <uni-text data-v-359aa7e0="" class="info-value"><span>{{ nickname }}</span></uni-text>
              <uni-text data-v-359aa7e0="" class="cuIcon-right"><span></span></uni-text>
            </uni-view>
          </uni-view>

          <uni-view data-v-359aa7e0="" class="borderBottom flex margin-bottom-sm align-center justify-between padding-lr-sm padding-tb" style="border-radius: 6px;" @click="goBind">
            <uni-view data-v-359aa7e0="" class="flex align-center"><uni-view data-v-359aa7e0="" class="margin-left-sm title">绑定手机</uni-view></uni-view>
            <uni-view data-v-359aa7e0="" class="flex align-center text-grey">
              <uni-text data-v-359aa7e0="" class="info-value"><span>{{ maskedPhone }}</span></uni-text>
              <uni-text data-v-359aa7e0="" class="cuIcon-right"><span></span></uni-text>
            </uni-view>
          </uni-view>

          <uni-view data-v-359aa7e0="" class="borderother flex margin-bottom-sm align-center justify-between padding-lr-sm padding-tb" style="border-radius: 6px;">
            <uni-view data-v-359aa7e0="" class="flex align-center"><uni-view data-v-359aa7e0="" class="margin-left-sm title">钱包地址</uni-view></uni-view>
            <uni-view data-v-359aa7e0="" class="flex align-center text-grey">
              <uni-text data-v-359aa7e0="" class="info-value over" style="max-width: 200px;"><span>{{ addr }}</span></uni-text>
              <uni-text data-v-359aa7e0="" class="cuIcon-copy" @click="copyAddr"><span></span></uni-text>
            </uni-view>
          </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view data-v-359aa7e0="" class="cu-modal bottom-modal nickname-modal" :class="{ show: sheet }">
      <uni-view data-v-359aa7e0="" class="cu-dialog nickname-sheet">
        <uni-view data-v-359aa7e0="" class="nickname-sheet-title">修改昵称</uni-view>
        <uni-view data-v-359aa7e0="" class="nickname-sheet-body">
          <uni-view data-v-359aa7e0="" class="nickname-field-input">
            <uni-input data-v-359aa7e0="">
              <div class="uni-input-wrapper">
                <div class="uni-input-placeholder nickname-input-placeholder">请在此输入昵称...</div>
                <input maxlength="20" class="uni-input-input" :value="draft" @input="draft = $event.target.value" />
              </div>
            </uni-input>
          </uni-view>
        </uni-view>
        <uni-view data-v-359aa7e0="" class="nickname-sheet-footer">
          <uni-view data-v-359aa7e0="" class="sheet-btn outline" @click="sheet = false">返回</uni-view>
          <uni-view data-v-359aa7e0="" class="sheet-btn primary" @click="saveName">确定</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { authUser, toast } from '@/utils/interact'

const router = useRouter()
const sheet = ref(false)
const draft = ref('')
const nickname = ref('')
const phone = ref('')
const addr = ref('')

/** 登录后才有真实身份信息；未登录时给出占位并引导登录 */
function ensure() {
  const u = authUser.value
  if (!u) {
    // 未登录也给可见占位，避免整行空白（配合 .info-value 深色样式才看得见）
    if (!nickname.value) nickname.value = '未登录'
    if (!addr.value) addr.value = '登录后查看钱包地址'
    return false
  }
  phone.value = u.phone || ''
  if (!nickname.value || nickname.value === '未登录') {
    nickname.value = u.name || 'ICARD用户' + String(u.phone || '').slice(-4)
  }
  if (!addr.value || addr.value === '登录后查看钱包地址') {
    addr.value = '0x' + String(u.phone || '13800138000') + '0000000000000000f5'
  }
  return true
}
ensure()

const maskedPhone = computed(() =>
  phone.value ? phone.value.slice(0, 3) + '****' + phone.value.slice(-4) : '未绑定'
)

function saveName() {
  const v = draft.value.trim()
  if (!v) return toast('昵称不能为空')
  nickname.value = v
  draft.value = ''
  sheet.value = false
  toast('昵称已更新为 ' + v)
}

function pickAvatar() {
  toast('演示环境暂不支持更换头像')
}

function goBind() {
  if (phone.value) {
    toast('已绑定手机 ' + maskedPhone.value)
    return
  }
  router.push('/pages/login/login')
}

async function copyAddr() {
  if (!addr.value) return toast('请先登录查看钱包地址')
  try {
    if (navigator.clipboard && navigator.clipboard.writeText) await navigator.clipboard.writeText(addr.value)
  } catch {
    /* file:// 下剪贴板不可用 */
  }
  toast('钱包地址已复制：' + addr.value)
}
</script>
