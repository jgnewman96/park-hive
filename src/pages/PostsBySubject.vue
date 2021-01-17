<template>
  <div id="post_by_subject">
    <div class="header">
      <h2>Subject : {{ subject }}</h2>
    </div>
    <ul id="array-rendering">
      <li v-for="item in posts" :key="item.id">
        <router-link :to="`/post/${item.link_path}`">
          <span id="title">{{ item.metadata.title }}</span>
        </router-link>

        <ul id="metadata_medium">
          <li>
            📚
            <router-link
              :to="`/medium/${item.metadata.medium}`"
              style="color: black; padding: 3px"
            >
              {{ item.metadata.medium }}
            </router-link>
          </li>
          <li>🗓 {{ item.metadata.date_published_str }}</li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import { ref, watch, onMounted, toRefs } from "vue";

export default {
  name: "PostsBySubject",
  props: ["subject", "backendUrl"],
  setup(props) {
    const { subject } = toRefs(props);
    const posts = ref([]);
    const getPosts = async () => {
      const promise = axios.get(props.backendUrl + "get_posts_by_subject", {
        params: { subject: props.subject },
      });
      posts.value = await promise.then((response) => response.data);
    };
    onMounted(getPosts);
    watch(subject, getPosts);

    return { posts, getPosts };
  },
};
</script>

<style>
ul#metadata_medium li {
  display: inline-block;
  padding: 4px;
}

ul#metadata_medium {
  padding: 4px;
  position: relative;
}
</style>
