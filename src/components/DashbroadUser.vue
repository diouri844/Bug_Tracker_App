<template>
  <div class="main">
    <h1 class="main-title">
      <i class="fas fa-house custom-element"></i>
       Your Home  
       <span class="custom-element"> {{ userName }} </span>
    </h1>
    <div class="btn-group">
      <button type="button" class="btn dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
      <i class="fa-solid fa-user"></i>
      {{ userName }}  <span class="visually-hidden">Toggle Dropdown</span>
      </button>
      <ul class="dropdown-menu">
        <li><span class="dropdown-item" ><i class="fa-solid fa-gear"></i> Setting</span></li>
        <li v-on:click="logout_to_home"><span class="dropdown-item"><i class="fa-solid fa-right-from-bracket"></i> Logout</span></li>
      </ul>
    </div>
    <UserProjectList class="side-item"></UserProjectList>
  </div>
  
</template>

<script>
// separt dashbroad to many components : teams list/current user projects-engagement:
import UserProjectList from "@/components/UserProjectList.vue"
export default {
    props:['userName'],
    components:{
      UserProjectList
    },
    methods:{
      logout_to_home(){
        //send custom-event to main component :
        this.$emit("tooglelogout");
      }
    }
}
</script>

<style scoped>
.main{
  top:0px;
  right:0px;
  bottom:0px;
  left:0px;
  background:linear-gradient(to right,#E8126B,#0e0e0e);
  position:absolute;
  display:grid;
  grid-template-columns:repeat(12,1fr);
  grid-template-rows:repeat(12,1fr);
}

.btn{
  margin:5% auto;
  width:50px;
  height: 50px;
  color:#fff;
  border:none;
  border-bottom: 1px solid #fff;
}

.dropdown-menu{
  background:none;
}
.dropdown-item{
  color:#fff;
  text-align: center;
}

.dropdown-item:hover{
  background-color: #537895;
  border-radius: 20px;
}

.main-title{
  margin: 1% auto;
  width: 50%;
  border-bottom: 2px solid #537895;
  color:#fff;
  padding: 10px;
  text-align: center;
  grid-column: 1/ span 11;
  grid-row: span 1;
}

.custom-element{
  font-family: fantasy;
  color: #537895;
}
.side-item{
  grid-column: 2/ span 10 ;
  grid-row: 3/ span 5;
}
</style>