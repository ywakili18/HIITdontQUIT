import VueRouter from 'vue-router'
import Home from './pages/Home'
import Login from './pages/Login'
import SignUp from './components/SignUp'
import About from './pages/About'
import MyWorkouts from './pages/MyWorkouts'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/login', component: Login, name: 'Login' },
  { path: '/signup', component: SignUp, name: 'SignUp' },
  { path: '/about', component: About, name: 'About' },
  { path: '/my_workouts', component: MyWorkouts, name: 'MyWorkouts' }
]

export default new VueRouter({ routes, mode: 'history' })
