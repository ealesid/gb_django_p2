import Vue from 'vue'
import Router from 'vue-router'

import PageMain from '../components/PageMain.vue'
import PageLogin from '../components/PageLogin.vue'

Vue.use(Router);

export default new Router({
  mode: 'history',

  routes: [
    { path: '/', name: 'main', component: PageMain },
    { path: '/login', name: 'login', component: PageLogin },
  ],
});
