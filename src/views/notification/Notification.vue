<template>
  <uni-view data-v-53f7b619="" class="container">
    <uni-view data-v-53f7b619="" class="page-bg">
      <uni-image data-v-53f7b619="" class="page-bg-img" style="height: 812px;">
        <div style="background-image: url(&quot;/static/images/index/icon/bg.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
        <img src="/static/images/index/icon/bg.png" draggable="false"></uni-image>
    </uni-view>

    <uni-view data-v-53f7b619="" class="hero-watermark-wrap" style="top: 12px;">
      <uni-image data-v-53f7b619="" class="hero-watermark">
        <div style="background-image: url(&quot;/static/images/login/2.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div>
        <img src="/static/images/login/2.png" draggable="false"></uni-image>
    </uni-view>

    <uni-view data-v-53f7b619="" class="page-content">
      <uni-view data-v-53f7b619="" class="notice-header" style="padding-top: 8px;">
        <uni-view data-v-53f7b619="" class="notice-header-bg">
          <uni-image data-v-53f7b619="" class="notice-header-bg-img" style="height: 812px;">
            <div style="background-image: url(&quot;/static/images/index/icon/bg.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
            <img src="/static/images/index/icon/bg.png" draggable="false"></uni-image>
        </uni-view>

        <uni-view data-v-53f7b619="" class="hero-watermark-wrap header-watermark">
          <uni-image data-v-53f7b619="" class="hero-watermark">
            <div style="background-image: url(&quot;/static/images/login/2.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div>
            <img src="/static/images/login/2.png" draggable="false"></uni-image>
        </uni-view>

        <uni-view data-v-53f7b619="" class="notice-header-inner padding-lr flex flex-direction">
          <uni-view data-v-53f7b619="" class="brand-row">
            <uni-view data-v-53f7b619="" class="brand-left">
              <uni-image data-v-53f7b619="" class="tag-icon" style="width: 56px;">
                <div style="background-image: url(&quot;/static/images/index/icon/icon.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
                <img src="/static/images/index/icon/icon.png" draggable="false"></uni-image>
              <uni-text data-v-53f7b619="" class="slogan"><span>收藏每一份热爱</span></uni-text>
            </uni-view>
            <uni-view data-v-53f7b619="" class="brand-actions">
              <uni-view data-v-53f7b619="" class="action-btn" @click="focusSearch">
                <uni-text data-v-53f7b619="" class="cuIcon-search"><span></span></uni-text>
              </uni-view>
              <uni-view data-v-53f7b619="" class="assist-btn" @click="toService">
                <uni-image data-v-53f7b619="" class="assist-gif">
                  <div style="background-image: none; background-position: center center; background-size: contain; background-repeat: no-repeat;"></div>
                </uni-image>
              </uni-view>
            </uni-view>
          </uni-view>

          <uni-view data-v-53f7b619="" class="search-row">
            <uni-view data-v-53f7b619="" class="search-box">
              <uni-text data-v-53f7b619="" class="cuIcon-search search-icon"><span></span></uni-text>
              <uni-input data-v-53f7b619="" class="search-input">
                <div class="uni-input-wrapper">
                  <div class="uni-input-placeholder placeholder">输入搜索的信息</div>
                  <input maxlength="40" class="uni-input-input" :value="kw" @input="kw = $event.target.value" />
                </div>
              </uni-input>
              <uni-text v-if="kw" data-v-53f7b619="" class="cuIcon-close search-clear" @click="kw = ''"><span></span></uni-text>
            </uni-view>
          </uni-view>
        </uni-view>

        <uni-scroll-view data-v-53f7b619="" class="category-scroll">
          <div class="uni-scroll-view">
            <div class="uni-scroll-view" style="overflow: auto hidden;">
              <div class="uni-scroll-view-content">
                <uni-view data-v-53f7b619="" class="category-tabs">
                  <uni-view
                    v-for="c in CATS"
                    :key="c"
                    data-v-53f7b619="" class="text-lg text-center items cat-tab"
                    :class="{ active: cat === c }"
                    style="position: relative;"
                    @click="cat = c"
                  >
                    <uni-view data-v-53f7b619="" class="over"> {{ c }} </uni-view>
                    <uni-view v-if="cat === c" data-v-53f7b619="" class="line"></uni-view>
                  </uni-view>
                </uni-view>
              </div>
            </div>
          </div>
        </uni-scroll-view>
      </uni-view>

      <uni-view data-v-53f7b619="" class="notice-header-spacer" style="height: 155px;"></uni-view>

      <uni-view data-v-53f7b619="" class="margin-lr notice-list-wrap">
        <uni-view data-v-53f7b619="" class="notice-list">
          <uni-view v-for="n in shown" :key="n.title" data-v-53f7b619="" class="notice-card margin-bottom-sm" @click="go(n)">
            <uni-view data-v-53f7b619="" class="notice-card-top">
              <uni-view data-v-53f7b619="" class="flex align-center publisher-row flex-sub">
                <uni-image data-v-53f7b619="" class="publisher-avatar" :style="bgImg(n.avatar)">
                  <div :style="bgImg(n.avatar)"></div>
                  <img :src="n.avatar" draggable="false"></uni-image>
                <uni-view data-v-53f7b619="" class="flex-sub margin-left-sm">
                  <uni-view data-v-53f7b619="" class="publisher-name"> {{ n.publisher }} </uni-view>
                  <uni-view data-v-53f7b619="" class="publisher-time">{{ n.time }}</uni-view>
                </uni-view>
              </uni-view>
            </uni-view>

            <uni-view data-v-53f7b619="" class="title-row margin-top-sm">
              <uni-text data-v-53f7b619="" class="cu-tag2 notice-tag radius sm" :style="n.tagStyle">
                <span> {{ n.tag }} </span>
              </uni-text>
              <uni-text data-v-53f7b619="" class="notice-title-text"><span>{{ n.title }}</span></uni-text>
            </uni-view>

            <uni-view v-if="n.images && n.images.length" data-v-53f7b619="" class="notice-imgs margin-top-sm">
              <uni-image
                v-for="(im, k) in n.images"
                :key="k"
                data-v-53f7b619="" class="notice-img"
                :style="bgImg(im)"
              >
                <div :style="bgImg(im)"></div>
                <img :src="im" draggable="false"></uni-image>
            </uni-view>
          </uni-view>

          <uni-view v-if="!shown.length" data-v-53f7b619="" class="empty-box"> 没有匹配的公告 </uni-view>
        </uni-view>
      </uni-view>

      <uni-view data-v-53f7b619="" style="height: 60px;"></uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { NOTICES } from '@/mock/data'
import { toast } from '@/utils/interact'

const router = useRouter()

const CATS = ['全部', '寄售公告', '上新公告', '活动公告', '运营公告', '辟谣公告', '空投公告', '合成公告', '公司新闻']
const cat = ref('全部')
const kw = ref('')

const shown = computed(() => {
  let list = cat.value === '全部' ? NOTICES : NOTICES.filter((n) => n.tag === cat.value)
  const q = kw.value.trim()
  return q ? list.filter((n) => n.title.includes(q) || n.tag.includes(q)) : list
})

function bgImg(url) {
  if (!url) return {}
  return { backgroundImage: 'url(' + url + ')', backgroundPosition: 'center center', backgroundSize: 'cover', backgroundRepeat: 'no-repeat' }
}

function go(n) {
  const i = NOTICES.indexOf(n)
  router.push({ path: '/pages/notification/details', query: { n: String(i + 1) } })
}

function focusSearch() {
  const el = document.querySelector('.notice-header .uni-input-input')
  if (el && el.focus) el.focus()
  toast('可直接输入关键词筛选公告')
}

function toService() {
  router.push('/pages/account/service')
}
</script>
