<template>
  <div>
    <Nav/>
    <us_content/>
    <Footer/>
  </div>
</template>

<script>
import Nav from "../components/Nav";
import Footer from "../components/Footer";
import us_content from "../components/us_content";

export default {
name: "us",
   components: {
    Nav,
    Footer,
    us_content
  }
}
</script>

<style scoped>

</style>