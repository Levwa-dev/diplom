<template>
  <div>
    <Nav/>
    <section class="registration">
      <div class="wrap">
        <h2 v-if="this.registr === false" class="registration__title">Регистрация пользователя</h2>
        <div v-if="this.registr === true" class="done">
          <h2 class="registration__title">Спасибо за регистрацию</h2>
          <button @click="redirection()" class="submit">На главную</button>
        </div>
        <p v-if="this.registr === false" class="registration__description">Для создания аккаунта заполните следующие поля</p>
        <div v-if="this.registr === false" class="registration__form form">
          <input v-model="first_name" type="text" class="form__first_name" placeholder="Вашe имя*">
          <span v-if="this.vfname === true">Имя отсутствует или было введенно некорректно</span>
          <input v-model="last_name" type="text" class="form__second_name" placeholder="Ваша фамилия*">
          <span v-if="this.vlname === true">Фамилия отсутствует или была введенна некорректно</span>
          <input v-model="email" type="email" class="form__email" placeholder="Ваша электронная почта*">
          <span v-if="this.vemail === true">Почта отсутствует или была введенна некорректно</span>
          <span v-if="this.vemail2 === true">Email уже занят</span>
          <input v-model="password" type="password" class="form__email" placeholder="Пароль*">
          <span v-if="this.vpassword === true">{{this.message}} </span>
          <input v-model="password2" type="password" class="form__email" placeholder="Повторите пароль*">
          <span v-if="this.vpassword2 === true">Пароли не совпадают</span>
          <button @click="registration()" class="form__submit">Зарегистрироваться</button>
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
  name: "registration",
  data(){
    return{
      first_name: null,
      last_name: null,
      email:null,
      password:null,
      password2:null,
      regWord: /[A-Za-zА-Яа-яЇїІіЁё]/,
      regEmail: /^(([^<>()[\]\\.,;:\s@]+(\.[^<>()[\]\\.,;:\s@]+)*)|(.+))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
      regPassword:/(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}/,
      valid:false,
      vfname:false,
      vlname:false,
      vemail:false,
      vemail2:false,
      vpassword:false,
      vpassword2:false,
      message:null,
      registr:false
    }
  },
  methods:{
    validation(){
      if (!this.regWord.test(this.first_name) || this.first_name == null){
        this.vfname = true
      }else{this.vfname = false}

      if(!this.regWord.test(this.last_name) || this.last_name == null){
        this.vlname = true
      }else{this.vlname = false}

      if(!this.regEmail.test(this.email) || this.email == null){
        this.vemail = true
      }else{this.vemail = false}

      if(!this.regPassword.test(this.password) || this.password == null){
        const i = /[0-9]/
        const j = /[a-z]/
        const J = /[A-Z]/
        if(!i.test(this.password)){
          this.message = 'Пароль не содержит цыфру'
          this.vpassword = true
        }else if(!j.test(this.password)){
          this.message = 'Пароль не содержит букву английского алфавита в нижнем регистре'
          this.vpassword = true
        }else if(!J.test(this.password)){
          this.message = 'Пароль не содержит букву английского алфавита в верхнем регистре'
          this.vpassword = true
        }else if(this.password.length<8){
          this.message = 'Пароль должен быть не менее 8 символов в длину'
          this.vpassword = true
        }else{this.vpassword = false}
      }else{this.vpassword = false}

       if(this.password != this.password2){
         this.vpassword2 = true
       }else{this.vpassword2 = false}

      if((this.vfname || this.vlname || this.vemail || this.vpassword || this.vpassword2)===false){
        this.valid = true
      }
    },
    redirection(){
      this.$router.push('/')
    },
    async registration(){
      this.validation()
      if (this.valid===true){
        let data ={
          email: this.email,
          password: this.password,
          password2: this.password2,
          first_name: this.first_name,
          last_name: this.last_name
        }
        await fetch(`${this.$store.getters.getSeverUrl}/registr/`,
            {
              method: "POST",
              headers:{
                'Content-Type': 'application/json',
              },
              body: JSON.stringify(data)
            }
        ).then((response) => {
          response.json().then((data) => {
            if(data.status == 'Email уже занят'){
              this.vemail2 = true
            }else{
              this.vemail2 = false
              this.registr = true
            }
          })
        })
      }
    }
  },
  components: {Footer, Nav}
}
</script>

<style scoped>
section{
  min-height: 100vh;
}
.wrap{
  width: 100%;
  max-width: 1320px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.registration__title{
  padding: 50px 0px;
  font-size: 25px;
  text-align: center;
  width: 400px;
}
.registration__description{
  font-size: 18px;
  text-align: center;
  width: 600px;
  margin-bottom: 25px;
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
  width: 200px;
  height: 40px;
  border: 1px solid;
  font-size: 18px;
  border-radius: 5px;
}
button:hover{
  color: #fff;
  background-color: crimson;
}
done{
  width: 600px;
  position: relative;
}
.submit{
  margin-top: 25px;
  margin-left: 110px;
  width: 200px;
  height: 40px;
  border: 1px solid;
  font-size: 18px;
  border-radius: 5px;
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