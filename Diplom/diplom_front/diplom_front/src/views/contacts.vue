<template>
  <div>
    <Nav/>
    <contacts_content/>
    <Footer/>
  </div>
</template>

<script>
import Nav from "../components/Nav";
import Footer from "../components/Footer";
import contacts_content from "../components/contacts_content";

export default {
name: "contacts",
   components: {
    Nav,
    Footer,
    contacts_content
  }
}
</script>

<style scoped>

</style>