<template >
        <button v-if="display_close_btn" type="button" class="btn-close btn-danger" aria-label="Close" v-on:click="close_search_area_team"></button>
        <template  v-for="(item,index) in Data" :key="index">
            <div v-show="display_search_area"  class="container">
                <div class="header">
                    <h5 class="project-title"><i class="fa-solid fa-folder"></i> {{ item.TeamName }}</h5>
                    <h6 class="teammanager">  {{ item.TeamManager }} </h6>
                    <h6 class="project-contributors_number"> {{ item.TeamGroup.length }} membre </h6>
                </div>
                <div class="body">
                    <ul class="teamMember" v-for="(member,index_member) in item.TeamGroup" :key="index_member">
                        <li class="member-item"> {{ member }}</li>
                    </ul>
                    <ul class="teamProject" v-for="(project,index_project) in item.TeamProject" :key="index_project">
                        <li class="project-item"> {{ project }}</li>
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
            "display_close_btn":false
        }
    },
    mounted(){
        this.display_search_area = true;
        this.display_close_btn = this.display_search_area;
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

.fa-folder{
    color:orange;
}

.header{
    display: grid;
    grid-template-columns: repeat(12,1fr);
    margin-bottom: 10px;
    display:flex;
    justify-content: space-between;
}
.project-title{
    background: -webkit-linear-gradient( #eee,#fff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-transform: capitalize;
    grid-column: span 5;
}
.project-contributors_number{
    text-transform: capitalize;
    color:gray;
    grid-column: 8/ span 5;
    font-size:13px;
}
.description{
    background-color:#202131;
    padding:10px 10px;
    border-radius: 15px;
    color:#fff;
    text-transform: capitalize;
    text-justify: newspaper;
    font-family: monospace;
    font-size: 15px;
}

.footer{
    display:flex;
    justify-content: space-between;
}
.footer .project-start-date{
    color:#00ff0d;
    font-family: Times;
    font-size: 15px;
    text-decoration: underline;
    margin-right:5%;
}
.footer .project-state{
    color:#c6d9dc;
    font-family:-apple-system;
    font-size: 15px;
    margin-right:5%;
}
.footer .project-end-date{
    color:#fff;
    font-family: Times;
    font-size: 15px;
}

</style>