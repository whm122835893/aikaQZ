<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const props = defineProps({ title: { type: String, default: '' } })
</script>

<template>
  <uni-page-head uni-page-head-type="default">
    <div class="uni-page-head" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);">
      <div class="uni-page-head-hd">
        <div class="uni-page-head-btn" @click="router.back()">
          <i class="uni-btn-icon" style="color: rgb(0, 0, 0); font-size: 27px;">&#xe601;</i>
        </div>
        <div class="uni-page-head-ft"></div>
      </div>
      <div class="uni-page-head-bd">
        <div class="uni-page-head__title" style="font-size: 16px; opacity: 1;">{{ props.title }}</div>
      </div>
      <div class="uni-page-head-ft"></div>
    </div>
    <div class="uni-placeholder"></div>
  </uni-page-head>
</template>
