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
    background: center / contain url("@/assets/images/cookie.png") no-repeat;
    height: calc(var(--header-height) - 10px);
    width: calc(var(--header-height) - 10px);
    margin: 15px 25px 15px;
  }
</style>