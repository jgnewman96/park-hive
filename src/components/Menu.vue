<template>
  <div class="menu">
    <float-menu
      :position="'center'"
      :dimension="90"
      :menu-data="items"
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
  setup(props, { emit }) {
    const handleSelection = (selectedItem) => {
      emit("menu-selection", selectedItem);
    };

    return { handleSelection };
  },
  data: () => ({
    viewMode: true,
    items: [
      { name: "New" },
      {
        name: "Edit",
        subMenu: {
          name: "edit-items",
          items: [{ name: "Copy" }, { name: "Paste" }],
        },
      },
      {
        name: "Open Recent",
      },
      {
        name: "",
      },
    ],
  }),
};
</script>