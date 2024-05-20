<script>
  import ListItem from "./Item/Item.vue";

  export default {
    components: {
      ListItem,
    },

    data() {
      return {
        items: [],
      }
    },

    props: {
      items: {
        type: Array,
        default: [],
      },
    },

    methods: {
      fetchAll() {
        this.$emit('refresh-list')
      },
    }
  }
</script>

<template>
  <div class="list">
    <TransitionGroup name="list" tag="div">
      <ListItem 
        v-for="item in items"
        :key = item.productId
        :item = item
        :index = index
        @refresh-list="fetchAll"
      />
    </TransitionGroup>
  </div>
</template>

<style scoped lang="scss">
  .list {
    padding: 2.5px 5px 2.5px;
    background-color: var(--primary-dark);
    border-radius: 5px;
    margin-top: 5px;
  }

  .list-enter-active,
  .list-leave-active {
    transition: all 0.5s ease;
  }
  .list-enter-from,
  .list-leave-to {
    opacity: 0;
    transform: translateX(30px);
  }

</style>