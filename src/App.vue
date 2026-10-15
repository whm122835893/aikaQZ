<script setup>
import { computed, onMounted, onBeforeUnmount } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import TabBar from './components/TabBar.vue'
import PageHead from './components/PageHead.vue'
import { PAGE_HEADS } from './data/pageHeads'
import { installNavDelegation } from './nav'
import { installActionFallback } from './nav/actions'

const TAB_ROUTES = [
  '/pages/home/home',
  '/pages/colorfulMix/colorfulMix',
  '/pages/market/market',
  '/pages/notification/notification',
  '/pages/account/account'
]
const route = useRoute()
const router = useRouter()
const showTabBar = computed(() => TAB_ROUTES.includes(route.path))
const headTitle = computed(() => PAGE_HEADS[route.path.replace(/^\//, '')] ?? null)

// 页面组件是静态快照，没有自带跳转，统一由全局事件委托接管
let disposeNav = null
let disposeAction = null
onMounted(() => {
  disposeNav = installNavDelegation(router)
  // 兜底接住剩余「可点但无反应」的控件（表单提交 / 弹层确认 / 复制等）
  disposeAction = installActionFallback()
})
onBeforeUnmount(() => {
  if (disposeNav) disposeNav()
  if (disposeAction) disposeAction()
})
</script>

<template>
  <uni-app>
    <uni-page>
      <PageHead v-if="headTitle !== null" :title="headTitle" />
      <uni-page-wrapper>
        <uni-page-body>
          <router-view />
        </uni-page-body>
        <TabBar v-if="showTabBar" />
      </uni-page-wrapper>
    </uni-page>
  </uni-app>
</template>
