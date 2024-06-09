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
        searchValue: '',
        sortingMethod: 'By Alphabet',

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
        this.searchValue = value;
        this.arrangeItems();
      },

      changeSorting(value) {
        this.sortingMethod = value;
        this.arrangeItems();
      },
      
      arrangeItems() {
        let rawItems = this.rawItems.filter((item) => {
          if (this.searchValue.length < 3) {
            return true;
          }

          if ((item.productName.toUpperCase()).includes(this.searchValue.toUpperCase()) || (item.productId) === this.searchValue) {
            return true;
          } else {
            return false;
          }
        });

        if (this.sortingMethod === 'By Alphabet') {
          this.items = rawItems.sort((a, b) => {
            if (a.productName < b.productName) {
              return -1;
            }
            if (a.productName > b.productName) {
              return 1;
            }
            return 0;
          });
        } else {
          this.items = rawItems.sort((a, b) => {
            if (a.reviewCount > b.reviewCount) {
              return -1;
            }
            if (a.reviewCount < b.reviewCount) {
              return 1;
            }
            
            // if same amount of reviews:
            if (a.productName < b.productName) {
              return -1;
            }
            if (a.productName > b.productName) {
              return 1;
            }
            return 0;
          });
        }
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
      @change-sorting="changeSorting"
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
    margin: 10px;
    padding: 5px;
    border-radius: 10px;
    width: calc(100% - 30px);
  }
</style>