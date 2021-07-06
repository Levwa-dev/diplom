<template>
  <section class="info">
    <div class="wrap">
      <div class="help">
        <i class="fas fa-headset"></i>
        <div class="description">
          <h3>Підтримка</h3>
          <p>Консультуємо з будь-якого питання</p>
        </div>
      </div>
      <div class="sales">
        <i class="fas fa-tags"></i>
       <div class="description">
          <h3>Знижки</h3>
          <p>Отримайте знижку при покупці від 3-х товарів</p>
        </div>
      </div>
      <div class="guarantee">
        <i class="fas fa-scroll"></i>
        <div class="description">
          <h3>Гарантія</h3>
          <p>Гарантії від 12 місяців</p>
        </div>
      </div>
      <div class="delivery">
        <i class="fas fa-truck"></i>
        <div class="description">
          <h3>Доставка</h3>
          <p>Доставимо безкоштовно в будь-яке місто України</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
name: "promo"
}
</script>

<style scoped>
  .info{
    margin-top: 25px;
  }
  .wrap{
      width: 100%;
      max-width: 1240px;
      margin: 0 auto;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
    }
  .help,.sales,.guarantee,.delivery{
    display: flex;
    margin-bottom: 25px;
  }
  i{
    margin-top: 5px;
    font-size: 50px;
    color: #e01f1f;
    margin-right: 15px;
  }
  h3{
    font-size: 20px;
    margin-bottom: 10px;
  }
  p{
    width: 100%;
    max-width: 200px;
    font-size: 14px;
  }
   @media screen and (max-width: 1300px) {
    .wrap{
      max-width: 1100px;
    }
     p{
      width: 100%;
      max-width: 170px;
      font-size: 14px;
    }
   }
  @media screen and (max-width: 1150px) {
     .wrap{
       max-width: 950px;
     }
     i{
       font-size: 40px;
     }
   }
  @media screen and (max-width: 990px) {
      .wrap{
        max-width: 600px;
        padding-left: 90px;
        justify-content: normal;
      }
      .sales,.delivery{
        margin-left: 90px;
      }
      i{
        margin-top: 10px;
      }
  }
</style>