<template>
  <div class="menu">
    <float-menu
      :position="'center'"
      :dimension="90"
      :menu-data="menuItems"
      :on-selected="handleSelection"
    >
      Drag
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