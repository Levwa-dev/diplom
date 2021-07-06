<template>
  <footer>
    <div class="wrap">
        <div class="footer__help help">
          <h3 class="title">Допомога</h3>
          <ul class="help__list">
            <li class="help__item"><a href="#">Доставка та оплата</a></li>
            <li class="help__item"><a href="/guarantee">Гарантія</a></li>
            <li class="help__item"><a href="/return-product">Поверненя товару</a></li>
          </ul>
        </div>
        <div class="footer__socials socials">
          <h3 class="title">Наші соцмережі</h3>
          <ul class="socials__list">
            <li class="socials__item"><a target="_blank" href="https://телеграм.онлайн"><i class="fab fa-telegram"></i></a></li>
            <li class="socials__item"><a target="_blank" href="https://www.facebook.com"><i class="fab fa-facebook"></i></a></li>
            <li class="socials__item"><a target="_blank" href="https://www.instagram.com/?hl=ru"><i class="fab fa-instagram-square"></i></a></li>
          </ul>
        </div>
        <div class="footer__info info">
          <h3 class="title">Інформація</h3>
          <ul class="info__list">
            <li class="info__item"><a href="/about-us">Про нас</a></li>
            <li class="info__item"><a href="/vacancies">Ваканcії</a></li>
          </ul>
        </div>
      <div class="footer__contact contact">
          <h3 class="title">Контакти</h3>
          <ul class="contact__list">
            <li class="contact__item"><a href="tel:+380888888888">+380888888888</a></li>
            <li class="contact__item"><a href="tel:+380999999999">+380999999999</a></li>
            <li class="contact__item">it.galaxy@gmail.com</li>
          </ul>
        </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer"
}
</script>

<style scoped>
footer {
  margin-top: 25px;
  padding-top: 50px;
  width: 100%;
  background: #222;
}
.wrap{
    width: 100%;
    max-width: 1320px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
  }
.footer__help,.footer__socials,.footer__info,.footer__contact {
  width: 240px;
  margin-right: 25px;
  margin-bottom: 50px;
}
.footer__contact{
   margin-right: 0px;
}
.title {
  color: #fff;
  font-size: 18px;
  margin-bottom: 31px;

}
.help__item,.info__item,.contact__item {
  text-decoration: none;
  list-style: none;
  color: #aef5e4;
  font-size: 14px;
  line-height: 38px;
}

.socials__list{
  display: flex;
  align-items: center;
  height: 100px;
}
.socials__item{
  margin-right: 40px;
  font-size: 40px;
}
.socials__item>a{
  text-decoration: none;
  color:  #3bf5d3;
}
.help__item>a,.info__item>a,.contact__item>a {
  text-decoration: none;
  color: #aef5e4;
}
  @media screen and (max-width: 1390px) {
    .wrap{
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
      flex-wrap: wrap;
    }
    .footer__help,.footer__socials,.footer__info,.footer__contact {
    width: 240px;
    margin-right: 0px;
    }
  }
</style>