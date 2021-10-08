import VueRouter from 'vue-router'
import Home from './pages/Home'
import Login from './pages/Login'
import SignUp from './components/SignUp'
import MyWorkouts from './pages/MyWorkouts'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/login', component: Login, name: 'Login' },
  { path: '/signup', component: SignUp, name: 'SignUp' },
  { path: '/my_workouts', component: MyWorkouts, name: 'MyWorkouts' }
]

export default new VueRouter({ routes, mode: 'history' })
