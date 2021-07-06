<template>
  <div>
    <Nav/>
    <promo/>
    <Cont/>
    <Footer/>
  </div>
</template>

<script>
import Nav from "../components/Nav";
import Footer from "../components/Footer";
import Cont from "../components/Cont";
import promo from "../components/promo";
export default {
name: "Home",
  components: {
    Nav,
    Footer,
    Cont,
    promo
  }
}
</script>

<style scoped>

</style>