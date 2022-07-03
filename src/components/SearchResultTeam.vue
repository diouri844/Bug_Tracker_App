<template >
        <button v-if="display_close_btn" type="button" class="btn-close btn-danger" aria-label="Close" v-on:click="close_search_area_team"></button>
        <template  v-for="(item,index) in Data" :key="index">
            <div v-show="display_search_area"  class="container">
                <div class="header">
                    <h5 class="project-title"><i class="fa-solid fa-users"></i> {{ item.TeamName }}</h5>
                    <h6 class="teammanager">  {{ item.TeamManager }} </h6>
                    <h6 class="project-contributors_number"> {{ item.TeamGroup.length }} membre </h6>
                </div>
                <div class="body">
                    <a class="btn-display" data-bs-toggle="collapse" href="#collapseUsers" role="button" aria-expanded="false" aria-controls="collapseUsers">
                        <i class="fa-solid fa-list"></i> Users <span class="number"> ({{ item.TeamGroup.length }})</span>
                    </a>
                    <ul class="teamMember" id="collapseUsers" v-for="(member,index_member) in item.TeamGroup" :key="index_member">
                        <li class="member-item"><i class="fa-solid fa-user"></i> {{ member }}</li>
                    </ul>
                    <a class="btn-display" data-bs-toggle="collapse" href="#collapseProject" role="button" aria-expanded="false" aria-controls="collapseProject">
                        <i class="fa-solid fa-list"></i> Projects <span class="number"> ({{ item.TeamProject.length }})</span>
                    </a>
                    <ul class="teamProject" id="collapseProject" v-for="(project,index_project) in item.TeamProject" :key="index_project">
                        <li class="project-item"><i class="fa-solid fa-folder"></i> {{ project }}
                         <span :class="{ 'progress': isProgress , 'stoped': isStoped}" :currentState='item.ProjectState[index_project]'>{{ item.ProjectState[index_project] }} </span> </li>
                    </ul>
                </div>                
            </div>
        </template>
        
</template>



<script scoped>
export default {
    props: ["Data"],
    data(){
        return{
            "display_search_area":false,
            "display_close_btn":false,
            "isProgress":false,
            "isStoped":false,
            "currentState":''
        }
    },
    mounted(){
        this.display_search_area = true;
        this.display_close_btn = this.display_search_area;
        if(this.currentState==="In progression"){
            this.isProgress = true;
        }
        if(this.currentState==="On hold"){
            this.isStoped = true;
        }
        console.log(this.currentState);
    }
    ,methods:{
    close_search_area_team(){
        this.display_search_area = false;
        //send custom event to the main component:
        this.$emit("display_deafault_team")
    }
}
}
</script>

<style scoped>
.container {
  max-width: 700px;
  padding:10px 10px;
  margin-top:8px;
  display:grid;
  grid-column:  span 10;
  border-radius: 15px;
  background-color: #000;
}

.btn-close{
    margin-bottom: 5px;
    margin-top: 1px;
    padding:5px 5px;
    grid-column: 9/ span 3;
    background-color:#202131;
    border-radius: 15px;
    outline: none;
}
.progress{
    background-color:green;
}
.stoped{
    background-color:yellow;
}


.btn-display{
    color:#eee;
    max-width:250px;
    outline: none;
    text-decoration: none;
    font-size: 20px;
    margin-left:15px;
    margin-bottom:10px;
}

.fa-users{
    margin-left:3px;
    color:#1ecbe1;
}

.member-item {
    color:#eee;
    list-style: none;
}

.state{
    margin-left:20%;
    text-align: center;
    padding: 8px 8px;
    font-size: 14px;
    color:#fff;
    border-radius:15px;
}





.teammanager{
    color:#fff;
}



.header{
    display: grid;
    grid-template-columns: repeat(12,1fr);
    margin-bottom: 10px;
    display:flex;
    justify-content: space-between;
}
.project-title{
    margin-left:5px;
    background: -webkit-linear-gradient( #eee,#fff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-transform: capitalize;
    grid-column: span 5;
}
.project-contributors_number,.number{
    text-transform: capitalize;
    color:gray;
    grid-column: 8/ span 5;
    font-size:13px;
}
.body{
    display: grid;
    justify-content: space-between1;
}

.teamMember{
    
}
.teamProject{
    
}
.project-item{
    color:#eee;
    list-style: none;
}

</style>