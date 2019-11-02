import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// 挂载axios
import axios from 'axios';
// 轮播图
// 搜索框
import Vant, {Lazyload, Search} from 'vant';
import 'vant/lib/index.css';

Vue.prototype.$http = axios;

Vue.config.productionTip = false

Vue.use(Vant);

// options 为可选参数，无则不传
Vue.use(Lazyload);

Vue.use(Search);


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
