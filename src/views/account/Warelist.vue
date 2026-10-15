<template>
  <uni-view data-v-78c277ef class="container padding" style="min-height: 100vh;">
    <uni-view data-v-78c277ef class="flex align-center justify-between" style="padding-top: 0px;">
      <uni-view data-v-78c277ef class="action flex align-center justify-center" style="width: 25px; height: 25px;">
        <uni-view data-v-78c277ef class="cuIcon-back" style="font-size: 15px; font-weight: bold;"></uni-view>
      </uni-view>
      <uni-view data-v-78c277ef class="text-black" style="font-size: 17px; font-weight: bold; font-family: new;">云仓提货</uni-view>
      <uni-view data-v-78c277ef></uni-view>
    </uni-view>

    <uni-scroll-view data-v-78c277ef style="height: calc(-50px + 100vh);">
      <div class="uni-scroll-view">
        <div class="uni-scroll-view" style="overflow: hidden auto;">
          <div class="uni-scroll-view-content">
            <uni-view data-v-78c277ef>
              <uni-view v-if="rows.length" data-v-78c277ef class="margin-top flex flex-wrap">
                <uni-view
                  v-for="g in rows"
                  :key="g.id"
                  data-v-78c277ef
                  class="ware-card"
                  @click="openDetail(g)"
                >
                  <uni-image data-v-78c277ef class="ware-img">
                    <div :style="`background-image: url(&quot;${g.image}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div>
                    <img :src="g.image" alt="" draggable="false" />
                  </uni-image>
                  <uni-view data-v-78c277ef class="ware-name over">{{ g.name }}</uni-view>
                  <uni-view data-v-78c277ef class="ware-meta">{{ g.series }} · 持有 {{ g.own }} 个</uni-view>
                  <uni-view data-v-78c277ef class="ware-price">¥{{ g.price }}</uni-view>
                </uni-view>
              </uni-view>

              <uni-view
                v-else
                data-v-4d930ea0
                data-v-78c277ef
                class="flex align-center justify-center"
                style="height: 50vh;"
              >
                <uni-view data-v-4d930ea0 class="text-center">
                  <uni-image data-v-4d930ea0 style="width: 90px; height: 80px;">
                    <div style="background-image: url(&quot;/static/images/empty1.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
                    <img src="/static/images/empty1.png" alt="" draggable="false" />
                  </uni-image>
                  <uni-view data-v-4d930ea0 class="text-grey margin-top-xs"> 暂无数据 </uni-view>
                </uni-view>
              </uni-view>

              <!-- 藏品详情弹层 -->
              <uni-view data-v-78c277ef class="cu-modal bottom-modal" :class="{ show: !!detail }">
                <uni-view data-v-78c277ef class="cu-dialog bg-white" style="border-radius: 19px 19px 0px 0px;">
                  <uni-view data-v-78c277ef class="padding-sm text-left">
                    <uni-view data-v-78c277ef class="flex align-center justify-between margin-top-sm">
                      <uni-view data-v-78c277ef class="flex align-center">
                        <uni-view data-v-78c277ef class="margin-left flex align-end">
                          <uni-view data-v-78c277ef class="over text-lg" style="font-weight: 500; font-size: 18px; color: rgb(34, 34, 34);">{{ detail ? detail.name : '' }}</uni-view>
                          <uni-view data-v-78c277ef class="text-sm text-grey margin-left" style="font-weight: 400; font-size: 11px; color: rgb(102, 102, 102); margin-top: 5px;">持有: {{ detail ? detail.own : 0 }} 个</uni-view>
                        </uni-view>
                      </uni-view>
                    </uni-view>

                    <uni-view data-v-78c277ef class="flex align-center justify-end margin-top ware-acts">
                      <uni-view data-v-78c277ef class="cu-btn sm bg-gray radius margin-right" @click="openSell(detail)">批量寄售</uni-view>
                      <uni-view data-v-78c277ef class="cu-btn sm bg-gold radius" @click="openPick(detail)">提货</uni-view>
                    </uni-view>

                    <uni-view data-v-78c277ef class="ware-detail-tip">该藏品下链上编号均可提货，点击「提货」填写收货信息</uni-view>
                    <uni-view v-if="detail" data-v-78c277ef class="ware-token-list">
                      <uni-view v-for="(t, i) in tokens" :key="i" data-v-78c277ef class="token-row">
                        <uni-view data-v-78c277ef class="token-tag">#{{ t }}</uni-view>
                        <uni-view data-v-78c277ef class="token-state">可提货</uni-view>
                      </uni-view>
                    </uni-view>

                    <uni-view data-v-78c277ef class="ware-detail-footer">
                      <uni-view data-v-78c277ef class="cu-btn lg bg-gray radius flex-sub" @click="detail = null">关闭</uni-view>
                    </uni-view>
                  </uni-view>
                </uni-view>
              </uni-view>

              <!-- 批量寄售弹层 -->
              <uni-view data-v-78c277ef class="cu-modal" :class="{ show: sellShow }">
                <uni-view data-v-78c277ef class="cu-dialog bg-white text-left padding radius">
                  <uni-view data-v-78c277ef class="text-center text-bold text-lg">批量寄售</uni-view>
                  <uni-view data-v-78c277ef class="margin-top">
                    <uni-view data-v-78c277ef>寄售价格</uni-view>
                    <uni-view data-v-78c277ef class="padding-sm margin-top radius bg-gray">
                      <uni-input data-v-78c277ef>
                        <div class="uni-input-wrapper">
                          <div v-if="!sellPrice" class="uni-input-placeholder text-df" data-v-78c277ef>请输入价格</div>
                          <input maxlength="140" inputmode="decimal" type="text" class="uni-input-input" :value="sellPrice" @input="sellPrice = $event.target.value" />
                        </div>
                      </uni-input>
                    </uni-view>
                  </uni-view>
                  <uni-view data-v-78c277ef class="margin-top flex align-center justify-between">
                    <uni-view data-v-78c277ef class="text-grey">预计收益</uni-view>
                    <uni-view data-v-78c277ef class="text-bold">￥ {{ income }}</uni-view>
                  </uni-view>
                  <uni-view data-v-78c277ef class="margin-top-sm flex align-center justify-between">
                    <uni-view data-v-78c277ef class="text-grey">服务费(5%)</uni-view>
                    <uni-view data-v-78c277ef class="text-bold">￥ {{ fee }}</uni-view>
                  </uni-view>
                  <uni-view data-v-78c277ef class="padding margin-top">
                    <uni-view data-v-78c277ef class="flex">
                      <uni-view data-v-78c277ef class="cu-btn lg bg-gray radius margin-right flex-sub" @click="sellShow = false">返回</uni-view>
                      <uni-view data-v-78c277ef class="cu-btn lg bg-gold radius flex-sub" @click="doSell">寄售</uni-view>
                    </uni-view>
                  </uni-view>
                </uni-view>
              </uni-view>

              <!-- 开启结果弹层 -->
              <uni-view data-v-78c277ef class="cu-modal" :class="{ show: resultShow }">
                <uni-view data-v-78c277ef class="cu-dialog bg-white">
                  <uni-view data-v-78c277ef class="padding">
                    <uni-view data-v-78c277ef>开启结果</uni-view>
                    <uni-view data-v-78c277ef class="margin-top">
                      <uni-image data-v-78c277ef class="radius" style="width: 150px; height: 150px;">
                        <div :style="`background-image: url(&quot;${resultImg}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div>
                        <img :src="resultImg" alt="" draggable="false" />
                      </uni-image>
                    </uni-view>
                    <uni-view data-v-78c277ef class="margin-top-sm">{{ resultText }}</uni-view>
                    <uni-view data-v-78c277ef class="flex margin-top">
                      <uni-view data-v-78c277ef class="cu-btn round margin-lr-xl lg flex-sub bg-black text-green" @click="resultShow = false">确定</uni-view>
                    </uni-view>
                  </uni-view>
                </uni-view>
              </uni-view>

              <!-- 提货弹层 -->
              <uni-view data-v-78c277ef class="cu-modal" :class="{ show: pickShow }">
                <uni-view data-v-78c277ef class="cu-dialog bg-white text-left padding radius">
                  <uni-view data-v-78c277ef class="text-center text-bold text-lg">提货</uni-view>
                  <uni-view data-v-78c277ef class="margin-top">
                    <uni-view data-v-78c277ef>收货地址</uni-view>
                    <uni-view data-v-78c277ef class="padding-sm margin-top radius bg-gray" @click="chooseAddr">
                      <uni-view data-v-78c277ef class="flex align-center justify-between">
                        {{ addr || '请设置默认地址' }}
                        <uni-text data-v-78c277ef class="cuIcon-right"><span></span></uni-text>
                      </uni-view>
                    </uni-view>
                  </uni-view>
                  <uni-view data-v-78c277ef class="margin-top">
                    <uni-view data-v-78c277ef>备注</uni-view>
                    <uni-view data-v-78c277ef class="padding-sm margin-top radius bg-gray">
                      <uni-textarea data-v-78c277ef>
                        <div class="uni-textarea-wrapper">
                          <div v-if="!remark" class="uni-textarea-placeholder textarea-placeholder" data-v-78c277ef>请输入备注</div>
                          <textarea maxlength="140" class="uni-textarea-textarea" style="overflow-y: auto;" :value="remark" @input="remark = $event.target.value"></textarea>
                        </div>
                      </uni-textarea>
                    </uni-view>
                  </uni-view>
                  <uni-view data-v-78c277ef class="margin-top">
                    <uni-view data-v-78c277ef class="flex">
                      <uni-view data-v-78c277ef class="cu-btn lg margin-right bg-gray light flex-sub radius" @click="pickShow = false">返回</uni-view>
                      <uni-view data-v-78c277ef class="cu-btn lg bg-gold flex-sub radius" @click="doPick"> 提货 </uni-view>
                    </uni-view>
                  </uni-view>
                </uni-view>
              </uni-view>
            </uni-view>
          </div>
        </div>
      </div>
    </uni-scroll-view>
  </uni-view>
</template>

<script setup>
/**
 * 云仓提货
 * 源站该页是纯静态空壳：只有 2 个 item-placeholder 占位块 + 永久「暂无数据」，
 * 4 个弹层（藏品详情 / 批量寄售 / 开启结果 / 提货）结构虽在，但没有任何数据与事件。
 * 克隆版补齐：6 条可提货藏品、点击开详情（展开链上编号列表）、
 * 批量寄售（价格输入 + 收益/服务费实时试算）、提货（地址 + 备注 + 提交）。
 */
import { computed, ref } from 'vue'
import { GOODS } from '@/mock/goods'
import { toast } from '@/utils/interact'

/** 云仓可提货藏品：沿用页面原有的 .item-placeholder / .flex-wrap 栅格 */
const rows = ref(
  GOODS.slice(0, 6).map((g, i) => ({
    id: g.id,
    name: g.name,
    series: g.series,
    image: g.img,
    price: g.floor,
    own: (i % 3) + 1
  }))
)

const detail = ref(null)
const tokens = computed(() =>
  detail.value ? Array.from({ length: detail.value.own }, (_, i) => 1000 + i * 37 + detail.value.id.charCodeAt(0)) : []
)

const sellShow = ref(false)
const sellPrice = ref('')
const sellNum = computed(() => detail.value?.own || 1)
const fee = computed(() => {
  const v = parseFloat(sellPrice.value) * sellNum.value
  return Number.isFinite(v) ? (v * 0.05).toFixed(2) : '0.00'
})
const income = computed(() => {
  const v = parseFloat(sellPrice.value) * sellNum.value
  return Number.isFinite(v) ? (v * 0.95).toFixed(2) : '0.00'
})

const resultShow = ref(false)
const resultImg = ref('')
const resultText = ref('')

const pickShow = ref(false)
const addr = ref('')
const remark = ref('')


function openDetail(g) {
  detail.value = g
}

function openSell(g) {
  if (!g) return
  detail.value = g
  sellPrice.value = String(g.price)
  sellShow.value = true
}

function doSell() {
  if (!parseFloat(sellPrice.value)) return toast('请输入寄售价格')
  sellShow.value = false
  resultImg.value = detail.value.image
  resultText.value = `${detail.value.name} × ${sellNum.value} 已提交寄售，预计到账 ¥${income.value}`
  /* 写进 sessionStorage，供 /pages/market/saleResult 结果页读取展示 */
  try {
    sessionStorage.setItem('icard_sale_result', JSON.stringify({
      name: detail.value.name,
      image: detail.value.image,
      token: tokens.value[0] || 1103,
      qty: sellNum.value,
      price: (parseFloat(sellPrice.value) * sellNum.value).toFixed(2)
    }))
  } catch (e) { /* 隐私模式下忽略 */ }
  resultShow.value = true
}

function openPick(g) {
  if (!g) return
  detail.value = g
  pickShow.value = true
}

function chooseAddr() {
  addr.value = addr.value ? '' : '王小明 138****8000 浙江省杭州市西湖区文三路 100 号'
}

function doPick() {
  if (!addr.value) return toast('请先设置收货地址')
  pickShow.value = false
  detail.value = null
  toast('提货申请已提交，1-3 个工作日内发货')
}
</script>