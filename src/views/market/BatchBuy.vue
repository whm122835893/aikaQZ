<template>
  <uni-view data-v-38c6881c="" class="batch-page"><uni-view data-v-38c6881c="" class="hero-watermark-wrap" style="top: 12px;"><uni-image data-v-38c6881c="" class="hero-watermark"><div style="background-image: url(&quot;/static/images/login/2.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/images/login/2.png" draggable="false"></uni-image></uni-view><uni-view data-v-38c6881c="" class="header" style="padding-top: 24px;"><uni-view data-v-38c6881c="" class="back-btn" @click="goBack"><uni-text data-v-38c6881c="" class="cuIcon-back"><span></span></uni-text></uni-view><uni-view data-v-38c6881c="" class="page-title">批量购买</uni-view><uni-view data-v-38c6881c="" class="header-placeholder"></uni-view></uni-view><uni-view data-v-38c6881c="" class="content-wrap"><uni-view data-v-38c6881c="" class="form-card product-card"><uni-view data-v-38c6881c="" class="product-row"><uni-image data-v-38c6881c="" class="product-img"><div :style="bgImg(g.img)"></div><img :src="g.img" draggable="false"></uni-image><uni-view data-v-38c6881c="" class="product-info"><uni-view data-v-38c6881c="" class="product-title-row"><uni-view data-v-38c6881c="" class="product-title">{{ g.name }}</uni-view></uni-view><uni-view data-v-38c6881c="" class="floor-row"><uni-text data-v-38c6881c="" class="floor-label"><span>地板价</span></uni-text><uni-text data-v-38c6881c="" class="floor-price"><span>¥ {{ floorText }}</span></uni-text></uni-view></uni-view></uni-view></uni-view><uni-view data-v-38c6881c="" class="form-card"><uni-view data-v-38c6881c="" class="card-label">购买单价</uni-view><uni-view data-v-38c6881c="" class="card-hint">请输入可接受的最高单价（元）</uni-view><uni-view data-v-38c6881c="" class="price-input-row"><uni-text data-v-38c6881c="" class="price-symbol"><span>¥</span></uni-text><uni-input data-v-38c6881c="" class="field-input price-input" type="digit" :value="price" @input="price = $event.target.value" placeholder="1-99999"><div class="uni-input-wrapper"><div class="uni-input-placeholder field-placeholder" data-v-38c6881c="">1-99999</div><input maxlength="140" step="0.000000000000000001" enterkeyhint="done" autocomplete="off" inputmode="decimal" type="number" class="uni-input-input"></div></uni-input></uni-view></uni-view><uni-view data-v-38c6881c="" class="form-card"><uni-view data-v-38c6881c="" class="card-label">购买数量</uni-view><uni-view data-v-38c6881c="" class="card-hint"> 最大批量购买数量 {{ maxQty }} </uni-view><uni-input data-v-38c6881c="" class="field-input" type="number" :value="qty" @input="qty = $event.target.value" :placeholder="'小于等于' + maxQty"><div class="uni-input-wrapper"><div class="uni-input-placeholder field-placeholder" data-v-38c6881c="">小于等于{{ maxQty }}</div><input maxlength="140" step="0.000000000000000001" enterkeyhint="done" pattern="[0-9]*" autocomplete="off" inputmode="numeric" type="number" class="uni-input-input"></div></uni-input></uni-view><uni-view data-v-38c6881c="" class="form-card freeze-card"><uni-view data-v-38c6881c="" class="freeze-row"><uni-text data-v-38c6881c="" class="card-label freeze-label"><span>预计金额</span></uni-text><uni-text data-v-38c6881c="" class="freeze-amount"><span>¥ {{ total }}</span></uni-text></uni-view><uni-view data-v-38c6881c="" class="freeze-tip"> 若购买成功，金额将扣除，如未支付，不会扣除对应金额。 </uni-view></uni-view></uni-view><uni-view data-v-38c6881c="" class="bottom-bar"><uni-view data-v-38c6881c="" class="bottom-left"><uni-view data-v-38c6881c="" class="bottom-price">¥ {{ total }}</uni-view><uni-view data-v-38c6881c="" class="bottom-label">最高支付总额</uni-view></uni-view><uni-view data-v-38c6881c="" class="buy-btn" @click="submitBuy">立即购买</uni-view></uni-view></uni-view>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getGoods } from '@/mock/goods'
import { toast, isLogin } from '@/utils/interact'

const route = useRoute()
const router = useRouter()

const g = computed(() => getGoods(route.query.id))
const floorText = computed(() => (g.value.floor == null ? '--' : Number(g.value.floor).toFixed(2)))
const maxQty = computed(() => Math.min(g.value.listed || 50, 50))

const price = ref('')
const qty = ref('1')

const total = computed(() => {
  const p = parseFloat(price.value) || 0
  const q = parseInt(qty.value) || 0
  return (p * q).toFixed(2)
})

function bgImg(url) {
  return {
    backgroundImage: 'url(' + url + ')',
    backgroundPosition: 'center center',
    backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat'
  }
}

function goBack() {
  router.back()
}

function submitBuy() {
  if (!isLogin()) return toast('请先登录')
  const p = parseFloat(price.value)
  const q = parseInt(qty.value)
  if (!p || p <= 0) return toast('请输入购买单价')
  if (!q || q <= 0) return toast('请输入购买数量')
  if (q > maxQty.value) return toast('购买数量不能超过 ' + maxQty.value)
  toast('已提交批量购买，共 ' + q + ' 份，单价 ¥' + p.toFixed(2))
}
</script>
