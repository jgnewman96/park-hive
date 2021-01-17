<template>
  <div id="header">
    <a href="/" style="text-decoration: none; color: #ffffff"
      >Judah Newman's Archive</a
    >

    <ul id="icon_links">
      <li>
        <a href="https://github.com/jgnewman96">
          <img border="0" src="../../img/gh.jpg" width="30" height="30" />
        </a>
      </li>
      <li>
        <a href="https://github.com/jgnewman96">
          <img border="0" src="../../img/li.jpg" width="30" height="30" />
        </a>
      </li>
      <li>
        <a href="mailto:judah.newman@gmail.com">
          <img border="0" src="../../img/mail.jpg" width="30" height="30" />
        </a>
      </li>
    </ul>
  </div>
</template>


<script>
export default {
  name: "website_header",
};
</script>

<style>
#header {
  padding: 30px;
  text-align: left;
  background: #5c946e;
  color: white;
  font-size: 35px;
  width: 100%;
  position: relative;
}

ul#icon_links {
  display: inline;
  list-style-type: none;
  position: absolute;
  left: 78%;
  top: 0%;
}

ul#icon_links li {
  display: inline;
  padding: 4px;
}
</style>