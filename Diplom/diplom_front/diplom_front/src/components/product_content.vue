<template>
  <section class="about-us">
    <div class="wrap">
      <div class="product__content">
        <div class="product__photos photos">
          <div class="photos__list">
            <div v-if="this.countSlides>0" class="photos__item" :style="{'margin-left': '-' + (100*currentSlideIndex) +'%'}">
              <slider_item
                v-for="item in prod.slides"
                :key="item.id"
                :item_data="item"
            />
            </div>
            <div v-else class="photos__item"><img :src="prod.picture" alt=""></div>
          </div>
          <button @click="previousSlide" class="left"><i class="fas fa-arrow-left"></i></button>
          <button @click="nextSlide" class="right"><i class="fas fa-arrow-right"></i></button>
        </div>
        <div class="product__buy buy">
          <h3 class="buy__title">{{prod.name}}</h3>
          <div class="buy__main">
            <div class="buy__info">
              <span class="buy__cost">{{prod.price}} грн.</span>
              <span v-if = 'prod.inStock' class="buy__in-stock">Є в наявності</span>
              <span v-else class="buy__out-of-stock">Нет в наличии</span>
            </div>
            <button v-if="prod.incart==false" @click="addToCart" class="buy__btn">Купити</button>
            <a v-if="prod.incart==true" href="/cart"><button class="buy__btn-in">Товар в кошику</button></a>
          </div>
          <div class="buy__guarantee guarantee">
            <div class="guarantee__title">Гарантія</div>
            <p>12 місяців.</p>
            <p>Обмін / повернення товару протягом 14 днів.</p>
          </div>
        </div>
      </div>
      <div class="product__info">
        <div class="product__characteristic">
          <div class="product__description description">
            <div class="description__title">Опис товару</div>
            <p class="description__text">{{prod.description}}</p>
          </div>
          <div class="description__title">Характеристики</div>
          <div class="character__content character" v-for="charact in prod.characters" :key="charact.id">
            <div class="character__body">
              <span class="character__name">{{charact.character}}</span>
              <span class="character__description">{{charact.chararacter_v}}</span>
            </div>
          </div>
        </div>
        <div class="product__recall recall">
          <h2 class="recall__title">Відгуки покупців</h2>
          <div v-if="paginatedData.length>0" class="recall__body">
            <div v-for="coment in paginatedData" :key="coment.id" >
              <div class="recall__comment comment">
                <div class="comment__header">
                  <span class="comment__fname">{{coment.first_name}}</span>
                  <span class="comment__lname">{{coment.last_name}}</span>
                  <span class="comment__date">{{coment.date}}</span>
                </div>
                <div class="comment__text">{{coment.text}}</div>
                <button @click="modalOpen( '.popup', '.form__close', coment.id)" class="comment__reply">Ответить</button>
              </div>
              <div v-for="child in coment.children " :key="child.id">
                <div class="recall__comment comment" style="margin-left: 19px; width: 600px">
                  <div class="comment__header" style="width: 580px">
                    <span class="comment__fname">{{child.first_name}}</span>
                    <span class="comment__lname">{{child.last_name}}</span>
                    <span class="comment__date">{{child.date}}</span>
                  </div>
                  <div class="comment__text"><span style="font-weight: bold; margin-left: 20px">{{coment.first_name}} {{coment.last_name}}</span>,<br/>{{child.text}}</div>
                  <button @click="modalOpen( '.popup', '.form__close', child.id)" class="comment__reply">Ответить</button>
                </div>
              </div>
            </div>
          </div>
          <div v-else class="recall__title2">
            <h2>До цього товару немає жодного відгука</h2>
          </div>
          <div v-if="paginatedData.length>0" class="recall__nav">
            <button class="next_btn" :disabled="pageNumber === 0"  @click="prevPage">Назад</button>
            <span>{{pageNow}} з</span>
            <span> {{pageCount}}</span>
            <button class="prev_btn" :disabled="pageNumber >= pageCount -1" @click="nextPage">Вперед</button>
          </div>
          <button @click="modalOpen( '.popup', '.form__close')" class="recall__popup">Залишити відгук</button>
        </div>
      </div>
      <div class="popup">
        <div class="recall__form form">
          <div class="form__header">
            <h2 class="form__title">Оставить отзыв</h2>
            <span class="form__close">X</span>
          </div>
          <div class="form__body">
            <input v-model="email" type="text" class="form__email" placeholder="Ваш email">
            <input v-model="fname" type="text" class="form__fname" placeholder="Ваше имя">
            <input v-model="lname" type="text" class="form__lname" placeholder="Ваша фамилия">
            <textarea  v-model="text" class="form__text" cols="30" rows="10" placeholder="Коментарий"></textarea>
            <button @click="sendReview" class="form__btn">Отправить</button>
          </div>
          <span class="form__invalid" v-if="this.valid === false">Форма заполнена некорректно</span>
          <span class="form__valid" v-if="this.valid === true">Спасибо за ваш отзыв</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import slider_item from '../components/slider_item'
import {mapMutations} from 'vuex'

export default {
  name: "product_content",
  props:['prod', 'reviews','countSlides'],
  components: {
     slider_item
  },
  data (){
    return{
      currentSlideIndex: 0,
      productInCartList:[],
      pageNumber:0,
      pageNumber2:1,
      size:4,
      email:null,
      fname:null,
      lname:null,
      text:null,
      regWord: /[A-Za-zА-Яа-яЇїІіЁё]/,
      regEmail: /^(([^<>()[\]\\.,;:\s@]+(\.[^<>()[\]\\.,;:\s@]+)*)|(.+))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
      vlname:false,
      vfname:false,
      vemail:false,
      vtext:false,
      valid:null
    }
  },
  methods:{
    ...mapMutations(['getCartData']),
    addToCart(){
        this.prod.incart=true
        this.getCartData(this.prod)
    },
    previousSlide(){
      if(this.currentSlideIndex>0){
        this.currentSlideIndex--
      }
      if(this.currentSlideIndex===0){
        this.currentSlideIndex=this.prod.slides.length-1
      }
    },
    nextSlide(){
      if (this.currentSlideIndex >= this.prod.slides.length-1){
        this.currentSlideIndex = 0
      }
      else{
        this.currentSlideIndex++
      }
    },
    nextPage(){
      this.pageNumber++
      this.pageNumber2++
    },
    prevPage(){
      this.pageNumber--
      this.pageNumber2--
    },
    validation() {
      if (!this.regWord.test(this.fname) || this.fname == null) {
        this.vfname = true
      } else {this.vfname = false}

      if (!this.regWord.test(this.lname) || this.lname == null) {
        this.vlname = true
      } else {this.vlname = false}

      if (!this.regEmail.test(this.email) || this.email == null) {
        this.vemail = true
      } else {this.vemail = false}

      if(this.text === null){
        this.vtext = true
      } else {this.vtext = false}

      if ((this.vfname || this.vlname || this.vemail || this.vtext) === false){
        this.valid = true
      }else{this.valid = false}
    },
    addParent(id){
      this.parent = id
    },
    async sendReview(){
      this.validation()
      if(this.valid===true){
        let data = {
          email:this.email,
          first_name:this.fname,
          last_name:this.lname,
          text:this.text,
          product:this.prod.id,
          parent:this.parent
        }
        await fetch(`${this.$store.getters.getSeverUrl}/review/`,
            {
              method: "POST",
              headers:{
                'Content-Type': 'application/json',
              },
              body: JSON.stringify(data)
            }
            ).then(Response => Response).catch(err => alert(err))
        location.reload()
      }
    },
    modalOpen(popupsel, closesel, id){
      this.addParent(id)
      const modal = document.querySelector(popupsel)
      const close = document.querySelector(closesel)
      const pop = document.querySelector('.popup')
      pop.style.display = 'flex';
      document.body.style.overflow = '';

      close.addEventListener('click', () => {
        modal.style.display = 'none';
        document.body.style.overflow = '';
      })
      modal.addEventListener('click',(e) => {
        if (e.target === modal){
          modal.style.display = 'none'
          document.body.style.overflow = '';
        }
      })
    },
  },
  computed:{
    pageCount(){
      let l = this.reviews.length,
          s = this.size
      return Math.ceil(l/s)
    },
    paginatedData(){
      const start = this.pageNumber * this.size,
          end = start + this.size
      return this.reviews.slice(start, end)
    },
    pageNow(){
      return this.pageNumber2
    }
  },
}
</script>

<style scoped>
  section{
    margin-top: 25px;
    margin-bottom: 125px;
  }
  .wrap{
    position: relative;
    width: 100%;
    max-width: 1320px;
    margin: 0 auto;
  }
  .buy__title{
    margin-top: 35px;
    font-size: 20px;
    width: 100%;
    text-align: center;
    margin-bottom: 90px;
  }
  .product__content{
    width: 100%;
    display: flex;
  }
  .product__photos{
    position: relative;
    width: 500px;
  }
   .photos__list{
     margin: 0 auto;
     max-width: 400px;

     overflow: hidden;
  }
   .photos__item{
     display: flex;
   }
   .photos__item-none{
     margin-left: 40px;
     margin-right: 40px;
   }
  .left,.right{
    position: absolute;
    top: 40%;
    border-radius: 50%;
    height: 40px;
    width: 40px;
    background-color: #fff;
    color: crimson;
    font-size: 20px;
    border: 1px solid crimson;
  }
  .right{
    right: 0;
  }
  .product__buy{
    width: 600px;
    margin-left: 200px;
    margin-top: 10px;
    box-shadow: 0 0 10px #b1b7d6;
    display: flex;
    flex-direction: column;
  }
  .buy__main{
    display: flex;
    justify-content: space-between;
    margin-left: 30px;
    margin-right: 30px;
  }
  .buy__btn{
    width: 150px;
    height: 50px;
    margin-top: 5px;
    font-size: 20px;
    background-color:#e01f1f;
    color: #fff;
    border-radius: 10px;
    border: none;
  }
  .buy__btn-in{
    width: 150px;
    height: 50px;
    margin-top: 5px;
    font-size: 20px;
    background-color:forestgreen;
    color: #fff;
    border-radius: 10px;
    border: none;
  }
  .buy__btn:hover{
    background-color: #f01347;
  }
  .buy__info{
    display: flex;
    flex-direction: column;
  }
  .buy__cost{
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 15px;
  }
  .buy__in-stock{
    font-size: 16px;
    color: #1dd10d;
    margin-bottom: 15px;
  }
   .buy__out-of-stock{
    font-size: 16px;
    color: crimson;
     margin-bottom: 15px;
  }
   .buy__guarantee{
     margin-top: 50px;
   }
   .guarantee__title{
     text-align: center;
     font-size: 18px;
     margin-bottom: 15px;
   }
   .buy__guarantee p {
     text-align: center;
     margin-bottom: 10px;
   }
    .product__info {
      margin-top: 50px;
      display: flex;
    }
    .description__title,.recall__title{
      font-size: 26px;
      font-weight: bolder;
      margin-bottom: 20px;
    }
    .description__text{
      font-size: 18px;
      line-height: 2rem;
      width: 100%;
      max-width: 650px;
      margin-bottom: 20px;
    }
    .character__content{
      width: 650px;
    }
    .character__body{
      display: flex;
      justify-content: space-between;
      width: 100%;
      border-bottom: 1px solid #000000;
    }

    .character__name, .character__description{
      font-size: 20px;
      margin-bottom: 10px;
      margin-right: 15px;
      padding-top: 10px;
    }
    .slide{
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%,-50%);
      vertical-align: middle;
      max-width: 400px;
      max-height: 390px;
    }
    .product__characteristic{
      max-width: 650px;
      margin-right: 25px;
    }
    .product__recall{
      overflow: hidden;
      max-width: 650px;
      width: 100%;
      display: flex;
      align-items: center;
      flex-direction: column;
    }
    .recall__body{
      width: 100%;
      overflow-y: scroll;
      height: 640px;
    }
    .recall__comment{
      width:620px;
      min-height: 150px;
      border: 1px solid #000000;
      margin-bottom: 10px;
      margin-top: 10px;
      position: relative;
    }
    .comment__header{
      display: flex;
      width: 600px;
      padding: 10px 10px;
      position: relative;
      border-bottom: 1px solid #000000;
    }
    .comment__fname,.comment__lname{
      font-size: 16px;
      font-weight: bold;
      margin-right: 10px;
    }
    .comment__date{
      font-size: 16px;
      position: absolute;
      top:10px;
      right:10px;
    }
    .comment__text{
      font-size: 16px;
      line-height: 25px;
      margin-top: 10px;
      margin-bottom: 10px;
      max-width: 600px;
      width: 100%;
      padding: 5px;
      min-height: 60px;
    }
    .comment__reply{
      margin-left: 15px;
      margin-bottom: 15px;
      border:none;
      background-color: #fff;
      color:red
    }
    .recall__nav{
      margin-top: 15px;
      margin-bottom: 30px;
    }
    .next_btn{
      margin-right: 10px;
      border:none;
      background-color: #fff;
      color:red
    }
    .prev_btn,.recall__popup{
      margin-left: 10px;
      border:none;
      background-color: #fff;
      color:red
    }
  .recall__popup{
    font-size: 20px;
  }
    .form__title{
      padding: 20px 0px;
      font-size: 20px;
      text-align: center;
      width: 100%;
    }
    .form{
      margin: 20px 0;
      width: 500px;
      border: 1px solid #000;
      display: flex;
      flex-direction: column;
      background-color: #ffffff;

    }
    .form__body{
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
    }
  input{
    margin: 10px;
    height: 30px;
    width: 220px;
    border: 1px solid #000;
    border-radius: 5px;
  }
  .form__email{
    width: 300px;
    margin: 0 auto;
  }
  .form__text{
    width: 460px;
    margin: 0 20px;
    border: 1px solid #000;
    border-radius: 3px;
  }
  .form__header {
    display: flex;
  }
  .form__close{
    margin-top:10px;
    margin-right: 10px;
    font-size: 20px;
    color: red;
  }
  .form__close:hover{
    cursor: pointer;
  }
  .form__btn{
    margin: 0 auto;
    margin-top: 20px;
    margin-bottom: 20px;
    width: 200px;
    height: 40px;
    border: 1px solid;
    font-size: 18px;
    border-radius: 5px;
  }
  .form__invalid,.form__valid{
    text-align: center;
    color:red;
    font-size: 20px;
    margin-bottom: 20px;
  }
  .form__valid{
    color: forestgreen;
  }
  .popup{
    position: fixed;
    height: 100%;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.7);
    top: 0;
    left: 0;
    z-index: 100;
    display: none;
    justify-content: center;
    align-items: center;
  }
  .recall__title2{
    font-size: 20px;
    margin-top: 55px;
    margin-bottom: 20px;
    text-align: center;
  }
  @media screen and (max-width: 1390px) {
      .wrap {
        max-width: 1100px;
      }
      .product__photos{
        padding-right: 40px;
      }
      .photos__list{
        margin-left: 45px;
      }
    }
  @media screen and (max-width: 1150px) {
      .wrap {
        max-width: 950px;
      }
       .product__content{
        width: 100%;
        display: flex;
         flex-wrap: wrap;
         justify-content: center;
      }
    .product__photos{
      padding-right: 0px;
      margin-bottom: 50px;
    }
       .product__buy{
         width: 600px;
         margin:0 auto;

       }
    }
  @media screen and (max-width: 990px) {
      .wrap {
        max-width: 600px;
      }
    .photos{
      margin-bottom: 50px;
    }
    .product__buy{
      width: 100%;
      margin: 0;
    }
    .description{
      width: 100%;
      max-width: 500px;
      }

    .photos__list{
      margin-left: 72px;
    }

    }

</style>