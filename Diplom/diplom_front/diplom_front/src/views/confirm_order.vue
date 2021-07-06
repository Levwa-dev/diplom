<template>
  <div class="wrap">
    <div class="buyer__info info">
      <div class="info__content">
        <h2>Дані покупця</h2>
        <form action="">
          <input onchange="style.border='1px solid #000'" id="first_name" v-model='first_name' type="text" class="info__first-name" placeholder="Им'я">
          <input onchange="style.border='1px solid #000'"  id="last_name" v-model='last_name' type="text" class="info__last-name" placeholder="Фамилия">
          <input onchange="style.border='1px solid #000'" id="patronymic" v-model='patronymic' type="text" class="info__patronymic" placeholder="Отчество">
          <input onchange="style.border='1px solid #000'" id="tel" v-model='tel' type="text"  class="info__tel" placeholder="Номер телефонa">
          <select onchange="style.border='1px solid #000'" id="region" v-model='region'>
            <option value="">Выберите область</option>
            <option value="Винницкая область">Винницкая область</option>
            <option value="Волынская область">Волынская область</option>
            <option value="Днепропетровская область">Дніпропетровська область</option>
          </select>
          <input onchange="style.border='1px solid #000'" id="city" v-model='city' type="text" class="info__city" placeholder="Город">
          <h2>Доставка</h2>
          <p><input onchange="style.border='1px solid #000'"  v-model='delivery' class="checkbox" type="radio" name="option1" value="Доставка Новою Поштою">Доставка Новою Поштою</p>
          <p><input onchange="style.border='1px solid #000'"  v-model='delivery' class="checkbox" type="radio" name="option1" value="Доставка УКРПОШТОЙ">Доставка УКРПОШТОЙ</p>
          <input  onchange="style.border='1px solid #000'" id="post" v-model='post' type="text"  class="info__post" placeholder="Номер отделения почты">
          <h2>Оплата</h2>
          <p><input onchange="style.border='1px solid #000'" v-model="payment" class="checkbox" type="radio" name="option2" value="Оплата при получении">Оплата при отриманні</p>
          <p><input onchange="style.border='1px solid #000'" @click="OnlinePay" v-model='payment' class="checkbox" type="radio" name="option2" value="Прямий безготівковий переказ">Прямий безготівковий переказ</p>
        </form>
        <button @click="sendOrder()" class="submit">Підтвердити замовлення</button>
      </div>
    </div>
  </div>
</template>

<script>

import {mapMutations} from 'vuex'

export default {
name: "confirm_order",
  props:['productInCartList', 'total'],
  data(){
  return{
    first_name: null,
    last_name:null,
    patronymic:null,
    tel:null,
    region:'',
    city:null,
    delivery:null,
    post:null,
    payment:null,
    val:true
    }
  },
  methods: {
  valid(){
    this.val = true
    if(this.first_name === null){
      document.getElementById('first_name').style.border='2px dashed red'
      this.val=false
    }
     if(this.last_name === null){
       document.getElementById('last_name').style.border='2px dashed red'
       this.val=false
     }
     if(this.patronymic == null){
       document.getElementById('patronymic').style.border='2px dashed red'
       this.val=false
     }
     if(this.tel == null){
       document.getElementById('tel').style.border='2px dashed red'
       this.val=false
     }
     if(this.region == null){
       document.getElementById('region').style.border='2px dashed red'
       this.val=false
     }
     if(this.city == null){
       document.getElementById('city').style.border='2px dashed red'
       this.val=false
     }
     if(this.post == null){
       document.getElementById('post').style.border='2px dashed red'
       this.val=false
     }
     if(this.val===false){
        alert("Заполните форму правильно")
     }



  },
    async sendOrder(){
      this.valid()
      if (this.val===true){
        let cartList = []
        for(let i =0;i<=this.productInCartList.length-1;i++){
          let prod={
            name:this.productInCartList[i].name,
            quantity:this.productInCartList[i].quantit,
            price: this.productInCartList[i].summaryPrice,
            product_id: this.productInCartList[i].id
          }
          cartList.push(prod)
        }
        let data = {
          first_name: this.first_name,
          last_name: this.last_name,
          patronymic: this.patronymic,
          telephone: this.tel,
          region: this.region,
          city: this.city,
          delivery: this.delivery,
          post: this.post,
          payment: this.payment,
          total:this.total,
          cart:cartList
        }
        await fetch(`${this.$store.getters.getSeverUrl}/order_s_info/`,
            {
              method: "POST",
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify(data)
            }
        ).then(Response => Response).catch(err => alert(err));
        this.$store.commit('resetCart');
        this.$router.push('/thanks')
      }

    },
    async OnlinePay(){
      this.valid()
      if (this.val===true){
        let data = {
          amount: this.total
        }
        this.localOrderInfo()
        fetch(`${this.$store.getters.getSeverUrl}/payUrl/`,
            {
              method: "POST",
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify(data)
            }
        ).then((response) => {
          response.json().then((data) => {
            window.location = (data.payUrl)
          })
        })
      }
    },
    ...mapMutations(['getOrderInfo']),
    localOrderInfo(){
    let cartList = []
      for(let i =0;i<=this.productInCartList.length-1;i++){
        let prod={
          name:this.productInCartList[i].name,
          quantity:this.productInCartList[i].quantit,
          price: this.productInCartList[i].summaryPrice,
          product_id: this.productInCartList[i].id
        }
        cartList.push(prod)
      }
      let orderInfo = {
        first_name: this.first_name,
        last_name: this.last_name,
        patronymic: this.patronymic,
        telephone: this.tel,
        region: this.region,
        city: this.city,
        delivery: this.delivery,
        post: this.post,
        payment: null,
        total:this.total,
        cart:cartList
      }
      this.getOrderInfo(orderInfo)
    }
  }
}
</script>

<style scoped>
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
.buyer__info{
  display: flex;
  justify-content: center;
}

.info__content,form{
  display: flex;
  flex-direction: column;
}
input,select{
  height: 30px;
  width: 400px;
  margin: 10px;
  border: 1px solid #000;
  border-radius: 5px;
}
select{
  width: 407px;
  height: 35px;
}
.checkbox{
  height: 15px;
  width: 15px;
  margin: 10px;
}
.submit{
  margin: 0 auto;
  margin-top: 25px;
  margin-bottom: 40px;
  width: 250px;
  height: 40px;
  border: 1px solid;
  font-size: 20px;
  border-radius: 5px;
}
.submit:hover{
  color: #fff;
  background-color: crimson;
}
@media screen and (max-width: 1390px) {
  .wrap {
    max-width: 1100px;
  }
}
@media screen and (max-width: 1150px) {
  .wrap{
    max-width: 950px;
  }
}
@media screen and (max-width: 990px) {
  .wrap {
    max-width: 600px;
  }
}
</style>