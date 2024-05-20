<script>
  import BlockHeader from './Header/Header.vue'
  import List from './List/List.vue'
  import ProductRepository from "@/domain/ProductsRepository";

  export default {
    components: {
      BlockHeader,
      List,
    },

    data() {
      return {
        repository: new ProductRepository('http://127.0.0.1:5000'), // TODO: replace with .env constraint
        search_value: '',

        items: [

        ],

        rawItems: [
          
        ],
      }
    },

    mounted() {
      this.fetchAll();
    },

    methods: {
      updateSearch(value) {
        console.log(value)
        this.search_value = value
        this.arrangeItems()
      },
      
      arrangeItems() {

        let rawItems = this.rawItems.filter((item) => {
          if (this.search_value.length < 3) {
            return true
          }

          if ((item.productName.toUpperCase()).includes(this.search_value.toUpperCase()) || (item.productId) === this.search_value) {
            return true
          } else {
            return false
          }
        })

        this.items = rawItems.sort((a, b) => {
          if (a.reviewCount > b.reviewCount) {
            return -1;
          }
          if (a.reviewCount < b.reviewCount) {
            return 1;
          }
          return 0;
        })
      },

      async fetchAll() {
        const rawJSON = await this.repository.getProductList(true)
        console.log(rawJSON)
        this.rawItems = await JSON.parse(rawJSON);
        this.arrangeItems()
      },
    },
  }
</script>

<template>
  <!-- <p>Hello World!</p> -->
  <div class="content__block">
    <BlockHeader 
    @refresh-list="fetchAll" 
    @update-search="updateSearch"
    :itemsCount="items.length"
    />
    <List 
      @refresh-list="fetchAll"
      :items="items"
    />
  </div>
</template>

<style scoped lang="scss">
  .content__block {
    background-color: var(--secondary-dark);
    margin: 15px;
    padding: 5px;
    border-radius: 10px;
    width: calc(100% - 30px);
  }
</style>