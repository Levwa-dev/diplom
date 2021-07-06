<template>
  <div>
    <Nav/>
    <product_content :prod="product" :reviews="reviews" :countSlides="slides"/>
    <Footer/>
  </div>
</template>

<script>
import Nav from "../components/Nav";
import Footer from "../components/Footer";
import product_content from "../components/product_content";

export default {
name: "contacts",
  props: ['id'],
  data(){
    return{
      slides:null,
      product:{},
      reviews:[],
    }
  },
  created() {
    this.loadProduct()
  },
  methods:{
    async loadProduct(){
      this.product = await fetch(
      `${this.$store.getters.getSeverUrl}/products/${this.id}`
      ).then(response => response.json())
      this.Products()
    },
    Products(){
      this.productInCartList=this.$store.state.cart
      for(let i = 0; i<=this.productInCartList.length-1;i++){
        if(this.productInCartList[i].id === this.product.id){
          this.product.incart=true
        }
      }
      this.slides = this.product.slides.length
      this.reviews = this.product.reviews
    },
  },
  components: {
    Nav,
    Footer,
    product_content
  }
}
</script>

<style scoped>

</style>