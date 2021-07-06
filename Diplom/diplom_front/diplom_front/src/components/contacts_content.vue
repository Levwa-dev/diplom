<template>
  <section class="about-us">
    <div class="wrap">
      <h2>Как с нами связаться</h2>
      <div class="about-us__content">
        <h3 class="about-us__title">Соцсети и почта</h3>
        <ul>
          <li>Instagram: <a  target="_blank" href="https://www.instagram.com/?hl=ru">instagram.com/it-galaxy/</a></li>
          <li>Facebook: <a target="_blank" href="https://www.facebook.com">facebook.com/it-galaxy/</a></li>
          <li>Telegram: <a target="_blank" href="https://телеграм.онлайн">+380888888888</a></li>
          <li>Почта: <a target="_blank" href="https://www.google.com">dmitriev.valerii65@gmail.com</a></li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "contacts_content"
}
</script>

<style scoped>
  section{
    margin-top: 25px;
    margin-bottom: 125px;
  }
  .wrap{
    height: 100vh;
    width: 100%;
    max-width: 1440px;
    margin: 0 auto;
  }
  h2{
    font-size: 25px;
    text-align: center;
    width: 300px;
    margin: 0 auto;
    margin-bottom: 15px;
  }
  .about-us__content{
    width: 100%;
    max-width: 700px;
    margin: 0 auto;
  }
  .about-us__title{
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  li{
    margin-bottom: 10px;
  }
  li>a{
    text-decoration: none;
    color: brown;
  }
  li>a:hover{
    text-decoration: none;
    color: coral;
  }
    @media screen and (max-width: 1300px) {
      .wrap {
        max-width: 1100px;
      }
    }
      @media screen and (max-width: 990px) {
      .wrap {
        max-width: 510px;
      }
    }

</style>