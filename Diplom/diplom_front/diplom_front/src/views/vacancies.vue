<template>
  <div>
    <Nav/>
    <vacancies_content/>
    <Footer/>
  </div>
</template>

<script>
import Nav from "../components/Nav";
import Footer from "../components/Footer";
import vacancies_content from "../components/vacancies_content";

export default {
name: "vacancies",
   components: {
    Nav,
    Footer,
    vacancies_content
  }
}
</script>

<style scoped>

</style>