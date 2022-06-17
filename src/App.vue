<template>
  <div class="container">
    <h1> bug tracer app by <span>Ch</span>__<span>B</span>uilder</h1>
    <hr class="ligne">
    <nav>
      <button class="nav-item" v-on:click="update_btn_state"><i class="fa-solid fa-user-plus"></i></button>
      <button class="nav-item" v-on:click="update_btn_state"><i class="fa-solid fa-right-to-bracket"></i></button>
    </nav>
    <login-form v-show="show_login"></login-form>
    <RegistrationForm v-show="show_registration"></RegistrationForm>
  </div>
</template>
<script>
import loginForm from "@/components/LoginForm.vue"
import RegistrationForm from "@/components/RegistrationForm.vue"
export default {
  components: {
    loginForm,
    RegistrationForm
  },
  data() {
    return{
      'show_login':true,
      'show_registration':false
    }
  },
  methods:{
    update_btn_state(){
      this.show_login=!this.show_login;
      this.show_registration=!this.show_registration;
      console.log(this.login,this.show_registration)
    }
  }
}
</script>
<style>
#app {
  font-family: Times, "Times New Roman", Georgia, serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #c6d9dc;
  background:linear-gradient(0deg,#5F1B2A,#0d0f0c 100%);
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  background:#0d0f0c;
  display: inline;
  margin:10% auto;
  width:60%;
  height:600px;
  border-radius: 25px;
  box-shadow: 0px 7px 29px 0px rgba(100, 100, 111, 0.2) ;
}
.container h1{
  text-transform: capitalize;
  color: #c6d9dc;
  letter-spacing: 2px;
}
span{
  color:#238636;
}

.ligne{
  margin-left:35%;
  width: 50px;
  height: 1px;
  background-color: #238636;
  border: none;
  margin-top: -7px;
  margin-bottom: 3%;
}
nav{
  margin-bottom: 3%;
}
.nav-item{
  padding: 10px 10px;
  margin:10px 10px;
  background:transparent;
  color:#c6d9dc;
  border-top:0px;
  border-right:0px;
  border-bottom:0px;
  border-left:3px solid #238636; 
  border-radius:10px;
  font-size:17px;
}
.nav-item:hover{
  border-left:3px solid #c6d9dc;
  color: #238636;
}

</style>
