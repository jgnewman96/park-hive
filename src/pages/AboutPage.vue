<template>
  <div class="markdown">
    <div class="header">
      <h2 style="font-size: 35px; text-align: center">{{ post.title }}</h2>
    </div>
    <span v-html="post.file"></span>
  </div>
</template>

<script>
import axios from "axios";
import * as showdown from "showdown";
import { toRefs, ref, onMounted, watch } from "vue";

export default {
  name: "AboutPage",
  props: ["pageName"],
  setup(props) {
    const { pageName } = toRefs(props);
    const converter = new showdown.Converter();
    const post = ref([]);

    const axios_client = axios.create({
      baseURL: process.env.BASE_URL,
    });

    const getPost = async () => {
      const promise = axios_client.get("get_file", {
        params: { link_path: props.pageName },
      });
      const value = await promise.then((response) => response.data);

      post.value.title = value["metadata"]["title"];
      post.value.file = converter.makeHtml(value["file"]);
      post.value.data_published = value["metadata"]["date_published_str"];
      post.value.medium = value["metadata"]["medium"];
      post.value.subjects = value["metadata"]["subjects"];
    };

    onMounted(getPost);
    watch(pageName, getPost);

    return { post, getPost };
  },
};
</script>

<style>
</style>