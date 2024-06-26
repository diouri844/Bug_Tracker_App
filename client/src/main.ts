import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import appRouter from './utils/router.config'

createApp(App)
.use(appRouter)
.mount('#app')
