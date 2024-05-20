<script>
  import { RouterLink } from 'vue-router';

  export default {
    props: {
      item: {
        type: Object,
        default: () => ({}),
      },
      selected: {
        type: Boolean,
        default: false,
      },
    },

    computed: {
      formatStyle() {
        return 'background: center / contain no-repeat url("' + this.item.icon + '")'
      },
    },

    methods: {
      onClick() {
        this.$emit('select-item', this.item.name);
      },
    },
  }
</script>

<template>
  <RouterLink :to="item.redirect">
    <div 
      class="item" 
      :class='{ "selected": selected }'
      @click="onClick"
    >
      <div 
        class="icon" 
        :style="formatStyle"
      ></div>
      <h4 class="title">
        {{ item.name }}
      </h4>
    </div>
  </RouterLink>
</template>

<style scoped lang="scss">
  .item {
    width: 100%;
    aspect-ratio: 4/1;

    display: flex;
    align-items: center;

    border-left: 0px solid;
    box-sizing: border-box;

    transition: 0.2s;
    &:hover {
      border-left: 7px var(--copper) solid;
      background-color: var(--highlight-darker);
      
    }
  }

  .icon {
    width: 20%;
    aspect-ratio: 1/1;
    margin-left: 15px;
    margin-right: 15px;

    background: center / contain no-repeat;
  }

  .title {
    color: var(--primary-text);
    font-family: var(--main-font);
    font-weight: 400;
    font-size: 20px;
  }

  /* Effects */
  .selected {
    background-color: #2e2e33;
  }
</style>