<template>
  <div>
    <div class="slide__wrap">
      <img :src="item_data.image" alt="">
    </div>
  </div>
</template>

<script>

export default {
name: "slider_items",
  props:{
    item_data:{
      type: Object,
      default: () =>{}
    },
  },
  components: {

  }
}
</script>

<style scoped>
  .slide__wrap{
    text-decoration: none;
    height: 390px;
    width: 400px;
    background-color: #fff;
    display: block;
    position: relative;
  }
  img{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    vertical-align: middle;
    max-width: 400px;
    max-height: 390px;
  }
</style>