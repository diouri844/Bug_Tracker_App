<template>
  <div class="main">
    <h1> Your dashbroad page {{ userName }} </h1>
  </div>
  
</template>

<script>
// separt dashbroad to many components : teams list/current user projects-engagement:
export default {
    props:['userName']
}
</script>

<style scoped>
.main{
  /*
  background-color: #0cbaba;
  background-image: linear-gradient(315deg, #0cbaba 0%, #380036 74%);
  */
  /*
  background-color: #63a4ff;
  background-image: linear-gradient(315deg, #63a4ff 0%, #83eaf1 74%);
  */
  background-color: #537895;
  background-image: linear-gradient(315deg, #537895 0%, #09203f 74%);
  position:absolute;
  top:0px;
  right:0px;
  bottom:0px;
  left:0px;
}

</style>