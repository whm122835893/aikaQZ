<template>
  <uni-view data-v-30aa5904="" class="detail-page"><uni-view data-v-30aa5904="" class="page-header" style="padding-top: 12px;"><uni-view data-v-30aa5904="" class="header-back is-hero"><uni-text data-v-30aa5904="" class="cuIcon-back"><span></span></uni-text></uni-view><uni-view data-v-30aa5904="" class="header-title"></uni-view><uni-view class="header-fav is-hero" data-v-30aa5904="" @click="toggleFav"><uni-text class="cuIcon-favorfill" data-v-30aa5904="" :style="{color: faved ? '#dc3335' : '#fff'}"><span></span></uni-text></uni-view></uni-view><uni-view data-v-30aa5904="" class="hero-section" style="padding-top: 88px;"><uni-view class="hero-cover-bg" data-v-30aa5904=""><div :style="bgImg(g.img)"></div></uni-view><uni-view data-v-30aa5904="" class="hero-cover-mask"></uni-view><uni-view data-v-30aa5904="" class="hero-content"><uni-view data-v-30aa5904="" class="hero-cover-wrap"><uni-image data-v-30aa5904="" class="hero-cover"><div :style="bgImg(g.img)"></div><img :src="g.img" draggable="false"></uni-image></uni-view><uni-view class="hero-title" data-v-30aa5904="">{{ g.name }}</uni-view><uni-view data-v-30aa5904="" class="hero-stats"><uni-view data-v-30aa5904="" class="stat-tag"><uni-text data-v-30aa5904="" class="stat-tag-label"><span>发行</span></uni-text><uni-text class="stat-tag-value" data-v-30aa5904=""><span>{{ g.issued }}份</span></uni-text></uni-view><uni-view data-v-30aa5904="" class="stat-tag"><uni-text data-v-30aa5904="" class="stat-tag-label"><span>流通</span></uni-text><uni-text class="stat-tag-value" data-v-30aa5904=""><span>{{ g.circ }}份</span></uni-text></uni-view></uni-view></uni-view></uni-view><uni-view data-v-30aa5904="" class="page-body"><uni-view data-v-30aa5904="" class="panel-card"><uni-view id="tabs-anchor" class="main-tabs" data-v-30aa5904=""><uni-view class="main-tab" data-v-30aa5904="" :class="{active: mainTab === 'list'}" @click="mainTab = 'list'"><uni-text data-v-30aa5904=""><span>挂单列表</span></uni-text><uni-view class="tab-line" data-v-30aa5904="" :class="{active: mainTab === 'list'}"></uni-view></uni-view><uni-view class="main-tab" data-v-30aa5904="" :class="{active: mainTab === 'notice'}" @click="mainTab = 'notice'"><uni-text data-v-30aa5904=""><span>相关公告</span></uni-text></uni-view></uni-view><uni-view data-v-30aa5904=""><uni-view data-v-30aa5904="" class="sub-tabs"><uni-view class="sub-tab-item" data-v-30aa5904="" :class="{active: subTab === 'sell'}" @click="subTab = 'sell'">寄售</uni-view><uni-view class="sub-tab-item" data-v-30aa5904="" :class="{active: subTab === 'bid'}" @click="subTab = 'bid'">求购</uni-view><uni-view class="sub-tab-item" data-v-30aa5904="" :class="{active: subTab === 'entrust'}" @click="subTab = 'entrust'">委托<uni-text class="sub-tab-lock" data-v-30aa5904="">🔒</uni-text></uni-view></uni-view><uni-view data-v-30aa5904="" class="list-section"><uni-view data-v-30aa5904="" class="list-header"><uni-view data-v-30aa5904="" class="list-header-left">藏品名称 | 编号</uni-view><uni-view data-v-30aa5904="" class="list-item-cols"><uni-view data-v-30aa5904="" class="list-header-sort list-col-price active"><uni-text data-v-30aa5904=""><span>价格</span></uni-text><uni-view data-v-30aa5904="" class="sort-arrows"><uni-view data-v-30aa5904="" class="sort-arrow up on"></uni-view><uni-view data-v-30aa5904="" class="sort-arrow down"></uni-view></uni-view></uni-view><uni-view data-v-30aa5904="" class="list-header-sort list-col-no"><uni-text data-v-30aa5904=""><span>编号</span></uni-text><uni-view data-v-30aa5904="" class="sort-arrows"><uni-view data-v-30aa5904="" class="sort-arrow up"></uni-view><uni-view data-v-30aa5904="" class="sort-arrow down"></uni-view></uni-view></uni-view></uni-view></uni-view><uni-view data-v-30aa5904=""><uni-view data-v-4d930ea0="" data-v-30aa5904="" class="list-content"><uni-view v-if="mainTab === 'list'"><uni-view v-for="(row, i) in listRows" :key="i" class="sale-list-item" data-v-30aa5904="" @click="quickBuy(row)"><uni-view class="sale-item-main" data-v-30aa5904=""><uni-view class="sale-item-left" data-v-30aa5904=""><uni-view class="sale-item-title" data-v-30aa5904="">{{ g.name }}</uni-view><uni-view class="sale-item-no" data-v-30aa5904="">#{{ row.no }}</uni-view></uni-view><uni-view class="sale-item-right" data-v-30aa5904=""><uni-view class="sale-item-price" data-v-30aa5904=""><uni-text class="sale-price-symbol" data-v-30aa5904="">¥</uni-text><uni-text class="sale-price-num" data-v-30aa5904="">{{ row.price }}</uni-text></uni-view><uni-view class="sale-item-wallet" data-v-30aa5904=""><uni-text class="sale-wallet-label" data-v-30aa5904="">支付钱包</uni-text><uni-text class="sale-wallet-tag" data-v-30aa5904="">A</uni-text></uni-view></uni-view></uni-view><uni-text class="sale-item-arrow" data-v-30aa5904="">›</uni-text></uni-view><uni-view v-if="!listRows.length" class="text-center text-grey margin-top-xl">暂无数据</uni-view></uni-view><uni-view v-else><uni-view v-for="(n, i) in notices" :key="i" class="relative-notice-item" @click="goNotice"><uni-text class="notice-item-title">{{ n.title }}</uni-text><uni-text class="notice-item-meta">{{ n.tag }} · {{ n.time }}</uni-text></uni-view></uni-view></uni-view></uni-view></uni-view></uni-view></uni-view><uni-view data-v-30aa5904="" class="bottom-spacer"></uni-view></uni-view><uni-view data-v-30aa5904="" class="bottom-bar"><uni-view class="bottom-btn outline flex-sub" data-v-30aa5904="" @click="openSheet('batch')">批量购买</uni-view><uni-view class="bottom-btn primary flex-sub" data-v-30aa5904="" @click="openSheet('buy')">快捷购买</uni-view></uni-view><uni-view class="cu-modal bottom-modal begbuy-modal" :class="{show: sheet === 'bid'}" @click.self="closeSheet"><uni-view class="cu-dialog bid-sheet"><uni-view class="bottom-sheet-header"><uni-view class="bottom-sheet-title">发起求购</uni-view><uni-view class="bottom-sheet-close" @click="closeSheet"><uni-text class="cuIcon-close"><span></span></uni-text></uni-view></uni-view><uni-view class="bottom-sheet-body"><uni-view data-v-30aa5904="" class="cell"><uni-text class="cell-label">求购数量</uni-text><uni-text class="cell-value">{{ qty }}</uni-text></uni-view><uni-view data-v-30aa5904="" class="cell"><uni-text class="cell-label">限价（¥）</uni-text><uni-text class="cell-value">{{ limitPrice }}</uni-text></uni-view><uni-view data-v-30aa5904="" class="cell"><uni-text class="cell-label">合计</uni-text><uni-text class="cell-value">¥{{ total }}</uni-text></uni-view><uni-view class="sheet-actions"><uni-view class="bottom-btn flex-sub" @click="closeSheet">取消</uni-view><uni-view class="bottom-btn primary flex-sub" @click="submitBid">确认求购</uni-view></uni-view></uni-view></uni-view></uni-view><uni-view class="cu-modal bottom-modal entrust-modal" :class="{show: sheet === 'entrust'}" @click.self="closeSheet"><uni-view class="cu-dialog entrust-sheet"><uni-view class="bottom-sheet-header"><uni-view class="bottom-sheet-title">发起委托</uni-view><uni-view class="bottom-sheet-close" @click="closeSheet"><uni-text class="cuIcon-close"><span></span></uni-text></uni-view></uni-view><uni-view class="bottom-sheet-body"><uni-view data-v-30aa5904="" class="cell"><uni-text class="cell-label">委托价格（¥）</uni-text><uni-text class="cell-value">{{ limitPrice }}</uni-text></uni-view><uni-view data-v-30aa5904="" class="cell"><uni-text class="cell-label">服务费</uni-text><uni-text class="cell-value">2%</uni-text></uni-view><uni-view data-v-30aa5904="" class="cell"><uni-text class="cell-label">预计到账</uni-text><uni-text class="cell-value">¥{{ netIn }}</uni-text></uni-view><uni-view class="sheet-actions"><uni-view class="bottom-btn flex-sub" @click="closeSheet">取消</uni-view><uni-view class="bottom-btn primary flex-sub" @click="submitEntrust">确认寄售</uni-view></uni-view></uni-view></uni-view></uni-view><uni-view data-v-30aa5904="" class="cu-modal bottom-modal"><uni-view data-v-30aa5904="" class="cu-dialog bg-white padding"><uni-view data-v-30aa5904=""> 批量购买 </uni-view><uni-view data-v-30aa5904="" class="flex align-center justify-between margin-top-xl"><uni-view data-v-30aa5904=""> 限价 </uni-view><uni-view data-v-30aa5904="" class="flex align-center"> 最高 <uni-input data-v-30aa5904="" class="text-center radius bg-gray margin-lr-sm" style="width: 100px;"><div class="uni-input-wrapper"><div class="uni-input-placeholder text-df" data-v-30aa5904="">限价</div><input maxlength="140" step="" enterkeyhint="done" autocomplete="off" inputmode="text" type="text" class="uni-input-input"></div></uni-input> 元 </uni-view></uni-view><uni-view data-v-30aa5904="" class="flex align-center justify-between margin-top"><uni-view data-v-30aa5904=""> 下单数量 </uni-view><uni-view data-v-30aa5904="" class="flex align-center"><uni-view data-v-30aa5904="" class="radius flex btn-action-yellow align-center justify-center" style="width: 25px; height: 25px;"><uni-text data-v-30aa5904="" class="cuIcon-move"><span></span></uni-text></uni-view><uni-view data-v-30aa5904=""><uni-input data-v-30aa5904="" class="text-center bg-gray radius margin-lr-sm" style="width: 100px; height: 25px;"><div class="uni-input-wrapper"><div class="uni-input-placeholder input-placeholder" data-v-30aa5904="" style="display: none;"></div><input maxlength="140" step="" enterkeyhint="done" autocomplete="off" inputmode="text" type="text" class="uni-input-input"></div></uni-input></uni-view><uni-view data-v-30aa5904="" class="radius flex btn-action-yellow align-center justify-center" style="width: 25px; height: 25px;"><uni-text data-v-30aa5904="" class="cuIcon-add"><span></span></uni-text></uni-view></uni-view></uni-view><uni-view data-v-30aa5904="" style="height: 50px;"></uni-view><uni-view data-v-30aa5904="" class="margin-top-xl flex align-center justify-center"><uni-view data-v-30aa5904="" class="cu-btn flex-sub lg btn-action-yellow round"> 批量下单 </uni-view></uni-view></uni-view></uni-view></uni-view>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getGoods, MAKING_LIST, BID_LIST, RELATED_NOTICES } from '@/mock/goods'
import { toast, isLogin } from '@/utils/interact'

const route = useRoute()
const router = useRouter()

const g = computed(() => getGoods(route.query.id))
const mainTab = ref('list')
const subTab = ref('sell')
const sheet = ref('')
const qty = ref(1)
const limitPrice = ref(10)
const faved = ref(false)

// 切换藏品时重置表单状态
watch(() => route.query.id, () => {
  mainTab.value = 'list'
  subTab.value = 'sell'
  sheet.value = ''
  qty.value = 1
  limitPrice.value = Number(g.value.floor) || 10
  faved.value = !!g.value.fav
}, { immediate: true })

const notices = RELATED_NOTICES
const total = computed(() => (qty.value * limitPrice.value).toFixed(2))
const netIn = computed(() => (limitPrice.value * 0.98).toFixed(2))

const listRows = computed(() => {
  if (subTab.value === 'bid') return BID_LIST(g.value)
  if (subTab.value === 'entrust') return MAKING_LIST(g.value).slice(0, 5)
  return MAKING_LIST(g.value)
})

/** 生成 background-image 样式，避免在模板里拼引号 */
function bgImg(url) {
  return {
    backgroundImage: 'url(' + url + ')',
    backgroundPosition: 'center center',
    backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat',
    width: '100%',
    height: '100%'
  }
}

function onTop(label) {
  if (label === '寄售') {
    /* 把当前藏品信息带过去，否则寄售表单页拿不到名称 / 图片 / 买入价 */
    try {
      sessionStorage.setItem('icard_sale_goods', JSON.stringify({
        id: g.value.id, name: g.value.name, series: g.value.series, image: g.value.img,
        token: 1000 + (Number(String(g.value.id).replace(/\D/g, '')) || 1) * 37 % 9000,
        buyPrice: Number(g.value.floor || 0).toFixed(2)
      }))
    } catch (e) { /* 隐私模式下忽略 */ }
    router.push('/pages/market/sale')
  } else if (label === '求购') openSheet('bid')
  else openSheet('entrust')
}

function openSheet(k) {
  if (!isLogin()) return toast('请先登录')
  if (k === 'batch') {
    router.push('/pages/market/batchBuy?id=' + encodeURIComponent(g.value.id))
    return
  }
  if (k === 'buy') {
    router.push('/pages/market/createOrder?id=' + encodeURIComponent(g.value.id))
    return
  }
  sheet.value = k
}

function closeSheet() {
  sheet.value = ''
}

function quickBuy(row) {
  if (!isLogin()) return toast('请先登录')
  toast('已购买 #' + row.no + '，价格 ¥' + row.price)
}

function toggleFav() {
  faved.value = !faved.value
  toast(faved.value ? '已收藏' : '已取消收藏')
}

function submitBid() {
  if (qty.value < 1) return toast('求购数量至少 1 份')
  closeSheet()
  toast('求购单已提交，可在「我的-求购」查看')
}

function submitEntrust() {
  closeSheet()
  toast('寄售单已提交，可在「我的-委托」查看')
}

function goNotice() {
  router.push('/pages/notification/details')
}
</script>
