<template>
  <uni-view data-v-f3269ace="" class="third-wallet-page"><uni-view data-v-f3269ace="" class="nav-bar" style="padding-top: 0px; height: 44px;"><uni-view data-v-f3269ace="" class="nav-back"><uni-view data-v-f3269ace="" class="back-arrow"></uni-view></uni-view><uni-view data-v-f3269ace="" class="nav-title">汇付钱包</uni-view><uni-view data-v-f3269ace="" class="nav-placeholder"></uni-view></uni-view><uni-view data-v-f3269ace="" class="wallet-frame-wrap" style="top: 44px;"><uni-view style="padding: 60px 24px 0; box-sizing: border-box;"><uni-view style="background: #f7f8fa; border-radius: 12px; padding: 18px 16px; box-sizing: border-box;"><uni-view style="font-size: 15px; font-weight: 600; color: #111;">汇付钱包</uni-view><uni-view style="margin-top: 8px; font-size: 13px; color: #999; line-height: 1.7;">该页面在源站是通过内嵌 iframe 拉起汇付钱包的收银台，需要真实商户号与登录态才能加载。克隆版本地环境无法访问该第三方页面，此处保留原版式的说明卡。</uni-view><uni-view style="margin-top: 16px; font-size: 13px; color: #666; line-height: 1.9;">·&nbsp;钱包地址　{{ wallet.address }}<br />·&nbsp;可用余额　¥{{ wallet.balance }}<br />·&nbsp;累计收益　¥{{ wallet.income }}<br />·&nbsp;冻结金额　¥{{ wallet.frozen }}</uni-view></uni-view></uni-view></uni-view></uni-view>
</template>

<script setup>
import { WALLET } from '@/mock/data'

// 源站此处是一个 wallet-iframe（第三方收银台），无网/ 无商户号时加载为空白。
// 保留 wallet-frame-wrap 这个定位容器，内部换成可读的说明卡。
const wallet = WALLET
</script>