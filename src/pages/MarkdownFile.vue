<template>
  <div class="markdown-file">
    <VueShowdown :markdown="data" flavor="allOn" :options="{ emoji: true }" />
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MarkdownFile",
  props: ["markdownFile", "backendUrl"],
  async setup(props) {
    const promise = axios.get(props.backendUrl + "get_file", {
      params: { link_path: props.markdownFile },
    });
    const data = await promise.then((response) => response.data);

    return { data };
  },
};
</script>

<style>
blockquote {
  margin-left: 20;
}
</style>