<template>
  <div class="markdown-file">
    <VueShowdown :markdown="data" flavor="github" :options="{ emoji: true }" />
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MarkdownFile",
  props: ["markdownFile", "backendUrl"],
  async setup(props) {
    const promise = axios.get(props.backendUrl + "get_notes");
    const data = await promise.then((response) => response.data);

    return { data };
  },
};
</script>