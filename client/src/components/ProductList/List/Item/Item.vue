<script>
  import Icon from '../../Icon/Icon.vue';
  import ItemButton from '../../Button/Button.vue';
  import ProductRepository from "@/domain/ProductsRepository";

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

    methods: {
      deleteProduct() {
        this.repository.deleteProduct(this.item.productId).then(() => {
          this.$emit('refresh-list');
        });
      },

      refreshProduct() {
        this.notLoading = false;
        this.repository.refreshProduct(this.item.productId).then(() => {
          this.$emit('refresh-list');
          this.notLoading = true;
        })
      }
    },
  }
</script>

<template>
  <div class="item" v-if="notLoading">
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
        {{ (item.productName).slice(0, 48) }}
      </routerLink>
    </div>

    <div class="item__label label__id">
      <VTooltip>
        <a 
        style="text-decoration: none; color: var(--secondary-text)"
        :href="`https://ceneo.pl/${ this.item.productId }`"
        target="_blank"
        > {{ item.productId }} </a>
      
        <template #popper>
          <p class="tooltip__text">
            Product Id
          </p>
          <p class="tooltip__text">
            (Click to open)
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
          <p class="tooltip__text">
            ({{ (item.rating * 5).toFixed(1) }}/5.0)
          </p>
        </template>
      </VTooltip>
    </div>

    <div class="sub label__buttons">
      <VTooltip>
        <ItemButton @click="refreshProduct"
          img="../src/assets/images/bundle.png" 
          size="25px" 
          icon_size="25px" 
          rectangular=true 
        />

        <template #popper>
          <p class="tooltip__text">
            Update
          </p>
        </template>
      </VTooltip>

      <VTooltip>
        <ItemButton @click="deleteProduct"
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

  <div class="item" v-else>
    <div class="item__label label__wait">
      <p>Loading...</p>
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

    box-sizing: border-box;

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

</style>