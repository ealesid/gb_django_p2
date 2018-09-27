<template>
  <div class="col s7 m9 l10 page-content">
    <div class="row">
      <div class="col s12 m6 l3 product-item" v-for="product in products">
        <div class="card hoverable">
          <div class="card-image">
            <img :src="product.image">
            <!--<img src="/static/img/projector01.jpg">-->
            <a class="btn-floating halfway-fab waves-effect waves-light red"><i class="material-icons">add_shopping_cart</i></a>
          </div>
          <div class="card-content">
            <strong v-text="product.name"></strong>
            <p v-text="product.short_desc"></p>
          </div>
          <div class="card-action">
            <p>{{ product.price }}</p>
            <!--<a href="#">{{ product.price }}</a>-->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapState, } from 'vuex'
  
  export default {
    computed: {
      ...mapState([ 'products', ]),
    },
  }
</script>

<style scoped>
  .page-content {
    margin: 0.5rem 0 1rem 0;
  }
  .product-item {
    padding: 0 8px 8px 0;
  }
  .card {
    margin: 0;
  }
  .row {
    margin: 0;
  }
</style>
