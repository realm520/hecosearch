import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VueRouter from 'vue-router'
import api from '@/api'
import InvitationReward from './components/InvitationReward';

Vue.config.productionTip = false
Vue.prototype.$api = api
api.setUrl("http://api.beerswap.vip/invitation_reward")
Vue.use(VueRouter)

const router = new VueRouter({
    routes: [
        { path: '/', component: InvitationReward }
    ]
})

new Vue({
    router,
    vuetify,
    render: h => h(App)
}).$mount('#app')
