<template>
    <div v-show="currentuserHasProjects" class="container" appear>
        <ul class="responsive-table">
            <li class="table-header">
                <div class="col col-1"> Id</div>
                <div class="col  col-2"><i class="fa-solid fa-user-tie"></i> Creator </div>
                <div class="col col-3"><i class="fa-solid fa-people-group"></i> Team </div>
                <div class="col col-4"><i class="fa-solid fa-spinner"></i> Status</div>
            </li>
            <div v-show="dontcurrentuserHasProjects" class="No-project-Handler">    
              <vuetyped :strings="['No project yet :).......... ']" :typeSpeed="70" class="typing-comp">
                <h1 class="typing handler-message"> </h1>
              </vuetyped>
            </div>
            <perfect-scrollbar tag="div" class="body_tab">
            <li v-for="(item,index) in Data" :key="index" class="table-row">
                <div class="col col-1 col-1-data" data-label="Job Id">{{ item.Name }}</div>
                <div class="col col-2" data-label="Customer Name">{{ item.Owner }}</div>
                <div class="col col-3 team-name" data-label="Amount" >{{ item.Team }}</div>
                <div class="col col-4" data-label="Payment Status">{{ item.State }}</div>
            </li>
            </perfect-scrollbar>
        </ul>
    </div>
</template>

<script scoped>
import vuetyped from "vue3typed/libs/typed";
import axios from "axios";    
    export default{
    props:{
      User:{
        type: String,
        required: true
      }
    },
    components: {
      vuetyped
    },
    mounted(){
        console.log("loading mounted : ",this.isloading);
        //fecth data from endpoint : 
        axios.get("http://127.0.0.1:5000/get-all-project/User/"+this.User)
        .then(response =>{
          console.log(response.data.reponse_data);
          this.isloading = false;
          if(response.data.reponse_data.length===0){
            this.currentuserHasProjects = false;
            this.dontcurrentuserHasProjects = true;
          }else{
            this.currentuserHasProjects = true;
            this.dontcurrentuserHasProjects = false;
            this.Data = response.data.reponse_data;
          }
        })
        .catch(error =>{
          console.error(error);
          this.dontcurrentuserHasProjects = true;
        });
    },
    unmounted(){
      this.$forceUpdate();
        //fecth data from endpoint : 
        axios.get("http://127.0.0.1:5000/get-all-project/User/"+this.User)
        .then(response =>{
          if(response.data.reponse_data.length===0){
            this.currentuserHasProjects = false;
            this.dontcurrentuserHasProjects = true;
          }else{
            this.currentuserHasProjects = true;
            this.dontcurrentuserHasProjects = false;
            this.Data = response.data.reponse_data;
          }
        })
        .catch(error =>{
          console.error(error);
          this.dontcurrentuserHasProjects = true;
        });
    },
    data(){
        return {
            "Data":'',
            "currentuserHasProjects":false,
            "dontcurrentuserHasProjects":false,
        }
    },
    methode:{
        click_table_row(){
            console.log("row click detected ");
        }
    }
    }
</script>


<style scoped>
.bounce-enter-active {
        animation: bounce-in 1.5s;
    }
    .bounce-leave-active {
        animation: bounce-in 0.01s reverse;
    }
    @keyframes bounce-in {
        0% {
            transform: scale(0);
        }
        50% {
            transform: scale(1.1);
        }
        100% {
            transform: scale(1);
        }
    }

.content-side{
    margin:0;
    padding:5px 15px;
    border: 1px solid #537895;
    background:linear-gradient(to right,#E8126B,#0e0e0e);
    border-radius: 18px;
    color:#fff;

}

body {
  font-family: 'lato', sans-serif;
}
.container {
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 10px;
  padding-right: 10px;
  margin-top:20px;
  height: auto;
}

.No-project-Handler{
    width: 1000px;
    height:40px;
    padding:10px 10px;
    margin-top:8px;
    display:grid;
    grid-template-columns: repeat(12,1fr);
    grid-column: 3/ span 9;
    text-align:left;
    align-content: center;
    color:#fff;
}

.typing-comp{
  grid-column: 2/ span 9;
  display:flex;
  width:500px;
}
.handler-message{
  grid-column: 2/ span 9;
  display: flex;
  font-size:20px;
  text-transform: capitalize;
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}

.body_tab{
  height:330px;
}
.responsive-table li {
    border-radius: 3px;
    padding: 25px 30px;
    display: flex;
    justify-content: space-between;
    margin-bottom: 25px;
  }
.responsive-table  .table-header {
    color:#fff;/* #95A5A6;*/
    background:linear-gradient(to right,#E8126B,#0e0e0e);
    font-size: 14px;
    text-transform: capitalize;
    letter-spacing: 0.03em;
  }
.responsive-table  .table-row {
    background:linear-gradient(to right, #95A5A6,#000);
    color:#fff;
    box-shadow: 0px 0px 9px 0px rgba(0,0,0,0.1);
  }
.table-row:hover{
    box-shadow: 0px 0px 9px 0px #fff;
}
.fa-people-group{
    font-size: 19px;
}
.team-name{
    background-color:#537895;
    color: #fff;
    width:auto;
    text-align: left;
    border-radius: 25px;
    padding:2px 1px;
    margin-right:25px;
}


.responsive-table .col-1 {
    flex-basis: 25%;
    text-transform: uppercase;
}
.responsive-table .col-1-data:hover {
    display:flex;
    color:#eee;
    cursor: pointer;
    text-decoration: underline;
    padding-bottom: 5px;
    text-decoration-color:#eee;
}


.responsive-table .col-2 {
    flex-basis: 20%;
}


.responsive-table .col-3 {
    flex-basis: 25%;
    text-align: center;
  }

.responsive-table .col-4 {
    flex-basis: 25%;
}

.table-header {
    display: none;
}

li {
    display: block;
}
.col {
flex-basis: 100%;      
}

</style>