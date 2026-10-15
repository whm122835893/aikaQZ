<template>
  <uni-view data-v-22bfe69e class="order-page" style="padding-top: 0px;">
    <uni-view data-v-22bfe69e class="header margin-lr">
      <uni-view data-v-22bfe69e class="back-btn"><uni-text data-v-22bfe69e class="cuIcon-back"><span></span></uni-text></uni-view>
      <uni-view data-v-22bfe69e class="page-title">实物订单</uni-view>
      <uni-view data-v-22bfe69e class="header-placeholder"></uni-view>
    </uni-view>

    <uni-view data-v-22bfe69e class="tab-bar">
      <uni-view
        v-for="(t, i) in mainTabs"
        :key="t"
        data-v-22bfe69e
        class="tab-item"
        :class="{ active: main === i }"
        @click="main = i"
      >
        <uni-text data-v-22bfe69e><span>{{ t }}</span></uni-text>
        <uni-view data-v-22bfe69e class="tab-line"></uni-view>
      </uni-view>
    </uni-view>

    <uni-scroll-view data-v-22bfe69e class="nav">
      <div class="uni-scroll-view">
        <div class="uni-scroll-view" style="overflow: auto hidden;">
          <div class="uni-scroll-view-content">
            <uni-view
              v-for="(t, i) in subTabs"
              :key="t"
              data-v-22bfe69e
              class="cu-item text-grey text-sm flex-sub"
              @click="sub = i"
            >
              <uni-view
                data-v-22bfe69e
                class="cu-tag round padding-sm"
                :class="sub === i ? 'tab-active' : 'no-active'"
              >{{ t }}</uni-view>
            </uni-view>
          </div>
        </div>
      </div>
    </uni-scroll-view>

    <uni-view data-v-22bfe69e class="list margin-top-sm padding-bottom">
      <uni-view
        v-for="o in rows"
        :key="o.id"
        data-v-22bfe69e
        class="po-item"
        @click="openDetail(o)"
      >
        <uni-view data-v-22bfe69e class="po-head">
          <uni-text data-v-22bfe69e class="po-no"><span>订单号：{{ o.no }}</span></uni-text>
          <uni-text data-v-22bfe69e class="po-status" :class="statusClass(o.status)"><span>{{ o.status }}</span></uni-text>
        </uni-view>

        <uni-view data-v-22bfe69e class="po-body">
          <uni-view data-v-22bfe69e class="po-thumb">
            <uni-image data-v-22bfe69e>
              <div :style="`background-image: url(&quot;${o.image}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div>
              <img :src="o.image" alt="" draggable="false" />
            </uni-image>
          </uni-view>

          <uni-view data-v-22bfe69e class="po-info">
            <uni-view data-v-22bfe69e class="po-name">{{ o.name }}</uni-view>
            <uni-view data-v-22bfe69e class="po-spec">{{ o.spec }} · 数量 x{{ o.qty }}</uni-view>
            <uni-view data-v-22bfe69e class="po-time">{{ o.time }}</uni-view>
          </uni-view>

          <uni-view data-v-22bfe69e class="po-right">
            <uni-view data-v-22bfe69e class="po-price">¥{{ o.price }}</uni-view>
            <uni-view data-v-22bfe69e class="po-acts">
              <uni-view
                v-if="o.status === UNPAID"
                data-v-22bfe69e
                class="po-btn primary"
                @click.stop="pay(o)"
              >去支付</uni-view>
              <uni-view
                v-else-if="o.status === PAID"
                data-v-22bfe69e
                class="po-btn"
                @click.stop="openDetail(o)"
              >查看物流</uni-view>
            </uni-view>
          </uni-view>
        </uni-view>
      </uni-view>

      <uni-view
        v-if="!rows.length"
        data-v-4d930ea0
        data-v-22bfe69e
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
    </uni-view>

    <!-- 订单详情弹层 -->
    <uni-view data-v-22bfe69e class="cu-modal bottom-modal" :class="{ show: !!detail }">
      <uni-view data-v-22bfe69e class="cu-dialog po-sheet">
        <uni-view data-v-22bfe69e class="po-sheet-title">实物订单详情</uni-view>
        <uni-view v-if="detail" data-v-22bfe69e class="po-sheet-body">
          <uni-view data-v-22bfe69e class="po-row"><uni-text data-v-22bfe69e><span>订单号</span></uni-text><uni-text data-v-22bfe69e class="po-row-v"><span>{{ detail.no }}</span></uni-text></uni-view>
          <uni-view data-v-22bfe69e class="po-row"><uni-text data-v-22bfe69e><span>商品</span></uni-text><uni-text data-v-22bfe69e class="po-row-v"><span>{{ detail.name }}</span></uni-text></uni-view>
          <uni-view data-v-22bfe69e class="po-row"><uni-text data-v-22bfe69e><span>规格</span></uni-text><uni-text data-v-22bfe69e class="po-row-v"><span>{{ detail.spec }} × {{ detail.qty }}</span></uni-text></uni-view>
          <uni-view data-v-22bfe69e class="po-row"><uni-text data-v-22bfe69e><span>类型</span></uni-text><uni-text data-v-22bfe69e class="po-row-v"><span>{{ detail.type }}</span></uni-text></uni-view>
          <uni-view data-v-22bfe69e class="po-row"><uni-text data-v-22bfe69e><span>金额</span></uni-text><uni-text data-v-22bfe69e class="po-row-v strong"><span>¥{{ detail.price }}</span></uni-text></uni-view>
          <uni-view data-v-22bfe69e class="po-row"><uni-text data-v-22bfe69e><span>状态</span></uni-text><uni-text data-v-22bfe69e class="po-row-v"><span>{{ detail.status }}</span></uni-text></uni-view>
          <uni-view data-v-22bfe69e class="po-row"><uni-text data-v-22bfe69e><span>下单时间</span></uni-text><uni-text data-v-22bfe69e class="po-row-v"><span>{{ detail.time }}</span></uni-text></uni-view>
          <uni-view data-v-22bfe69e class="po-row"><uni-text data-v-22bfe69e><span>物流</span></uni-text><uni-text data-v-22bfe69e class="po-row-v"><span>{{ detail.status === PAID ? '顺丰速运 SF7364920184 · 运输中' : '暂无物流信息' }}</span></uni-text></uni-view>
        </uni-view>
        <uni-view data-v-22bfe69e class="po-sheet-footer">
          <uni-view data-v-22bfe69e class="po-sheet-btn" @click="detail = null">关闭</uni-view>
          <uni-view data-v-22bfe69e class="po-sheet-btn primary" @click="contact">联系客服</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
/**
 * 实物订单页
 * 源站该页是纯静态空壳：只有 tab 骨架 + 「暂无数据」占位，没有任何数据与交互。
 * 克隆版补齐：主 Tab（全部/购买/托管/寄售）× 子 Tab（全部/待付款/已支付/订单取消）
 * 双向过滤、12 条真实演示数据、订单卡点击开详情弹层、去支付 / 查看物流 / 联系客服动作。
 */
import { computed, ref } from 'vue'
import { pickPhysical, UNPAID, PAID } from '@/mock/orders'
import { toast } from '@/utils/interact'

const mainTabs = ['全部', '购买', '托管', '寄售']
const subTabs = ['全部', '待付款', '已支付', '订单取消']
const MAIN_TYPE = { 全部: '全部', 购买: '实物购买', 托管: '实物托管', 寄售: '实物寄售' }
const SUB_STATUS = { 全部: [], 待付款: [UNPAID], 已支付: [PAID], 订单取消: ['订单取消'] }

const main = ref(0)
const sub = ref(0)
const detail = ref(null)

const rows = computed(() => pickPhysical(MAIN_TYPE[mainTabs[main.value]], SUB_STATUS[subTabs[sub.value]]))

function statusClass(s) {
  if (s === UNPAID) return 'st-unpaid'
  if (s === PAID) return 'st-paid'
  return 'st-closed'
}

function openDetail(o) {
  detail.value = o
}

function pay(o) {
  toast('订单 ' + o.no + ' 跳转支付…')
}

function contact() {
  toast('客服热线 400-888-6666（演示）')
}
</script>