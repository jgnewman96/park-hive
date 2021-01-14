<template>
  <div class="menu">
    <float-menu
      position="top right"
      :dimension="90"
      :menu-data="menuItems"
      :on-selected="handleSelection"
      :theme="{
        primary: '#485665',
        textColor: '#000',
        menuBgColor: '#fff',
        textSelectedColor: '#ffb5c2',
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