<template>
  <div>
		<h3>HiitdontQuit</h3>
    <b-button v-b-toggle.sidebar-1 >Dashboard</b-button>
    <b-sidebar id="sidebar-1" title="Sidebar">
    <div class="px-3 py-2">
  <ul>
    <li><router-link to ="/">Home</router-link></li>
    <li><router-link to = "/about">About</router-link></li>
    <li><router-link to = "/login">Login</router-link></li>
    <li><router-link to = "/myworkouts">My Workouts</router-link></li>
  </ul>
      </div>
    </b-sidebar>
  </div>

</template>


<script>
export default {
  name: 'Nav' 
}
</script>



<style scoped>

button{
  background-color: #546278; /* Green */
  border: none;
  color: rgb(249, 249, 249);
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
	
}
a{
	color: red;
	
}
li{
	list-style: none;
}

</style>
