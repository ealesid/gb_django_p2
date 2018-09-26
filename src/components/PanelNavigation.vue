<template>
    <div class="card col s5 m3 l2 nav-bar">
      <div class="card-image">
        <img src="/static/img/sample-1.jpg" alt="title">
        <span class="card-title">{{ title }}</span>
      </div>
      <div class="card-content">
        <div class="collection">
          <router-link class="collection-item" :to="{name: 'login'}"> Вход / Регистрация</router-link>
          <div class="collection-item">Фильтры по параметрам</div>
        </div>
      </div>
      <div class="card-action">
        <router-link :to="{name: 'main'}">На главную</router-link>
      </div>
    </div>
</template>

<script>
  export default {
    props: [ 'title', ],
  }
</script>

<style scoped>
  .card-content {
    padding: 0;
  }
  .collection {
    border: none;
  }
  .item-link:hover {
    background: #ddd;
    cursor: pointer;
  }
  .nav-bar {
    height: 99%;
    margin: 8px 0 0 0;
    padding: 0;
  }
</style>
