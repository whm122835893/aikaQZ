<template>
  <uni-view data-v-8b2c1436 class="padding container">
    <uni-view data-v-8b2c1436 class="bg-white radius padding-sm">
      <uni-view data-v-8b2c1436 class="padding-sm radius bg-gray text-center">
        <uni-view data-v-8b2c1436 style="font-size: 40px;">
          <uni-text data-v-8b2c1436 class="cuIcon-roundcheckfill text-green"><span></span></uni-text>
        </uni-view>
        <uni-view data-v-8b2c1436 class="text-lg text-bold" style="position: relative; z-index: 2;">寄售成功</uni-view>
        <uni-view data-v-8b2c1436 class="margin-top-sm text-sm text-gray">返回我的藏品</uni-view>
        <uni-view data-v-8b2c1436 class="flex align-center justify-center">
          <uni-view
            data-v-8b2c1436
            class="cu-btn radius bg-consign margin-top-xl"
            style="width: 200px;"
            @click="toWarelist"
          >
            我的藏品
          </uni-view>
        </uni-view>
      </uni-view>

      <uni-view data-v-8b2c1436 class="bg-white padding-sm radius flex align-center">
        <uni-image data-v-8b2c1436 class="radius margin-right" style="width: 80px; height: 81px;">
          <div :style="`background-image: url(&quot;${goods.image}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div>
          <img :src="goods.image" alt="" draggable="false" />
        </uni-image>
        <uni-view data-v-8b2c1436 class="flex-sub">
          <uni-view data-v-8b2c1436 class="text-bold">{{ goods.name }}</uni-view>
          <uni-view data-v-8b2c1436 class="margin-top-xs">#{{ goods.token }} · x{{ goods.qty }}</uni-view>
          <uni-view data-v-8b2c1436 class="text-right text-xl text-bold">￥{{ goods.price }}</uni-view>
        </uni-view>
      </uni-view>

      <uni-view data-v-8b2c1436 class="sell-result-tip">
        寄售订单已提交，成交后款项将打款至钱包余额，可在「售出记录」中查看进度。
      </uni-view>

      <uni-view data-v-8b2c1436 class="flex align-center justify-center sell-result-footer">
        <uni-view data-v-8b2c1436 class="cu-btn radius bg-gray margin-right" @click="toSaleList">查看售出记录</uni-view>
        <uni-view data-v-8b2c1436 class="cu-btn radius bg-consign" @click="toWarelist">继续寄售</uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
/**
 * 寄售成功结果页
 * 源站为纯静态空壳：金额 / 编号 / 图片全为空（￥ 与 # 后面无内容），
 * 且「我的藏品」按钮没有任何跳转 —— 点上去完全没反应。
 * 克隆版：从 sessionStorage 读取上一页提交的寄售信息，并补齐两个按钮跳转。
 */
import { onMounted, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { GOODS } from '@/mock/goods'

const router = useRouter()

/** 默认取第一件藏品兜底，避免直接打开本页时出现空白 */
const goods = reactive({
  name: GOODS[0]?.name || '国潮之光',
  image: GOODS[0]?.img || '',
  token: 1103,
  qty: 1,
  price: Number(GOODS[0]?.floor || 188).toFixed(2)
})

onMounted(() => {
  try {
    const raw = sessionStorage.getItem('icard_sale_result')
    if (raw) {
      const d = JSON.parse(raw)
      if (d.name) goods.name = d.name
      if (d.image) goods.image = d.image
      if (d.token) goods.token = d.token
      if (d.qty) goods.qty = d.qty
      if (d.price) goods.price = Number(d.price).toFixed(2)
    }
  } catch (e) {
    /* 解析失败时保留兜底数据 */
  }
})

function toWarelist() {
  router.push('/pages/account/Warelist')
}

function toSaleList() {
  router.push('/pages/account/saleList')
}
</script>
