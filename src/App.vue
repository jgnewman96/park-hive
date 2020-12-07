<template>
  <div id="app">
    <BackendClient @get-notes="getPage" />
    <PageList
      @change-page="changePage"
      @new-page="newPage"
      :pages="pages"
      :activePage="index"
    />
    <Page
      @save-page="savePage"
      @delete-page="deletePage"
      :page="pages[index]"
    />
  </div>
</template>

<script>
import PageList from "./components/PageList";
import Page from "./components/Page";
import BackendClient from "./components/BackendClient";

export default {
  name: "app",
  components: {
    PageList,
    Page,
    BackendClient,
  },
  data: () => ({
    pages: [],
    index: 0,
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
    savePage() {
      // nothing as of yet
    },
    deletePage() {
      this.pages.splice(this.index, 1);
      this.index = Math.max(this.index - 1, 0);
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