<template>
  <div>
    <Nav/>
    <promo/>
    <section class="product">
      <div class="wrap">
        <div class="products__filter">
          <h3>Фільтр</h3>
          <div class="slidecontainer">
            <input v-model="price" type="range" min="450" max="200000" step="50" class="slider" id="myRange">
          </div>
          <span style="margin-left: 100px; font-weight: bold">Ціна > 550 грн</span>
          <div style="margin-top: 15px" class="filter__content" v-for="character in characters" :key="character.id">
            <p class="filter__item" style="font-size: 14px; font-weight: bold; margin: 10px">{{character.name}}</p>
            <div class="filter__v" style="display: flex; position: relative" v-for="value in character.characters_value" :key="value.id">
              <p class="filter__value" style="margin: 10px">{{value.description}}</p>
              <input type="checkbox" style="position: absolute; top:11px; left:270px; height: 15px; width: 15px">
            </div>
            <span style="margin-left: 100px; font-size: 13px; color: #21a6c4; text-decoration: underline">Більше...</span>
          </div>
          <button style="background-color:#424242; border: 1px solid #222222; color:#ffffff;margin-left: 50px; margin-top: 10px">Применить фильтры</button>
        </div>
        <div class="products__filter-mob filter-mob">
          <span>Фильтры</span><i class="fas fa-filter"></i>
          <div class="filter-mob__content">
            <ul class="filter-mob__list">
              <li></li>
            </ul>
          </div>
        </div>
        <div class="s">
        <div class="products__cont">
          <div class="products__title" style="text-align: center">{{category}}</div>
          <div class="products__content">
            <div class="products__product" v-for="product in productList" :key="product.id">
              <div class="products__photo">
                <a href="" @click="goTo(product.id)"><img :src="product.picture" alt="Товар"></a>
              </div>
              <div class="products__product-bottom">
                <a href="" @click="goTo(product.id)"><p class="products__description">{{product.name}}</p></a>
                <div class="products__info">
                  <span class="products__cost">{{product.price}} <img src="../assets/images/uah.png" alt="Грн."></span>
                  <a v-if="product.incart" href="/cart"><button class="products__incart"><i class="fa fa-shopping-basket"></i></button></a>
                  <button v-else @click="addToCart(product.id)" class="products__cart"><i class="fa fa-shopping-basket"></i></button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="recall__nav">
          <button class="next_btn" :disabled="pageNumber === 0">Назад</button>
          <span>{{1}} з</span>
          <span> {{2}}</span>
          <button class="prev_btn" :disabled="pageNumber >= pageCount -1">Вперед</button>
        </div>
        </div>
      </div>
    </section>
    <Footer/>
  </div>
</template>

<script>
import Nav from "../components/Nav";
import Footer from "../components/Footer";
import promo from "../components/promo";
import {mapMutations} from 'vuex'

export default {
  name: "Categorie_products",
  components: {
    Nav,
    Footer,
    promo
  },
  props: ['id'],
  data(){
    return{
      productList:[],
      prod:{},
      productInCartList:[],
      category:null,
      characters:[],
      z:[]
    }
  },
  created() {
    this.loadlistProducts()

  },
  methods:{
    async loadlistProducts(){
      this.productList = await fetch(
          `${this.$store.getters.getSeverUrl}/product_categories/${this.id}`
      ).then(response => response.json())
      this.loadCaharacters()
      this.getCategory()
      this.Products()
    },
    async loadCaharacters(){
      this.characters = await fetch(
          `${this.$store.getters.getSeverUrl}/characters/${this.id}`
      ).then(response => response.json())
    },
    getCategory(){
      this.category = this.productList[0].category
    },
    goTo(id){
      this.$router.push({name : 'product', params: {id: id} })
    },
    ...mapMutations(['getCartData']),
    addToCart(id){
      let data = this.productList
      this.prod = data.filter(produ => produ.id === id)
      for(let i = 0; i<=this.prod.length-1;i++){
        this.prod[i].incart=true
        this.getCartData(this.prod[i])
      }
    },
    Products(){
      this.productInCartList=this.$store.state.cart
      for(let i = 0; i<=this.productList.length-1;i++){
        for(let j = 0; j<=this.productInCartList.length-1;j++){
          if(this.productList[i].name === this.productInCartList[j].name){
            this.productList[i].incart=true
          }
        }
      }
    },
  },
}
</script>

<style scoped>

.s{
  display: flex;
  align-items: center;
  flex-direction: column;
}
.recall__nav{
  padding: 30px 0;
}
.next_btn{
  margin-right: 10px;
  border:none;
  background-color: #fff;
  color:red
}
.prev_btn{
  margin-left: 10px;
  border:none;
  background-color: #fff;
  color:red
}

.wrap{
  width: 100%;
  max-width: 1320px;
  margin: 0 auto;
  display: flex;
}
.products__filter{
  margin-top: 25px;
  width: 299px;
  min-width: 299px;
  margin-right: 15px;
  border-right: 1px solid #222;
}
a{
  text-decoration: none;
  color: black;
}
h3{
  text-align: center;
  font-size: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid #222;
}
.products__cont{
  width: 100%;
  margin-top: 30px;
  font-size: 24px;
  display:flex;
  flex-direction: column
}
.products__content{
  margin-left: 25px;
  padding-top: 25px;
  width: 100%;
  display: flex;
  flex-wrap: wrap;
}
.products__product {
  margin-bottom: 15px;
  margin-right: 15px;
  width: 225px;
  height: 340px;
  background-color: #eff1f0;
  box-shadow: 0 0 10px #b1b7d6;
}
.products__description{
  width: 215px;
  padding: 0 5px;
  min-height: 40px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  font-size: 14px;
  line-height: 20px;
  margin-bottom: 7px;
}
.products__photo>a{
  text-decoration: none;
  margin: 5px;
  height: 200px;
  width: 215px;
  background-color: #fff;
  padding-bottom: 15px;
  display: block;
  position: relative;
}
.products__photo>a>img {
  max-width: 200px;
  max-height: 215px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  vertical-align: middle;
}
.products__cart,.products__incart {
  outline: none;
  cursor: pointer;
  margin-left: 12px;
  width: 45px;
  height: 45px;
  background-color: #e01f1f;
  border: none;
  border-radius: 50%;
  color: #fff;
  font-size: 20px;
}
.products__incart{
  background-color: green;
}
.products__product-bottom{
  margin-top: 15px;
}
.products__info{
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 210px;
  margin: 0 auto;
  margin-bottom: 15px;
}
.products__cost{
  margin-top: 10px;
  font-size: 22px;
}
.products__cost>img{
  width: 15px;
  height: 20px;
  padding-bottom: 5px;
}
.products__filter-mob{
  display: none;
}
.slidecontainer{
  margin: 20px
}
.slider {
  -webkit-appearance: none;
  width: 100%;
  height: 15px;
  border-radius: 5px;
  background: #d3d3d3;
  outline: none;
  opacity: 0.7;
  -webkit-transition: .2s;
  transition: opacity .2s;
}

.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 25px;
  height: 25px;
  border-radius: 50%;
  background: #e01f1f;
  cursor: pointer;
}
@media screen and (max-width: 1390px) {
  .wrap{
    max-width: 1100px;
  }
  .products__content{
    width: 100%;
    margin-left: 0;
  }
  .products__product:nth-child(3n) {
    margin-right: 0;
  }

}
@media screen and (max-width: 1150px) {
  .wrap{
    max-width: 950px;
  }

  .products__product:nth-child(3n) {
    margin-right: 15px;
  }
  .products__product:nth-child(2n) {
    margin-right: 0;
  }
  .products__content{
    margin-left: 45px;
    width: 100%;
    justify-content: start;
    flex-wrap: wrap;
  }
}
@media screen and (max-width: 990px) {
  .wrap{
    max-width: 600px;
    display: block;
  }
  .products__filter{
    display: none;
  }
  .products__filter-mob{
    display: block;
    width: 92%;
    margin-left: 45px;
    height: 40px;
    border: 1px solid #222222;
    text-align: center;
    line-height: 40px;
  }
  .products__filter-mob>span{
    font-size: 20px;
    margin-right: 10px;
  }
  .products__product{
    margin-right: 40px;
  }
  .products__product:nth-child(3n) {
    margin-right: 40px;
  }
  .products__product:nth-child(2n) {
    margin-right: 0;
  }
  .products__content{
    margin-left: 75px;
    width: 100%;
    justify-content: start;
    flex-wrap: wrap;
  }
}
</style>