<template>
  <div id="post_by_subject">
    <ul id="array-rendering">
      <li v-for="item in posts" :key="item.id">
        <router-link :to="`/post/${item.link_path}`">
          {{ item.metadata.title }}
        </router-link>
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
</style>
