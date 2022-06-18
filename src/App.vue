<template>
    <h1> bug tracer app by <span>Ch</span>__<span>B</span>uilder</h1>
    <hr class="ligne">
    <nav>
      <button class="nav-item" v-on:click="update_btn_state"><i class="fa-solid fa-right-to-bracket"></i></button>
      <button class="nav-item" v-on:click="update_btn_state"><i class="fa-solid fa-user-plus"></i></button>
    </nav>
    <login-form v-show="show_login"></login-form>
    <RegistrationForm v-show="show_registration"></RegistrationForm>
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
  display: flex;
  justify-content: center;
  align-items: center;
  display: inline;
  margin:10% auto;
}


h1{
  text-transform: capitalize;
  color: #c6d9dc;
  letter-spacing: 2px;
}
span{
  color:#CCCA0D;
}

.ligne{
  margin-left:35%;
  width: 50px;
  height: 1px;
  background-color: #CCCA0D;
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
  color:#CCCA0D;
  border-top:0px;
  border-right:0px;
  border-bottom:0px;
  border-left:3px solid #fff; 
  border-radius:10px;
  font-size:24px;
}
.nav-item:hover{
  border-left:3px solid #c6d9dc;
  color: #238636;
}

</style>
