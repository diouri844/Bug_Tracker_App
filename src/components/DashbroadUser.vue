<template>
  <div class="main">
    <h1 class="main-title">
      <i class="fas fa-house custom-element"></i>
       Your Home  
       <span class="custom-element"> {{ userName }} </span>
    </h1>
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