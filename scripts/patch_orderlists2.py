#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MarketOrderList.vue —— 3 个状态 Tab 可切换 + 列表渲染"""
import io

P = 'src/views/account/MarketOrderList.vue'
s = io.open(P, encoding='utf-8').read()
orig = len(s)

# ---------- Tab 改v-for ----------
i = s.find('<div class="uni-scroll-view-content">')
j = s.find('</div></div></div></uni-scroll-view>', i)
assert i > 0 and j > i
new_tabs = (
    '<div class="uni-scroll-view-content">'
    '<uni-view v-for="(t, i) in tabs" :key="t" :data-id="i"'
    ' class="cu-item text-gray flex-sub" :class="tab === i ? \'text-bold text-white\' : \'\'"'
    ' @click="tab = i"> {{ t }} <uni-view class="line"></uni-view></uni-view>'
)
s = s[:i] + new_tabs + s[j:]

# ---------- 列表区替换 ----------
i = s.find('<uni-view data-v-7144ea85="" class="list">')
j = s.find('</template>', i)
assert i > 0 and j > i
rows = (
    '<uni-view data-v-7144ea85="" class="list">'
    '<uni-view v-for="o in rows" :key="o.id" class="item padding-sm radius bg-grey margin-bottom-sm" @click="go(o)">'
    '<uni-view data-v-7144ea85="" class="text-sm text-right" :class="tab === 0 ? \'text-orange\' : \'\'"> {{ tabName(o.status) }} </uni-view>'
    '<uni-view data-v-7144ea85="" class="flex align-center">'
    '<uni-view data-v-7144ea85="" style="width: 210px;">'
    '<uni-view data-v-7144ea85="" class="over"> {{ o.name }} </uni-view>'
    '<uni-view data-v-7144ea85="" class="flex align-center margin-top-sm">'
    '<uni-view data-v-7144ea85="" class="round bg-orange flex align-center justify-center text-black" style="width: 20px; height: 20px;"><uni-text data-v-7144ea85="" class="cuIcon-cardboardfill"><span></span></uni-text></uni-view>'
    '<uni-view data-v-7144ea85="" class="text-black bg-orange padding-lr-sm flex align-center justify-center" style="height: 15px; margin-left: -2px; position: relative; z-index: 0; border-radius: 5px;"> #{{ o.token }} </uni-view>'
    '</uni-view>'
    '<uni-view data-v-7144ea85="" class="margin-top-xs"><uni-text data-v-7144ea85=""><span>￥</span></uni-text><uni-text data-v-7144ea85="" class="text-xl text-bold" style="font-family: new;"><span>{{ o.price }}</span></uni-text></uni-view>'
    '<uni-view data-v-7144ea85="" class="text-right text-sm text-gray"> {{ o.time }} </uni-view>'
    '</uni-view>'
    '</uni-view>'
    '</uni-view>'
    '</uni-view>'
    '<uni-view v-if="!rows.length" data-v-7144ea85="" class="empty-box"> 暂无数据 </uni-view>'
)
s = s[:i] + rows + s[j:]

script = '''
<script setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { pickOrders, UNPAID, PAID, CLOSED } from '@/mock/orders'
import { toast } from '@/utils/interact'

const router = useRouter()
const tabs = [UNPAID, PAID, CLOSED]
const tab = ref(0)

/** 只取常规交易这一类订单 */
const rows = computed(() => pickOrders('常规交易', [tabs[tab.value]]))

function tabName(status) {
  return status
}

function go(o) {
  if (o.status === UNPAID) {
    toast('订单 ' + o.no + ' 待支付，演示环境不真实扣款')
    return
  }
  toast('订单 ' + o.no + ' · ' + o.name)
}
</script>
'''
s = s.replace('\n</template>\n', '\n</template>\n' + script, 1)
io.open(P, 'w', encoding='utf-8').write(s)
print('MarketOrderList %d -> %d' % (orig, len(s)))


# ================= BidList.vue =================
P2 = 'src/views/account/BidList.vue'
s2 = io.open(P2, encoding='utf-8').read()
o2 = len(s2)

i = s2.find('<div class="uni-scroll-view-content">')
j = s2.find('</div></div></div></uni-scroll-view>', i)
assert i > 0 and j > i
new_tabs2 = (
    '<div class="uni-scroll-view-content">'
    '<uni-view v-for="(t, i) in tabs" :key="t" :data-id="i" class="cu-item text-gray flex-sub"'
    ' :class="tab === i ? \'text-bold text-black text-lg\' : \'\'"'
    ' @click="tab = i"> {{ t }} </uni-view>'
)
s2 = s2[:i] + new_tabs2 + s2[j:]

i = s2.find('<uni-view data-v-857ee3e0="" class="list margin-top-sm padding-bottom">')
j = s2.find('</template>', i)
assert i > 0 and j > i
rows2 = (
    '<uni-view data-v-857ee3e0="" class="list margin-top-sm padding-bottom">'
    '<uni-view v-for="o in rows" :key="o.id" class="bid-item padding-sm radius bg-grey margin-bottom-sm" @click="go(o)">'
    '<uni-view data-v-857ee3e0="" class="flex align-center justify-between">'
    '<uni-view data-v-857ee3e0="" class="over bid-name"> {{ o.name }} </uni-view>'
    '<uni-view data-v-857ee3e0="" class="bid-status" :class="statusClass(o.status)"> {{ o.status }} </uni-view>'
    '</uni-view>'
    '<uni-view data-v-857ee3e0="" class="flex align-center justify-between margin-top-sm">'
    '<uni-view data-v-857ee3e0="" class="text-sm text-gray"> 单号 {{ o.no }} · #{{ o.token }} </uni-view>'
    '<uni-view data-v-857ee3e0="" class="text-sm text-gray"> {{ o.time }} </uni-view>'
    '</uni-view>'
    '<uni-view data-v-857ee3e0="" class="margin-top-xs bid-price">￥{{ o.price }} <uni-text data-v-857ee3e0="" class="text-sm text-gray"><span>x{{ o.qty }}</span></uni-text></uni-view>'
    '</uni-view>'
    '</uni-view>'
    '<uni-view v-if="!rows.length" class="flex align-center justify-center" style="height: 50vh;">'
    '<uni-view class="text-center">'
    '<uni-image style="width: 90px; height: 80px;">'
    '<div style="background-image: url(&quot;/static/images/empty1.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>'
    '<img src="/static/images/empty1.png" draggable="false"></uni-image>'
    '<uni-view class="text-grey margin-top-xs"> 暂无数据 </uni-view>'
    '</uni-view></uni-view>'
)
s2 = s2[:i] + rows2 + s2[j:]

script2 = '''
<script setup>
import { computed, ref } from 'vue'
import { pickOrders, BIDDING, DONE, CLOSED, SOLD } from '@/mock/orders'
import { toast } from '@/utils/interact'

const tabs = ['全部', BIDDING, DONE, CLOSED, SOLD]
const tab = ref(0)

const statusMap = {
  全部: ['all'],
  求购中: [BIDDING],
  已成交: [DONE],
  已关闭: [CLOSED],
  已售出: [SOLD]
}

const rows = computed(() => {
  const pool = statusMap[tabs[tab.value]] || ['all']
  // 求购单与委托单都归到求购页展示
  const a = pool === ['all'] ? pickOrders('求购订单') : pickOrders('求购订单', pool)
  const b = pool === ['all'] ? pickOrders('委托订单') : pickOrders('委托订单', pool)
  return a.concat(b)
})

function statusClass(s) {
  if (s === BIDDING) return 'st-open'
  if (s === CLOSED) return 'st-closed'
  return 'st-done'
}

function go(o) {
  toast('求购单 ' + o.no + ' · ' + o.name)
}
</script>
'''
s2 = s2.replace('\n</template>\n', '\n</template>\n' + script2, 1)
io.open(P2, 'w', encoding='utf-8').write(s2)
print('BidList %d -> %d' % (o2, len(s2)))