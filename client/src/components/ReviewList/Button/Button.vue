<script>
  import Icon from '../Icon/Icon.vue'

  export default {
    components: {
      Icon,
    },

    props: {
      img: {
        type: String,
        default: "",
      },

      label: {
        type: String,
        default: '',
      },

      size: {
        type: String,
        default: '20px',
      },

      rectangular: {
        type: String,
        default: "false",
      },
      
      icon_size: {
        type: String,
        default: '20px',
      }
    },
    
    computed: {
      hasGap() {
        return (this.img != "" && this.label != "")
      }
    },
  }
</script>

<template>
  <div 
    class="button"
    :class="{ 'button__gap': hasGap, 'button__rectangular': (rectangular === 'true') }"
    :style="'height: ' + size"
  >
    <Icon :img="img" :size="icon_size"/>
    <p class="button__label">{{ label }}</p>
  </div>
</template>

<style scoped lang="scss">
  .button {
    background-color: var(--secondary-light);
    border-radius: 5px;
    height: 30px;
    padding: 5px;

    display: flex;
    justify-content: center;
    align-items: center;
    // gap: 5px;

    transition: 0.15s;

    cursor: pointer;

    &__label {
      color: var(--primary-text);
      font-family: var(--main-font);
      font-weight: 400;
    }

    &__gap {
      gap: 5px;
    }

    &__rectangular {
      aspect-ratio: 1/1;
    }

    &:hover {
      background-color: var(--highlight-light);
    }
  }

</style>