<template>
<div class="login">
  <div class="form">
    <h2>Welcome back to HIITDONTQUIT!</h2>
    <input type="text" placeholder="Username">
    <input type="password" placeholder="Password">
    <input type="submit" value="Sign In" class="submit">
    <p>Don't have an account? Click <router-link to = 'signup'>Here</router-link> to sign up!</p>
  </div>
  
</div>
    
   
  
</template>



<script>
export default {
    name: 'Login',
    
     
}
</script>


<style scoped>
* {
  box-sizing: border-box;
  font-family: sans-serif;
  
}
body {
    background: url(https://images.unsplash.com/photo-1517838277536-f5f99be501cd?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1470&q=80) no-repeat center center fixed !important;
  -webkit-background-size: cover !important;
  -moz-background-size: cover !important;
  -o-background-size: cover !important;
  background-size: cover !important;
}
.login {
  width: 320px;
  height: 450px;
  border: 1px solid #CCC;
  background: url(https://cdn.dribbble.com/users/2300748/screenshots/4644522/weight-lifting.gif) center center no-repeat;
  background-size: cover;
  margin: 30px auto;
  border-radius: 20px;
}
.login .form {
  width: 100%;
  height: 100%;
  padding: 15px 25px;
}
.login .form h2 {
  color: #FFF;
  text-align: center;
  font-weight: normal;
  font-size: 18px;
  margin-top: 60px;
  margin-bottom: 80px;
}
.login .form input {
  width: 100%;
  height: 40px;
  margin-top: 20px;
  background: rgba(255, 255, 255, 0.13);
  border: 1px solid rgba(255,255,255,.1);
  padding: 0 15px;
  color: #FFF;
  border-radius: 5px;
  font-size: 14px;
  opacity: 100%;
}
.login .form input:focus {
  border: 1px solid rgba(255,255,255,.8);
  outline: none;
}
::-webkit-input-placeholder {
    color: #DDD;
}
.login .form input.submit {
  background: rgba(255,255,255,.9);
  color: #444;
  font-size: 15px;
  margin-top: 40px;
  font-weight: bold; }
</style>



