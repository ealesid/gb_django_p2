<template>
  <div class="col s7 m9 l10 page-content">
    <div class="row">
      <div class="col s12">
        <div class="card ">
          <div class="card-content">
            <span class="card-title" v-if="user">Рады снова видеть Вас на нашем сайте</span>
            <div class="row">
              <div class="col s12 m4 l5">
                <div class="input-field">
                  <input id="email" type="email" class="validate" v-model="email" @change="fetchUser($event.target.value)">
                  <label for="email">Email:</label>
                </div>
              </div>
              <div class="col s12 m4 l5">
                <div class="input-field">
                  <input id="password" type="password" v-model="password">
                  <label for="password">Пароль</label>
                </div>
              </div>
              <div class="col s12 m4 l2">
                <div class="file-field input-field">
                  <div
                    :class="user || (email && password) ? 'btn' : 'btn disabled'"
                    @click="user ? getLoggedIn() : getRegisteredIn({email, password})"
                  >
                    {{ user || !(email && password) ? 'Войти' : 'Продолжить' }}
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="socials">Войти через: <a class="red-text hoverable"><i class="fa fa-google-plus-square fa-3x"></i></a></div>
            </div>
          </div>
          <div class="card-content" v-if="!user || !user.is_active">
            <template v-if="user">
              <p>Для завершения регистрации необходимо пройти по ссылке, отправленной на {{user.email}}</p>
              <hr>
              <router-link :to="{name: 'main'}" @click.native="userFetched(null)">На главную</router-link>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapMutations, mapState, } from 'vuex'
  import M from 'materialize-css'
  
  export default {
    computed: {
      ...mapState([ 'user', ]),
    },
    
    data() {
      return {
        email: '',
        password: '',
      }
    },
    
    methods: {
      ...mapActions([ 'fetchUser', 'getLoggedIn', 'getRegisteredIn', ]),
      ...mapMutations([ 'userFetched', ]),
    },
    
    created() {
      M.updateTextFields()
    }
  }
</script>

<style scoped>
  .page-content {
    margin-top: 20%;
  }
  .socials {
    text-align: center;
  }
  .socials > a {
    cursor: pointer;
    line-height: 3em;
  }
  i.fa {
    vertical-align: middle;
  }
</style>
