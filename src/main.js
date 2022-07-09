import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import "@fortawesome/fontawesome-free/js/all";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.js";
import Notifications from '@kyvg/vue3-notification';
import PerfectScrollbar from 'vue3-perfect-scrollbar'
import 'vue3-perfect-scrollbar/dist/vue3-perfect-scrollbar.css'


createApp(App).use(store).use(router).use(Notifications).use(PerfectScrollbar).mount('#app')
