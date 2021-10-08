<template>
  <div id="app">
<header >
  <Nav />
  </header>
  <main>
    <router-view header='HIITDONTQUIT'></router-view>
  </main>
  </div>
</template>

<script>

import Nav from './components/Nav.vue'

export default {
  name: 'App',
  components: {
   Nav
  }
}
</script>

<style>
/*  */

@import url('https://fonts.googleapis.com/css2?family=Bree+Serif&family=Righteous&display=swap');

body{
   background: url(https://images.unsplash.com/photo-1551063346-c818dcab95f8?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1470&q=80) no-repeat center center fixed; 
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
#app{

font-family: 'Righteous', cursive;
}
</style>


