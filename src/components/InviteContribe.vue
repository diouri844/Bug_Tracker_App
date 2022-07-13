<template>
    <div class="modal-overlay open-modal">
            <div class="modal-container">
                <div class="modal-header">
                    <h3 class="header">
                        <i class="fa-solid fa-plus"></i>
                        {{ headermessage }}  
                    </h3>
                    <button type="button" class="btn-close btn-light bg-light" 
                    aria-label="Close"
                    @click="CloseMe"></button>
                </div>
                    <div v-show="step1" class="modal-body">
                            <div class="search">
                                <input type="text" placeholder="Search for project" class="projectname" v-model="projectname">
                                <button 
                                class="btn-search"
                                @click="find_project">
                                    <i class="fa-solid fa-magnifying-glass"></i>
                                </button>
                            </div>
                            <div v-show="isloading" class="loading_message">
                                <h1> Hum something loud while others stare .......  </h1>
                            </div>
                            <div v-if="isfailed" class="error_message">
                                <h1> No Results Found   </h1>
                                <i class="fa-solid fa-face-sad-tear"></i>
                            </div>
                            <div v-show="has_resultat" class="result_team_message">
                                <h3>
                                        {{ projectresultat }}
                                </h3>
                            </div>
                    </div>
                    <div v-show="step2" class="modal-body">
                            <div class="search">
                                <input type="text" placeholder="Search for user" class="username" v-model="username">
                                <button 
                                class="btn-search"
                                @click="find_user">
                                    <i class="fa-solid fa-magnifying-glass"></i>
                                </button>
                            </div>
                            <div v-show="isloading" class="loading_message">
                                <h1> Hum something loud while others stare .......  </h1>
                            </div>
                            <div v-if="isfailed" class="error_message">
                                <h1> No Results Found   </h1>
                                <i class="fa-solid fa-face-sad-tear"></i>
                            </div>
                            <div v-show="has_resultat" class="result_team_message">
                                <h3>
                                        <i class="fa-solid fa-folder"></i>
                                        {{ projectresultatname }}
                                </h3>
                            </div>
                    </div>

            </div>
        </div>
</template>



<script scoped>
import axios from "axios"

export default {
    props:{
      User:{
        type: String,
        required: true
      }
    },
    data(){
        return{
            'step1':true,
            'step2':false,
            'projectname':'',
            'username':'',
            'headermessage':' select project ',
            'isloading':false,
            'isfailed':false,
            'has_resultat':false,
            'projectresultat':'',
            'projectresultatname':''
        }
    },
    methods:{
        CloseMe(){
            this.$emit("CloseModal");
        },
        find_project(){
            console.log(this.projectname);
            //check if user input are valid or note :
            if(this.projectname.length === 0 ||  /\s/.test(this.projectname)){
                this.$notify({
                        type:"error",
                        title: "Search Project Error ",
                        text: "Project name cannot be empty or contain spaces",
                        position:"bottom right"
                    });
            }else{
                //send get request to the back-end endpoint :
                this.isloading = true;
                axios.get("http://127.0.0.1:5000/get-all-project/Id/"+this.projectname)
                .then(response => {
                    //check response len :
                    if(response.data.reponse_data.length===0){
                        this.isloading = false;
                        this.isfailed = true;
                        setTimeout(()=>{
                        this.isfailed = false;
                        this.projectname = '';
                        },2000); 
                    }else{
                        this.projectresultat = response.data.reponse_data[0];
                        this.projectresultatname = this.projectresultat.Name;
                        this.isloading = false;
                        this.has_resultat = true;
                        //switch to the next step : 
                        this.step1 = false;
                        this.headermessage = " select user";
                        this.step2 = true;
                    }
                })
                .catch(error => {
                    console.error(error);
                });
            }
        },
        find_user(){
            if(this.username.length === 0 ||  /\s/.test(this.username)){
                this.$notify({
                        type:"error",
                        title: "Search User Error ",
                        text: "User name cannot be empty or contain spaces",
                        position:"bottom right"
                    });
            }else{
                this.isloading = true;
                axios.get("http://127.0.0.1:5000/get-all-project/User/"+this.username)
                .then(response => {
                    this.isloading = false;
                    if(response.data.reponse_data.length===0){
                        this.isfailed = true;
                        setTimeout(()=>{
                        this.isfailed = false;
                        this.step2 = false;
                        this.step1 = true;
                        this.headermessage=' select project ';
                        this.projectname = '';
                        this.username = '';
                        },2000);
                         this.has_resultat = false;
                    }else{
                        // i need to change end-point :)..........
                        // if return response len > 0 => user account exist:
                        // teste if the connected user is the owner of the project :
                        if(this.User === this.projectresultat.Owner){
                            let error_message = '';
                            let is_error = false;
                            console.log("you can submit invit or pullrequest ");
                            this.projectresultatname = "Invite "+this.username+" to contribute in "+this.projectname;
                            // check if the user target is in project target contributors liste :
                            if(this.projectresultat.Contributors.includes(this.username)===true){
                                // user alrady existe in project contrib user list :
                                error_message = 'User already within project contributors.';
                                is_error = true;
                            }
                            if(this.username === this.projectresultat.Owner){
                                error_message = 'The user is the proprietor of the project.';
                                is_error = true;
                            }
                            if(is_error === true){
                                this.$notify({
                                    type:"error",
                                    title: "Permission Error ",
                                    text: error_message,
                                    position:"bottom right"
                                });
                                setTimeout(()=>{
                                    this.has_resultat=false;
                                    this.step2 = false;
                                    this.step1 = true;
                                    this.headermessage=' select project ';
                                    this.projectname = '';
                                    this.username = '';
                            },2000);         
                            }else{
                                // no error all is great ==> send invit request :
                                let invitation = new FormData();
                                invitation.append("From",this.User);
                                invitation.append("To",this.username);
                                invitation.append("Project",this.projectname);
                                invitation.append("Satate","sended");
                                // sned to end-point:
                                axios.post("http://127.0.0.1:5000/invitation",invitation)
                                .then(response => {
                                    console.log(response);
                                }).catch(error => {
                                    console.error(error);
                                });
                            }
                        }else{
                            // the connected user is not the owner of project => you can't invit contribs :
                            this.$notify({
                                type:"error",
                                title: "Permission Error ",
                                text: "You are not the owner of project , you can't invit users ",
                                position:"bottom right"
                            });
                            setTimeout(()=>{
                                this.has_resultat=false;
                                this.step2 = false;
                                this.step1 = true;
                                this.headermessage=' select project ';
                                this.projectname = '';
                            },2000);
                        }
                    }
                }).catch(error => {
                    console.error(error);
                });
            }
        }
    }
    
}
</script>

<style scoped>
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
    padding:10px 10px;
    margin-top:8px;
    color:#ccc;
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