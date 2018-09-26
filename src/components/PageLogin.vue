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
              <!--<div class="socials">Войти через: <a class="red-text hoverable" @click="googleLogin"><i class="fa fa-google-plus-square fa-3x"></i></a></div>-->
              
              <div id="gSignInWrapper">
                <span class="label">Войти через: </span>
                <div id="customBtn" class="customGPlusSignIn hoverable">
                  <span class="icon"></span>
                  <!--<span class="buttonText">Google</span>-->
                </div>
              </div>
              <div id="name"></div>
            
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
      ...mapActions([ 'fetchUser', 'getLoggedIn', 'getRegisteredIn', 'startGoogleAuthApp', ]),
      ...mapMutations([ 'userFetched', ]),
    },
  
    mounted: function () {
      M.updateTextFields();
      this.startGoogleAuthApp();
    }
  }
</script>

<style scoped>
  .page-content {
    /*margin-top: 20%;*/
  }
  
  #customBtn {
    display: inline-block;
    background: white;
    color: #444;
    width: auto;
    border-radius: 5px;
    border: thin solid #888;
    /*box-shadow: 1px 1px 1px grey;*/
    white-space: nowrap;
  }
  #customBtn:hover {
    cursor: pointer;
  }
  span.label {
    margin-right: 10px;
  }
  span.icon {
    background: url('/static/img/g-normal.png') transparent 5px 50% no-repeat;
    display: inline-block;
    vertical-align: middle;
    width: 42px;
    height: 24px;
  }
  span.buttonText {
    display: inline-block;
    vertical-align: middle;
    padding-left: 0;
    padding-right: 8px;
    font-size: 14px;
    font-weight: bold;
    /* Use the Roboto font that is loaded in the <head> */
    font-family: 'Roboto', sans-serif;
  }

</style>
