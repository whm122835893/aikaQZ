<template>
  <uni-view data-v-a8b9ecec="" class="setting-page" style="padding-top: 0px;">
    <uni-view data-v-a8b9ecec="" class="header">
      <uni-view data-v-a8b9ecec="" class="back-btn"><uni-text data-v-a8b9ecec="" class="cuIcon-back"><span></span></uni-text></uni-view>
      <uni-view data-v-a8b9ecec="" class="page-title">隐私设置</uni-view>
      <uni-view data-v-a8b9ecec="" class="header-placeholder"></uni-view>
    </uni-view>

    <uni-view data-v-a8b9ecec="" class="section">
      <uni-view data-v-a8b9ecec="" class="setting-list">
        <uni-view data-v-a8b9ecec="" class="setting-item" @click="setPwd">
          <uni-view data-v-a8b9ecec="" class="setting-left">
            <uni-image data-v-a8b9ecec="" class="setting-icon">
              <div style="background-image: url(&quot;/static/images/user/3.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div>
              <img src="/static/images/user/3.png" draggable="false"></uni-image>
            <uni-text data-v-a8b9ecec="" class="setting-label"><span>设置操作密码</span></uni-text>
          </uni-view>
          <uni-view data-v-a8b9ecec="" class="setting-right">
            <uni-text data-v-a8b9ecec="" class="setting-value"><span>{{ pwdSet ? '已设置' : '未设置' }}</span></uni-text>
            <uni-text data-v-a8b9ecec="" class="cuIcon-right"><span></span></uni-text>
          </uni-view>
        </uni-view>

        <uni-view data-v-a8b9ecec="" class="setting-item" @click="toForget">
          <uni-view data-v-a8b9ecec="" class="setting-left">
            <uni-image data-v-a8b9ecec="" class="setting-icon">
              <div style="background-image: url(&quot;/static/images/user/4.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div>
              <img src="/static/images/user/4.png" draggable="false"></uni-image>
            <uni-text data-v-a8b9ecec="" class="setting-label"><span>找回密码</span></uni-text>
          </uni-view>
          <uni-view data-v-a8b9ecec="" class="setting-right">
            <uni-text data-v-a8b9ecec="" class="cuIcon-right"><span></span></uni-text>
          </uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view data-v-a8b9ecec="" class="cu-modal" :class="{ show: sheet }">
      <uni-view data-v-a8b9ecec="" class="cu-dialog bg-white text-left padding radius">
        <uni-view data-v-a8b9ecec="" class="text-center text-bold text-lg"> 设置操作密码 </uni-view>
        <uni-view data-v-a8b9ecec="" class="margin-top">
          <uni-text data-v-a8b9ecec="" class="text-sm text-grey"><span>操作密码用于购买、寄售、转赠等关键操作确认</span></uni-text>
        </uni-view>
        <uni-view data-v-a8b9ecec="" class="margin-top-sm radius padding bg-gray">
          <uni-input data-v-a8b9ecec="">
            <div class="uni-input-wrapper">
              <div class="uni-input-placeholder text-grey text-sm">请输入6 位操作密码</div>
              <input maxlength="6" type="password" class="uni-input-input" :value="pwd" @input="pwd = $event.target.value" />
            </div>
          </uni-input>
        </uni-view>
        <uni-view data-v-a8b9ecec="" class="margin-top radius padding bg-gray">
          <uni-input data-v-a8b9ecec="">
            <div class="uni-input-wrapper">
              <div class="uni-input-placeholder text-grey text-sm">请再次输入操作密码</div>
              <input maxlength="6" type="password" class="uni-input-input" :value="pwd2" @input="pwd2 = $event.target.value" />
            </div>
          </uni-input>
        </uni-view>
        <uni-view data-v-a8b9ecec="" class="margin-top-xl flex align-center">
          <uni-view data-v-a8b9ecec="" class="cu-btn lg bg-gray flex-sub radius margin-right-sm" @click="sheet = false"> 取消 </uni-view>
          <uni-view data-v-a8b9ecec="" class="cu-btn lg btn-action-yellow flex-sub radius" @click="submit"> 确定 </uni-view>
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
  if (!/^\d{6}$/.test(pwd.value)) return toast('操作密码需为 6 位数字')
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
