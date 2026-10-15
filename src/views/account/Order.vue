<template>
  <uni-view data-v-5cd26038 class="page" style="padding-top: 0px;">
    <uni-view data-v-5cd26038 class="flex align-center justify-between padding-xs" style="height: 40px; position: relative; z-index: 99;">
      <uni-view data-v-5cd26038 class="cuIcon-back" style="color: rgb(0, 0, 0); font-weight: bold;"></uni-view>
      <uni-view data-v-5cd26038 class="text-center radius flex tab_item align-center justify-center text-sel" style="width: 33%; height: 80%; font-size: 17px; font-family: new;">
        <uni-text data-v-5cd26038><span>提货订单列表</span></uni-text>
      </uni-view>
      <uni-view data-v-5cd26038></uni-view>
    </uni-view>

    <uni-scroll-view data-v-5cd26038 class="nav" style="position: relative; z-index: 99;">
      <div class="uni-scroll-view">
        <div class="uni-scroll-view" style="overflow: auto hidden;">
          <div class="uni-scroll-view-content">
            <uni-view data-v-5cd26038 class="flex justify-around">
              <uni-view
                v-for="(t, i) in tabs"
                :key="t"
                data-v-5cd26038
                class="pick-tab"
                :class="{ on: tab === i }"
                @click="tab = i"
              >{{ t }}</uni-view>
            </uni-view>
          </div>
        </div>
      </div>
    </uni-scroll-view>

    <uni-view v-if="rows.length" data-v-5cd26038 class="padding-lr" style="border-radius: 8px 8px 0px 0px; position: relative; z-index: 99;">
      <uni-view
        v-for="o in rows"
        :key="o.id"
        data-v-5cd26038
        class="pick-item"
        @click="openDetail(o)"
      >
        <uni-view data-v-5cd26038 class="pick-head">
          <uni-text data-v-5cd26038 class="pick-no"><span>单号 {{ o.no }}</span></uni-text>
          <uni-text data-v-5cd26038 class="pick-status" :class="statusClass(o.status)"><span>{{ o.status }}</span></uni-text>
        </uni-view>

        <uni-view data-v-5cd26038 class="pick-body">
          <uni-image data-v-5cd26038 class="pick-thumb">
            <div :style="`background-image: url(&quot;${o.image}&quot;); background-position: center center; background-size: cover; background-repeat: no-repeat;`"></div>
            <img :src="o.image" alt="" draggable="false" />
          </uni-image>
          <uni-view data-v-5cd26038 class="pick-info">
            <uni-view data-v-5cd26038 class="pick-name over">{{ o.name }}</uni-view>
            <uni-view data-v-5cd26038 class="pick-token">#{{ o.token }} · x{{ o.qty }}</uni-view>
            <uni-view data-v-5cd26038 class="pick-time">{{ o.time }}</uni-view>
          </uni-view>
        </uni-view>

        <uni-view data-v-5cd26038 class="pick-foot">
          <uni-text data-v-5cd26038 class="pick-addr over"><span>{{ o.addr }}</span></uni-text>
          <uni-view v-if="o.status === '待发货'" data-v-5cd26038 class="pick-btn" @click.stop="remind(o)">提醒发货</uni-view>
          <uni-view v-else-if="o.status === '已发货'" data-v-5cd26038 class="pick-btn primary" @click.stop="openDetail(o)">查看物流</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-view
      v-else
      data-v-4d930ea0
      data-v-5cd26038
      class="flex align-center justify-center list"
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

    <!-- 提货详情弹层 -->
    <uni-view data-v-5cd26038 class="cu-modal bottom-modal" :class="{ show: !!detail }">
      <uni-view data-v-5cd26038 class="cu-dialog bg-white pick-sheet">
        <uni-view data-v-5cd26038 class="pick-sheet-title">提货订单详情</uni-view>
        <uni-view v-if="detail" data-v-5cd26038 class="pick-sheet-body">
          <uni-view data-v-5cd26038 class="pick-row"><uni-text data-v-5cd26038><span>单号</span></uni-text><uni-text data-v-5cd26038 class="pick-row-v"><span>{{ detail.no }}</span></uni-text></uni-view>
          <uni-view data-v-5cd26038 class="pick-row"><uni-text data-v-5cd26038><span>藏品</span></uni-text><uni-text data-v-5cd26038 class="pick-row-v"><span>{{ detail.name }}</span></uni-text></uni-view>
          <uni-view data-v-5cd26038 class="pick-row"><uni-text data-v-5cd26038><span>编号</span></uni-text><uni-text data-v-5cd26038 class="pick-row-v"><span>#{{ detail.token }} × {{ detail.qty }}</span></uni-text></uni-view>
          <uni-view data-v-5cd26038 class="pick-row"><uni-text data-v-5cd26038><span>状态</span></uni-text><uni-text data-v-5cd26038 class="pick-row-v"><span>{{ detail.status }}</span></uni-text></uni-view>
          <uni-view data-v-5cd26038 class="pick-row"><uni-text data-v-5cd26038><span>收货地址</span></uni-text><uni-text data-v-5cd26038 class="pick-row-v"><span>{{ detail.addr }}</span></uni-text></uni-view>
          <uni-view data-v-5cd26038 class="pick-row"><uni-text data-v-5cd26038><span>物流</span></uni-text><uni-text data-v-5cd26038 class="pick-row-v"><span>{{ detail.status === '已发货' ? '顺丰速运 SF7364920184 · 运输中' : '暂未发货' }}</span></uni-text></uni-view>
          <uni-view data-v-5cd26038 class="pick-row"><uni-text data-v-5cd26038><span>下单时间</span></uni-text><uni-text data-v-5cd26038 class="pick-row-v"><span>{{ detail.time }}</span></uni-text></uni-view>
        </uni-view>
        <uni-view data-v-5cd26038 class="pick-sheet-footer">
          <uni-view data-v-5cd26038 class="pick-sheet-btn" @click="detail = null">关闭</uni-view>
          <uni-view data-v-5cd26038 class="pick-sheet-btn primary" @click="contact">联系客服</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
/**
 * 提货订单列表
 * 源站该页是纯静态空壳：顶部只有一个写死的标题、Tab 容器是空的、永远「暂无数据」。
 * 克隆版补齐：4 个状态 Tab 过滤 + 7 条提货订单 + 详情弹层 + 提醒发货 / 查看物流。
 */
import { computed, ref } from 'vue'
import { GOODS } from '@/mock/goods'
import { toast } from '@/utils/interact'

const tabs = ['全部', '待发货', '已发货', '已完成']
const WAIT = '待发货'
const SHIPPED = '已发货'
const DONE = '已完成'

const tab = ref(0)
const detail = ref(null)

const SEED = [
  [WAIT, 2, '2026-10-08 14:31'],
  [WAIT, 1, '2026-10-05 09:22'],
  [SHIPPED, 1, '2026-09-29 20:15'],
  [SHIPPED, 3, '2026-09-21 11:47'],
  [DONE, 1, '2026-09-12 16:03'],
  [DONE, 2, '2026-09-03 10:38'],
  [DONE, 4, '2026-08-25 19:52']
]

const ADDRS = [
  '王小明 138****8000 浙江省杭州市西湖区文三路 100 号',
  '李小明 139****1234 广东省深圳市南山区科技园南路 8 号',
  '张小红 137****5678 上海市浦东新区张江高科路 66 号'
]

const ALL = SEED.map(([status, qty, time], i) => {
  const g = GOODS[i % GOODS.length]
  return {
    id: 50000 + i,
    no: 'IC' + String(20260870000 + i * 191),
    status,
    name: g.name,
    image: g.img,
    token: 1000 + i * 61,
    qty,
    addr: ADDRS[i % ADDRS.length],
    time
  }
})

const rows = computed(() => (tab.value === 0 ? ALL : ALL.filter((o) => o.status === tabs[tab.value])))

function statusClass(s) {
  if (s === WAIT) return 'st-wait'
  if (s === SHIPPED) return 'st-ship'
  return 'st-done'
}


function openDetail(o) {
  detail.value = o
}

function remind(o) {
  toast('已提醒商家尽快发货：' + o.name)
}

function contact() {
  toast('客服热线 400-888-6666（演示）')
}
</script>