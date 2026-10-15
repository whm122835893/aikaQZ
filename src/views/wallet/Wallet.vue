<template>
  <uni-view data-v-d64374fc="" class="wallet-page" style="padding-top: 0px;"><uni-view data-v-d64374fc="" class="header"><uni-view data-v-d64374fc="" class="back-btn"><uni-text data-v-d64374fc="" class="cuIcon-back"><span></span></uni-text></uni-view><uni-view data-v-d64374fc="" class="page-title">我的钱包</uni-view><uni-view data-v-d64374fc="" class="header-placeholder"></uni-view></uni-view><uni-view data-v-d64374fc="" class="wallet-card" data-nav-to="/pages/wallet/thirdWallet"><uni-view data-v-d64374fc="" class="wallet-tag">默认</uni-view></uni-view><uni-view data-v-d64374fc="" class="wallet-card1" data-nav-to="/pages/wallet/wallet1"></uni-view><uni-view style="margin-top: 14px; background: #fff; border-radius: 12px; padding: 14px; box-sizing: border-box;"><uni-view data-v-d64374fc="" class="wallet-info"><uni-view data-v-d64374fc="" class="wallet-name">钱包地址</uni-view><uni-view data-v-d64374fc="" class="wallet-desc">{{ wallet.address }}</uni-view></uni-view><uni-view data-v-d64374fc="" class="wallet-info" style="margin-top: 14px;"><uni-view data-v-d64374fc="" class="wallet-name">资产概览</uni-view><uni-view data-v-d64374fc="" class="wallet-desc">可用余额 ¥{{ wallet.balance }}<br />累计收益 ¥{{ wallet.income }}<br />冻结金额 ¥{{ wallet.frozen }}</uni-view></uni-view><uni-view class="wallet-btn" style="position: static; text-align: right; margin-top: 14px;" data-nav-to="/pages/wallet/wallet1">查看明细</uni-view></uni-view></uni-view>
</template>

<script setup>
import { WALLET } from '@/mock/data'

// 源站此页依赖登录态的钱包接口，未登录时只剩一张空卡壳。
// 钱包卡自身的文案（汇付支付 / 易宝支付 / 进入钱包）已烤进背景图
// have.png 与 no.png，因此这里不再叠加文字，只补上卡片点击跳转与资产信息。
const wallet = WALLET
</script>