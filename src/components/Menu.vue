<template>
  <div class="menu">
    <float-menu
      position="top right"
      :dimension="90"
      :menu-data="menuItems"
      :on-selected="handleSelection"
      :theme="{
        primary: 'var(--third-color)',
        textColor: '#000',
        menuBgColor: '#fff',
        textSelectedColor: 'var(--border-color)',
      }"
    >
      Menu
    </float-menu>
  </div>
</template>


<script>
import { FloatMenu } from "vue-float-menu";
import "vue-float-menu/dist/vue-float-menu.css";

export default {
  name: "app",
  components: {
    FloatMenu,
  },
  props: ["menuItems"],
  setup(props, { emit }) {
    const handleSelection = (selectedItem) => {
      emit("menu-selection", selectedItem);
    };

    return { handleSelection };
  },
};
</script>

<style scoped>
</style>