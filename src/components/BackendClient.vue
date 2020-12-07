<template>
  <div id="backend">
    <button @click="getNotes()">Test</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "backend",
  data: () => ({
    url: "http://0.0.0.0:8100/",
    posts: [],
  }),
  methods: {
    getNotes() {
      axios.get("http://0.0.0.0:8100/get_notes").then((response) => {
        this.posts = response.data;
      });
      this.$emit("get-notes", this.posts);
    },
  },
};
</script>

 <style>
</style>