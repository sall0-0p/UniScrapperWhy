<script>
  import Icon from '../Icon/Icon.vue';
  import HeaderButton from '../Button/Button.vue';
  import ProductRepository from "@/domain/ProductsRepository";

  export default {
    components: {
      Icon,
      HeaderButton,
    },

    data() {
      return {
        repository: new ProductRepository('http://127.0.0.1:5000'),
        downloading: false,
        sortingMethod: "By Alphabet", // "By Review Count"
        sortingIcon: "../src/assets/images/attribute_filter.png",
        search: '',
      };
    },
    
    props: {
      itemsCount: {
        type: Number,
        default: 0,
      },
    },

    methods: {
      formChanged() {
        this.$emit('update-search', this.search);
      },

      changeSortingMethod() {
        if (this.sortingMethod === "By Alphabet") {
          this.sortingIcon = "../src/assets/images/filter.png";
          this.sortingMethod = "By Review Count";
          this.$emit("change-sorting", "By Review Count")
        } else {
          this.sortingIcon = "../src/assets/images/attribute_filter.png";
          this.sortingMethod = "By Alphabet";
          this.$emit("change-sorting", "By Alphabet");
        }
      },
    },
  }
</script>

<template>
  <div class="header">
    <h3 class="header__title">Reviews ({{ this.itemsCount }})</h3>

    <div class="search">
      <Icon size="20px" img="../src/assets/images/spyglass.png"/>
      <input class="search__input" 
        placeholder="Search" 
        v-model="search" 
        @input="formChanged" 
        @submit="createNew"
        id="search"
      >
    </div>

    <div class="header__buttons">
      <VTooltip>
        <HeaderButton
          img="../src/assets/images/bundle.png"
          @click="changeSortingMethod"
        />

        <template #popper>
          <p class="tooltip__text">Reload</p>
        </template>
      </VTooltip>
    </div>
  </div>
</template>

<style scoped lang="scss">
  .header {
    display: flex;
    align-items: center;
    margin-right: 5px;

    &__title {
      color: var(--primary-text);
      font-family: var(--main-font);
      font-size: 17px;
      font-weight: 500;

      flex-grow: 1;
      margin: 5px;
    }

    &__buttons {
      display: flex;
      gap: 5px;
    }
  }

  .search {
    background-color: var(--secondary-light);
    border-radius: 5px;
    height: 20px;
    padding: 5px;
    width: 60%;
    margin-right: 5px;

    display: flex;
    gap: 5px;

    &__input {
      color: var(--primary-text);
      font-family: var(--main-font);
      font-size: 16px;
      margin-top: -1px;

      background-color: var(--secondary-light);
      border: 0px;

      width: calc(100% - 10px);

      &:focus {
        border: 0px;
        outline: none;
      }
    }
  }

  ::placeholder {
    color: var(--secondary-text)
  }
</style>