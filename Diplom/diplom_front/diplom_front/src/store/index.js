import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

let cart = window.localStorage.getItem('cart');
let orderInfo = window.localStorage.getItem('orderInfo')

const store = new Vuex.Store({

    state: {
        backendUrl:'http://127.0.0.1:8000/api',
        cart: cart ? JSON.parse(cart) : [],
        search:'',
        orderInfo: orderInfo ? JSON.parse(orderInfo):[],
        authUrl:'http://127.0.0.1:8000/auth',

    },
    mutations:{
        SetSearchValue(state, value){
             state.search = value
         },
        getCartData(state, cartData){
            state.cart.push(cartData)
            this.commit('saveCart');
        },
        removeFromCart(state, product) {
            let id = state.cart.indexOf(product);
                state.cart.splice(id, 1);
                this.commit('saveCart');
        },
        saveCart(state) {
            window.localStorage.setItem('cart', JSON.stringify(state.cart));
        },
        resetCart(state){
            state.cart=[]
            this.commit('saveCart');
        },
        getOrderInfo(state, value){
            state.orderInfo.push(value)
            this.commit('saveOrderInfo')
        },
        saveOrderInfo(state){
            window.localStorage.setItem('orderInfo', JSON.stringify(state.orderInfo))
        },
        resetOrderInfo(state){
            state.orderInfo=[]
            this.commit('saveOrderInfo')
        }
    },
    actions:{
        GetSearchValue({commit}, value){
            commit('SetSearchValue', value)
        },
    },
    modules:{},
    getters:{
        getSeverUrl: state =>{
            return state.backendUrl
        },
        getAuthUrl: state =>{
            return state.authUrl
        },
        Cart(state){
            return state.cart
        },
        SEARCH_VALUE(state){
            return state.search
        }
    }
})

export default store