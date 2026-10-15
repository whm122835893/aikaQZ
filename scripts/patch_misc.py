#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ColorfulMix / Privacy / Download 三页的死控件补交互"""
import io

# ==================== ColorfulMix ====================
P = 'src/views/colorfulMix/ColorfulMix.vue'
s = io.open(P, encoding='utf-8').read()
o = len(s)

# 1) 第2 个 quick-card（active/5.png）没有 data-nav-to
i = s.find('class="quick-card"><uni-image data-v-c21e211e="" class="quick-img" style="height: 80px;"><div style="background-image: url(&quot;/static/images/active/5.png&quot;)')
assert i > 0
s = s[:i] + s[i:].replace(
    'class="quick-card">',
    'class="quick-card" data-nav-to="/pages/mix/mix" @click="tap(\'合成我的藏品\')">',
    1)

# 2) activity-card 加点击
old = '<uni-view data-v-c21e211e="" class="activity-card">'
assert old in s
s = s.replace(old, '<uni-view data-v-c21e211e="" class="activity-card" @click="actTap">', 1)

# 3) compose-banner-wrap 加跳转
old = '<uni-view data-v-c21e211e="" class="compose-banner-wrap">'
assert old in s
s = s.replace(old, '<uni-view data-v-c21e211e="" class="compose-banner-wrap" data-nav-to="/pages/mix/mix">', 1)

script = '''
<script setup>
import { useRouter } from 'vue-router'
import { toast } from '@/utils/interact'

const router = useRouter()

function tap(name) {
  toast(name + '（演示环境）')
}

function actTap() {
  toast('活动将于 2026-10-07 10:00 开始，可先查看合成记录')
  router.push('/pages/colorfulMix/records')
}
</script>
'''
s = s.replace('\n</template>\n', '\n</template>\n' + script, 1)
io.open(P, 'w', encoding='utf-8').write(s)
print('ColorfulMix %d -> %d' % (o, len(s)))


# ==================== Privacy ====================
P = 'src/views/account/Privacy.vue'
old = io.open(P, encoding='utf-8').read()
V = 'data-v-a8b9ecec=""'

tpl = '''<template>
  <uni-view ''' + V + ''' class="setting-page" style="padding-top: 0px;">
    <uni-view ''' + V + ''' class="header">
      <uni-view ''' + V + ''' class="back-btn"><uni-text ''' + V + ''' class="cuIcon-back"><span></span></uni-text></uni-view>
      <uni-view ''' + V + ''' class="page-title">隐私设置</uni-view>
      <uni-view ''' + V + ''' class="header-placeholder"></uni-view>
    </uni-view>

    <uni-view ''' + V + ''' class="section">
      <uni-view ''' + V + ''' class="setting-list">
        <uni-view ''' + V + ''' class="setting-item" @click="setPwd">
          <uni-view ''' + V + ''' class="setting-left">
            <uni-image ''' + V + ''' class="setting-icon">
              <div style="background-image: url(&quot;/static/images/user/3.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div>
              <img src="/static/images/user/3.png" draggable="false"></uni-image>
            <uni-text ''' + V + ''' class="setting-label"><span>设置操作密码</span></uni-text>
          </uni-view>
          <uni-view ''' + V + ''' class="setting-right">
            <uni-text ''' + V + ''' class="setting-value"><span>{{ pwdSet ? '已设置' : '未设置' }}</span></uni-text>
            <uni-text ''' + V + ''' class="cuIcon-right"><span></span></uni-text>
          </uni-view>
        </uni-view>

        <uni-view ''' + V + ''' class="setting-item" @click="toForget">
          <uni-view ''' + V + ''' class="setting-left">
            <uni-image ''' + V + ''' class="setting-icon">
              <div style="background-image: url(&quot;/static/images/user/4.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div>
              <img src="/static/images/user/4.png" draggable="false"></uni-image>
            <uni-text ''' + V + ''' class="setting-label"><span>找回密码</span></uni-text>
          </uni-view>
          <uni-view ''' + V + ''' class="setting-right">
            <uni-text ''' + V + ''' class="cuIcon-right"><span></span></uni-text>
          </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view ''' + V + ''' class="cu-modal" :class="{ show: sheet }">
      <uni-view ''' + V + ''' class="cu-dialog bg-white text-left padding radius">
        <uni-view ''' + V + ''' class="text-center text-bold text-lg"> 设置操作密码 </uni-view>
        <uni-view ''' + V + ''' class="margin-top">
          <uni-text ''' + V + ''' class="text-sm text-grey"><span>操作密码用于购买、寄售、转赠等关键操作确认</span></uni-text>
        </uni-view>
        <uni-view ''' + V + ''' class="margin-top-sm radius padding bg-gray">
          <uni-input ''' + V + '''>
            <div class="uni-input-wrapper">
              <div class="uni-input-placeholder text-grey text-sm">请输入6 位操作密码</div>
              <input maxlength="6" type="password" class="uni-input-input" :value="pwd" @input="pwd = $event.target.value" />
            </div>
          </uni-input>
        </uni-view>
        <uni-view ''' + V + ''' class="margin-top radius padding bg-gray">
          <uni-input ''' + V + '''>
            <div class="uni-input-wrapper">
              <div class="uni-input-placeholder text-grey text-sm">请再次输入操作密码</div>
              <input maxlength="6" type="password" class="uni-input-input" :value="pwd2" @input="pwd2 = $event.target.value" />
            </div>
          </uni-input>
        </uni-view>
        <uni-view ''' + V + ''' class="margin-top-xl flex align-center">
          <uni-view ''' + V + ''' class="cu-btn lg bg-gray flex-sub radius margin-right-sm" @click="sheet = false"> 取消 </uni-view>
          <uni-view ''' + V + ''' class="cu-btn lg btn-action-yellow flex-sub radius" @click="submit"> 确定 </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { toast } from '@/utils/interact'

const router = useRouter()
const sheet = ref(false)
const pwd = ref('')
const pwd2 = ref('')
const pwdSet = ref(false)

function setPwd() {
  sheet.value = true
}

function submit() {
  if (!/^\\d{6}$/.test(pwd.value)) return toast('操作密码需为 6 位数字')
  if (pwd.value !== pwd2.value) return toast('两次输入不一致')
  pwdSet.value = true
  sheet.value = false
  pwd.value = ''
  pwd2.value = ''
  toast('操作密码设置成功')
}

function toForget() {
  router.push('/pages/login/forget')
}
</script>
'''
io.open(P, 'w', encoding='utf-8').write(tpl)
print('Privacy %d -> %d' % (len(old), len(tpl)))


# ==================== Download ====================
P = 'src/views/download/Download.vue'
old = io.open(P, encoding='utf-8').read()
V = 'data-v-0b05f8fb=""'

tpl = '''<template>
  <uni-view ''' + V + ''' class="download-page">
    <uni-image ''' + V + ''' class="page-bg">
      <div style="background-image: url(&quot;/static/images/invite/bg.png&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;"></div>
      <img src="/static/images/invite/bg.png" draggable="false"></uni-image>

    <uni-view ''' + V + ''' class="page-content" style="padding-top: 0px;">
      <uni-view ''' + V + ''' class="back-btn"><uni-text ''' + V + ''' class="cuIcon-back"><span></span></uni-text></uni-view>

      <uni-view ''' + V + ''' class="brand-wrap">
        <uni-image ''' + V + ''' class="brand-img" style="height: 170px;">
          <div style="background-image: url(&quot;/static/images/invite/top.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
          <img src="/static/images/invite/top.png" draggable="false"></uni-image>
      </uni-view>

      <uni-view ''' + V + ''' class="download-btns">
        <uni-view ''' + V + ''' class="dl-card" @click="pick('H5')">
          <uni-image ''' + V + ''' class="download-btn" style="height: 70px;">
            <div style="background-image: url(&quot;/static/images/invite/6.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
            <img src="/static/images/invite/6.png" draggable="false"></uni-image>
          <uni-view ''' + V + ''' class="dl-name">网页版</uni-view>
          <uni-view ''' + V + ''' class="dl-desc">浏览器直接访问，无需安装</uni-view>
        </uni-view>
        <uni-view ''' + V + ''' class="dl-card" @click="pick('App')">
          <uni-image ''' + V + ''' class="download-btn" style="height: 70px;">
            <div style="background-image: url(&quot;/static/images/invite/7.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
            <img src="/static/images/invite/7.png" draggable="false"></uni-image>
          <uni-view ''' + V + ''' class="dl-name">App 客户端</uni-view>
          <uni-view ''' + V + ''' class="dl-desc">iOS / Android 均可下载</uni-view>
        </uni-view>
      </uni-view>

      <uni-view ''' + V + ''' v-if="qrText" class="qr-box">
        <uni-view ''' + V + ''' class="qr-fake big">{{ qrText }}</uni-view>
        <uni-view ''' + V + ''' class="qr-tip">扫码下载 {{ picked }}</uni-view>
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
'''
io.open(P, 'w', encoding='utf-8').write(tpl)
print('Download %d -> %d' % (len(old), len(tpl)))