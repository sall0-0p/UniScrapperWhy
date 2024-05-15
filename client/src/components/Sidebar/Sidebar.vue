<script>
  import SidebarHeader from './Header/Header.vue'
  import SidebarList from './List/List.vue'

  export default {
    components: {
      SidebarHeader,
      SidebarList,
    },

    props: {
      items: {
        type: Array,
        default: () => [],
      },
      footerItems: {
        type: Array,
        default: () => [],
      },
      selected: {
        Type: String,
        default: '',
      },
    },

    methods: {
      selectItem(payload) {
        this.$emit('select-item', payload);
      },
    },
  }
</script>

<template>
  <div class="sidebar shadow-l">
    <SidebarHeader />
    <div class="sidebar-wrapper nav-main">
      <SidebarList 
        :items="items"
        :selected="selected"
        @select-item="selectItem"
      />
    </div>
    <div class="sidebar-wrapper nav-footer">
      <SidebarList 
        :items="footerItems"
        :selected="selected"
        @select-item="selectItem"
      />
    </div>
  </div>
</template>

<style scoped>
  .sidebar {
    height: 100vh;
    background-color: var(--secondary-dark);
    width: 270px;
    z-index: 10;
    display: flex;
    flex-direction: column;
  }

  .sidebar-wrapper {
    width: 100%;
  }

  .nav-main {
    flex-grow: 1;
  }

  .nav-footer {
    background-color: #2e2e33;
  }
</style>