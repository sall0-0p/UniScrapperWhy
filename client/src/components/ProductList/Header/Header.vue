<script>
  import Icon from '../Icon/Icon.vue'
  import HeaderButton from '../Button/Button.vue'

  export default {
    components: {
      Icon,
      HeaderButton,
    },
  }
</script>

<template>
  <div class="header">
    <h3 class="header__title">Production Queue</h3>
    <div class="search">
      <Icon size="20px" img="../src/assets/images/spyglass.png"/>
      <input class="search__input" placeholder="Search">
    </div>
    <div class="header__buttons">
      <HeaderButton 
        img="../src/assets/images/clipboard_and_quill.png"
        label="NEW"
      />
      <VTooltip>
        <HeaderButton 
        img="../src/assets/images/bucket_lava.png"
        />

        <template #popper>
          <p class="tooltip__text">Clear All</p>
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
    margin-right: 10px;

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