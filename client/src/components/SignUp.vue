<template>
<div class="login">
  <div class="form">
    <h2>Welcome to HIITDONTQUIT!</h2>
    <input type="text" placeholder="First Name" required>
    <input type="text" placeholder="Last Name" required>
    <input type="number" placeholder="Goal Weight" required>
    <input type="text" placeholder="Username" required>
    <input type="email" placeholder="Email" required>
    <input type="password" placeholder="Password" required>
    <input type="submit" value="Create account" required class="submit">
  </div>
</div>
  
  
   
</template>


<script>
export default {
    name: 'SignUp'
}
</script>

<style scoped>
* {
  box-sizing: border-box;
  font-family: sans-serif;
}
.login {
  width: 320px;
  height: 750px;
  border: 1px solid #CCC;
  background: url(https://cdn.dribbble.com/users/406059/screenshots/5210740/dribbble2.gif) center center no-repeat;
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
  background: rgba(255,255,255,.5);
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
  font-weight: bold;
}
</style>


