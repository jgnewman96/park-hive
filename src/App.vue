<template>
  <div id="app">
    <Menu @menu-selection="ProcessSelection" :menuItems="menuItems" />
    <router-view />

    <BackendClient v-if="!viewMode" @get-notes="getPage" />
    <PageList
      v-if="!viewMode"
      @change-page="changePage"
      @new-page="newPage"
      :pages="pages"
      :activePage="index"
    />
    <Page
      v-if="!viewMode"
      @save-page="savePage"
      @delete-page="deletePage"
      @update-title="updateTitle"
      @update-content="updateContent"
      :page="pages[index]"
      :index="index"
    />
  </div>
</template>

<script>
import PageList from "./components/PageList";
import Page from "./components/Page";
import BackendClient from "./components/BackendClient";
import Menu from "./components/Menu";

export default {
  name: "app",
  components: {
    PageList,
    Page,
    BackendClient,
    Menu,
  },
  data: () => ({
    pages: [],
    index: 0,
    viewMode: true,
    menuItems: [
      { name: "New" },
      {
        name: "Edit",
        subMenu: {
          name: "edit-items",
          items: [{ name: "Copy" }, { name: "Paste" }],
        },
      },
      {
        name: "Books",
      },
      {
        name: "Switch Modes",
      },
    ],
  }),
  methods: {
    newPage() {
      this.pages.push({
        title: "",
        content: "",
      });
      this.index = this.pages.length - 1;
    },
    changePage(index) {
      this.index = index;
    },
    getPage(index) {
      console.log(index);
    },
    updateTitle(title) {
      this.pages[this.index].title = title;
    },
    updateContent(content) {
      this.pages[this.index].content = content;
    },
    switchMode() {
      this.viewMode = !this.viewMode;
    },
    savePage() {
      // nothing as of yet
    },
    deletePage() {
      this.pages.splice(this.index, 1);
      this.index = Math.max(this.index - 1, 0);
    },
    ProcessSelection(itemSelected) {
      console.log(itemSelected);
      if (itemSelected === "Switch Modes") {
        this.switchMode();
      } else {
        this.$router.push({ name: "Books" });
      }
    },
  },
};
</script>

 <style>
html,
body,
#app {
  height: 100%;
}

body {
  margin: 0;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  display: flex;
  flex-direction: row;
}
</style>