<template>
  <div id="app">
    <title>Judah Newman's Archive</title>
    <Header />
    <Menu @menu-selection="ProcessSelection" :menuItems="menuItems" />

    <recent-posts id="recent_posts" />
    <recent-posts v-if="!path_string" id="recent_posts_mobile" />

    <router-view id="main_content" />
    <Footer />
  </div>
</template>

<script>
import Menu from "./components/Menu";
import Header from "./components/Header";
import Footer from "./components/Footer";
import RecentPosts from "./components/RecentPosts";
import { useRoute } from "vue-router";
import { watch, computed } from "vue";

export default {
  name: "app",
  components: {
    Menu,
    Header,
    Footer,
    RecentPosts,
  },
  setup() {
    var goatcounter = document.createElement("script");
    goatcounter.setAttribute(
      "data-goatcounter",
      "https://jgnewman.goatcounter.com/count"
    );
    goatcounter.setAttribute("async", "true");
    goatcounter.setAttribute("allow_local", "true");
    goatcounter.setAttribute("src", "https://srcrs.top/assets/js/count.js");
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(goatcounter, s);

    const route = useRoute();
    const path_string = computed(() => {
      return route.path.split("/").pop();
    });

    const updateTitle = () => {
      if (path_string.value) {
        document.title = "Judah Newman's Archive - " + path_string.value;
        if (window.goatcounter) {
          window.goatcounter.count({ path: location.hash });
        }
      } else {
        document.title = "Judah Newman's Archive";
      }
    };

    watch(path_string, updateTitle);
    return { path_string, updateTitle };
  },
  data: () => ({
    pages: [],
    index: 0,
    viewMode: true,
    menuItems: [
      { name: "About This Project" },
      { name: "About Me" },
      { name: "Books" },
      { name: "Academic Papers" },
      { name: "Research" },
      { name: "Internet Reading" },
    ],
  }),
  methods: {
    ProcessSelection(itemSelected) {
      if (itemSelected === "Books") {
        this.$router.push({ path: "/medium/" + "book" });
      } else if (itemSelected === "Academic Papers") {
        this.$router.push({ path: "/medium/" + "paper" });
      } else if (itemSelected === "About This Project") {
        this.$router.push({ path: "/" });
      } else if (itemSelected === "About Me") {
        this.$router.push({ path: "/about_me" });
      } else if (itemSelected === "Research") {
        this.$router.push({ path: "/research/" });
      } else if (itemSelected === "Internet Reading") {
        this.$router.push({ path: "/internet_reading/" });
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

@media screen and (min-width: 800px) {
  #recent_posts {
    position: absolute;
    top: 200px;
    width: 20%;
  }
}

@media screen and (max-width: 800px) {
  #recent_posts {
    display: none;
  }
}

@media screen and (min-width: 800px) {
  #recent_posts_mobile {
    display: none;
  }
}

@media screen and (min-width: 800px) {
  #main_content {
    width: 60%;
    position: relative;
    left: 20%;
    margin-top: 1%;
    border-right: 4px solid #124653;
    border-left: 4px solid #124653;
    padding: 1%;
  }
}

@media screen and (max-width: 800px) {
  #main_content {
    width: 70%;
    position: relative;
    left: 2%;
    margin-top: 1%;
    padding: 1%;
  }
}
</style>