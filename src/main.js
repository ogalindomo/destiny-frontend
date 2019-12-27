import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// import ImageUploader from 'vue-image-upload-resize'
Vue.config.productionTip = false

var app = new Vue({
  render: h => h(App)
});
Vue.use(BootstrapVue)
// Vue.use(ImageUploader)
app.$mount('#app'); 