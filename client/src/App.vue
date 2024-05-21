<script>
  import Sidebar from './components/Sidebar/Sidebar.vue'
  import { RouterView } from 'vue-router'

  export default {
    components: {
      Sidebar,
    },

    data() {
      return {
        selected: 'Home',
        items: [
          {
            name: 'Home',
            redirect: '/',
            icon: '../src/assets/images/clipboard.png',
          },
          // {
          //   name: 'Extract',
          //   redirect: '/list',
          //   icon: '../src/assets/images/banner_pattern.png',
          // },
        ],

        footerItems: [
          {
            name: 'About',
            redirect: '/about',
            icon: '../src/assets/images/goggles.png',
          },
        ],
      }
    },

    methods: {
      selectItem(name) {
        this.selected = name;
        document.title = `Scrapper: ${this.selected}`;
      },
    },

    mounted() {
      document.title = `Scrapper: ${this.selected}`;
    }
  }
</script>

<template>
  <div class="app-main-container">
    <div class="app-main-container__sidebar">
      <Sidebar
        :items="items"
        :footer-items="footerItems"
        :selected="selected"
        @select-item="selectItem"
      />
    </div>
    <RouterView  
      :selected="selected"
      class="app-main-container__right"
    />
  </div>
</template>

<style lang="scss">
  @import './assets/reset.css';
  @import './assets/variables.css';
  @import './assets/styles/shadows.css';
  @import 'floating-vue/dist/style.css';

  .app-main-container {
    display: flex;
    background-color: var(--primary-dark);
    
    &__right {
      margin-left: 270px;
      flex-grow: 1;
    }

    &__sidebar {
      position: fixed;
    }
  }

  .tooltip__text {
    font-family: var(--main-font);
    text-align: center;
    padding: 1px;
  }
</style>
