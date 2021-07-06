<template>
  <section class="cart">
    <div class="wrap" v-if="productInCartList.length">
      <h2>Ваші покупки</h2>
      <div class="cart__content">
        <div class="cart__description description">
          <ul class="description__list">
            <li class="description__photo">Фото</li>
            <li class="description__name">Назва</li>
            <li class="description__quantity">Кіл-сть</li>
            <li class="description__price">Ціна</li>
            <li class="description__summ">Разом</li>
          </ul>
        </div>
        <div class="cart__product" v-for="product in productInCartList" :key="product.id">
          <div class="cart__photo">
            <img :src="product.picture" alt="Фото продукта">
            <span class="cart__name-mob">{{ product.name }}</span>
          </div>
          <div class="cart__name">
            <span>{{product.name}}</span>
          </div>
          <div class="cart__quantity quantity">
            <button class="quantity__minus" @click="quantityMinus(product.id)"></button>
            <div class="quantity__total">{{product.quantit}}</div>
            <button class="quantity__plus" @click="quantityPlus(product.id)"></button>
          </div>
          <div class="cart__price">
            <span>{{product.price}} грн.</span>
          </div>
          <div class="cart__summ">
            <span>{{product.summaryPrice}} грн.</span>
            <i @click="removeFromCart(product)" class="fas fa-trash"></i>
          </div>
        </div>
        <div class="cart__summary summary">
          <span class="summary__text">Всього до сплати: {{totalPrice}} грн.</span>
        </div>
      </div>
      <div class="cart__confirm">
        <button v-if="show == false" class="confirm" @click="SendOrder()">Оформити замовлення</button>
      </div>
      <confirm_order v-if="show == true" :productInCartList="productInCartList" :total="totalPrice"></confirm_order>
    </div>
    <div class="wrap" v-else>
      <h2 class="h_none">Ваш кошик порожній</h2>
      <div class="cart__none">
        <a class="continue__shop" href="/">Продолжить покупки</a>
      </div>
    </div>
  </section>
</template>

<script>
import confirm_order from "../views/confirm_order";
export default {
  name: "cart_content",
  props:['productInCartList'],
  data(){
    return{
      prod:[],
      data:this.productInCartList,
      show:false,
    }
  },
  created() {
    this.countSummaryProductPrice()
  },
  methods:{
    removeFromCart(product) {
      this.$store.commit('removeFromCart', product);
    },
    countSummaryProductPrice() {
      for(let i = 0; i<=this.productInCartList.length-1;i++){
        this.productInCartList[i].summaryPrice = this.productInCartList[i].price * this.productInCartList[i].quantit
      }
    },
    quantityPlus(id){
      this.prod = this.data.filter(produ => produ.id === id)
      for(let i = 0; i<=this.prod.length-1;i++){
        this.prod[i].quantit++
      }
      this.countSummaryProductPrice()

    },
    quantityMinus(id){
        this.prod = this.data.filter(produ => produ.id === id)
        for(let i = 0; i<=this.prod.length-1;i++){
          if(this.prod[i].quantit >1){
            this.prod[i].quantit--
          }
      }
      this.countSummaryProductPrice()
    },
    SendOrder(){
      this.show = true
    }
  },
  computed:{
    totalPrice() {
      let total = 0;
      for (let item of this.productInCartList) {
        total += item.summaryPrice;
      }
      return total;
    }
  },
  components:{
    confirm_order,
  }
}
</script>

<style scoped>
  section{
    margin-top: 25px;
    margin-bottom: 25px;
  }
  .wrap{
    width: 100%;
    max-width: 1380px;
    margin: 0 auto;
  }
   h2{
    font-size: 25px;
    text-align: center;
    width: 300px;
    margin: 0 auto;
    margin-top: 25px;
    margin-bottom: 40px;
  }
  .cart__content{
    width: 100%;
  }
  .cart__description,.cart__product,.cart__summary{
    border: 1px solid black;
    width: 100%;
    height: 40px;
  }
  .cart__product{
    border-top: none;
    min-height: 200px;
    display: flex;
    align-items: center;
  }
  .cart__summary{
    border-top: none;
  }
  .description__list,.summary__text{
    display: flex;
    text-transform: uppercase;
    font-weight: bold;
    text-align: center;
    line-height: 40px;
  }
  .cart__summary{
    display: flex;
    justify-content: flex-end;
  }
  .summary__text{
    margin-right: 25px;

  }
  .description__photo,.description__quantity,.description__price,.description__summ{
    width: 270px;
  }
  .description__photo{
    width: 200px;
  }
   .description__name {
     width: 350px
   }
   .cart__photo{
     width: 200px;
     height: 200px;
     text-decoration: none;
     background-color: #fff;
     display: block;
     position: relative;
  }
    .cart__photo>img{
      max-width: 190px;
      max-height: 160px;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%,-50%);
      vertical-align: middle;
     }
   .cart__name{
     font-size: 20px;
     width: 100%;
     max-width: 350px;
     text-align: center;
     margin-left: 15px;
   }
   .cart__quantity{
     width: 100%;
     max-width: 250px;
     display: flex;
     justify-content: center;
   }
   button{
     outline: none;
     position: relative;
     background-color: #fff;
     border-radius: 50%;
     border: none;
     height: 44px;
     width: 44px;
   }
   .quantity__minus:before{
     content: "\f056";
     font-family: FontAwesome;
     font-size: 46px;
     position: absolute;
     top: -1px;
     left: 0px;
     color: crimson;
   }
   .quantity__plus:before{
     content: "\f055";
     font-family: FontAwesome;
     font-size: 46px;
     position: absolute;
     top: -1px;
     left: 0px;
     color: crimson;
   }
   .quantity__total{
     margin-left: 2px;
     font-size: 20px;
     width: 44px;
     height: 44px;
     text-align: center;
     line-height: 44px;
   }
   .cart__price{
     width: 100%;
     margin-left: 10px;
     max-width: 285px;
     text-align: center;
     font-size: 20px;
   }
    .cart__summ{
     width: 100%;
     max-width: 230px;
     text-align: center;
     font-size: 20px;
     color: crimson;
   }
    .cart__summ>i{
      margin-left: 15px;
      font-size: 25px;
      cursor: pointer;
    }
    .cart__name-mob{
      display: none;
    }
    .cart__confirm{
      width: 100%;
      display: flex;
      justify-content: center;
    }
    .confirm{
      margin-top: 40px;
      margin-bottom: 40px;
      width: 240px;
      height: 40px;
      border: 1px solid;
      font-size: 20px;
      border-radius: 5px;
    }
    .confirm:hover{
      color: #fff;
      background-color: crimson;
    }
    .h_none{
      font-size: 30px;
      text-align: center;
      width: 350px;
      margin: 0 auto;
      margin-top: 70px;
      margin-bottom: 40px;
    }
    .cart__none{
      display: flex;
      justify-content: center;
      margin-bottom: 100vh;
    }
    .continue__shop{
      text-decoration: none;
      color: #000000;
      font-size: 25px;
      border: 1px solid;
      border-radius: 4px;
      padding: 10px;
      margin: 0 auto;
    }
    .continue__shop:hover{
      color: #fff;
      background-color: #e01f1f;
    }
    @media screen and (max-width: 1390px) {
      .wrap {
         max-width: 1100px;
      }
      .cart__name{
        max-width: 230px;
      }
      .cart__quantity{
         margin-left: 40px;
         max-width: 180px;
      }
      .cart__price{
        margin-left: 40px;
        max-width: 180px;
      }
    }

  @media screen and (max-width: 1150px) {
    .wrap{
        max-width: 950px;
    }
      .cart__photo{
        width: 140px;
        height: 110px;
    }
     .cart__photo>img{
        width: 130px;
        height: 110px;
     }
     .cart__name{
       width: 240px;
       font-size: 16px;
      }
     .cart__quantity{
         margin-left: 10px;
         max-width: 160px;
      }
     .cart__price{
        margin-left: 30px;
        max-width: 170px;
      }
     .cart__summ{
       margin-top: -3px;
       width: 180px;
     }
     .quantity__minus:before,.quantity__plus:before{
       font-size: 36px;
     }
    button{
      margin-top:5px;
      width: 34px;
      height: 34px;
    }
  }
  @media screen and (max-width: 990px) {
      .wrap {
        max-width: 600px;
      }
     .cart__photo{
        width: 75px;
        height: 65px;
        margin-left: 35px;
      }
     .cart__photo>img{
        width: 140px;
        height: 130px;
        padding: 5px;
      }
     .cart__quantity{
         margin-left: 30px;
         max-width: 150px;
      }
     .cart__price{
        margin-left: 10px;
        max-width: 130px;
        font-size: 16px;
      }
     .cart__summ{
       margin-left: 30px;
       max-width: 130px;
       padding-top: 5px;
       font-size: 16px;
      }
     .cart__summ>i{
       font-size: 18px;
      }
    button{
     outline: none;
     position: relative;
     background-color: #fff;
     border-radius: 50%;
     border: none;
     height: 34px;
     width: 34px;
   }
   .quantity__minus:before{
     content: "\f056";
     font-family: FontAwesome;
     font-size: 35px;
     position: absolute;
     top: -1px;
     left: 0px;
     color: crimson;
   }
   .quantity__plus:before{
     content: "\f055";
     font-family: FontAwesome;
     font-size: 35px;
     position: absolute;
     top: -1px;
     left: 0px;
     color: crimson;
   }
   .cart__name-mob{
    display: block;
    width: 150px;
    margin-left: -35px;
    margin-top: 100px;
    text-align: center;
  }
  .cart__product{
    border-top: none;
    min-height: 230px;
    display: flex;
    align-items: center;
  }
    .cart__name{
      display: none;
    }
    .description__name{
      display: none;
    }
    }
</style>