import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'

export default defineConfig({
  plugins: [
    vue({
      template: {
        // 资源全部走 public 静态目录，禁止 vite 改写 src
        transformAssetUrls: false,
        compilerOptions: {
          // 保留原始换行，避免模板压缩空白后与源站文本排版不一致
          whitespace: 'preserve',
          // uni-app 自定义元素，按原生元素处理，以便直接复用原站 DOM 与样式
          isCustomElement: (tag) => tag.startsWith('uni-')
        }
      }
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    host: '0.0.0.0',
    port: 5173
  }
})
