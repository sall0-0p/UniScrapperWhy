<script>
  import BlockHeader from './Header/Header.vue'
  import List from './List/List.vue'

  export default {
    components: {
      BlockHeader,
      List,
    },
  }
</script>

<template>
  <!-- <p>Hello World!</p> -->
  <div class="content__block">
    <BlockHeader />
    <List />
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