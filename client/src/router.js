import VueRouter from 'vue-router'
import Home from './pages/Home'
import Login from './pages/Login'
import SignUp from './components/SignUp'
import About from './pages/About'
const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/login', component: Login, name: 'Login' },
  { path: '/signup', component: SignUp, name: 'SignUp' },
  { path: '/about', component: About, name: 'About' }
]

export default new VueRouter({ routes, mode: 'history' })
