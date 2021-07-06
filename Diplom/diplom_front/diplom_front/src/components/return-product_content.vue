<template>
  <section class="about-us">
    <div class="wrap">
      <h2>Возврат продукции</h2>
      <div class="about-us__content">
        <h3 class="about-us__title">Политика возврата товара</h3>
        <p>У Вас есть возможность вернуть товары в течение 14 дней с момента покупки.
          Исходя из Приказа Министерства экономики Украины от 19 апреля 2007 года №103 «О правилах продажи товаров по заказу за пределами торговых или офисных помещений»,
          мы обязуемся вернуть Вам денежные средства не позднее 30 дней с момента письменного уведомления о возврате и возврата товара.</p>
        <h3 class="about-us__title">Товар не подлежит обмену и возврату если</h3>
        <p>1. Прошло более 14 календарных дней с момента приобретения товара.<br/>
            2. С момента покупки продукта не прошло 14 календарных дней, но товар был в пользовании, нарушена целостность упаковки, отсутствуют бирки.<br/>
            3. Товар содержится в перечне товаров, которые возврату и обмену не подлежат,
            согласно Постановлению Кабинета Министров Украины №172 от 19 марта 1994 года (в действующей редакции) http://zakon4.rada.gov.ua/laws/show/172-94-п.
        </p>
        <h3 class="about-us__title">Для возврата товара свяжитесь с нашими менеджерами. <a href="/contacts">Контакты</a></h3>
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
  a{
    text-decoration: none;
    color: brown;
  }
  a:hover{
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