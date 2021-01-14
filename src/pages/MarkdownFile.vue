<template>
  <div class="markdown">
    <div class="header">
      <h2>{{ post.title }}</h2>
      Date Published: {{ post.data_published }}
    </div>
    <span v-html="post.file"></span>
  </div>
</template>

<script>
import axios from "axios";
import * as showdown from "showdown";
import { toRefs, ref, onMounted, watch } from "vue";

export default {
  name: "MarkdownFile",
  props: ["markdownFile", "backendUrl"],
  async setup(props) {
    const { markdownFile } = toRefs(props);
    const converter = new showdown.Converter();
    const post = ref([]);

    const getPost = async () => {
      const promise = axios.get(props.backendUrl + "get_file", {
        params: { link_path: props.markdownFile },
      });
      const value = await promise.then((response) => response.data);

      post.value.title = value["metadata"]["title"];
      post.value.file = converter.makeHtml(value["file"]);
      post.value.data_published = value["metadata"]["date_published_str"];
    };

    onMounted(getPost(markdownFile.value));
    watch(markdownFile, getPost);

    await getPost(markdownFile.value);

    return { post, getPost };
  },
};
</script>

<style>
blockquote {
  background-color: #fcf0c5;
  border-width: 1px;
  border-style: solid;
  border-left: 1px solid;
  padding-left: 10px;
}

.markdown {
  margin: auto;
  width: 70%;
  border-right: 4px solid #124653;
  border-left: 4px solid #124653;
  position: relative;
  top: 10px;
}

.header {
  padding: 10px;
  text-align: center;
  background: #7cc6fe;
  color: white;
  font-size: 15px;
}
</style>