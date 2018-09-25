<template>
  <div class="row">
    <panel-navigation :title="name"/>
      <div>
        <transition name="fade" mode="out-in">
            <router-view />
        </transition>
      </div>
  </div>
</template>

<script>
  import { mapActions, } from 'vuex'
  import PanelNavigation from './components/PanelNavigation.vue'
  
  export default {
    data() {
      return {
        name: 'Movie Light'
      }
    },
    
    methods: {
      ...mapActions([ 'fetchProducts' ]),
    },
    
    components: {
      PanelNavigation,
    },
    
    created() {
      this.fetchProducts();
    },
  }
</script>

<style scoped>
  .row {
    height:100%;
    background: ghostwhite;
    margin: 0;
    padding: 0 8px;
  }
  
  .fade-enter {
    opacity: 0;
  }
  .fade-enter-active {
    transition: opacity 1s;
  }
  .fade-leave {
    /*opacity: 1;*/
  }
  .fade-leave-active {
    transition: opacity .5s;
    opacity: 0;
  }
</style>
