<template>
  <div id="recent_posts">
    <h2>Recent Posts</h2>

    <ul id="array-rendering">
      <li v-for="item in recent_posts" :key="item.id">
        <router-link :to="`/post/${item.link_path}`">
          {{ item.metadata.title }}
        </router-link>

        <ul id="recent_posts_metadata">
          <li>
            <ul id="recent_posts_subjects">
              🏷
              <li v-for="subject in item.metadata.subjects" :key="subject.id">
                <router-link
                  :to="`/subject/${subject}`"
                  style="background-color: #5c946e; color: white; padding: 1px"
                  >{{ subject }}</router-link
                >
              </li>
            </ul>
          </li>

          <li>
            📚
            <router-link
              :to="`/medium/${item.metadata.medium}`"
              style="background-color: #485665; color: white; padding: 3px"
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
import { onMounted, ref } from "vue";
export default {
  name: "RecentPosts",
  props: ["backendUrl"],
  setup(props) {
    const recent_posts = ref([]);
    const getRecentPosts = async () => {
      const promise = axios.get(props.backendUrl + "get_recent_posts", {
        params: { number_of_posts: 5 },
      });
      recent_posts.value = await promise.then((response) => response.data);
    };
    onMounted(getRecentPosts);

    return { recent_posts, getRecentPosts };
  },
};
</script>

<style>
ul#recent_posts_subjects li {
  padding: 4px;
  display: inline-block;
}

ul#recent_posts_subjects {
  padding: 4px;
  position: relative;
  left: -10px;
}

ul#recent_posts_metadata li {
  padding: 4px;
  list-style: none;
}

ul#recent_posts_metadata {
  padding: 4px;
  position: relative;
  left: -10px;
}
</style>
