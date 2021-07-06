<template>
  <header class="header">
    <div class="header__top">
      <div class="wrap">
        <div class="header__logo">
          <img src="../assets/images/logo.png" alt="LOGO">
          <span>IT-GALAXY</span>
        </div>
        <div class="header__contact contact">
          <span class="contact__title">Позвонити нам безкоштовно</span>
          <div class="contact__phone">
            <a class="contact__number" href="tel:++380888888888"><i class="fas fa-phone contact__icon"></i> 088-88-88-888</a>
          </div>
        </div>
         <div class="header__work work">
          <i class="far fa-clock"></i>
          <span class="work__time">08:00-21:00</span>
        </div>
        <div class="header__cart cart">
          <a href="/cart"><i class="fas fa-shopping-cart"></i></a>
          <div class="cart__sum">
            <span>{{productInCartList.length}}</span>
          </div>
        </div>
      </div>
    </div>
    <div class="header__bottom">
      <div class="wrap__bottom">
        <div class="header__navigation nav">
          <nav class="nav">
            <ul class="nav__list">
              <li class="nav__item"><a href="/">Головна</a></li>
              <li class="nav__item"><a href="/about-us">Про нас</a></li>
              <li class="nav__item"><a href="/contacts">Контакти</a></li>
              <li class="nav__item"><a href="/authorization">Ввійти</a></li>
            </ul>
          </nav>
        </div>
        <div class="header__mobile mobile">
          <span class="mobile__menu">Меню</span>
          <nav class="mobile__nav">
            <ul class="mobile__list">
              <li>
                <div class="mobile__catalog" >
                  <span>Каталог</span>
                  <i class="fas fa-bars header__bars"></i>
                  <div class="mobile__dropdown dropdown">
                    <ul class="dropdown__content" v-for="category in categories" :key="category.id">
                      <li><a href="" @click="goto(category.id)">{{category.name}}</a></li>
                    </ul>
                  </div>
                </div>
              </li>
              <li class="nav__item"><a href="/">Главная</a></li>
              <li class="nav__item"><a href="/about-us">О нас</a></li>
              <li class="nav__item"><a href="/contacts">Контакты</a></li>
              <li class="nav__item"><a href="/authorization">Войти</a></li>
            </ul>
          </nav>
        </div>
        <div class="header__search search">
          <div>
            <input v-model='searchValue' v-on:keyup.enter="search(searchValue)" type="search" placeholder="Пошук...">
            <i v-if="this.searchValue !=''" class="serach__cancel" @click="clearSearch()">X</i>
          </div>
          <button class="search__btn" @click="search(searchValue)"><i class="fas fa-search"></i></button>
          <div class="header__catalog" >
            <span>Каталог</span>
            <i class="fas fa-bars header__bars"></i>
            <div class="header__dropdown dropdown">
              <ul class="dropdown__content" v-for="category in categories" :key="category.id">
                <li><a href="" @click="goto(category.id)">{{category.name}}</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import {mapActions, mapGetters} from "vuex";


export default {
  name: "Nav",
  data() {
    return {
      categories:[],
      productInCartList:[],
      searchValue:''
    }
  },
  created() {
    this.loadlistCategories()
    this.Products()
  },
  computed:{
    ...mapGetters([
      'SEARCH_VALUE'
    ]),
  },
  methods: {
    async loadlistCategories() {
      this.categories = await fetch(
          `${this.$store.getters.getSeverUrl}/categories`
      ).then(respone => respone.json())
    },
    goto(id){
      this.$router.push({name : 'categorie_product', params: {id: id} })
    },
    Products(){
      this.productInCartList = this.$store.state.cart
      this.searchValue = this.SEARCH_VALUE
    },

    ...mapActions(['GetSearchValue']),
    search(value){
      this.GetSearchValue(value)
      if(this.$route.path !== '/'){
        this.$router.push('/')
      }
     },
    clearSearch(){
      this.searchValue = ''
      this.GetSearchValue(this.searchValue)
    }
  },
  watch:{
    searchValue(){
      if(this.searchValue == ''){
        this.clearSearch()
      }
    }
  }
}

</script>
<style scoped>
  .header {
    width: 100%;
    color: #fff;
  }
  .wrap,.wrap__bottom {
    width: 100%;
    max-width: 1320px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .header__top {
    background-color: #222222;
  }
  .header__logo {
    width: 240px;
    margin-right: 20px;
  }
  .header__logo>img {
    width: 90px;
    height: 80px;
  }
  .header__logo>span {
    font-weight: bold;
    font-size: 26px;
    color: #3bf5d3;
    text-shadow: 2px 2px 2px #21a6c4;
  }
  .work__time {
    font-size: 20px;
    margin-left: 5px;
  }
  .header__contact{
    width: 200px;
    margin-right: 20px;
    font-size: 12px;
  }
  .contact__phone {
    margin-top: 5px;
  }
  .contact__icon {
    font-size: 20px;
  }
  .contact__number {

    font-weight: bold;
    font-size: 18px;
    text-decoration: none;
    color: #fff;
  }
  .header__cart {
    width: 60px;
    font-size: 40px;
    position: relative;

  }
  .header__cart>a {
    text-decoration: none;
    color: #fff;
  }
  .cart__sum {
    position: absolute;
    text-align: center;
    top: -5px;
    left: 40px;
    width: 20px;
    height: 20px;
    font-size: 20px;
    background-color: #e01f1f;
    border-radius: 10px;

  }
  .header__bottom {
    background-color: #e01f1f;
    min-height: 86px;
    display: flex;
    font-size: 18px;
    text-transform: uppercase;
  }
  .header__search {
    display: flex;
    justify-content: space-between;

  }
  .header__search>div{
    position: relative;
  }
  .header__search>div>input {
    height: 30px;
    width: 200px;
    border: 1px solid #000;
    border-right: none;
  }
  .search__btn {
   width: 40px;
   height: 34px;
   background-color: #fff;
   border: 1px solid #000;
   border-left:none;
  }
  .serach__cancel{
    font-size: 22px;
    color: #000;
    position: absolute;
    top:5px;
    left: 190px;
    cursor: pointer;
  }
  .header__catalog {
    width: 150px;
    border: 1px solid #000;
    text-align: center;
    line-height: 30px;
    background-color: #222222;
    position: relative;
    cursor: pointer;
  }
  .header__bars {
    font-size: 16px;
    margin-left: 5px;
  }
  .header__dropdown {
    display: none;
    border: 1px solid #000;
    min-width: 395px;
    line-height: 30px;
    text-align: center;
    background-color: #222222;
    position: absolute;
    left: -246px;
    z-index: 1;
  }
  .dropdown__content>li>a {
    text-decoration: none;
    color: #fff;
  }
  .header__catalog:hover .header__dropdown {
      display: block;
  }
  .nav__list {
    width: 400px;
    display: flex;
    justify-content: space-between;
  }
  .nav__list>li>a {
    text-decoration: none;
    color: #fff;
  }
  .nav__list>li>a:hover {
    text-decoration: none;
    color: #fff;
    font-weight: bold;
  }

  .header__mobile {
    display: none;
  }

  @media screen and (max-width: 1390px) {
    .wrap,.wrap__bottom{
      max-width: 1100px;
    }
    .header__cart {
    width: 50px;
    margin-right: 0px;
    }
    .nav__list {
    padding-right: 0px;
    }
  }
   @media screen and (max-width: 1150px) {
     .wrap,.wrap__bottom {
       max-width: 950px;
     }
   }
  @media screen and (max-width: 990px) {
      .wrap,.wrap__bottom{
        max-width: 600px;
        flex-wrap: wrap;
    }
    .header__logo,.header__contact {
      width: 235px;
      margin: 0;
    }
    .header__contact {
      text-align: right;
    }
    .header__work {
      margin-left: 50px;
    }
    .header__cart {
      margin-right: 50px;
      margin-bottom: 10px;
    }
    .header__search {
      flex-wrap: wrap;
    }
   .header__navigation {
     display: none;
   }
    .header__mobile{
      margin-left: 45px;
      display: block;
      height: 32px;
      width: 150px;
      border: 1px solid #000;
      text-align: center;
      line-height: 30px;
      background-color: #222222;
      position: relative;
      cursor: pointer;
    }
    .mobile__nav {
    display: none;
    border: 1px solid #000;
    min-width: 150px;
    line-height: 30px;
    text-align: center;
    background-color: #222222;
    position: absolute;
    left: -1px;
    z-index: 1;
   }
    .header__mobile:hover .mobile__nav {
      display: block;
  }
    .nav__item>a{
      text-decoration: none;
      text-align: center;
      color: #fff;
    }
    .header__catalog{
      display: none;
    }
    .mobile__dropdown{
    display: none;
    border: 1px solid #000;
    min-width: 300px;
    line-height: 30px;
    text-align: center;
    background-color: #222222;
    position: absolute;
    left: 150px;
    top: -1px;
    z-index: 2;
   }
     .mobile__catalog:hover .mobile__dropdown {
      display: block;
  }
  }
</style>