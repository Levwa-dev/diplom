<template>
  <div>
    <Nav/>
    <section class="personal-area">
      <div class="wrap">
        <div class="personal-area__body">
          <div class="personal-area__left">
            <div class="left__info">
              <p class="left__name">{{user.first_name}} {{user.last_name}}</p>
              <p class="left__email">{{user.email}}</p>
            </div>
              <ul class="left__list list">
                <li @click="openOrders" class="list__item"><button>Мои заказы</button></li>
                <li @click="openComments" class="list__item"><button>Мои коментарии</button></li>
                <li class="list__item"><button>Изменить личную информацию</button></li>
              </ul>
          </div>
          <div class="personal-area__right">
            <div v-if="this.orders===true" class="right__orders orders">
              <div class="orders__title_cover">
                <h2 class="orders__title">Мои заказы</h2>
              </div>
              <div class="orders__body">
                <div class="orders__order order">
                  <p class="order__name">Видеокарта AFOX PCI-Ex GeForce GTX 750 Ti 2GB GDDR5 (128bit) (1020/5400) (DVI, VGA, HDMI) (AF750TI-2048D5H5-V7)</p>
                  <p class="order__quantity">Количетсво: 4</p>
                  <p class="order__cost">Стоимость: 7000 грн</p>
                  <p class="order__status">Статус: в обработке</p>
                  <a href="#">Просмотр продукта</a>
                </div>
                <div class="orders__order order">
                  <p class="order__name">Видеокарта AFOX PCI-Ex GeForce GTX 750 Ti 2GB GDDR5 (128bit) (1020/5400) (DVI, VGA, HDMI) (AF750TI-2048D5H5-V7)</p>
                  <p class="order__quantity">Количетсво: 4</p>
                  <p class="order__cost">Стоимость: 7000 грн</p>
                  <p class="order__status">Статус: в обработке</p>
                  <a href="#">Просмотр продукта</a>
                </div>
              </div>
            </div>
            <div v-if="this.comments===true" class="right__comments comments">
              <h2 class="comments__title">Ваши отзывы</h2>
              <div class="comments__body">
                <div class="comments__comment comment">
                  <div class="comment__header">
                    <span class="comment__name">Видеокарта AFOX PCI-Ex GeForce GTX 750 Ti 2GB GDDR5 (128bit) (1020/5400) (DVI, VGA, HDMI) (AF750TI-2048D5H5-V7)</span>
                    <span class="comment__date">31.05.2021</span>
                  </div>
                  <div class="comment__text">Фигня полная, не рекомендую!</div>
                  <button @click="s" class="comment__delete">Удалить</button>
                </div>
                <div class="comments__comment comment">
                  <div class="comment__header">
                    <span class="comment__name">Видеокарта AFOX PCI-Ex GeForce GTX 750 Ti 2GB GDDR5 (128bit) (1020/5400) (DVI, VGA, HDMI) (AF750TI-2048D5H5-V7)</span>
                    <span class="comment__date">31.05.2021</span>
                  </div>
                  <div class="comment__text">Фигня полная, не рекомендую! Самая худшая видюха И єто не шутка! Дорого и непонятно</div>
                  <button  class="comment__delete">Удалить</button>
                </div>
              </div>
            </div>
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
export default {
  name: "Personal_Area",
  data(){
    return{
      orders:true,
      comments:false,
      user:null
    }
  },
  created() {
    this.load()
  },
  methods:{
    openOrders(){
        this.orders = true
        this.comments = false
    },
    openComments(){
      this.orders = false
      this.comments = true
    },
    async load() {
      let i = window.sessionStorage.getItem('auth_token')
      this.user = await fetch(`${this.$store.getters.getAuthUrl}/users/me/`,
          {
            headers: {
              'Authorization': 'Token' + ' ' + i,
            },
          }).then(response => response.json())
      console.clear()
    }
  },
  components: {Footer, Nav}
}
</script>

<style scoped>
.wrap{
  min-height: 50vh;
  width: 100%;
  max-width: 1320px;
  margin: 0 auto;
}
.personal-area__body{
  display: flex;
}
.personal-area__left{
  width: 305px;
  border-right: 1px solid #000000;
}
.personal-area__left,.personal-area__right{
  padding: 20px 0;
  min-height: 100vh;
}
.personal-area__right{
  width: 100%;
  min-height: 1015px;
  padding-left: 20px;
}
.left__info{
  font-size: 14px;
  font-weight: bold;
  line-height: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid #000000;
  padding-left: 20px;
}
button{
  width: 100%;
  height: 40px;
  font-size: 18px;
  border: none;
  background-color: #fff;
  text-align: left;
}
button:hover{
  background-color: #f5c6c6;
}

.orders__title_cover{
  display: flex;
  justify-content: center;
}

.orders__title,.comments__title{
  font-size: 26px;
  padding: 40px 0;
  margin-bottom: 20px;
  text-align: center;
}
.orders__body{
  display: flex;
  flex-wrap: wrap;
}
.order{
  margin-bottom: 15px;
  padding: 5px;
  margin-right: 15px;
  width: 300px;
  height: 215px;
  box-shadow: 0 0 10px #b1b7d6;
  font-size: 18px;
  text-align: center;
}
.order>p{
  margin: 10px;
}
.order__name{
  min-height: 50px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
}
.comments__body{
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
.comment{
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
.comment__name{
  max-width: 500px;
  font-size: 16px;
  font-weight: bold;
  margin-right: 10px;
  line-height: 20px;
}
.comment__date{
  font-size: 16px;
  position: absolute;
  top:15px;
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
.comment__delete{
  width: 100px;
  margin-left: 15px;
  margin-bottom: 15px;
  border:none;
  background-color: #fff;
  color:red
}
.comment__delete:hover{
  font-size: 20px;
  background-color: #fff;
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
  .wrap{
    max-width: 600px;
    display: block;
  }

}
</style>