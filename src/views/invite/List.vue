<template>
  <uni-view data-v-42c514b8 class="invite-list-page">
    <uni-view data-v-42c514b8 class="invite-list-sticky-header">
      <uni-view data-v-42c514b8 class="tab-row padding-lr">
        <uni-view
          v-for="(t, i) in tabs"
          :key="t"
          data-v-42c514b8
          class="text-center radius flex tab_item text-grey align-center justify-center"
          :class="tab === i ? 'text-bold text-black' : ''"
          @click="tab = i"
        >
          {{ t }}
          <uni-view data-v-42c514b8 class="line"></uni-view>
        </uni-view>
      </uni-view>
    </uni-view>

    <uni-scroll-view data-v-42c514b8 class="invite-list-scroll-body" style="top: 40px; height: 658px;">
      <div class="uni-scroll-view">
        <div class="uni-scroll-view" style="overflow: hidden auto;">
          <div class="uni-scroll-view-content">
            <uni-view data-v-42c514b8 class="list-wrap padding-lr">
              <uni-view
                v-for="o in rows"
                :key="o.id"
                data-v-42c514b8
                class="inv-item"
                @click="openDetail(o)"
              >
                <uni-view data-v-42c514b8 class="inv-left">
                  <uni-view data-v-42c514b8 class="inv-avatar">{{ o.name.slice(0, 1) }}</uni-view>
                  <uni-view data-v-42c514b8 class="inv-info">
                    <uni-view data-v-42c514b8 class="inv-name">{{ o.name }}</uni-view>
                    <uni-view data-v-42c514b8 class="inv-phone">{{ o.phone }}</uni-view>
                  </uni-view>
                </uni-view>
                <uni-view data-v-42c514b8 class="inv-right">
                  <uni-view data-v-42c514b8 class="inv-state" :class="stateClass(o.state)">{{ o.state }}</uni-view>
                  <uni-view data-v-42c514b8 class="inv-time">{{ o.time }}</uni-view>
                  <uni-view v-if="o.reward" data-v-42c514b8 class="inv-reward">+{{ o.reward }} 积分</uni-view>
                </uni-view>
              </uni-view>

              <uni-view
                v-if="!rows.length"
                data-v-4d930ea0
                data-v-42c514b8
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

              <uni-view data-v-42c514b8 class="list-bottom-space"></uni-view>
            </uni-view>
          </div>
        </div>
      </div>
    </uni-scroll-view>

    <uni-view data-v-42c514b8 class="bottom_nav padding bg-white flex align-center justify-center">
      <uni-view data-v-42c514b8 class="cu-btn radius bg-grey flex-sub" style="height: 40px;" data-nav-to="/pages/account/invite"> 去邀请 </uni-view>
    </uni-view>

    <!-- 邀请详情弹层 -->
    <uni-view data-v-42c514b8 class="cu-modal bottom-modal" :class="{ show: !!detail }">
      <uni-view data-v-42c514b8 class="cu-dialog bg-white inv-sheet">
        <uni-view data-v-42c514b8 class="inv-sheet-title">邀请详情</uni-view>
        <uni-view v-if="detail" data-v-42c514b8 class="inv-sheet-body">
          <uni-view data-v-42c514b8 class="inv-row"><uni-text data-v-42c514b8><span>好友</span></uni-text><uni-text data-v-42c514b8 class="inv-row-v"><span>{{ detail.name }}</span></uni-text></uni-view>
          <uni-view data-v-42c514b8 class="inv-row"><uni-text data-v-42c514b8><span>手机号</span></uni-text><uni-text data-v-42c514b8 class="inv-row-v"><span>{{ detail.phone }}</span></uni-text></uni-view>
          <uni-view data-v-42c514b8 class="inv-row"><uni-text data-v-42c514b8><span>注册时间</span></uni-text><uni-text data-v-42c514b8 class="inv-row-v"><span>{{ detail.time }}</span></uni-text></uni-view>
          <uni-view data-v-42c514b8 class="inv-row"><uni-text data-v-42c514b8><span>状态</span></uni-text><uni-text data-v-42c514b8 class="inv-row-v"><span>{{ detail.state }}</span></uni-text></uni-view>
          <uni-view data-v-42c514b8 class="inv-row"><uni-text data-v-42c514b8><span>奖励</span></uni-text><uni-text data-v-42c514b8 class="inv-row-v strong"><span>{{ detail.reward ? '+' + detail.reward + ' 积分' : '待发放' }}</span></uni-text></uni-view>
        </uni-view>
        <uni-view data-v-42c514b8 class="inv-sheet-footer">
          <uni-view data-v-42c514b8 class="inv-sheet-btn" @click="detail = null">关闭</uni-view>
        </uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
/**
 * 分享/邀请记录（invite/List）
 * 源站只有 2 个 Tab + 永久「暂无数据」，底部「去邀请」按钮也无绑定。
 * 克隆版补齐：2 Tab 过滤 + 8 条邀请记录 + 详情弹层 + 底部按钮跳邀请页。
 */
import { computed, ref } from 'vue'

const tabs = ['分享中', '分享成功']
const tab = ref(0)
const detail = ref(null)

const ING = '分享中'
const OK = '分享成功'

const NAMES = ['陈小美', '刘子豪', '赵一诺', '孙浩然', '周雅静', '吴俊杰', '郑思远', '冯雨萱']

const rows = computed(() => {
  const want = tab.value === 0 ? ING : OK
  return [0, 1, 2, 3, 4, 5, 6, 7]
    .map((i) => ({
      id: 90000 + i,
      name: NAMES[i],
      phone: '1' + String(38 + (i % 5)) + '****' + String(1000 + i * 137).slice(0, 4),
      time: `2026-0${9 - (i % 3)}-${String(28 - i * 2).padStart(2, '0')} ${String(9 + i).padStart(2, '0')}:${String(12 + i * 3).slice(0, 2)}`,
      state: i % 2 === 0 ? OK : ING,
      reward: i % 2 === 0 ? 100 + i * 20 : 0
    }))
    .filter((o) => o.state === want)
})

function stateClass(s) {
  return s === OK ? 'st-done' : 'st-ing'
}

function openDetail(o) {
  detail.value = o
}
</script>