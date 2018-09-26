import Vue from 'vue'
import Vuex from 'vuex'

import * as actions from './actions'
import * as mutations from './mutations'

Vue.use(Vuex);

export default new Vuex.Store({
  actions,
  mutations,

  state: {
    client_id: '121471255218-ngm6pc28tmp1u3f800lpe0gri81iadqg.apps.googleusercontent.com',
    products: null,
    user: null,
  },
})
