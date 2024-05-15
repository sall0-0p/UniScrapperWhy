<script>
  export default {
    props: {
      selected: {
        type: String,
        default: '',
      },
    },
  }
</script>

<template>
  <div class="header shadow-m">
    <div class="header__left">
      <div class="title">
        {{ selected }}
      </div>
    </div>
  </div>
</template>

<style scoped>
  .header {
    display: flex;
    width: 100%;
    height: var(--header-height);
    z-index: 5;

    background-color: var(--secondary-dark);
  }
  .header__left {
    display: flex;
    align-items: center;
    justify-content: center;
    align-items: center;
    margin-left: 15px;
    margin-right: 15px;
  }
  .title {
    margin-left: 5px;
    margin-top: -1px;

    color: var(--primary-text);
    font-size: 20px;
    font-family: var(--main-font);
    font-weight: 300;
  }
</style>