<template>
  <div class="wrap">
    <div class="thanks">
      <h2 class="thanks__title">Ваше замовлення прийнято, наш менеджер з вами зв'яжеться</h2>
      <a href="/" class="thanks__url">За покупками!</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "ThanksForOrder"
}
</script>

<style scoped>
.wrap{
  width: 100%;
  min-height: 100vh;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #a19f9f;
}
.thanks{
  min-width:450px;
  min-height: 300px;
  box-shadow: 0 0 10px #b1b7d6;
  display: flex;
  align-items: center;flex-direction: column;
  background-color: #fff;
}
.thanks__title{
  padding:60px;
  width: 350px;
  font-size: 18px;
  font-weight: bold;
  text-align: center;
}
.thanks__url{
  margin-top: 40px;
  text-decoration: none;
  font-size: 20px;
  border: 1px solid #000000;
  border-radius: 3px;
  padding: 10px;
}
.thanks__url:hover{
  background-color: #fa2d2d;
  color: #fff;
}
</style>