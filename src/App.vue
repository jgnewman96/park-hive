<template>
  <div id="app">
    <Header />
    <Menu @menu-selection="ProcessSelection" :menuItems="menuItems" />

    <recent-posts id="recent_posts" :backendUrl="backendUrl" />
    <router-view id="main_content" />

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
    <Footer />
  </div>
</template>

<script>
import PageList from "./components/PageList";
import Page from "./components/Page";
import Menu from "./components/Menu";
import Header from "./components/Header";
import Footer from "./components/Footer";
import RecentPosts from "./components/RecentPosts";

export default {
  name: "app",
  components: {
    PageList,
    Page,
    Menu,
    Header,
    Footer,
    RecentPosts,
  },
  data: () => ({
    pages: [],
    index: 0,
    viewMode: true,
    backendUrl: "http://0.0.0.0:8100/",
    menuItems: [
      { name: "About This Project" },
      { name: "About Me" },
      { name: "Books" },
      { name: "Internet Reading" },
      { name: "Writing" }, //could make this a sub menu
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
      } else if (itemSelected === "Writing") {
        this.$router.push({ path: "/medium/" + "paper" });
      } else {
        this.$router.push({ path: "/post/" + itemSelected });
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
}
#recent_posts {
  position: absolute;
  top: 200px;
  width: 20%;
}

#main_content {
  width: 70%;
  height: auto;
  position: relative;
  left: 20%;
  margin-top: 1%;
  border-right: 4px solid #124653;
  border-left: 4px solid #124653;
}
</style>