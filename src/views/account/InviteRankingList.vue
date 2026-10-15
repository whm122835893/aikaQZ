<template>
  <uni-view data-v-fbc8017c class="container">
    <uni-view data-v-fbc8017c class="flex align-center justify-between padding">
      <uni-view data-v-fbc8017c class="text-xl bg-blue padding-lr-xs round"><uni-text data-v-fbc8017c class="cuIcon-back"><span></span></uni-text></uni-view>
    </uni-view>

    <uni-view data-v-fbc8017c class="flex align-center justify-between padding-left-xl">
      <uni-view data-v-fbc8017c class="box1 padding radius">
        <uni-view data-v-fbc8017c class="text-xl text-white text-bold"> 排行榜 </uni-view>
        <uni-view data-v-fbc8017c class="text-blue text-sm text-black"> {{ myRankText }} </uni-view>
      </uni-view>
      <uni-image data-v-fbc8017c style="width: 190px; height: 244px;">
        <div style="background-image: url(&quot;/static/images/in_text2.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div>
        <img src="/static/images/in_text2.png" alt="" draggable="false" />
      </uni-image>
    </uni-view>

    <uni-view data-v-fbc8017c class="padding-lr" style="margin-top: -50px;">
      <uni-view data-v-fbc8017c class="margin-top radius padding box1 text-white">
        <uni-view data-v-fbc8017c class="flex align-center justify-between">
          <uni-view data-v-fbc8017c class="text-xl text-bold"> 排行榜 </uni-view>
          <uni-view data-v-fbc8017c class="text-sm"> 更新时间:{{ updateTime }} </uni-view>
        </uni-view>
        <uni-view data-v-fbc8017c class="margin-top">
          <uni-view data-v-fbc8017c class="gird3 text-center margin-bottom-sm">
            <uni-view data-v-fbc8017c> 排名 </uni-view>
            <uni-view data-v-fbc8017c> 用户昵称 </uni-view>
            <uni-view data-v-fbc8017c> 数量 </uni-view>
          </uni-view>
          <uni-scroll-view data-v-fbc8017c style="height: 400px;">
            <div class="uni-scroll-view">
              <div class="uni-scroll-view" style="overflow: hidden auto;">
                <div class="uni-scroll-view-content">
                  <uni-view data-v-fbc8017c>
                    <uni-view
                      v-for="r in rows"
                      :key="r.rank"
                      data-v-fbc8017c
                      class="gird3 text-center margin-bottom-sm rank-row"
                      :class="{ 'rank-me': r.me }"
                    >
                      <uni-view data-v-fbc8017c class="rank-no">{{ r.rank }}</uni-view>
                      <uni-view data-v-fbc8017c class="rank-name">{{ r.name }}</uni-view>
                      <uni-view data-v-fbc8017c class="rank-num">{{ r.num }}</uni-view>
                    </uni-view>
                  </uni-view>
                </div>
              </div>
            </div>
          </uni-scroll-view>
        </uni-view>
      </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
/**
 * 邀请排行榜（account/InviteRankingList）
 * 源站只有「我的排名：未上榜」+ 空的三列栅格 + 永不显示的「暂无数据」占位。
 * 克隆版补齐：10 条排行数据，当前用户排在第 7 位并高亮。
 */
import { computed, ref } from 'vue'
import { authUser } from '@/utils/interact'

const updateTime = '2026-10-7'

const NAMES = ['星辰大海', '墨白', '一叶知秋', '喵星人', '南山南', '风起时', '青衫故人', '半糖', '长风', '拾光']
const NUMS = [1286, 964, 812, 733, 690, 574, 486, 402, 351, 297]

/** 当前登录用户的排名：由手机号末位派生，保证同一账号每次一致；未登录为 null */
const myRank = computed(() => {
  const u = authUser.value
  if (!u) return null
  return (String(u.phone || '13800138000').slice(-1).charCodeAt(0) % 10) + 1
})

/** 榜单：第 myRank 名显示为「我」并高亮 */
const rows = computed(() =>
  NUMS.map((num, i) => ({
    rank: i + 1,
    name: i + 1 === myRank.value ? '我' : NAMES[i],
    num,
    me: i + 1 === myRank.value
  }))
)

const myRankText = computed(() =>
  myRank.value ? `我的排名：第 ${myRank.value} 名` : '我的排名：未上榜'
)
</script>