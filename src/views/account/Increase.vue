<template>
  <uni-view data-v-37c82324="" class="padding container">
    <uni-view data-v-37c82324="" class="bg-white radius padding-lr-sm padding-tb flex align-center">
      <uni-view data-v-37c82324="" class="margin-right">
        <uni-image data-v-37c82324="" class="radius" style="width: 80px; height: 80px;" :style="bgImg(g.img)">
          <div :style="bgImg(g.img)"></div>
        </uni-image>
      </uni-view>
      <uni-view data-v-37c82324="" class="flex-sub">
        <uni-view data-v-37c82324="" class="text-bold text-lg text-black margin-bottom"> {{ g.name }} </uni-view>
        <uni-view data-v-37c82324="" class="text-sm text-grey">
          编号：# <uni-text data-v-37c82324="" class="text-bold text-lg text-black"><span>{{ g.id }}</span></uni-text> / {{ g.circ }}份流通
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view data-v-37c82324="" class="margin-top-xl text-lg text-grey">转售价格</uni-view>
    <uni-view data-v-37c82324="" class="margin-top radius padding bg-gray">
      <uni-input data-v-37c82324="" class="text-df">
        <div class="uni-input-wrapper">
          <div class="uni-input-placeholder text-grey text-sm">输入转售价格</div>
          <input maxlength="140" class="uni-input-input" :value="price" @input="onPrice($event.target.value)" />
        </div>
      </uni-input>
    </uni-view>

    <uni-view data-v-37c82324="" class="margin-top-xl text-lg text-grey">选择用户</uni-view>
    <uni-view data-v-37c82324="" class="margin-top radius padding bg-gray flex align-center">
      <uni-view data-v-37c82324="" class="text-xl margin-right-sm">
        <uni-text data-v-37c82324="" class="cuIcon-search"><span></span></uni-text>
      </uni-view>
      <uni-input data-v-37c82324="" class="text-df flex-sub">
        <div class="uni-input-wrapper">
          <div class="uni-input-placeholder text-grey text-sm">输入用户钱包地址</div>
          <input maxlength="140" class="uni-input-input" :value="addr" @input="onAddr($event.target.value)" />
        </div>
      </uni-input>
    </uni-view>

    <uni-view data-v-37c82324="" v-if="result" class="margin-top radius padding bg-white">
      <uni-view data-v-37c82324="" class="text-sm text-grey">查询结果</uni-view>
      <uni-view data-v-37c82324="" class="margin-top-sm text-black">持有人：{{ addr || '未填写' }}</uni-view>
      <uni-view data-v-37c82324="" class="margin-top-xs text-orange">当前报价 ￥{{ price || '0.00' }}</uni-view>
      <uni-view data-v-37c82324="" class="margin-top-xs text-sm text-grey">服务费(5%) ￥{{ fee }}，实际到账 ￥{{ net }}</uni-view>
    </uni-view>

    <uni-view data-v-37c82324="" class="bottom_nav padding-xl flex align-center justify-center">
      <uni-view data-v-37c82324="" class="round bg-green text-black flex align-center justify-center compose-item-gray" @click="query"> 查询 </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRoute } from 'vue-router'
import { getGoods } from '@/mock/goods'
import { toast } from '@/utils/interact'

const route = useRoute()
const g = getGoods(route.query.id)

const price = ref('')
const addr = ref('')
const result = ref(false)

const fee = computed(() => (Number(price.value || 0) * 0.05).toFixed(2))
const net = computed(() => (Number(price.value || 0) * 0.95).toFixed(2))

function bgImg(url) {
  if (!url) return {}
  return { backgroundImage: 'url(' + url + ')', backgroundPosition: 'center center', backgroundSize: 'cover', backgroundRepeat: 'no-repeat' }
}

function onPrice(v) {
  price.value = String(v).replace(/[^\d.]/g, '').slice(0, 10)
  result.value = false
}

function onAddr(v) {
  addr.value = String(v).slice(0, 64)
  result.value = false
}

function query() {
  if (!addr.value.trim()) return toast('请输入用户钱包地址')
  if (!(Number(price.value) > 0)) return toast('请输入转售价格')
  result.value = true
  toast('查询成功，已生成报价')
}
</script>
