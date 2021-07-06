<template>
  <div>
    <Nav/>
    <guarantee_content/>
    <Footer/>
  </div>
</template>

<script>
import Nav from "../components/Nav";
import Footer from "../components/Footer";
import guarantee_content from "../components/guarantee_content";

export default {
name: "contacts",
   components: {
    Nav,
    Footer,
    guarantee_content
  }
}
</script>

<style scoped>

</style>