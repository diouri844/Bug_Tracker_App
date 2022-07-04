import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import "@fortawesome/fontawesome-free/js/all";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.js";
import Notifications from '@kyvg/vue3-notification';


createApp(App).use(store).use(router).use(Notifications).mount('#app')
