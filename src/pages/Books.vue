<template>
  <div id="books">
    <div class="header">
      <h2>Books</h2>
    </div>
    <ul id="years_list">
      <li v-for="year in book_images" :key="year.id">
        <h3>{{ year[0] }}</h3>

        <ul id="book_list">
          <li v-for="book in year[1]" :key="book.id">
            <template v-if="year[0] !== `CURRENT`">
              <router-link :to="getLinkfromImg(book)">
                <img border="0" padding="5" :src="getImgUrl(book)" width="80" />
              </router-link>
            </template>
            <template v-else>
              <img border="0" padding="5" :src="getImgUrl(book)" width="80" />
            </template>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import { ref, onMounted } from "vue";

export default {
  name: "Books",
  setup() {
    const axios_client = axios.create({
      baseURL: process.env.BASE_URL,
    });

    const book_images = ref([]);
    const getBookImages = async () => {
      const promise = axios_client.get("get_book_images");
      book_images.value = await promise.then((response) => response.data);
    };
    onMounted(getBookImages);

    return { book_images, getBookImages };
  },
  methods: {
    getImgUrl(pic) {
      /// this is so we dont inlucde all these other files in the build pack
      /// we could include them though and then I would get autoreloading
      const pic_name = pic.slice(0, -4);
      return require("../../" + pic_name + ".jpg");
    },
    getLinkfromImg(img_path) {
      const link = "/post/" + img_path.split("/").pop().slice(0, -4);
      return link;
    },
  },
};
</script>

<style scoped>
ul#years_list li {
  display: inline-block;
  padding: 8px;
}
</style>
