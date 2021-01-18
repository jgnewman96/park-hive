<template>
  <div id="post_by_medium">
    <div class="header">
      <h2>Medium : {{ medium }}</h2>
    </div>
    <ul id="array-rendering">
      <li v-for="item in posts" :key="item.id">
        <router-link :to="`/post/${item.link_path}`">
          <span id="title">{{ item.metadata.title }}</span>
        </router-link>

        <ul id="metadata">
          <li>
            <ul>
              🏷
              <li v-for="subject in item.metadata.subjects" :key="subject.id">
                <router-link
                  :to="`/subject/${subject}`"
                  style="color: black; padding: 1px"
                  >{{ subject }}</router-link
                >
              </li>
            </ul>
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
  name: "PostsByMedium",
  props: ["medium"],
  setup(props) {
    const axios_client = axios.create({
      baseURL: process.env.BASE_URL,
    });

    const { medium } = toRefs(props);
    const posts = ref([]);
    const getPosts = async () => {
      const promise = axios_client.get("get_posts_by_medium", {
        params: { medium: props.medium },
      });
      posts.value = await promise.then((response) => response.data);
    };
    onMounted(getPosts);
    watch(medium, getPosts);

    return { posts, getPosts };
  },
};
</script>

<style>
ul#metadata li {
  display: inline-block;
  padding: 4px;
}

ul#metadata {
  padding: 4px;
  position: relative;
  left: -60px;
}
#title {
  font-size: 20px;
}
</style>

