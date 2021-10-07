<template>
   <div>
       <h2>Welcome back to HIITDONTQUIT!</h2>
       <br/>
       <br/>
    <form>
        <input type="text" placeholder="Enter Username"/>
        <br/>
        <input type="password" placeholder="Enter your password" />
        <br/>
        <button>Login</button>
    </form>
    <br/>
    <div><h6>Don't have an account? Click <router-link to = '/signup'>Here</router-link> to sign up!</h6></div>
   
  </div>
</template>



<script>
export default {
    name: 'Login',
    
     
}
</script>



<style scoped>

</style>