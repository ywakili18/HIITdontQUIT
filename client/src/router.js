import VueRouter from 'vue-router'
import Home from './pages/Home'
import Login from './pages/Login'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/login', component: Login, name: 'Login' }
]

export default new VueRouter({ routes, mode: 'history' })
