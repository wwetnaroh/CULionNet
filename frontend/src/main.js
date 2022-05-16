import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Element from 'element-plus'
import VueCookies from 'vue3-cookies'
import axios from 'axios'
import 'element-plus/dist/index.css'
// import * as ElIconModules from '@element-plus/icons'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.js'

const app=createApp(App)
app.use(router)
app.use(Element)
app.use(VueCookies)
router.beforeEach((to, from, next) => {
  /* 路由发生变化修改页面title */
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})
app.mount('#app')