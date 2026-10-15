<template>
  <uni-view data-v-60259f7a class="address-page">
    <uni-view data-v-60259f7a class="hero-watermark-wrap" style="top: 12px;">
      <uni-image data-v-60259f7a class="hero-watermark">
        <div style="background-image: url(&quot;/static/images/login/2.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div>
        <img src="/static/images/login/2.png" alt="" draggable="false" />
      </uni-image>
    </uni-view>

    <uni-view data-v-60259f7a class="address-sticky-header" style="padding-top: 24px;">
      <uni-view data-v-60259f7a class="header">
        <uni-view data-v-60259f7a class="back-btn"><uni-text data-v-60259f7a class="cuIcon-back"><span></span></uni-text></uni-view>
        <uni-view data-v-60259f7a class="page-title">收货地址</uni-view>
        <uni-view data-v-60259f7a class="header-placeholder"></uni-view>
      </uni-view>
    </uni-view>

    <uni-scroll-view data-v-60259f7a class="address-scroll-body" style="top: 64px; height: 688px;">
      <div class="uni-scroll-view">
        <div class="uni-scroll-view" style="overflow: hidden auto;">
          <div class="uni-scroll-view-content">
            <uni-view v-if="rows.length" data-v-60259f7a>
              <uni-view
                v-for="a in rows"
                :key="a.id"
                data-v-60259f7a
                class="addr-card"
                @click="pick(a)"
              >
                <uni-view data-v-60259f7a class="addr-top">
                  <uni-view data-v-60259f7a class="addr-name">{{ a.name }}</uni-view>
                  <uni-view data-v-60259f7a class="addr-phone">{{ a.phone }}</uni-view>
                  <uni-view v-if="a.def" data-v-60259f7a class="addr-tag">默认</uni-view>
                </uni-view>
                <uni-view data-v-60259f7a class="addr-detail">{{ a.province }}{{ a.city }} {{ a.detail }}</uni-view>
                <uni-view data-v-60259f7a class="addr-ops">
                  <uni-view v-if="!a.def" data-v-60259f7a class="addr-op" @click.stop="setDefault(a)">设为默认</uni-view>
                  <uni-view data-v-60259f7a class="addr-op" @click.stop="edit(a)">编辑</uni-view>
                  <uni-view data-v-60259f7a class="addr-op danger" @click.stop="remove(a)">删除</uni-view>
                </uni-view>
              </uni-view>
            </uni-view>

            <uni-view
              v-else
              data-v-4d930ea0
              data-v-60259f7a
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

            <uni-view data-v-60259f7a class="list-bottom-space"></uni-view>
          </div>
        </div>
      </div>
    </uni-scroll-view>

    <uni-view data-v-60259f7a class="bottom-bar">
      <uni-view data-v-60259f7a class="add-btn" data-nav-to="/pages/address/add"> 添加收货地址 </uni-view>
    </uni-view>
  </uni-view>
</template>

<script setup>
/**
 * 收货地址列表
 * 源站只有骨架 + 永久「暂无数据」，底部「添加收货地址」按钮也没有任何绑定。
 * 克隆版补齐：3 条地址、设为默认 / 编辑 / 删除、点击选中、底部按钮跳新增页。
 */
import { ref } from 'vue'
import { toast } from '@/utils/interact'

const rows = ref([
  {
    id: 1,
    name: '王小明',
    phone: '138****8000',
    province: '浙江省杭州市西湖区',
    city: '',
    detail: '文三路 100 号 3 单元 502',
    def: true
  },
  {
    id: 2,
    name: '李小明',
    phone: '139****1234',
    province: '广东省深圳市南山区',
    city: '',
    detail: '科技园南路 8 号 A 座 1806',
    def: false
  },
  {
    id: 3,
    name: '张小红',
    phone: '137****5678',
    province: '上海市浦东新区',
    city: '',
    detail: '张江高科路 66 号 12 号楼',
    def: false
  }
])

function pick(a) {
  toast('已选择收货地址：' + a.name + ' ' + a.phone)
}

function setDefault(a) {
  rows.value.forEach((x) => { x.def = x.id === a.id })
  toast('已设为默认地址')
}

function edit(a) {
  toast('演示环境暂不支持编辑地址')
}

function remove(a) {
  rows.value = rows.value.filter((x) => x.id !== a.id)
  toast('已删除该地址')
}
</script>