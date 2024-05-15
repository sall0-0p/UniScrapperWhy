<script>
  import { RouterLink } from 'vue-router';

  // export default {
  //   data() {
  //     logo: require('@/assets/images/cc_logo2.png')
  //   }
  // }
</script>

<template>
  <div class="header">
    <RouterLink to="/">
      <div class="icon"></div>
    </RouterLink>
  </div>
  
</template>

<style scoped>

  .header {
    display: flex;
    justify-content: center;
    align-items: center;

    width: 100%;
    height: var(--header-height);
  }

  .icon {
    background: center / contain url("@/assets/images/ceneo.png") no-repeat;
    width: 200px;
    height: 100px;
    outline: none;
    border: 0px solid;
  }
</style>