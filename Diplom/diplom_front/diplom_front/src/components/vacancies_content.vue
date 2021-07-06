<template>
  <section class="about-us">
    <div class="wrap">
      <h2>Вакансии</h2>
      <div class="about-us__content">
        <h3 class="about-us__title">Менеджер</h3>
        <p>Компания "IT-GALAXY" не будет останавливаться на достигнутом. В наших планах большую часть прибыли реинвестировать в рекламу нашего
          интернет магазина, для привлечения новых покупателей. Так же в связи со скорым увеличением объема продаж,
          всем желающим попробовать себя в роли менеджера интернет магазина, советуем иногда проверять раздел "Вакансии".</p>
      </div>

    </div>
  </section>
</template>

<script>
export default {
  name: "vacancies_content"
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
    width: 200px;
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