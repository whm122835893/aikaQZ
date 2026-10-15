<template>
  <uni-view data-v-345a65e0="" class="login-page"><uni-view data-v-345a65e0="" class="hero-watermark-wrap" style="top: 12px;"><uni-image data-v-345a65e0="" class="hero-watermark"><div style="background-image: url(&quot;/static/images/login/2.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/images/login/2.png" draggable="false"></uni-image></uni-view><uni-view data-v-345a65e0="" class="login-body" style="padding-top: 24px;"><uni-view data-v-345a65e0="" class="page-header"><uni-view data-v-345a65e0="" class="back-btn"><uni-text data-v-345a65e0="" class="cuIcon-back"><span></span></uni-text></uni-view></uni-view><uni-view data-v-345a65e0="" class="hero-section"><uni-view data-v-345a65e0="" class="hero-text-wrap"><uni-image data-v-345a65e0="" class="hero-title-img" style="height: 82px;"><div style="background-image: url(&quot;/static/images/login/3.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/images/login/3.png" draggable="false"></uni-image></uni-view><uni-image data-v-345a65e0="" class="hero-illus" style="height: 154px;"><div style="background-image: url(&quot;/static/images/login/1.png&quot;); background-size: 100% 100%; background-repeat: no-repeat;"></div><img src="/static/images/login/1.png" draggable="false"></uni-image></uni-view><uni-view data-v-345a65e0="" class="form-section"><uni-view data-v-345a65e0="" class="input-box"><uni-image data-v-345a65e0="" class="input-icon"><div style="background-image: url(&quot;/static/images/login/6.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/images/login/6.png" draggable="false"></uni-image><uni-input data-v-345a65e0="" class="input-field"><div class="uni-input-wrapper"><div class="uni-input-placeholder input-placeholder" data-v-345a65e0="">请输入手机号</div><input maxlength="11" step="0.000000000000000001" enterkeyhint="done" pattern="[0-9]*" autocomplete="off" inputmode="numeric" type="number" class="uni-input-input" :value="phone" @input="set('phone', $event.target.value)"></div></uni-input></uni-view><uni-view data-v-345a65e0="" class="input-box input-box-code"><uni-image data-v-345a65e0="" class="input-icon"><div style="background-image: url(&quot;/static/images/login/7.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/images/login/7.png" draggable="false"></uni-image><uni-input data-v-345a65e0="" class="input-field input-field-code"><div class="uni-input-wrapper"><div class="uni-input-placeholder input-placeholder" data-v-345a65e0="">请输入验证码</div><input maxlength="6" step="0.000000000000000001" enterkeyhint="done" pattern="[0-9]*" autocomplete="off" inputmode="numeric" type="number" class="uni-input-input" :value="code" @input="set('code', $event.target.value)"></div></uni-input><uni-view data-v-345a65e0="" class="code-btn"><uni-view data-v-2b24c83b="" data-v-345a65e0="" class="captcha-wrap"><uni-view class="captcha-trigger" @click="sendCode">{{ left > 0 ? left + 's' : '获取验证码' }}</uni-view><uni-view data-v-2b24c83b="" id="netease-captcha-element" class="captcha-element"></uni-view></uni-view></uni-view></uni-view><uni-view data-v-345a65e0="" class="input-box"><uni-image data-v-345a65e0="" class="input-icon"><div style="background-image: url(&quot;/static/images/login/4.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/images/login/4.png" draggable="false"></uni-image><uni-input data-v-345a65e0="" class="input-field input-field-pwd"><div class="uni-input-wrapper"><div class="uni-input-placeholder input-placeholder" data-v-345a65e0="">请输入密码</div><input maxlength="15" step="" enterkeyhint="done" autocomplete="off" type="password" class="uni-input-input" :value="pwd" @input="set('pwd', $event.target.value)"></div></uni-input><uni-view data-v-345a65e0="" class="pwd-toggle"><uni-text data-v-345a65e0="" class="cuIcon-attentionforbid"><span></span></uni-text></uni-view></uni-view><uni-view data-v-345a65e0="" class="input-box"><uni-image data-v-345a65e0="" class="input-icon"><div style="background-image: url(&quot;/static/images/login/4.png&quot;); background-position: center center; background-size: contain; background-repeat: no-repeat;"></div><img src="/static/images/login/4.png" draggable="false"></uni-image><uni-input data-v-345a65e0="" class="input-field input-field-pwd"><div class="uni-input-wrapper"><div class="uni-input-placeholder input-placeholder" data-v-345a65e0="">请确认密码</div><input maxlength="15" step="" enterkeyhint="done" autocomplete="off" type="password" class="uni-input-input" :value="pwd2" @input="set('pwd2', $event.target.value)"></div></uni-input><uni-view data-v-345a65e0="" class="pwd-toggle"><uni-text data-v-345a65e0="" class="cuIcon-attentionforbid"><span></span></uni-text></uni-view></uni-view><uni-view class="login-btn" @click="submit">确认</uni-view></uni-view></uni-view></uni-view>
</template>

<script setup>
import { ref, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { toast, signIn, checkPhone, checkPassword, checkCode, DEMO_CODE, DEMO_PWD } from '@/utils/interact'

const router = useRouter()
const phone = ref('')
const code = ref('')
const pwd = ref('')
const pwd2 = ref('')
const left = ref(0)
let timer = null

/** 统一处理输入：按字段做字符过滤与长度截断 */
function set(k, v) {
  const map = {
    phone: (v) => { phone.value = String(v).replace(/\D/g, '').slice(0, 11) },
    code: (v) => { code.value = String(v).replace(/\D/g, '').slice(0, 6) },
    pwd: (v) => { pwd.value = String(v).slice(0, 20) },
    pwd2: (v) => { pwd2.value = String(v).slice(0, 20) },
  }
  if (map[k]) map[k](v)
}

function sendCode() {
  const e = checkPhone(phone.value)
  if (e) return toast(e)
  if (left.value > 0) return
  left.value = 60
  timer = setInterval(() => {
    left.value -= 1
    if (left.value <= 0) { clearInterval(timer); timer = null }
  }, 1000)
  toast('验证码已发送，演示 ' + DEMO_CODE)
}

function submit() {
  const e1 = checkPhone(phone.value)
  if (e1) return toast(e1)
  const e2 = checkCode(code.value)
  if (e2) return toast(e2)
  if (code.value !== DEMO_CODE) return toast('验证码错误，演示验证码为 ' + DEMO_CODE)
  const e3 = checkPassword(pwd.value)
  if (e3) return toast(e3)
  if (pwd.value !== pwd2.value) return toast('两次输入的密码不一致')
  signIn({ phone: phone.value, name: 'ICARD用户' + phone.value.slice(-4), time: Date.now() })
  toast('密码重置成功')
  setTimeout(() => router.replace('/pages/login/login'), 700)
}

onUnmounted(() => { if (timer) clearInterval(timer) })
</script>
