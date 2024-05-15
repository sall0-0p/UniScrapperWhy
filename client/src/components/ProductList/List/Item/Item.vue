<script>
  import Icon from '../../Icon/Icon.vue'
  import ItemButton from '../../Button/Button.vue'

  export default {
    components: {
      Icon,
      ItemButton,
    },

    props: {
      item: {
        type: Object,
        default: () => ({}),
      },

      index: {
        type: String,
        default: '00000000',
      }
    },

    computed: {
      formatRating() {
        let numberOfStars = Math.round(this.item.rating / 0.2);
        return "★".repeat(numberOfStars) + "☆".repeat(5 - numberOfStars);
      },
    },

    mounted: function() {
      console.log(this.item);
      console.log(typeof(this.item));
    }
  }
</script>

<template>
  <div class="item">
      <div class="sub label__title">
        <Icon 
          :img="item.icon || '../assets/images/barrier.png'"
          size="30px"
        />
        <routerLink
          class="item__title"
          :to="{
              name: 'product',
              params: {
                productId: item.productId,
              },
          }"
        >
          {{ item.productName }}
        </routerLink>
      </div>
    <div class="item__label label__id">
      <VTooltip>
        <p>{{ item.productId }}</p>
      
        <template #popper>
          <p class="tooltip__text">
            Product Id
          </p>
        </template>
      </VTooltip>
    </div>

    <div class="item__label label__id">
      <VTooltip>
        <p>{{ item.reviewCount }}</p>
      
        <template #popper>
          <p class="tooltip__text">
            Number of Reviews
          </p>
        </template>
      </VTooltip>
    </div>

    <div class="item__label label__count">
      <VTooltip>
        <p>{{ formatRating }}</p>
      
        <template #popper>
          <p class="tooltip__text">
            Product Rating
          </p>
        </template>
      </VTooltip>
    </div>

    <div class="sub label__buttons">
      <VTooltip>
        <ItemButton 
          img="../src/assets/images/bundle.png" 
          size="25px" 
          icon_size="25px" 
          rectangular=true 
        />

        <template #popper>
          <p class="tooltip__text">
            Redownload
          </p>
        </template>
      </VTooltip>
      <VTooltip>
        <ItemButton 
          img="../src/assets/images/bucket_lava.png" 
          size="25px" 
          icon_size="25px" 
          rectangular=true 
        />

        <template #popper>
          <p class="tooltip__text">
            Delete item
          </p>
        </template>
      </VTooltip>
    </div>
  </div>
</template>

<style scoped lang="scss">
  .item {
    margin: 5px 0px 5px;
    padding: 5px;
    background-color: var(--secondary-dark);
    border-radius: 5px;

    display: flex;
    align-items: center;
    // gap: 10px;

    transition: 0.2s;

    &__title {
      color: var(--primary-text);
      font-family: var(--main-font);
      font-weight: 400;
      font-size: 20px;
      padding-left: 5px;

      display: flex;
      align-items: center;
      height: 22px;

      display: block;
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
    }

    &__label {
      color: var(--secondary-text);
      font-family: var(--main-font);
      font-weight: 200;
      font-size: 18px;

      display: block;
      white-space: nowrap;
      text-overflow: ellipsis;
      text-align: center;
      overflow: hidden;
      
      &__centered {
        text-align: center;
      }
    }

    &__status {
      padding: 7px;
      border-radius: 5px;

      width: 120px;
      height: 35px;
      font-size: 16px;
      
      font-weight: 500;

      display: flex;
      align-items: center;
      justify-content: center;
    }

    &:hover {
      border-left: 7px solid var(--copper);
      background-color: var(--highlight-dark);
    }
  }

  .label {
    &__title {
      width: 30%;
    }

    &__id {
      width: 20%;
      text-align: center;
    }

    &__count {
      width: 15%;
      font-size: 25px;
      margin-top: -5px;
      text-align: center;
    }

    &__eta {
      width: 10%;
      text-align: center;
    }

    &__buttons {
      width: 20%;
      justify-content: flex-end;
    }
  }

  .sub {
    display: flex;
    align-items: center;
    gap: 5px;
    margin-left: 5px;
  }

</style>