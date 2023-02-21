import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HomeMileage from '../views/HomeMileage.vue'
import Ecomall_list from '../views/Ecomall_list.vue'
import MileageBarcode from '../views/MileageBarcode.vue'
import MileageHistory from '../views/MileageHistory.vue'
import MileageGiftCard from '../views/MileageGiftCard.vue'
import MissionPhotoUpload from '../views/MissionPhotoUpload.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import AccountCreateView from '../views/AccountCreateView'
import AccountConfirmView from '../views/AccountConfirmView'


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
  path: '/ecomall-list',
  name: 'ecomall-list',
  component: Ecomall_list,
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
  {
    path: '/mileage/giftcard',
    name: 'mileage-giftcard',
    component: MileageGiftCard,
  },
  {
    path: '/mission/photoupload',
    name: 'mission-photoupload',
    component: MissionPhotoUpload,
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
  },
  {
    path: '/account',
    name: 'account',
    component: AccountCreateView,
  },
  {
    path: '/account/confirm',
    name: 'account-confirm',
    component: AccountConfirmView,
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
