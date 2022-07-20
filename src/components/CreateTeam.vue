<template>
    <div class="modal-overlay open-modal">
            <div class="modal-container">
                <div class="modal-header">
                    <div class="update">
                        <h3 class="header">
                            <i class="fa-solid fa-plus"></i>
                            {{ headermessage }}  
                        </h3>
                    </div>
                    <button class="btn-close btn-light bg-light" aria-label="Close" @click="CloseMe"></button>
                </div>
                    <div v-if="step1" class="modal-body">
                        <div class="search">
                            <input type="text" class="Nameteam" id="team" placeholder="Team-Name" v-model="teamName">
                            <button 
                                class="btn-search"
                                @click="check_team">
                                    <i class="fa-solid fa-paper-plane"></i>
                            </button>
                        </div>
                        <div v-show="isloading" class="loading_message">
                                <h1> Hum something loud while others stare .......  </h1>
                        </div>
                        <div v-show="isfailed" class="error_message">
                                <h1> Team name already used   </h1>
                                <i class="fa-solid fa-face-sad-tear"></i>
                        </div>
                    </div>
                    <div v-if="step2" class="modal-body">
                         <div class="search">
                            <input type="text" class="NameUser" id="team" placeholder="User-Name" v-model="userName">
                            <button 
                                class="btn-search"
                                @click="check_user">
                                    <i class="fa-solid fa-paper-plane"></i>
                            </button>
                        </div>
                        <div
                        v-show="has_resultat"
                            class="result_team_message">
                                <h5
                                class="item">
                                    <i class="fa-solid fa-user"></i>
                                    <span class="left"> {{ responseUser }}</span>
                                    <span
                                        type="button"
                                        v-if="beforcheck" 
                                        @click="invit_item()"
                                        class="right"
                                        id="liveToastBtn">
                                            <i  class="fa-solid fa-person-circle-plus"></i>
                                    </span>
                                    <span
                                        v-if="aftercheck"
                                        class="right">
                                        <i class="fa-solid fa-person-circle-check"></i>
                                    </span>
                                </h5>
                        </div>
                        <div
                        v-show="has_liste_invit"
                            class="result_team_invit">
                                <h4> {{ list_invitations.length }} invitations  : </h4>
                                <h6
                                v-for="(invit,index) in list_invitations" :key="index"
                                class="item">
                                    <i class="fa-solid fa-clock"></i>
                                    <span class="left"> {{ invit }} invited to <span class="teamname">{{ teamName }}</span></span>
                                    <span
                                        type="button"
                                        @click="delet_invit_item(index)"
                                        class="right">
                                        <i class="fa-solid fa-ban"></i>
                                    </span>
                                </h6>
                                <button
                                @click="send_invitation()" 
                                class="btn btn-outline-danger btn-sm">
                                    <i class="fa-solid fa-circle-check"></i>
                                    Create Team
                                </button>
                        </div>
                        <div v-show="isloading2" class="loading_message">
                                <h1> Hum something loud while others stare .......  </h1>
                        </div>
                        <div v-show="isfailed2" class="error_message">
                                <h1> No Results Found   </h1>
                                <i class="fa-solid fa-face-sad-tear"></i>
                        </div>
                    </div>
            </div>
        </div>
</template>


<script>
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
            'isloading':false,
            'isloading2':false,
            'isfailed':false,
            'isfailed2':false,
            'beforcheck':false,
            'aftercheck':false,
            'headermessage':'Create Team',
            'list_invitations':[],
            'has_liste_invit':false,
            'userName':'',
            'has_resultat':false,
            'responseUser':'',
            'teamName':''
        }
    },
    methods:{
        CloseMe(){
            this.$emit("closeModal");
        },
        send_invitation(){
            // create team for ferst : 
            let team_body = new FormData();
            team_body.append('TeamName',this.teamName);
            team_body.append('TeamManeger',this.User);
            // send request : 
            axios.post("http://127.0.0.1:5000/add/Team", team_body)
            .then(response => {
                this.$notify({
                    type:response.data.CreateState,
                    title: "Create Team info ",
                    text: response.data.message,
                    position:"bottom right"
                })
            })
            .catch(error => {
                console.error(error);
            })
            // send invitations for tergeted users :
            console.log("invitation sended service ");
            // create formdata :
            let subject = "I want you to join our team "+this.teamName;
            // parcour the invitation list :
            this.list_invitations.forEach(user =>{
                let current_invit = new FormData();
                current_invit.append('Target',this.teamName);
                current_invit.append('Type','Team');
                current_invit.append('from',this.User);
                current_invit.append('To',user);
                current_invit.append('Subject',subject);
                //send to the backend api :
                axios.post("http://127.0.0.1:5000/add/Invitation",current_invit)
                .then(response => {
                  this.$notify({
                    type:response.data.CreateState,
                    title: "Invite users to participate in Team info.",
                    text: response.data.message,
                    position:"bottom right"
                })  
                })
                .catch(error => {
                    console.error(error);
                });
            });
            setTimeout(()=>{
                this.CloseMe();
            },500);
        },
        invit_item(){
            console.log(this.list_invitations);
            //check if responseuser is already invited;
            if(this.list_invitations.includes(this.responseUser)===true){
                this.$notify({
                        type:"error",
                        title: "Invitation User Error ",
                        text: this.responseUser+" already invited ",
                        position:"bottom right"
                    });
                this.userName = '';
                this.has_resultat = false;
            }else{
                this.beforcheck = false;
                this.aftercheck = true;
                console.log("send invit to "+this.responseUser);
                this.list_invitations.push(this.responseUser);
                this.has_liste_invit = false;
                setTimeout(()=>{
                    this.has_liste_invit = true;
                },500);  
            }
        },
        delet_invit_item(index){
            // delet item from liste :
            const target_user = this.list_invitations[index]
            this.list_invitations = this.list_invitations.filter((invit)=>{
                return invit != target_user;
            });
            //update ui :
            this.$notify({
                        type:"succses",
                        title: "Delet invitation",
                        text: "Invitation to "+target_user+" deleted successfully",
                        position:"bottom right"
            });
            this.has_liste_invit = false;
            if(this.list_invitations.length > 0){
                setTimeout(()=>{
                    this.has_liste_invit = true;
                    this.has_resultat = false;
                },100);
            }
        },
        check_user(){
            this.has_resultat = false;
            this.beforcheck = true;
            this.aftercheck = false;
            if(this.userName.length=== 0 ||  /\s/.test(this.userName)){
                this.$notify({
                        type:"error",
                        title: "Search User Error ",
                        text: "User name cannot be empty or contain spaces",
                        position:"bottom right"
                    });
                this.userName = '';
            }else{
                //check if user target is the connected user :
                if(this.userName === this.User){
                    this.$notify({
                        type:"error",
                        title: "Search User Error ",
                        text: "There's no way you can send yourself an invitation.",
                        position:"bottom right"
                    });
                    this.userName = '';
                }else{
                    this.isloading2 = true;
                    axios.get("http://127.0.0.1:5000/check/user/"+this.userName)
                    .then(response => {
                        this.isloading2 = false;
                        console.log(response.data);
                        if(response.data.state===1){
                            this.beforcheck = true;
                            this.has_resultat = true;
                            this.responseUser = this.userName
                        }else{
                            this.isfailed2 = true;
                            setTimeout(()=>{
                                this.isfailed2 = false;
                                this.userName = '';
                            },1500);
                        }
                    })
                    .catch(error => {
                        console.error(error);
                    })
                }
            }
        }
        ,check_team(){
            if(this.teamName.length=== 0 ||  /\s/.test(this.teamName)){
                this.$notify({
                        type:"error",
                        title: "Search Team Error ",
                        text: "Team name cannot be empty or contain spaces",
                        position:"bottom right"
                    });
                this.teamName = '';
            }else{
                this.isloading = true;
                //send get request to the back-end:
                axios.get("http://127.0.0.1:5000/get-all-project/Team/"+this.teamName)
                .then(response => {
                    this.isloading = false;
                    if(response.data.reponse_data.length === 0){
                        // team not existe => switch to the next step :
                        console.log("to the seconde step :) ");
                        this.step1 = false;
                        this.step2 = true;
                        this.headermessage='Have users join your team.'   
                    }else{
                        this.isfailed = true;
                        setTimeout(()=>{
                            this.isfailed = false;
                            this.teamName = '';   
                        },2000);
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
.Nameteam, .NameUser{
    margin-bottom:10px;
    padding: 5px 10px;
    outline: none;
    background:transparent;
    color:#ccc;
    border:none;
    border-left: 5px solid #ccc;
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
.search{
    display:flex;
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

.loading_message h1{
  grid-column: 2/ span 7;
  display: flex;
  font-size:20px;
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}

.result_team_message{
    padding:10px 10px;
    margin-top:8px;
    color:#ccc;
}
.item{
    cursor:pointer;
    padding-left:15px;
}
.result_team_invit{
    padding:10px 10px;
    bottom: 1%;
    top:70%;
    position:absolute;
    width:100%;
    margin-top:15px;
    color:#fff;
}
.result_team_invit h4{
    border-bottom : 2px solid #eee;
    color:#eee;
}
.result_team_invit .btn-outline-danger{
    right:1%;
    margin-top:5px;
    position:absolute;
}

.result_team_invit .fa-solid{
    color:#ccc;
}

.result_team_invit .left .teamname{
    color:#ccc;
    text-decoration:underline;
}

.result_team_invit .right:hover{
    color:#ccc;
    cursor:pointer;
    font-size: 20px;
}




.right:hover{
    color:#fff;
    cursor:pointer;
    font-size: 25px;
}
.fa-person-circle-check{
    color:#fff;
}
.left{
    margin-left:5px;
}
.right{
    position: absolute;
    right: 0;
    margin-right:10px;
}

</style>