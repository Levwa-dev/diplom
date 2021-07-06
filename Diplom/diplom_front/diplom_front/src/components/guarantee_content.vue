<template>
  <section class="about-us">
    <div class="wrap">
      <h2>Все про гарантию</h2>
      <div class="about-us__content">
        <h3 class="about-us__title"></h3>
        <p>На товары в нашем магазине предоставляется гарантия, подтверждающая обязательства по отсутствию в товаре заводских дефектов.
          Гарантия предоставляется на срок от 2 недель до 12 месяцев в зависимости от сервисной политики производителя.
          Срок гарантии указан в описании каждого товара на нашем сайте.</p>
        <p class="warnings">Пожалуйста, проверяйте комплектность и отсутствие дефектов в товаре при получении.<br/><br/>
            Гарантийным обслуживанием занимаются сервисные центры, авторизованные производителями.<br/><br/>
            Адреса и телефоны сервисных центров можно найти на гарантийном талоне или в списке сервисных центров.
        </p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "guarantee_content"
}
</script>

<style scoped>
  section{
    margin-top: 25px;
    margin-bottom: 125px;
  }
  .wrap{
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
  p{
   line-height: 35px;
    margin-bottom: 25px;
  }
  .warnings{
    font-weight: bold;
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