<template>
  <uni-view data-v-25b6ee08 class="padding">
    <uni-view data-v-25b6ee08 class="bg-white flex-direction flex align-start radius" style="padding: 16px;">
      <uni-view data-v-25b6ee08 class="flex">
        <uni-image data-v-25b6ee08 class="radius" style="width: 88px; height: 88px;">
          <div :style="`background-image: url(&quot;${goods.image}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div>
          <img :src="goods.image" alt="" draggable="false" />
        </uni-image>
        <uni-view data-v-25b6ee08 class="margin-left flex flex-direction justify-between">
          <uni-view data-v-25b6ee08 class="text-bold over sale-good-name">{{ goods.name }}</uni-view>
          <uni-view data-v-25b6ee08 class="margin-top-sm sale-good-meta">#{{ goods.token }} / {{ goods.series }}</uni-view>
        </uni-view>
      </uni-view>

      <uni-view data-v-25b6ee08 class="margin-top">
        <uni-view data-v-25b6ee08>
          <uni-text data-v-25b6ee08 style="font-weight: 500; font-size: 16px; color: rgb(48, 48, 48);"><span>设置售价</span></uni-text>
          <uni-text data-v-25b6ee08 class="margin-left" style="font-weight: 500; font-size: 12px; color: rgb(104, 104, 104);"><span>您的买入价格（元）：{{ goods.buyPrice }}</span></uni-text>
        </uni-view>
        <uni-view data-v-25b6ee08 class="flex margin-top align-center">
          <uni-text data-v-25b6ee08 class="text-bold padding-right-sm" style="font-weight: 600; font-size: 24px; color: rgb(48, 48, 48);"><span>￥</span></uni-text>
          <uni-input data-v-25b6ee08>
            <div class="uni-input-wrapper">
              <div v-if="!price" class="uni-input-placeholder text-df" data-v-25b6ee08>请输入售价</div>
              <input
                :value="price"
                maxlength="140"
                step="0.01"
                enterkeyhint="done"
                pattern="[0-9.]*"
                autocomplete="off"
                inputmode="decimal"
                type="number"
                class="uni-input-input"
                @input="price = $event.target.value"
              />
            </div>
          </uni-input>
        </uni-view>
        <uni-view v-if="!canSubmit" data-v-25b6ee08 class="sale-input-hint">请输入大于 0 的售价</uni-view>
      </uni-view>
    </uni-view>

    <uni-view data-v-25b6ee08 class="margin-top bg-white radius padding">
      <uni-view data-v-25b6ee08 class="text-bold text-black" style="font-weight: 600; font-size: 14px; color: rgb(48, 48, 48);">收款账户</uni-view>
      <uni-view data-v-25b6ee08 class="flex margin-top align-center">
        <uni-view data-v-25b6ee08 style="width: 20px; height: 20px; background: rgb(29, 83, 241); border-radius: 200px; font-weight: 600; font-size: 12px; color: rgb(255, 255, 255); line-height: 20px; text-align: center;">A</uni-view>
        <uni-view data-v-25b6ee08 class="flex-sub margin-left">
          <uni-text data-v-25b6ee08 style="font-weight: 400; font-size: 14px; color: rgb(41, 41, 41);"><span>汇付</span></uni-text>
          <uni-text data-v-25b6ee08 class="margin-left" style="font-weight: 400; font-size: 14px; color: rgb(153, 153, 153);"><span>(汇付支付)</span></uni-text>
        </uni-view>
        <uni-view data-v-25b6ee08>
          <uni-label data-v-25b6ee08 class="radio uni-label-pointer">
            <uni-radio data-v-25b6ee08 style="transform: scale(0.7);">
              <div class="uni-radio-wrapper" style="--HOVER-BD-COLOR: #1D53F1;">
                <div class="uni-radio-input uni-radio-input-checked" style="color: rgb(255, 255, 255); background-color: rgb(29, 83, 241); border-color: rgb(29, 83, 241);"></div>
              </div>
            </uni-radio>
          </uni-label>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view data-v-25b6ee08 class="margin-top bg-white radius padding">
      <uni-view data-v-25b6ee08 class="text-bold text-black" style="font-weight: 600; font-size: 14px; color: rgb(48, 48, 48);">预计收入</uni-view>
      <uni-view data-v-25b6ee08 class="margin-top-sm flex align-center justify-between">
        <uni-view data-v-25b6ee08 class="desc">总售价</uni-view>
        <uni-view data-v-25b6ee08 class="text-bold">￥ {{ total }}</uni-view>
      </uni-view>
      <uni-view data-v-25b6ee08 class="margin-top-sm flex align-center justify-between">
        <uni-view data-v-25b6ee08 class="desc">服务费(5%)</uni-view>
        <uni-view data-v-25b6ee08 class="text-bold" style="color: red;">-￥ {{ fee }}</uni-view>
      </uni-view>
      <uni-view data-v-25b6ee08 class="margin-top-sm flex align-center justify-between">
        <uni-view data-v-25b6ee08 class="desc">预计收入</uni-view>
        <uni-view data-v-25b6ee08 class="text-bold">￥ {{ income }}</uni-view>
      </uni-view>
    </uni-view>

    <uni-view data-v-25b6ee08 class="bottom_nav padding flex align-center justify-center bg-white">
      <uni-view
        data-v-25b6ee08
        class="btn_abc lg text-white margin-lr-xl flex-sub"
        :style="{ background: canSubmit ? '#d82b2b' : 'rgb(210, 220, 255)', fontWeight: 400, fontSize: '17px' }"
        @click="submit"
      >
        上架到市场
      </uni-view>
    </uni-view>

    <uni-view data-v-25b6ee08 class="margin-top padding bg-white radius" style="color: rgb(155, 155, 155);">
      <uni-view data-v-25b6ee08 class="text-bold text-black" style="font-weight: 600; font-size: 14px; color: rgb(48, 48, 48);">上架</uni-view>
      <uni-view data-v-25b6ee08 class="margin-top-xs">1.商品未经购买前，可取消上架,取消挂单后三分钟禁止挂单。一经购买，无法取消上架。</uni-view>
      <uni-view data-v-25b6ee08 class="margin-top-xs">2.您将获得除综合服务费(5%)之外的所有售卖收入。</uni-view>
      <uni-view data-v-25b6ee08 class="margin-top-xs">3.商品出售成功后，售卖收入将默认进入钱包余额，钱包所有功能由第三方支付公司提供服务。</uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
/**
 * 寄售表单页 /pages/market/sale
 * 源站为纯静态空壳：商品名 / 编号 / 买入价全为空，售价输入框不绑定、
 * 预计收入的三个数字恒为 0.00，「上架到市场」按钮无任何反应。
 * 克隆版补齐：读取上一页藏品信息、售价输入 + 服务费实时试算、提交跳结果页。
 */
import { computed, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { GOODS } from '@/mock/goods'
import { toast } from '@/utils/interact'

const router = useRouter()

const goods = reactive({
  id: GOODS[0]?.id || 'g1',
  name: GOODS[0]?.name || '国潮之光',
  series: GOODS[0]?.series || '艾卡德',
  image: GOODS[0]?.img || '',
  token: 1103,
  buyPrice: Number(GOODS[0]?.floor || 188).toFixed(2)
})

const price = ref('')

const canSubmit = computed(() => parseFloat(price.value) > 0)
const total = computed(() => (canSubmit.value ? (parseFloat(price.value)).toFixed(2) : '0.00'))
const fee = computed(() => (canSubmit.value ? (parseFloat(price.value) * 0.05).toFixed(2) : '0.00'))
const income = computed(() => (canSubmit.value ? (parseFloat(price.value) * 0.95).toFixed(2) : '0.00'))

try {
  const raw = sessionStorage.getItem('icard_sale_goods')
  if (raw) {
    const d = JSON.parse(raw)
    Object.keys(d).forEach((k) => {
      if (d[k] !== undefined && d[k] !== '') goods[k] = d[k]
    })
  }
} catch (e) {
  /* 忽略解析异常，保留兜底藏品 */
}

function submit() {
  if (!canSubmit.value) return toast('请输入大于 0 的售价')
  try {
    sessionStorage.setItem('icard_sale_result', JSON.stringify({
      name: goods.name,
      image: goods.image,
      token: goods.token,
      qty: 1,
      price: total.value
    }))
  } catch (e) { /* 隐私模式下忽略 */ }
  toast('已提交上架，等待审核')
  router.push('/pages/market/saleResult')
}
</script>
