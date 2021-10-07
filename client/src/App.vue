<template>
  <div id="app">
<header>
  <Nav />
  </header>
  <main>
    <router-view header= 'HIITDONTQUIT'></router-view>
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

main {
  padding: 2em 0;
}
body {
  margin: 0;
  padding: 0;
  color: #eee;
  background: rgb(2,0,36) !important;
background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 0%, rgba(0,212,255,1) 63%) !important;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center !important;
  
}
</style>


