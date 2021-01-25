<template>
  <div class="markdown">
    <div class="header">
      <h2 style="font-size: 30px">{{ post.title }}</h2>

      <ul id="subjects">
        🏷
        <li v-for="item in post.subjects" :key="item.id">
          <router-link
            :to="`/subject/${item}`"
            style="background-color: #5c946e; color: white; padding: 1px"
            >{{ item }}</router-link
          >
        </li>
      </ul>

      📚
      <router-link
        :to="`/medium/${post.medium}`"
        style="background-color: #485665; color: white; padding: 3px"
      >
        {{ post.medium }} </router-link
      ><br />
      🗓 {{ post.data_published }}
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
  props: ["markdownFile"],
  setup(props) {
    const { markdownFile } = toRefs(props);

    const converter = new showdown.Converter({ parseImgDimensions: true });

    const post = ref([]);

    const axios_client = axios.create({
      baseURL: process.env.BASE_URL,
    });

    const getPost = async () => {
      const promise = axios_client.get("get_file", {
        params: { link_path: props.markdownFile },
      });
      const value = await promise.then((response) => response.data);

      post.value.title = value["metadata"]["title"];
      post.value.file = converter.makeHtml(value["file"]);
      post.value.data_published = value["metadata"]["date_published_str"];
      post.value.medium = value["metadata"]["medium"];
      post.value.subjects = value["metadata"]["subjects"];
    };

    onMounted(getPost);
    watch(markdownFile, getPost);

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
  position: relative;
  top: 10px;
}

.header {
  padding: 10px;
  text-align: left;
  background: #7cc6fe;
  color: white;
  font-size: 15px;
  text-transform: capitalize;
}

ul#subjects {
  text-align: left;
  position: relative;
  left: -40px;
  bottom: -8px;
}

ul#subjects li {
  display: inline-block;
  text-align: left;
  margin: 1px;
}

@media screen and (min-width: 800px) {
  .sidenote {
    float: right;
    clear: right;
    margin-right: -30%;
    font-style: italic;
    font-weight: normal;
    width: 25%;
    margin-top: 0.3rem;
    margin-bottom: 0;
    font-size: 0.9rem;
    line-height: 1.2;
    vertical-align: baseline;
    position: relative;
    color: black;
  }
}

@media screen and (max-width: 800px) {
  .sidenote {
    float: right;
    clear: right;
    margin-right: -70%;
    font-style: italic;
    font-weight: normal;
    width: 65%;
    margin-top: 0.3rem;
    margin-bottom: 0;
    font-size: 0.9rem;
    line-height: 1.2;
    vertical-align: baseline;
    position: relative;
    color: black;
  }
}
</style>