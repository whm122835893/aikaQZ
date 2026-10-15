<template>
  <uni-view data-v-00f45480="" class="text-sm" style="padding-top: 0px;"><uni-view data-v-00f45480="" class="cu-bar flex justify-between"><uni-view data-v-00f45480="" class="action round padding justify-start" style="width: 25px; height: 25px;" data-nav-back><uni-view data-v-00f45480=""><uni-text data-v-00f45480="" class="cuIcon-back text-black"><span></span></uni-text></uni-view></uni-view><uni-view data-v-00f45480="" class="padding" style="font-weight: 400; font-size: 13px; color: rgb(0, 0, 0);"> {{ policy.title }} </uni-view></uni-view><uni-view style="padding: 16px 18px 40px; box-sizing: border-box;"><uni-text style="font-size: 15px; font-weight: 700; color: rgb(17, 17, 17);"><span>{{ policy.title }}</span></uni-text><uni-view style="margin-top: 6px; font-size: 12px; color: rgb(153, 153, 153);"><uni-text><span>更新日期：2026-10-06</span></uni-text></uni-view><uni-view style="margin-top: 18px; font-size: 13px; line-height: 2; color: rgb(66, 66, 66); text-align: justify;"><uni-view v-for="(p, i) in policy.paragraphs" :key="i" style="margin-bottom: 14px;"><uni-text><span>{{ i + 1 }}. {{ p }}</span></uni-text></uni-view></uni-view></uni-view></uni-view>
</template>

<script setup>
// 源站此页是通用 webview 容器，正文由 URL 参数传入的富文本渲染，
// 无参访问时内容区为空。这里放入平台隐私政策正文，样式沿用原页内联风格。
const policy = {
  title: 'ICARD爱卡隐私政策',
  paragraphs: [
    '我们深知个人信息对您的重要性，并会尽全力保护您的个人信息安全可靠。本政策依据《中华人民共和国个人信息保护法》编制，说明 icard 爱卡平台（以下简称“本平台”）如何收集、使用、存储和保护您的个人信息。',
    '本平台收集的信息包括：注册时提供的手机号、昵称与头像；使用收藏、寄售、合成、置换等功能时产生的订单与藏品记录；以及您主动上传的图片与评论内容。',
    '我们仅在实现上述功能所必需的范围内处理您的信息，不会用于与上述目的无关的场景，也不会向无关第三方出售您的个人信息。',
    '您可以在「我的 - 账号安全」中修改昵称、头像与钱包地址，在「我的 - 隐私政策」中查阅本政策全文。如需注销账号，可在「我的 - 设置」中提交注销申请。',
    '本声明为 ICARD 爱卡平台克隆演示版本的内容示例，不构成任何实际法律文件。'
  ]
}
</script>