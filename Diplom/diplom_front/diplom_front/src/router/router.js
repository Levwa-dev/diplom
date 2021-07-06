import Vue from 'vue'
import Router from 'vue-router'

import Home from '../views/Home'
import product from "../views/product";
import cart from "../views/cart";
import Categorie_products from "../views/Categorie_products";

Vue.use(Router);

let router = new Router({
    mode: 'history',

    routes:[
        {
            path: '/',
            component: Home
        },
        {
            path: '/about-us',
            component: () => import('../views/us')
        },
        {
            path: '/contacts',
            component: () => import('../views/contacts')
        },
        {
            path: '/guarantee',
            component: () => import('../views/guarantee')
        },
        {
            path: '/return-product',
            component: () => import('../views/return-product')
        },
        {
            path: '/vacancies',
            component: () => import('../views/vacancies')
        },
        {
          path:'/authorization',
          component: ()  => import('../views/authorization')
        },
        {
            path:'/registration',
            component: () => import('../views/registration')
        },
        {
            path: '/personalArea',
            component: () => import ('../views/Personal_Area')
        },
        {
            path: '/confirm',
            component: () => import ('../views/ConfirmOlineOrder')
        },
        {
            path: '/thanks',
            component: () => import ('../components/ThanksForOrder')
        },
        {
            path: '/cart',
            name : 'cart',
            component: cart,
        },
        {
            path: '/product/:id',
            name : 'product',
            component: product,
            props: true
        },
        {
            path: '/product_categories/:id',
            name : 'categorie_product',
            component: Categorie_products,
            props: true
        },




    ]
})

export default router;