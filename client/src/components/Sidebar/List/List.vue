<script>
  import ListItem from './Item/Item.vue'

  export default {
    components: {
      ListItem
    },

    props: {
      items: {
        type: Array,
        default: () => [],
      },

      selected: {
        type: String,
        default: '',
      },
    },

    methods: {
      isSelected(title) {
        console.log(title, this.selected, title == this.selected)
        return title === this.selected
      },
      selectItem(payload) {
        this.$emit('select-item', payload);
      },
    }
  }
</script>

<template>
  <div class="list">
    <ListItem 
      v-for="item in items"
      :key="item.id"
      :item="item"
      :selected="item.name === selected"
      @select-item="selectItem"
    />
  </div>
</template>

<style scoped>
  .list {
    display: flex;
    flex-direction: column;
    width: 100%;
  }
</style>