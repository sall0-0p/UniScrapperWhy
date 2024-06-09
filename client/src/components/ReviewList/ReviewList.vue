<script>
  import BlockHeader from './Header/Header.vue'
  import List from './List/List.vue'

  export default {
    components: {
      BlockHeader,
      List,
    },

    data() {
      return {
        searchValue: '',
        sortingMethod: 'By Alphabet',

        reviews: []
      }
    },

    props: {
      item: {
        type: Object,
        default: () => ({})
      }
    },

    methods: {
      updateSearch(value) {
        this.searchValue = value;
        this.arrangeItems();
      },

      changeSorting(value) {
        this.sortingMethod = value;
        this.arrangeItems();
      },
      
      arrangeItems() {
        this.reviews = this.item.content
      },
    },

    mounted() {
      this.arrangeItems()
      new Promise(resolve => setTimeout(resolve, 200)).then(() => {
        this.arrangeItems()
      });
    },
  }
</script>

<template>
  <!-- <p>Hello World!</p> -->
  <div class="content__block">
    <BlockHeader 
      @refresh-list="arrangeItems" 
      @update-search="updateSearch"
      @change-sorting="changeSorting"
      :itemsCount="reviews.length"
    />
    <List 
      @refresh-list="arrangeItems"
      :items="reviews"
    />
  </div>
</template>

<style scoped lang="scss">
  .content__block {
    background-color: var(--secondary-dark);
    margin: 10px;
    padding: 5px;
    border-radius: 10px;
    width: calc(100% - 30px);
  }
</style>