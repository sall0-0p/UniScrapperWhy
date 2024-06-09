<script>
  import PageHeader from '../components/Header/Header.vue';
  import ProductRepository from '@/domain/ProductsRepository';
  import Product from '@/components/Product/Product.vue';
  import ReviewList from "@/components/ReviewList/ReviewList.vue"

  export default {
    components: {
      PageHeader,
      Product,
      ReviewList,
    },

    data() {
      return {
        repository: new ProductRepository('http://127.0.0.1:5000'),

        productId: this.$route.params.productId,
        item: {},
        meta: {},
        reviews: {},
      }
    },

    methods: {
      async fetchAll() {
        const responce = await this.repository.getProductData(this.productId);
        const rawJSON = await responce.json();
        this.item = await JSON.parse(rawJSON);
      }
    },

    mounted()  {
      this.fetchAll()
      
    },
  }
  
</script>

<template>
  <div class='main'>
    <PageHeader
        selected="Product Overview"
    />

    <Product
      :item="item"
      @update-item="fetchAll"
    />

    <ReviewList
      :item="item"
      @update-item="fetchAll"
    >
    </ReviewList>
  </div>
</template>

<style scoped lang="scss">
  
</style>