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
header {
  background-color: #212121;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  height: 3em;
  
}
header nav a {
  margin: 0 1em;
}

main {
  padding: 2em 0;
}
</style>


