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


main {
  padding: 2em 0;
}
body {
  
  color: #eee !important;
  background: url(assets/boxing.jpg) no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center !important;
  
}
</style>


