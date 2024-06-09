<script>
  import ProductData from './Data/Data.vue';
  
  export default {
    components: {
      ProductData,
    },
    
    props: {
      item: {
        type: Object,
        default: () => ({}),
      },
    },
    
    computed: {
      buildImage() {
        return `background: center / contain no-repeat url("${this.item?.meta?.icon || '../src/assets/images/barrier.png'}")`
      },
    }
  }
</script>

<template>
    <div class="content__block">
      <div class="wrapper wrapper__between">
        <ProductData 
          class="wrapper__left" 
          :item="item"
        
        />

        <div class="wrapper__right">
          <div class="image-container">
            <div 
              class="image-container__image"
              :style="buildImage"
            > 
            </div>
          </div>
        </div>
      </div>
    </div>

</template>

<style scoped lang="scss">
  .content__block {
    background-color: var(--secondary-dark);
    margin: 10px 10px 0px;
    padding: 5px;
    border-radius: 10px;
  }

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

  .image-container {
    background: rgb(255, 255, 255);
    height: calc(100% - 4px);
    width: calc(100% - 4px);

    border-radius: 5px;

    display: flex;
    justify-content: center;
    align-items: center;

    &__image {
      height: calc(100% - 16px);
      aspect-ratio: 1/1;
      object-fit: contain;
      image-rendering: pixelated;
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