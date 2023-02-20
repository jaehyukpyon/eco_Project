import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HomeMileage from '../views/HomeMileage.vue'
import MileageBarcode from '../views/MileageBarcode.vue'
import MileageHistory from '../views/MileageHistory.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/mileage',
    name: 'mileage',
    component: HomeMileage,
  },
  {
    path: '/mileage/barcode',
    name: 'mileage-barcode',
    component: MileageBarcode,
  },
  {
    path: '/mileage/history',
    name: 'mileage-history',
    component: MileageHistory,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
