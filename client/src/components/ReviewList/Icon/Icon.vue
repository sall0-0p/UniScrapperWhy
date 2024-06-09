<script>
  export default {
    props: {
      img: {
        type: String,
        default: "",
      },
      size: {
        type: String,
        default: "20px",
      }
    },

    computed: {
      buildStyle() {
        return `height: ${this.size}; background: center / contain no-repeat url("${this.img}")`;
      }
    }
  }
</script>

<template>
  <div class="icon" :style="buildStyle"></div>
</template>

<style scoped lang="scss">
  .icon {
    aspect-ratio: 1/1;
  }
</style>