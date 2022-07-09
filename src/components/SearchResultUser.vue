<template>
        <button v-show="display_close_btn" type="button" class="btn-close btn-danger" aria-label="Close" v-on:click="close_search_area"></button>
        <template  v-for="(item,index) in Data" :key="index">
            <div v-show="display_search_area"  class="container">
                <div class="header">
                    <h5 class="project-title"><i class="fa-solid fa-folder"></i> {{ item.Name }}</h5>
                    <h6 class="project-contributors_number" 
                    @click="show_liste_contributors(item)"
                    > {{ item.Contributors.length }} contributors </h6>
                </div>
                <div class="body">
                    <p class="description">
                        {{ item.Discription }}
                    </p>
                </div>
                <div class="footer">
                    <h7 class="project-start-date"> {{ item.Sdate }}</h7>
                    <h7 class="project-state"> {{ item.State }}</h7>
                    <h7 class="project-end-date"> {{ item.Edate }}</h7>
            </div>                
            </div>
        </template>
    <ProjectContributorsListe 
        class=""
        v-show="display_contributors"
        v-bind:Project="projectTarget"
        @CloseModal="CloseModaleEvent"
        ></ProjectContributorsListe>         
</template>


<script scoped>
import ProjectContributorsListe from "@/components/ProjectContributorsListe.vue"
export default {
    props: ["Data"],
    components: {
        ProjectContributorsListe
    },
    data(){
        return{
            "display_search_area":false,
            "display_close_btn":false,
            "display_contributors":false,
            "projectTarget":''
        }
    },
    mounted(){
        this.display_search_area = true;
        this.display_close_btn = true;
    }
    ,methods:{
    close_search_area(){
        this.display_search_area = false;
        //send custom event to the main component:
        this.$emit("display_deafault")
    },
    show_liste_contributors(item ){
        this.projectTarget = item.Contributors;
        this.display_contributors = true;
        console.log(" detect click .......");
    },
    CloseModaleEvent(){
        this.display_contributors = false;
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
    cursor: pointer;
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