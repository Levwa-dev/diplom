<template>
  <div>
    <Nav/>
    <return_product_content/>
    <Footer/>
  </div>
</template>

<script>
import Nav from "../components/Nav";
import Footer from "../components/Footer";
import return_product_content from "../components/return-product_content";

export default {
name: "contacts",
   components: {
    Nav,
    Footer,
    return_product_content
  }
}
</script>

<style scoped>

</style>