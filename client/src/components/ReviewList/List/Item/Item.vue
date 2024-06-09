<script>
  import Icon from '../../Icon/Icon.vue';
  import ItemButton from '../../Button/Button.vue';
  import ProductRepository from "@/domain/ProductsRepository";
  import Review from './Review.vue'

  export default {
    data() {
      return {
        repository: new ProductRepository('http://127.0.0.1:5000'),
        notLoading: true,
      }
    },

    components: {
      Icon,
      ItemButton,
      Review,
    },

    props: {
      review: {
        type: Object,
        default: () => ({}),
      },
    },

    computed: {
      getReviewIcon() {
        if (this.review.recommendation) {
          return '../src/assets/images/dye_powder_lime.png'
        } else {
          return '../src/assets/images/dye_powder_red.png'
        }
      },

      formatRating() {
        let numberOfStars = Math.round(this.review.score / .2);
        return "★".repeat(numberOfStars) + "☆".repeat(5 - numberOfStars);
      },
    },
  }
</script>

<template>
  <div class="item">
    <div class="sub">
      <VTooltip>
        <Icon 
          :img="getReviewIcon"
          size="25px"
        />

        <template #popper>
          <p class="tooltip__text" v-if="this.review.recommendation">
            Recommended
          </p>

          <p class="tooltip__text" v-else>
            Not recommended
          </p>
        </template>
      </VTooltip>
      
      <div class="item__title">
        {{ review.author }}
      </div>
      <div class="item__label label__count">
        {{ formatRating }}
      </div>
    </div>
    <div class="item__content">
        {{ review.content }}
    </div>

    <div class="reviews__container">
      <div class="reviews__column">
        <Review 
          :item="review.pros"
        ></Review>
      </div>
      <div class="reviews__column">
        <Review 
          :item="review.cons"
        ></Review>
      </div>
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
    flex-direction: column;

    transition: 0.2s;

    box-sizing: border-box;

    &__title {
      color: var(--primary-text);
      font-family: var(--main-font);
      font-weight: 300;
      font-size: 16px;
      padding-top: 5px;

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

    &__content {
        color: var(--secondary-text);
        font-family: var(--main-font);
        font-weight: 100;
        font-size: 15px;

        margin-left: 5px;
        margin-bottom: 5px;

        width: 80%;
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
      margin-left: 10px;
      font-size: 25px;
      margin-top: -7px;
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

    &__wait {
      height: 25px;
      padding: 5px;
      
      display: flex;
      align-items: center;
      justify-content: center;
    }
  }

  .sub {
    display: flex;
    align-items: center;
    gap: 5px;
    margin-left: 5px;
  }

  .reviews {
    &__container {
      padding: 5px;
      padding-top: 0px;
      margin-top: -5px;
      display: flex;
    }
    &__column {
      width: 40%;
    }
  }

</style>