<template>
  <div>

  </div>
</template>

<script>

export default {
  name: "ConfirmOlineOrder",
  data(){
    return{
      stat:null,
    }
  },
  created() {
    this.loadResponse()
  },
  methods: {
    async loadResponse() {
      this.stat = await fetch(
          `${this.$store.getters.getSeverUrl}/payResponse/`
      ).then(response => response.json())
      if(this.stat.response === 'approved'){
        this.sendOrder()
        this.$store.commit('resetOrderInfo');
        this.$store.commit('resetCart');
        this.$router.push('/thanks')
      }else{
        this.$router.push('/')
      }
    },
    async sendOrder(){
      let orderInf = this.$store.state.orderInfo
      let data = orderInf[0]
      data.payment = "Оплачено через FONDY"
      await fetch(`${this.$store.getters.getSeverUrl}/order_s_info/`,
          {
            method: "POST",
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
          }
      ).then(Response => Response).catch(err => alert(err));
    }
  }
}
</script>

<style scoped>

</style>