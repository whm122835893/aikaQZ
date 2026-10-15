#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OrderList.vue —— 双层 Tab 接数据 + 订单详情弹层"""
import io, re, sys

P = 'src/views/account/OrderList.vue'
s = io.open(P, encoding='utf-8').read()
orig = s

# ---------- 1. 顶部主 Tab：改成 v-for ----------
old_top = re.search(r'<uni-view data-v-38529c3e="" class="tab-bar-inner">.*?</uni-view></div></div></div></uni-scroll-view>', s, re.S)
assert old_top, 'top tab not found'
new_top = (
    '<uni-view data-v-38529c3e="" class="tab-bar-inner">'
    '<uni-view v-for="t in topTabs" :id="\'top-tab-\' + t.id" :key="t.id"'
    ' class="tab-item" :class="{ active: top === t.id }" @click="setTop(t.id)">'
    '<uni-text data-v-38529c3e=""><span>{{ t.label }}</span></uni-text>'
    '<uni-view data-v-38529c3e="" class="tab-line"></uni-view>'
    '</uni-view>'
    '</div></div></div></uni-scroll-view>'
)
s = s[:old_top.start()] + new_top + s[old_top.end():]

# ---------- 2. 子 Tab：改成 v-for ----------
old_sub = re.search(r'<uni-view data-v-38529c3e="" class="sub-tab-capsule-wrap">.*?</uni-view></div></div></div></uni-scroll-view></uni-view>', s, re.S)
assert old_sub, 'sub tab not found'
new_sub = (
    '<uni-view data-v-38529c3e="" class="sub-tab-capsule-wrap"><uni-view data-v-38529c3e="" class="sub-tab-capsule">'
    '<uni-view v-for="(st, i) in subTabs" :id="\'sub-tab-\' + i" :key="st"'
    ' class="sub-tab-item" :class="{ active: sub === i }" @click="sub = i">'
    '<uni-text data-v-38529c3e=""><span>{{ st }}</span></uni-text>'
    '</uni-view>'
    '</uni-view></div></div></div></uni-scroll-view></uni-view>'
)
s = s[:old_sub.start()] + new_sub + s[old_sub.end():]

# ---------- 3. 列表区：渲染订单 + 空态受控 ----------
i = s.find('<uni-view data-v-38529c3e="" class="order-list"></uni-view>')
j = s.find('class="flex align-center justify-center" style="height: 50vh;"')
k = s.find('暂无数据', j)
k2 = s.find('</uni-view></uni-view>', k) + len('</uni-view></uni-view>')
assert i > 0 and j > i and k > j, 'list block not found'
row_tpl = (
    '<uni-view data-v-38529c3e="" class="order-list">'
    '<uni-view v-for="o in rows" :key="o.id" class="order-item" @click="openDetail(o)">'
    '<uni-view data-v-38529c3e="" class="order-item-head">'
    '<uni-text data-v-38529c3e="" class="order-item-no"><span>订单编号：{{ o.no }}</span></uni-text>'
    '<uni-text data-v-38529c3e="" class="order-item-status" :class="statusClass(o.status)"><span>{{ o.status }}</span></uni-text>'
    '</uni-view>'
    '<uni-view data-v-38529c3e="" class="order-item-body">'
    '<uni-view data-v-38529c3e="" class="order-thumb"></uni-view>'
    '<uni-view data-v-38529c3e="" class="order-info">'
    '<uni-view data-v-38529c3e="" class="over order-name">{{ o.name }}</uni-view>'
    '<uni-view data-v-38529c3e="" class="order-token">#{{ o.token }} · 数量 {{ o.qty }}</uni-view>'
    '<uni-view data-v-38529c3e="" class="order-time">{{ o.time }}</uni-view>'
    '</uni-view>'
    '<uni-view data-v-38529c3e="" class="order-price">￥<uni-text data-v-38529c3e="" class="text-xl text-bold"><span>{{ o.price }}</span></uni-text></uni-view>'
    '</uni-view>'
    '</uni-view>'
    '</uni-view>'
)
empty_tpl = (
    '<uni-view v-if="!rows.length" class="flex align-center justify-center" style="height: 50vh;">'
    '<uni-view class="text-center">'
    '<uni-image style="width: 90px; height: 80px;">'
    '<div style="background-image: url(&quot;/static/images/empty1.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>'
    '<img src="/static/images/empty1.png" draggable="false"></uni-image>'
    '<uni-view class="text-grey margin-top-xs"> 暂无数据 </uni-view>'
    '</uni-view></uni-view>'
)
s = s[:i] + row_tpl + empty_tpl + s[k2:]

# ---------- 4. 底部详情弹层：填数据 + 打开关闭 ----------
i4 = s.find('<uni-view data-v-38529c3e="" class="cu-modal bottom-modal">')
i5 = s.find('</template>', i4)
assert i4 > 0 and i5 > i4, 'modal not found'
new_modal = (
    '<uni-view class="cu-modal bottom-modal" :class="{ show: !!detail }">'
    '<uni-view class="cu-dialog bg-white">'
    '<uni-view class="padding text-left" @click="detail = null">'
    '<uni-view class="flex align-center justify-between">'
    '<uni-view class="text-grey"> 订单编号: {{ detail ? detail.no : \'\' }} </uni-view>'
    '<uni-text class="cuIcon-close"><span></span></uni-text>'
    '</uni-view>'
    '<uni-view class="flex align-center justify-between margin-top-sm">'
    '<uni-view class="flex align-center">'
    '<uni-view class="radius order-thumb"></uni-view>'
    '<uni-view class="margin-left padding-top">'
    '<uni-view class="over text-lg">{{ detail ? detail.name : \'\' }}</uni-view>'
    '<uni-view class="margin-top-xl text-black"> ￥{{ detail ? detail.price : \'0.00\' }} </uni-view>'
    '</uni-view>'
    '</uni-view>'
    '</uni-view>'
    '<uni-view class="flex align-center justify-between margin-top">'
    '<uni-view class="text-grey"> 接收人区块链地址 </uni-view>'
    '<uni-view class="text-black">{{ detail ? detail.token : 0 }}</uni-view>'
    '</uni-view>'
    '<uni-view class="margin-top-xl flex align-center justify-center" @click="goPay">'
    '<uni-view class="cu-btn lg btn-action-yellow radius pay-btn">{{ detail ? actionText : \'关闭\' }}</uni-view>'
    '</uni-view>'
    '</uni-view>'
    '</uni-view>'
    '</uni-view>'
)
s = s[:i4] + new_modal + '\n' + s[i5:]

# ---------- 5. 注入 script ----------
script = '''
<script setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { pickOrders, UNPAID, PAID, CANCELED } from '@/mock/orders'
import { toast } from '@/utils/interact'

const router = useRouter()

/** 主 Tab：id 对应原有 top-tab-N 的 N */
const topTabs = [
  { id: 1, label: '首发订单' },
  { id: 2, label: '常规交易' },
  { id: 4, label: '求购订单' },
  { id: 7, label: '委托订单' },
  { id: 3, label: '盲盒订单' }
]

const top = ref(1)
const sub = ref(0)
const detail = ref(null)

const subTabs = computed(() => ['全部', UNPAID, PAID, CANCELED])

const statusMap = {
  待付款: ['all', UNPAID],
  已支付: ['all', PAID],
  订单取消: ['all', CANCELED],
  已关闭: ['all'],
  已成交: ['all'],
  已售出: ['all'],
  求购中: ['all'],
  待发货: [UNPAID],
  已收货: [PAID]
}

const rows = computed(() => {
  const t = topTabs.find((x) => x.id === top.value)
  const st = subTabs.value[sub.value]
  const pool = statusMap[st] || ['all']
  return pool === ['all'] ? pickOrders(t.label) : pickOrders(t.label, pool)
})

const actionText = computed(() => (detail.value && detail.value.status === UNPAID ? '去支付' : '关闭'))

function statusClass(s) {
  if (s === UNPAID) return 'st-unpaid'
  if (s === CANCELED || s === '已关闭') return 'st-closed'
  return 'st-paid'
}

function setTop(id) {
  if (top.value === id) return
  top.value = id
  sub.value = 0
}

function openDetail(o) {
  detail.value = o
}

function goPay() {
  if (!detail.value) return
  if (detail.value.status !== UNPAID) {
    detail.value = null
    return
  }
  toast('已跳转收银台（演示环境不真实扣款）')
  detail.value = null
}
</script>
'''
s = s.replace('\n</template>\n', '\n</template>\n' + script, 1)

io.open(P, 'w', encoding='utf-8').write(s)
print('OrderList patched, len %d -> %d' % (len(orig), len(s)))