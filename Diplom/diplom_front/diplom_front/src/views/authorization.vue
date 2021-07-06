<template>
  <div>
    <Nav/>
    <section class="enter">
      <div class="wrap">
        <h2 class="enter__advatages">
          Зачем регистрироваться?
        </h2>
        <p class="enter__description">
          Регистрация в нашем интренет магазине позволит вам оставлять коментарии к товарам,
          быстрее заполнять форму заказа, а так же просматривать состояние вашего заказа в личном кабинете.
        </p>
        <div class="enter__form form">
          <input v-model="login" type="text" class="form__login" placeholder="Ваш логин (email)">
          <span v-if="this.vlogin === true">Логин отсутствует или был введен некорректно</span>
          <input v-model="password" type="password" class="form__password" placeholder="Ваш пароль">
          <span v-if="this.vpassword === true">Пароль отсутствует или был введен некорректно</span>
          <span v-if="this.vauth === true">Логин или пароль неверен</span>
          <button @click="auth" class="form__submit">Авторизоваться</button>
          <a href="/registration" class="form__registration">Нету аккаунта? Зарегистрируйтесь сейчас!</a>
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
  name: "authorization",
  data(){
    return{
      login:this.login,
      password:this.password,
      vlogin: false,
      vpassword:false,
      valid:false,
      vauth:false,
      regEmail: /^(([^<>()[\]\\.,;:\s@]+(\.[^<>()[\]\\.,;:\s@]+)*)|(.+))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
      regPassword:/(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}/,
    }
  },
  methods:{
    validation(){
      if(!this.regEmail.test(this.login) || this.login == null){
        this.vlogin = true
      }else{this.vlogin = false}

      if(!this.regPassword.test(this.password) || this.password == null){
        this.vpassword = true
      }else{this.vpassword = false}

      if ((this.vlogin || this.vpassword) === false){
        this.valid = true
      }else{ this.valid = false }
    },
    async auth(){
      this.validation()
      if( this.valid === true){
        let data = {
          email:this.login,
          password:this.password
        }
         await fetch(`${this.$store.getters.getAuthUrl}/token/login/`,
            {
              method: "POST",
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify(data)
             }).then((response) =>
              {
                 if(response.status===400){
                   console.clear()
                   this.vauth = true
                 }else{
                   response.json().then((data) => {
                     window.sessionStorage.setItem('auth_token', data.auth_token)
                   })
                   this.$router.push('/personalArea')
                 }
               })
      }
    }
  },
  components: {Footer, Nav}
}
</script>

<style scoped>
.wrap{
  width: 100%;
  max-width: 1320px;
  margin: 0 auto;
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  align-items: center;
}
.enter__advatages{
  padding: 50px 0px;
  font-size: 25px;
  text-align: center;
  width: 400px;
}
.enter__description{
  padding: 10px 0px;
  padding-bottom: 40px;
  font-size: 20px;
  line-height: 30px;
  width: 600px;
}
.form{
  padding-top: 20px;
  margin-bottom: 40px;
  width: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid #000;
  border-radius: 5px;
  box-shadow: 0 0 10px #b1b7d6;

}
input{
  margin: 10px;
  height: 30px;
  width: 300px;
  border: 1px solid #000;
  border-radius: 5px;
}
button{
  margin: 0 auto;
  margin-top: 25px;
  margin-bottom: 30px;
  width: 150px;
  height: 40px;
  border: 1px solid;
  font-size: 18px;
  border-radius: 5px;
}
.form__registration{
  text-decoration: none;
  color: #1220a3;
  margin-bottom: 25px;
}
button:hover{
  color: #fff;
  background-color: crimson;
}
span{
  font-size: 14px;
  color: red;
  text-align: center;
  width: 300px;
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