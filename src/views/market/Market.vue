<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { GOODS } from '@/mock/goods'
import { toast } from '@/utils/interact'

const router = useRouter()
const route = useRoute()

const activeTab = ref('活动市场')
const activeTag = ref('小试牛刀')
const activeSort = ref('全部份数')
const kw = ref(String(route.query.kw || ''))
const viewMode = ref('list') // 'list' | 'grid'

function toggleViewMode() {
  viewMode.value = viewMode.value === 'list' ? 'grid' : 'list'
}

/** 列表数据：把 null 地板价统一显示为 '--' */
const rows = GOODS.map((g) => ({
  ...g,
  floor: g.floor == null ? '--' : String(g.floor)
}))

const shown = computed(() => {
  let arr = rows.filter((r) => {
    if (activeTab.value === '自由市场') return r.floor !== '--'
    if (activeTab.value === '我的关注') return r.fav
    return true
  })

  const t = activeTag.value
  if (t === '小试牛刀') arr = arr.filter((r) => r.issued <= 8000)
  else if (t === '初露锋芒') arr = arr.filter((r) => r.floor !== '--')
  else if (t === '大显身手') arr = arr.filter((r) => r.circ >= 8000)
  else if (t === '一鸣惊人') arr = arr.filter((r) => r.vol >= 10)

  return arr.slice().sort((a, b) =>
    activeSort.value === '全部份数'
      ? a.issued - b.issued
      : (parseFloat(a.floor) || 1e9) - (parseFloat(b.floor) || 1e9)
  )
})

/** 叠加搜索关键词 */
const searched = computed(() => {
  const q = kw.value.trim()
  return q ? shown.value.filter((r) => r.name.includes(q)) : shown.value
})

function goDetail(r) {
  router.push('/pages/market/details?id=' + encodeURIComponent(r.id))
}

function doSearch() {
  if (!kw.value.trim()) return toast('请输入藏品名称')
  const n = searched.value.length
  toast(n ? '找到 ' + n + ' 件藏品' : '没有匹配的藏品')
}
</script>

<template>
  <uni-view data-v-603934c6="" class="market-page"><uni-view data-v-603934c6="" class="page-bg"><uni-image data-v-603934c6="" class="page-bg-img" style="height: 812px;"><div style="background-image: url(&quot;/static/images/index/icon/bg.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/images/index/icon/bg.png" draggable="false"></uni-image></uni-view><uni-view data-v-603934c6="" class="hero-watermark-wrap" style="top: 44px;"><uni-image data-v-603934c6="" class="hero-watermark"><div style="background-image: url(&quot;/static/images/login/2.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/images/login/2.png" draggable="false"></uni-image></uni-view><uni-view data-v-603934c6="" class="safe-top-probe"></uni-view><uni-view data-v-603934c6="" class="market-sticky-header" style="padding-top: 22px;"><uni-view data-v-603934c6="" class="header-content"><uni-view data-v-603934c6="" class="search-bar"><uni-view data-v-603934c6="" class="search-left"><uni-text data-v-603934c6="" class="cuIcon-search search-icon"><span></span></uni-text><uni-input class="search-input" data-v-603934c6="" :value="kw" @input="kw = $event.target.value"><div class="uni-input-wrapper"><div class="uni-input-placeholder search-placeholder" data-v-603934c6="">ICard</div><input maxlength="140" step="" enterkeyhint="done" autocomplete="off" inputmode="text" type="text" class="uni-input-input"></div></uni-input></uni-view><uni-view class="search-btn" data-v-603934c6="" @click="doSearch">搜索</uni-view></uni-view></uni-view><uni-view data-v-603934c6="" class="category-tabs margin-bottom-sm"><uni-view data-v-603934c6="" class="category-tab" :class="{active: activeTab==='活动市场'}" @click="activeTab='活动市场'"><uni-text data-v-603934c6="" class="tab-text"><span>活动市场</span></uni-text><uni-view data-v-603934c6="" class="tab-line" :class="{active: activeTab==='活动市场'}"></uni-view></uni-view><uni-view data-v-603934c6="" class="category-tab" :class="{active: activeTab==='自由市场'}" @click="activeTab='自由市场'"><uni-text data-v-603934c6="" class="tab-text"><span>自由市场</span></uni-text><uni-view data-v-603934c6="" class="tab-line" :class="{active: activeTab==='自由市场'}"></uni-view></uni-view><uni-view data-v-603934c6="" class="category-tab" :class="{active: activeTab==='我的关注'}" @click="activeTab='我的关注'"><uni-text data-v-603934c6="" class="tab-text"><span>我的关注</span></uni-text><uni-view data-v-603934c6="" class="tab-line" :class="{active: activeTab==='我的关注'}"></uni-view></uni-view></uni-view><uni-scroll-view data-v-603934c6="" class="sub-tags-scroll"><div class="uni-scroll-view"><div class="uni-scroll-view" style="overflow: auto hidden;"><div class="uni-scroll-view-content"><uni-view data-v-603934c6="" class="sub-tags"><uni-view data-v-603934c6="" class="sub-tag"><uni-text data-v-603934c6="" class="recommend-badge"><span>推荐</span></uni-text><uni-view data-v-603934c6="" class="sub-tag-chip" :class="{active: activeTag==='小试牛刀'}" @click="activeTag='小试牛刀'"><uni-text data-v-603934c6="" class="sub-tag-text"><span>小试牛刀</span></uni-text></uni-view></uni-view><uni-view data-v-603934c6="" class="sub-tag"><uni-text data-v-603934c6="" class="recommend-badge"><span>推荐</span></uni-text><uni-view data-v-603934c6="" class="sub-tag-chip" :class="{active: activeTag==='初露锋芒'}" @click="activeTag='初露锋芒'"><uni-text data-v-603934c6="" class="sub-tag-text"><span>初露锋芒</span></uni-text></uni-view></uni-view><uni-view data-v-603934c6="" class="sub-tag"><uni-text data-v-603934c6="" class="recommend-badge"><span>推荐</span></uni-text><uni-view data-v-603934c6="" class="sub-tag-chip" :class="{active: activeTag==='大显身手'}" @click="activeTag='大显身手'"><uni-text data-v-603934c6="" class="sub-tag-text"><span>大显身手</span></uni-text></uni-view></uni-view><uni-view data-v-603934c6="" class="sub-tag"><uni-text data-v-603934c6="" class="recommend-badge"><span>推荐</span></uni-text><uni-view data-v-603934c6="" class="sub-tag-chip" :class="{active: activeTag==='一鸣惊人'}" @click="activeTag='一鸣惊人'"><uni-text data-v-603934c6="" class="sub-tag-text"><span>一鸣惊人</span></uni-text></uni-view></uni-view></uni-view></div></div></div></uni-scroll-view><uni-view data-v-603934c6="" class="filter-row"><uni-view data-v-603934c6="" class="filter-row-main"><uni-view data-v-17a66432="" data-v-603934c6="" class="da-dropdown-wrap"><uni-view data-v-17a66432="" class="da-dropdown" style="--dropdown-theme-color: #DC3335; --dropdown-text-color: #666666; --dropdown-background-color: transparent; --dropdown-popup-duration: 0.3s; --dropdown-fixed-top: 0px;"><uni-view data-v-17a66432="" class="da-dropdown-menu"><uni-view data-v-17a66432="" class="da-dropdown-menu-item" @click="activeSort='全部份数'"><uni-text data-v-17a66432="" class="da-dropdown-menu-item--text"><span>全部份数</span></uni-text><uni-view data-v-17a66432="" class="da-dropdown-menu-item--icon"><uni-text data-v-17a66432="" class="is--arrdown"><span></span></uni-text></uni-view></uni-view><uni-view data-v-17a66432="" class="da-dropdown-menu-item" @click="activeSort='全部价格'"><uni-text data-v-17a66432="" class="da-dropdown-menu-item--text"><span>全部价格</span></uni-text><uni-view data-v-17a66432="" class="da-dropdown-menu-item--icon"><uni-text data-v-17a66432="" class="is--arrdown"><span></span></uni-text></uni-view></uni-view></uni-view><uni-view data-v-17a66432="" class="da-dropdown-content"><uni-view data-v-17a66432="" class="da-dropdown-content-popup"></uni-view></uni-view></uni-view></uni-view></uni-view><uni-view data-v-603934c6="" class="view-mode-toggle" @click="toggleViewMode"><uni-image data-v-603934c6="" class="view-mode-icon"><div style="background-image: url(&quot;/static/images/market/1.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/images/market/1.png" draggable="false"></uni-image></uni-view></uni-view><uni-view data-v-603934c6="" class="market-table-head" v-if="viewMode==='list'" style="padding: 0px 16px;"><uni-view data-v-603934c6="" class="col-name">藏品名称 | 发行流通</uni-view><uni-view data-v-603934c6="" class="col-floor sort-col active"><uni-text data-v-603934c6=""><span>地板价</span></uni-text><uni-view data-v-603934c6="" class="sort-arrows"><uni-view data-v-603934c6="" class="sort-arrow up"></uni-view><uni-view data-v-603934c6="" class="sort-arrow down on"></uni-view></uni-view></uni-view><uni-view data-v-603934c6="" class="col-volume sort-col"><uni-text data-v-603934c6=""><span>成交量</span></uni-text><uni-view data-v-603934c6="" class="sort-arrows"><uni-view data-v-603934c6="" class="sort-arrow up"></uni-view><uni-view data-v-603934c6="" class="sort-arrow down"></uni-view></uni-view></uni-view></uni-view></uni-view><uni-scroll-view data-v-603934c6="" class="market-scroll-body"><div class="uni-scroll-view"><div class="uni-scroll-view" style="overflow: hidden auto;"><div class="uni-scroll-view-content"><div class="uni-scroll-view-refresher" style="background-color: transparent; height: 0px;"><uni-view data-v-a0f2fc02="" data-v-603934c6="" class="refresher-slot" style="height: 54px; min-height: 54px;"><uni-image data-v-a0f2fc02="" class="refresher-slot__icon" style="width: 36px; height: 36px;"><div style="background-image: url(&quot;/static/icard.gif&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/icard.gif" draggable="false"></uni-image></uni-view></div><uni-view data-v-603934c6="" class="market-list-wrap"><uni-view v-if="viewMode==='list'" data-v-603934c6=""><uni-view v-for="(r, i) in searched" :key="r.id" class="market-table-row" :data-id="r.id" data-v-603934c6="" @click="goDetail(r)"><uni-view data-v-603934c6="" class="col-name"><uni-image data-v-603934c6="" class="market-list-thumb"><div :style="{backgroundImage:'url(' + r.img + ')', backgroundPosition:'center center', backgroundSize:'cover', backgroundRepeat:'no-repeat'}"></div><img :src="r.img" draggable="false"></uni-image><uni-view data-v-603934c6="" class="market-list-info"><uni-view data-v-603934c6="" class="market-list-title">{{ r.name }}</uni-view><uni-view data-v-603934c6="" class="market-list-meta"> 发行 {{ r.issued }} 流通 {{ r.circ }} </uni-view></uni-view><uni-view data-v-603934c6="" class="market-list-fav"><uni-text data-v-603934c6="" class="cuIcon-favor"><span></span></uni-text></uni-view></uni-view><uni-view data-v-603934c6="" class="col-floor">{{ r.floor }}</uni-view><uni-view data-v-603934c6="" class="col-volume">{{ r.vol }}</uni-view></uni-view><uni-view data-v-603934c6="" style="height: 60px;"></uni-view></uni-view><uni-view v-else data-v-603934c6=""><uni-view class="grid-wrap" data-v-603934c6="" style="padding:4px 0 8px"><uni-view v-for="r in searched" :key="r.id" class="grid-card" :data-id="r.id" data-v-603934c6="" @click="goDetail(r)"><uni-view class="grid-card-cover" data-v-603934c6=""><uni-image class="grid-card-img" data-v-603934c6=""><div :style="{backgroundImage:'url(' + r.img + ')', backgroundPosition:'center center', backgroundSize:'cover', backgroundRepeat:'no-repeat'}"></div><img :src="r.img" draggable="false"></uni-image><uni-view class="grid-card-fav" data-v-603934c6=""><uni-text class="cuIcon-favor" data-v-603934c6=""><span></span></uni-text></uni-view></uni-view><uni-view class="grid-card-body" data-v-603934c6=""><uni-view class="grid-card-title-row" data-v-603934c6=""><uni-view class="grid-card-title" data-v-603934c6="">{{ r.name }}</uni-view><uni-view v-if="r.floor==='--'" class="grid-card-badge" data-v-603934c6="">退市</uni-view></uni-view><uni-view class="grid-card-tags" data-v-603934c6=""><uni-view class="grid-card-tag" data-v-603934c6="">限量 {{ r.issued }}</uni-view><uni-view class="grid-card-tag" data-v-603934c6="">流通 {{ r.circ }}</uni-view></uni-view><uni-view class="grid-card-price" data-v-603934c6=""><uni-text class="price-symbol" data-v-603934c6="">¥</uni-text><uni-text class="price-num" data-v-603934c6="">{{ r.floor }}</uni-text></uni-view></uni-view></uni-view></uni-view><uni-view data-v-603934c6="" style="height: 60px;"></uni-view></uni-view></uni-view></div></div></div></uni-scroll-view></uni-view>
</template>
