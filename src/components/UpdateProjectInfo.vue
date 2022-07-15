<template>
    <div class="modal-overlay open-modal">
            <div class="modal-container">
                <div class="modal-header">
                    <div class="search">
                                <input type="text" placeholder="Search for project" class="projectname" v-model="projectname">
                                <button 
                                class="btn-search"
                                @click="find_project">
                                    <i class="fa-solid fa-magnifying-glass"></i>
                                </button>
                            </div>
                    <button type="button" class="btn-close btn-light bg-light" 
                    aria-label="Close"
                    @click="CloseMe"></button>
                </div>
                    <div v-if="step1" class="modal-body">
                            <div v-show="isloading" class="loading_message">
                                <h1> Hum something loud while others stare ...... </h1>
                            </div> 
                            <div v-if="isfailed" class="error_message">
                                <h1> No Results Found   </h1>
                                <i class="fa-solid fa-face-sad-tear"></i>
                            </div>
                            <perfect-scrollbar tag="div"
                            v-show="has_resultat"
                            class="result_team_message">
                                <h4 @click="update_item(item)"
                                    class="item" 
                                    v-for="(item,index) in data" :key="index">
                                        <i class="fa-solid fa-folder"></i>
                                        <span class="left"> {{ item.Name }}</span>
                                        <span class="right">{{ item.Sdate}}</span>
                                </h4>
                            </perfect-scrollbar>
                            <div v-show="dontcurrentuserHasProjects" class="No-project-Handler">    
                                <vuetyped :strings="['No project yet :).......... ']" :typeSpeed="70" class="typing-comp">
                                    <h1 class="typing handler-message"> </h1>
                                </vuetyped>
                            </div>
                    </div>
                    <div v-if="step2" class="modal-body">
                            <div v-show="isloading2" class="loading_message">
                                <h1> Hum something loud while others stare .......  </h1>
                            </div>
                            <div v-show="isfailed2" class="error_message">
                                <h1> No Results Found   </h1>
                                <i class="fa-solid fa-face-sad-tear"></i>
                            </div>
                            <div v-show="has_resultat2" class="result_team_message">
                                <h3 
                                @click="update_item(this.data_search)"
                                class="item"
                                >
                                    <i class="fa-solid fa-folder"></i>
                                    <span class="left"> {{ this.data_search.Name }}</span>
                                    <span class="right">{{ this.data_search.Sdate}}</span>
                                </h3>
                            </div>
                    </div>
            </div>
        </div>    
</template>


<script scoped>
import axios from 'axios'
import vuetyped from "vue3typed/libs/typed";
export default {
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
        this.isloading = true;
        // fetch all project names of connected user :
        axios.get("http://127.0.0.1:5000/get-all-project/User/"+this.User)
        .then(response =>{
          this.isloading = false;
          console.log(response.data.reponse_data.length);
          if(response.data.reponse_data.length===0){
            // show message : 
            this.dontcurrentuserHasProjects = true;
            setTimeout(()=>{
                this.dontcurrentuserHasProjects = false;
                this.CloseMe();
            },2500);
          }else{
            // current user has project = > display all project as an liste :
            this.data = response.data.reponse_data;
            this.has_resultat = true;
          }
        })
        .catch(error => {
            console.error(error);
        });
    },
    data(){
        return{
            'headermessage':'',
            'step1':Boolean,
            'step2':Boolean,
            'projectname':'',
            'data':'',
            'data_search':'',
            'isloading':false,
            'isloading2':false,
            'isfailed':false,
            'isfailed2':false,
            'has_resultat':false,
            'has_resultat2':false,
            'dontcurrentuserHasProjects2':false,
            'dontcurrentuserHasProjects':false
        }
    },
    methods:{
        CloseMe(){
            this.$emit("CloseModal");
        },
        update_item(item){
            console.log(item.Name);
        },
        find_project(){
            this.step1 = false;
            this.step2 = false;
            this.has_resultat2 = false;
            if(this.projectname.length === 0 ||  /\s/.test(this.projectname)){
                this.$notify({
                        type:"error",
                        title: "Search Project Error ",
                        text: "Project name cannot be empty or contain spaces",
                        position:"bottom right"
                    });
            }else{
                this.step1 = false;
                // displaye seconde step :
                this.step2 = true;
                this.isloading2 = true;
                //send get request to the end-point:
                axios.get("http://127.0.0.1:5000/get-all-project/Id/"+this.projectname)
                .then(response => {
                    this.isloading2 = false;
                    if(response.data.reponse_data.length===0){
                        this.isfailed2 = true;
                        setTimeout(()=>{
                            this.isfailed2 = false;
                            this.step2 = false;
                            this.step1 = true;
                            this.projectname = '';
                        },2500);
                    }else{
                        // project founded : 
                        this.data_search = response.data.reponse_data[0];
                        this.has_resultat2 = true;
                    }
                })
                .catch(error => {
                    console.error(error);
                })
            }
        }
    }
    
}
</script>


<style scoped>
.No-project-Handler{
    width: 800px;
    padding:10px 10px;
    margin-top:8px;
    display:grid;
    grid-template-columns: repeat(12,1fr);
    grid-column: 1/ span 4;
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
  grid-column: 2/ span 7;
  display: flex;
  font-size:20px;
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}


.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #000000CE;
  display: grid;
  place-items: center;
  visibility: hidden;
  z-index: -10;
}

.open-modal {
  visibility: visible;
  z-index: 10;
}
.modal-container {
  border-radius: 20px;
  width: 550px;
  height: auto;
  text-align: left;
  display: grid;
  place-items: left;
  position: relative;
  text-transform: capitalize;
  color:#eee;
  background:transparent;
}
.modal-header{
    display:flex;
    max-width:500px;
    min-width:500px;
}
.btn-search:hover{
    color:#fff;
    border-bottom: 1px solid #fff;
    border-color: #fff;
}
.btn-search{
    color:#ccc;
    border:none;
    background: transparent;
}
.loading_message{
    width: 800px;
    padding:10px 10px;
    margin-top:8px;
    display:grid;
    grid-template-columns: repeat(12,1fr);
    grid-column: 1/ span 4;
    text-align:left;
    align-content: center;
    color:#fff;
}
.loading_message h1{
  grid-column: 2/ span 7;
  display: flex;
  font-size:20px;
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
.btn-samll{
    color:#ccc;
    border:1px solid #ccc;
    background:transparent;
    padding: 8px 15px;
    border-radius:18px;
    margin: 0px 0px 0px auto;
    display:flex;
    outline:none;
    cursor:pointer;
    font-size:13px;
}
.fa-check{
    margin-right: 8px;
    margin-top:5px;
}
.btn-samll:hover{
    background-color:#ccc;
    color:#fff;
    border-color: #fff;
}

.error_message{
  width: 800px;
    padding:10px 10px;
    margin-top:8px;
    display:grid;
    grid-template-columns: repeat(12,1fr);
    grid-column: 1/ span 7;
    text-align:left;
    align-content: center;
    color:#ccc;
}
.result_team_message{
    height:400px;
    padding:10px 10px;
    margin-top:8px;
    color:#ccc;
}
.item{
    cursor:pointer;
    padding-left:15px;
}
.item:hover{
    color:#fff;
    border-left: 5px solid #ccc;
}
.left{
    margin-left:5px;
}
.right{
    position: absolute;
    right: 0;
    margin-right:10px;
}


.error_message h1{
  grid-column: 3/ span 4;
  display: flex;
  font-size:20px;
  text-transform: capitalize;
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
.error_message .fa-face-sad-tear{
  font-size:20px;
  margin-left:10px;
}



.header{
    color:#ccc;
    padding-left:15px;
    padding-right:15px;
    margin-right:15px;
}

.btn-close{
    padding: 10px 10px;
    border-radius: 15px;
    outline:none;
}

.modal-body{
    display:grid;
    width:80%;
    place-items: left;
}
.projectname , .username{
    margin-bottom:10px;
    padding: 5px 10px;
    outline: none;
    background:transparent;
    color:#ccc;
    border:none;
    border-left: 5px solid #ccc;
}

</style>