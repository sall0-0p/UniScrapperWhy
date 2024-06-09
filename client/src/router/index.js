import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import Product from '../pages/Product.vue'
import About from '../pages/About.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/product/:productId',
      name: 'product',
      component: Product,
    },
    {
      path: '/about',
      name: 'about',
      component: About,
    },
  ]
})

export default router
