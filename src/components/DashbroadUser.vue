<template>
  <div class="main">
    <h1 class="main-title">
      <i class="fas fa-house custom-element"></i>
      Your Home
      <span class="custom-element"> {{ userName }} </span>
    </h1>
    <div class="search-area">
      <button class="search-btn-start" v-bind:onclick="search_Now"><i class="fa-solid fa-magnifying-glass"></i></button>
      <input type="text" placeholder="Search" class="input_search" v-model="search_input" />
      <select name="type" id="search_global_subject" v-model="search_subject">
        <option class="option_item" value="Id">Project Id</option>
        <option class="option_item" value="User">User </option>
        <option class="option_item" value="Team">Team </option>
      </select>
    </div>
    <div class="btn-group">
      <button type="button" class="btn dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown"
        aria-expanded="false">
        <i class="fa-solid fa-user"></i>
        {{ userName }} <span class="visually-hidden">Toggle Dropdown</span>
      </button>
      <ul class="dropdown-menu">
        <li><span class="dropdown-item"><i class="fa-solid fa-gear"></i> Setting</span></li>
        <li v-on:click="logout_to_home"><span class="dropdown-item"><i class="fa-solid fa-right-from-bracket"></i>
            Logout</span></li>
      </ul>
    </div>
    <UserProjectList class="side-item" v-if="isdefault" :User="this.userName">
    </UserProjectList>
    <div v-show="isloading" class="loading_message">
      <h1> Hum something loud while others stare ....... </h1>
    </div>
    <div v-if="isfailed" class="error_message">
      <h1> No Results Found </h1>
      <i class="fa-solid fa-face-sad-tear"></i>
    </div>
    <SearchResultUser @display_deafault="redirect_to_home" class="side-item" v-if="show_search_result"
      v-bind:Data="search_result_data">
    </SearchResultUser>
    <SearchResultTeam @display_deafault_team="redirect_to_home_form_team" class="side-item"
      v-if="show_search_team_result" v-bind:Data="search_result_data">
    </SearchResultTeam>
    <SearchResultId @display_deafault_id="redirect_to_home_from_id" class="side-item" v-if="show_search_Id_result"
      v-bind:Data="search_result_data">
    </SearchResultId>
    <FoterTool v-if="isdefault" class="footer-comp" @addProject="addNewProject = true" @addContrib="invitContrib = true"
      @UpdateProject="updateProject = true" @addTeam="addTeam = true" @showNotifications="DisplayNotifications">
    </FoterTool>
    <CreateProject v-bind:User="userName" v-if="addNewProject" @closeModal="force_closing_modal">
    </CreateProject>
    <InviteContribe v-if="invitContrib" @closeModal="force_closing_modal" v-bind:User="userName">
    </InviteContribe>
    <UpdateProjectInfo v-if="updateProject" @closeModal="force_closing_modal" v-bind:User="userName">
    </UpdateProjectInfo>
    <CreateTeam v-if="addTeam" @closeModal="force_closing_modal" v-bind:User="userName">
    </CreateTeam>
    <UserInvitationsListe class="side-item"  v-if="showInvitations" @closeMe="force_closing_modal"
      v-bind:User="userName">
    </UserInvitationsListe>
  </div>
</template>

<script>
// separt dashbroad to many components : teams list/current user projects-engagement:
import UserProjectList from "@/components/UserProjectList.vue"
import SearchResultUser from "@/components/SearchResultUser.vue"
import SearchResultTeam from "@/components/SearchResultTeam.vue"
import SearchResultId from "@/components/SearchResultId.vue"
import FoterTool from "@/components/FoterTool.vue"
import CreateProject from "@/components/CreateProject.vue"
import  InviteContribe from "@/components/InviteContribe.vue"
import UpdateProjectInfo from "@/components/UpdateProjectInfo.vue"
import CreateTeam from "@/components/CreateTeam.vue"
import UserInvitationsListe from "@/components/UserInvitationsListe.vue"
import axios from 'axios'


export default {
    props:{
      userName:{
        type: String,
        required: true
      }
    },
    components:{
      UserProjectList,
      SearchResultUser,
      SearchResultTeam,
      SearchResultId,
      FoterTool,
      CreateProject,
      InviteContribe,
      UpdateProjectInfo,
      CreateTeam,
      UserInvitationsListe
    },
    data(){
      return{
        "isdefault":true,
        "search_input":'',
        "search_subject":'Id',
        "show_search_result":false,
        "show_search_team_result":false,
        "show_search_Id_result":false,
        "search_result_data":'',
        "isloading":false,
        "isfailed":false,
        "addNewProject":false,
        "invitContrib":false,
        "updateProject":false,
        "addTeam":false,
        "showInvitations":false,
        'search_dispo':true,
        "currentUserData":''
      }
    },
    methods:{
      logout_to_home(){
        //send custom-event to main component :
        this.$emit("tooglelogout");
      },
      redirect_to_home(){
          this.show_search_result = false;
          this.isdefault = true;
      },
      redirect_to_home_form_team(){
        this.show_search_team_result = false;
        this.isdefault = true;
      },
      redirect_to_home_from_id(){
        this.show_search_Id_result = false;
        this.isdefault = true;
      },
      DisplayNotifications(){
        this.isdefault = false;
        //this.search_dispo = false;
        this.showInvitations = true;
      },
      force_closing_modal(){
        this.isdefault = false;
        this.addNewProject = false;
        this.invitContrib =false;
        this.updateProject = false;
        this.addTeam = false;
        this.showInvitations = false;
        //this.isloading = true;
        setTimeout(()=>{
          //this.search_dispo = true;
          this.isdefault = true;
        },500);
        this.$forceUpdate();
        
      },
      search_Now(){
        //check if entry is failed :
        if(this.search_input.length===0  || /\s/.test(this.search_input)){
          this.$notify({
                        type:"error",
                        title: "Search Error ",
                        text: "Invalid search input :)",
                        position:"bottom right"
                    });
        }else{
          this.isloading = true;
          this.show_search_result = false;
          this.show_search_team_result= false;
          this.show_search_Id_result = false;
          console.log(this.search_input,this.search_subject);
          this.isdefault = false;
          this.show_search_result=false;
          // get_all_project && fetch :
         axios.get("http://127.0.0.1:5000/get-all-project/"+this.search_subject+"/"+this.search_input).then(response =>{
          // display result in result_component JSON.stringify(:
          this.search_result_data = response.data['reponse_data'];
          this.isloading = false;
          if(response.data.reponse_data.length===0){
            //displaye error :
            this.isfailed = true;
            setTimeout(()=>{
              this.isfailed = false; 
              this.isdefault = true;  
            },1500);
          }else{
            //check search subject :
            if(this.search_subject==="User"){
              this.show_search_result=true;
            }
            if(this.search_subject==="Team"){
              this.show_search_team_result = true;
            }
            if(this.search_subject==="Id"){
              this.show_search_Id_result = true;
            }
          }
          console.log(this.search_result_data);

        }).catch(error => {
          console.error(error);
        });
        }
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
  background-color: #310e68;
  background-image: linear-gradient(316deg, #310e68 0%, #5f0f40 74%);
  position:absolute;
  display:grid;
  grid-template-columns:repeat(12,1fr);
  grid-template-rows:repeat(12,1fr);
}
.fa-magnifying-glass{
  color:#fff;
  font-size:18px;
  padding:5px 5px;
  border-radius:8px;
  border:2px solid #fff;
}
.fa-magnifying-glass:hover{
  background-color:#0E685E;
  color:#fff;
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
  border-radius: 26px 5px 5px 6px;
}

select option[value="Id"] {
  background-color:#0E685E;
}
select option[value="User"] {
  background-color:#0E685E;
}

select option[value="Team"] {
  background-color:#0E685E;
}
.search-btn-start{
  display: flex;
  background:transparent;
  border:none;
}

  .search-area{
    display:grid;
    grid-template-columns: repeat(12,1fr);
    justify-content: center;
    align-items: center;
    grid-row: 2/ span 3;
    grid-column: 4/ span 7;
}
.loading_message{
    width: 1000px;
    padding:10px 10px;
    margin-top:8px;
    display:grid;
    grid-template-columns: repeat(12,1fr);
    grid-column: 3/ span 9;
    text-align:left;
    align-content: center;
    color:#fff;
}

.error_message{
  width: 1000px;
    padding:10px 10px;
    margin-top:8px;
    display:grid;
    grid-template-columns: repeat(12,1fr);
    grid-column: 3/ span 9;
    text-align:left;
    align-content: center;
    color:#ccc;
}

.error_message h1{
  grid-column: 3/ span 2;
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
  grid-column: 2/ span 9;
  display: flex;
  font-size:20px;
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
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
  max-width:100px;
  text-align: center;
  border:none;
  padding:5px 5px;
}
.dropdown-item, .dropdown-toggle-split{
  color:#fff;
  cursor:pointer;
  width:auto;
  background:transparent;
  max-width:120px;
  outline:none;
}
.dropdown-item{
  margin-left:28%;
}
.dropdown-item:hover, .dropdown-toggle-split:hover{
  color:#fff;
  background-color: #0E685E;
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
  color:#0E685E;
}

.side-item{
  grid-column: 2/ span 10 ;
  grid-row: 4/ span 5;
}


</style>