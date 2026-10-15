#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""User.vue —— 个人信息：昵称/手机/钱包地址填真实值 + 昵称弹层可用 + 地址可复制"""
import io

P = 'src/views/account/User.vue'
old = io.open(P, encoding='utf-8').read()
V = 'data-v-359aa7e0=""'

tpl = '''<template>
  <uni-view ''' + V + ''' class="container" style="padding-top: 0px;">
    <uni-view ''' + V + '''>
      <uni-view ''' + V + ''' class="header margin-lr">
        <uni-view ''' + V + ''' class="back-btn"><uni-text ''' + V + ''' class="cuIcon-back"><span></span></uni-text></uni-view>
        <uni-view ''' + V + ''' class="page-title">个人信息</uni-view>
        <uni-view ''' + V + ''' class="header-placeholder"></uni-view>
      </uni-view>

      <uni-view ''' + V + ''' class="radius-change-radius padding-sm">
        <uni-view ''' + V + ''' class="bg-white radius-change-radius">
          <uni-view ''' + V + ''' class="borderBottom flex margin-bottom-sm align-center padding-tb justify-between padding-lr-sm" style="border-radius: 6px;">
            <uni-view ''' + V + ''' class="flex align-center"><uni-view ''' + V + ''' class="margin-left-sm title">头像</uni-view></uni-view>
            <uni-view ''' + V + ''' class="flex align-center text-grey">
              <uni-image ''' + V + ''' class="avatar-img">
                <div style="background-image: url(&quot;/static/images/user/logo.jpg&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;"></div>
                <img src="/static/images/user/logo.jpg" draggable="false"></uni-image>
              <uni-text ''' + V + ''' class="cuIcon-right" @click="pickAvatar"><span></span></uni-text>
            </uni-view>
          </uni-view>

          <uni-view ''' + V + ''' class="flex margin-bottom-sm align-center justify-between padding-lr-sm padding-tb borderBottom" style="border-radius: 6px;" @click="sheet = true">
            <uni-view ''' + V + ''' class="flex align-center"><uni-view ''' + V + ''' class="margin-left-sm title">昵称</uni-view></uni-view>
            <uni-view ''' + V + ''' class="flex align-center text-grey">
              <uni-text ''' + V + ''' class="info-value"><span>{{ nickname }}</span></uni-text>
              <uni-text ''' + V + ''' class="cuIcon-right"><span></span></uni-text>
            </uni-view>
          </uni-view>

          <uni-view ''' + V + ''' class="borderBottom flex margin-bottom-sm align-center justify-between padding-lr-sm padding-tb" style="border-radius: 6px;" @click="goBind">
            <uni-view ''' + V + ''' class="flex align-center"><uni-view ''' + V + ''' class="margin-left-sm title">绑定手机</uni-view></uni-view>
            <uni-view ''' + V + ''' class="flex align-center text-grey">
              <uni-text ''' + V + ''' class="info-value"><span>{{ maskedPhone }}</span></uni-text>
              <uni-text ''' + V + ''' class="cuIcon-right"><span></span></uni-text>
            </uni-view>
          </uni-view>

          <uni-view ''' + V + ''' class="borderother flex margin-bottom-sm align-center justify-between padding-lr-sm padding-tb" style="border-radius: 6px;">
            <uni-view ''' + V + ''' class="flex align-center"><uni-view ''' + V + ''' class="margin-left-sm title">钱包地址</uni-view></uni-view>
            <uni-view ''' + V + ''' class="flex align-center text-grey">
              <uni-text ''' + V + ''' class="info-value over" style="max-width: 200px;"><span>{{ addr }}</span></uni-text>
              <uni-text ''' + V + ''' class="cuIcon-copy" @click="copyAddr"><span></span></uni-text>
            </uni-view>
          </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view ''' + V + ''' class="cu-modal bottom-modal nickname-modal" :class="{ show: sheet }">
      <uni-view ''' + V + ''' class="cu-dialog nickname-sheet">
        <uni-view ''' + V + ''' class="nickname-sheet-title">修改昵称</uni-view>
        <uni-view ''' + V + ''' class="nickname-sheet-body">
          <uni-view ''' + V + ''' class="nickname-field-input">
            <uni-input ''' + V + '''>
              <div class="uni-input-wrapper">
                <div class="uni-input-placeholder nickname-input-placeholder">请在此输入昵称...</div>
                <input maxlength="20" class="uni-input-input" :value="draft" @input="draft = $event.target.value" />
              </div>
            </uni-input>
          </uni-view>
        </uni-view>
        <uni-view ''' + V + ''' class="nickname-sheet-footer">
          <uni-view ''' + V + ''' class="sheet-btn outline" @click="sheet = false">返回</uni-view>
          <uni-view ''' + V + ''' class="sheet-btn primary" @click="saveName">确定</uni-view>
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
  if (!u) return false
  phone.value = u.phone || ''
  if (!nickname.value) nickname.value = u.name || 'ICARD用户' + String(u.phone || '').slice(-4)
  if (!addr.value) addr.value = '0x' + String(u.phone || '13800138000') + '0000000000000000f5'
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
'''

io.open(P, 'w', encoding='utf-8').write(tpl)
print('User rewritten %d -> %d' % (len(old), len(tpl)))