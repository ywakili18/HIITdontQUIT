import VueRouter from 'vue-router'
import Home from './pages/Home'
import Login from './pages/Login'
import SignUp from './components/SignUp'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/login', component: Login, name: 'Login' },
  { path: '/signup', component: SignUp, name: 'SignUp' }
]

export default new VueRouter({ routes, mode: 'history' })
