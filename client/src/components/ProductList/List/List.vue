<script>
import ListItem from "./Item/Item.vue"

  export default {
    components: {
      ListItem,
    },

    data() {
      return {
        items: [
          {
            productName: 'Some Product',
            productId: '26538772',
            icon: '../src/assets/images/brass_hand.png',
            reviewCount: 20,
            rating: 0.8,
          },
          {
            productName: 'Another Product',
            productId: '15858488',
            icon: '../src/assets/images/brass_hand.png',
            reviewCount: 1546,
            rating: 0.6,
          },
          {
            productName: 'And Just Another Product BLA',
            productId: '35095301',
            icon: '../src/assets/images/brass_hand.png',
            reviewCount: 20,
            rating: 1,
          },
        ],
      }
    },
  }
</script>

<template>
  <div class="list">
    <ListItem 
      v-for="(item, index) in items"
      :key = item.productId
      :item = item
      :index = index
    />
  </div>
</template>

<style scoped lang="scss">
  .list {
    padding: 2.5px 5px 2.5px;
    background-color: var(--primary-dark);
    border-radius: 5px;
    margin-top: 5px;
  }
</style>