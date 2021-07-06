<template>
  <div id="app">
    <start/>
  </div>
</template>

<script>

import start from "./components/start";
export default {
  name: 'App',
  components: {
    start
  }
}
</script>

<style>
#app{
  font-family: 'Montserrat', sans-serif;
}
@import "./assets/css/reset.css";
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,700;1,400&display=swap');
</style>
