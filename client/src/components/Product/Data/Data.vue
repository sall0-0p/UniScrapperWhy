<script>
  export default {
    props: {
      item: {
        type: Object,
        default: () => ({}),
      },
    },
  }
</script>

<template>
  <div class="wrapper">
    <div>
      <h2 class="product__title">{{ item.meta?.productName || "Loading..." }}</h2>
      <h1 class="product__tags">{{ item.meta?.tags }}</h1>
    </div>
    <div class="wrapper">
      <div class="tag">
        <a :href="`https://ceneo.pl/${item.meta?.productId}`">
          {{ this.item?.meta?.price + 'zl'}}
        </a>
      </div>
      <!-- <div class="tag">
        {{ this.item?.meta?.productId }}
      </div> -->
    </div>
  </div>
</template>

<style scoped lang="scss">
  .wrapper {
    display: flex;
    
    &__right {
      background-color: var(--secondary-light);
      width: 25%;
      margin-left: 5px;
      padding: 5px;
      border-radius: 5px;
      aspect-ratio: 2/1.5;

      display: flex;
      justify-content: center;
      align-items: center;
    }

    &__left {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    &__between {
      justify-content: space-between;
    }
  }

  .product {
    &__title {
      padding: 8px;
      padding-bottom: 10px;
      font-size: 23px;
      font-family: var(--main-font);
      color: var(--primary-text);
      background-color: var(--secondary-light);
      border-radius: 5px;
    }

    &__tags {
      margin: 5px 0px 5px;
      padding: 5px 5px 5px;
      width: 70%;
      color: var(--secondary-text);
      font-family: var(--main-font);
      font-weight: 100;

      border-left: 5px solid var(--secondary-light);
    }
  }

  .tag {
    margin-right: 5px;
    padding: 5px 10px;
    border-radius: 5px;
    background-color: var(--secondary-light);
    color: var(--primary-text);
    white-space: nowrap;
    text-align: center;
    font-weight: 400;

    font-family: var(--main-font);
    font-size: 20px;
    width: fit-content;
  }
</style>