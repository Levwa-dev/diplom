<template>
  <div>
    <Nav/>
    <cart_content :productInCartList="productInCartList"/>
    <Footer/>
  </div>
</template>

<script>
import Nav from "../components/Nav";
import Footer from "../components/Footer";
import cart_content from "../components/cart_content";

export default {
name: "contacts",
  data(){
    return {
    productInCartList:[]
    }
  },
  created() {
    this.Products()
  },
  methods:{
    Products(){
       this.productInCartList=this.$store.state.cart
    }
  },
   components: {
    Nav,
    Footer,
    cart_content
  }
}
</script>

<style scoped>

</style>