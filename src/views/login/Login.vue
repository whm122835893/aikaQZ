<template>
  <uni-view data-v-03685db7="" class="login-page"><uni-view data-v-03685db7="" class="hero-watermark-wrap" style="top: 12px;"><uni-image data-v-03685db7="" class="hero-watermark"><div style="background-image: url(&quot;/static/images/login/2.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/images/login/2.png" draggable="false"></uni-image></uni-view><uni-view data-v-03685db7="" class="login-body" style="padding-top: 24px;"><uni-view data-v-03685db7="" class="hero-section"><uni-view data-v-03685db7="" class="hero-text-wrap"><uni-image data-v-03685db7="" class="hero-title-img" style="height: 82px;"><div style="background-image: url(&quot;/static/images/login/3.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/images/login/3.png" draggable="false"></uni-image></uni-view><uni-image data-v-03685db7="" class="hero-illus"><div style="background-image: url(&quot;/static/images/login/1.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/images/login/1.png" draggable="false"></uni-image></uni-view><uni-view data-v-03685db7="" class="form-section"><uni-view data-v-03685db7="" class="input-box"><uni-image data-v-03685db7="" class="input-icon"><div style="background-image: url(&quot;/static/images/login/6.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/images/login/6.png" draggable="false"></uni-image><uni-input data-v-03685db7="" class="input-field"><div class="uni-input-wrapper"><div class="uni-input-placeholder input-placeholder" data-v-03685db7="">请输入账号</div><input maxlength="11" step="0.000000000000000001" enterkeyhint="done" pattern="[0-9]*" autocomplete="off" inputmode="numeric" type="number" class="uni-input-input" :value="phone" @input="set('phone', $event.target.value)"></div></uni-input></uni-view><uni-view data-v-03685db7="" class="input-box"><uni-image data-v-03685db7="" class="input-icon"><div style="background-image: url(&quot;/static/images/login/4.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/images/login/4.png" draggable="false"></uni-image><uni-input data-v-03685db7="" class="input-field input-field-pwd"><div class="uni-input-wrapper"><div class="uni-input-placeholder input-placeholder" data-v-03685db7="">请输入密码</div><input maxlength="15" step="" enterkeyhint="done" autocomplete="off" type="password" class="uni-input-input" :value="pwd" @input="set('pwd', $event.target.value)"></div></uni-input><uni-view data-v-03685db7="" class="pwd-toggle"><uni-text data-v-03685db7="" class="cuIcon-attentionforbid"><span></span></uni-text></uni-view></uni-view><button id="" class="login-btn" @click="submit"> 登录 </button><uni-view data-v-03685db7="" class="link-row"><uni-text class="link-text" @click="toReg"><span> 注册账号 </span></uni-text><uni-text class="link-text" @click="toCode"><span> 验证码登录 </span></uni-text><uni-text class="link-text" @click="toForget"><span> 忘记密码? </span></uni-text></uni-view></uni-view><uni-view data-v-03685db7="" class="agreement-bar"><uni-view data-v-03685db7="" class="agreement-check"><uni-view data-v-03685db7="" class="check-box checked"><uni-text data-v-03685db7="" class="cuIcon-check"><span></span></uni-text></uni-view></uni-view><uni-view data-v-03685db7="" class="agreement-text"><uni-text data-v-03685db7="" class="agreement-normal"><span>我已阅读并同意</span></uni-text><uni-text class="agreement-link" @click="toAgree"><span>《用户协议》</span></uni-text><uni-text data-v-03685db7="" class="agreement-link"><span>，</span></uni-text><uni-text class="agreement-link" @click="toAgree"><span>《隐私政策》</span></uni-text></uni-view></uni-view></uni-view></uni-view>
</template>

<script setup>
import { ref, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { toast, signIn, checkPhone, checkPassword, checkCode, DEMO_CODE, DEMO_PWD } from '@/utils/interact'

const router = useRouter()
const phone = ref('')
const pwd = ref('')

/** 统一处理输入：按字段做字符过滤与长度截断 */
function set(k, v) {
  const map = {
    phone: (v) => { phone.value = String(v).replace(/\D/g, '').slice(0, 11) },
    pwd: (v) => { pwd.value = String(v).slice(0, 20) },
  }
  if (map[k]) map[k](v)
}

function submit() {
  const e1 = checkPhone(phone.value)
  if (e1) return toast(e1)
  const e2 = checkPassword(pwd.value)
  if (e2) return toast(e2)
  if (pwd.value !== DEMO_PWD) return toast('密码错误，演示密码为 ' + DEMO_PWD)
  signIn({ phone: phone.value, name: 'ICARD用户' + phone.value.slice(-4), time: Date.now() })
  toast('登录成功')
  setTimeout(() => router.replace('/pages/home/home'), 700)
}

function toReg() { router.push('/pages/login/register') }
function toCode() { toast('演示环境仅支持密码登录') }
function toForget() { router.push('/pages/login/forget') }
function toAgree() { toast('演示环境无协议页') }
</script>
