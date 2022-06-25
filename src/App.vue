<template>
    <nav v-if="is_home">
      <div class="nav-header">
          <h1> bug tracker app by <span>Ch</span>__<span>B</span>uilder</h1>
        <div class="nav-links">
          <button class="nav-item" v-on:click="update_btn_state"><i class="fa-solid fa-right-to-bracket"></i></button>
          <button class="nav-item" v-on:click="update_btn_state"><i class="fa-solid fa-user-plus"></i></button>
        </div>
      </div>
    </nav>
    <login-form v-show="show_login" @toogleComponent="updateLoginState($event)"></login-form>
    <RegistrationForm v-show="show_registration" @toogletologin="updateRegistrationStatetoLogin"></RegistrationForm>
    <DashbroadUser v-if="isMainPage" v-bind:userName="this.currentConnectedUser" ></DashbroadUser>
    <notifications />
</template>
<script>
import loginForm from "@/components/LoginForm.vue"
import RegistrationForm from "@/components/RegistrationForm.vue"
import DashbroadUser from "@/components/DashbroadUser.vue"

export default {
  components: {
    loginForm,
    RegistrationForm,
    DashbroadUser
  },
  data() {
    return{
      'show_login':true,
      'show_registration':false,
      'is_home':true,
      'isMainPage':false,
      'currentConnectedUser':""
    }
  },
  methods:{
    update_btn_state(){
      this.show_login=!this.show_login;
      this.show_registration=!this.show_registration;
      // using options
      console.log(this.login,this.show_registration)
    },
    updateLoginState(e){
      this.currentConnectedUser = e;
      // update show state for login component and navbar component:
      this.show_login = false;
      this.is_home = false;
      this.isMainPage = true;
    },
    updateRegistrationStatetoLogin(){
      this.show_registration = false;
      this.show_login = true;
    }
  }
}
</script>
<style scoped>
#app {
  font-family: Times, "Times New Roman", Georgia, serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;
  display: flex;
  /*justify-content: center;
  align-items: center;
  display: inline;*/
}
.nav-header{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
}

h1{
  text-transform: capitalize;
  color: #c6d9dc;
  letter-spacing: 2px;
}
span{
  color:#CCCA0D;
}

.nav-item{
  margin-left: 2rem;
  color:#c6d9dc;
  background:transparent;
  border:none;
  font-size:24px;
}
.nav-item:hover{
  color: #fff;
}

</style>
