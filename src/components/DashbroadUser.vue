<template>
  <div class="main">
    <h1 class="main-title">
      <i class="fas fa-house custom-element"></i>
       Your Home  
       <span class="custom-element"> {{ userName }} </span>
    </h1>
     <div class="search-area">
      <i class="fa-solid fa-magnifying-glass"></i>
       <input type="text" placeholder="Search" class="input_search" v-model="search_input"/>
        <select name="type" id="search_global_subject" v-model="search_subject">
          <option class="option_item" value="Id" >Project Id</option>
          <option class="option_item" value="User" >User </option>
          <option class="option_item" value="Team">Team </option>
        </select>
        <button class="search-btn-start" v-bind:onclick="search_Now"> search </button>
     </div>
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
    <UserProjectList class="side-item" v-show="isdefault"></UserProjectList>
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
    data(){
      return{
        "isdefault":true,
        "search_input":'',
        "search_subject":'Id'
      }
    },
    methods:{
      logout_to_home(){
        //send custom-event to main component :
        this.$emit("tooglelogout");
      },
      search_Now(){
        console.log(this.search_input,this.search_subject);
        this.isdefault = false;
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

.input_search{
    padding: 3px 8px;
    border:none;
    border-bottom: 1px solid #fff;
    color:#fff;
    background:transparent;
}
.input_search:not(:placeholder-shown) {
  border-color: #537895;
}
.input_search:focus{
  outline: none;
}

#search_global_subject{
  margin-left:5px;
  margin-right:10px;
  padding:3px 8px;
  outline: none;
  color:#fff;
  background:transparent;
  border-bottom:1px solid #fff;
  outline: none;
}

select option[value="Id"] {
  background-color:#537895;
}

select option[value="User"] {
  background-color:#537895;
}

select option[value="Team"] {
  background-color:#537895;
}
.search-btn-start{
  display: flex;
  background:transparent;
  padding: 3px 15px;
  border:1px solid #fff;
  color:#fff;
  border-radius:18px;
}
/*CCCA0D */
.search-btn-start:hover{
  background-color:#537895;
  color:#fff;
  border:none;
}

  .search-area{
    display:grid;
    grid-template-columns: repeat(12,1fr);
    justify-content: center;
    align-items: center;
    grid-row: 2/ span 3;
    grid-column: 3/ span 7;
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
  grid-row: 4/ span 5;
}
</style>