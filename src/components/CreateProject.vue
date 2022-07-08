<template> 
        <Transition name="bounce" appear>
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
                <transition name="nested" appear>
                    <div v-if="step1" class="modal-body">
                            <input type="text" placeholder="Project Name" class="projectname" v-model="projectname">
                            <textarea v-model="projectdescrib" placeholder="describe your project " cols="50" rows="5" class="description"></textarea>
                            <label for="startedDate"> Start date </label>
                            <input type="date" class="Date" id="startedDate" v-model="projectsdate">
                            <label for="endedDate"> Expected end  date </label>
                            <input type="date" class="Date" id="endedDate" v-model="projectedate">
                    </div>
                </transition>
                <transition name="nested" appear>
                    <div v-if="step2" class="modal-body">
                            <div class="search">
                                <input type="text" placeholder="Search for team" class="projectteam" v-model="projectteam">
                                <button class="btn-search">
                                    <i class="fa-solid fa-magnifying-glass"></i>
                                </button>
                            </div>
                    </div>
                </transition>
                <button 
                class="btn"
                @click="switchtostep2"
                v-show="step1"
                >
                    Next
                    <i class="fa-solid fa-circle-arrow-right"></i>
                </button>
            </div>
        </div>
        </Transition>
</template>

<script>
export default {
    data(){
        return{
            "headermessage":"Create New Project",
            "step1":Boolean,
            "step2":Boolean,
            "projectname":'',
            "projectdescrib":'',
            "projectsdate":'',
            "projectedate":''
        }
    },
    mounted(){
        this.step1= true;
        this.step2 = false;
    },
    methods:{
        CloseMe(){
            this.$emit("closeModal");
        },
        switchtostep2(){
            let counter = 0;
            let err_message = '';
            if(this.projectname.length === 0 ||  /\s/.test(this.projectname)){
                err_message = "Project name cannot be empty or contain spaces";
                counter = 1;
                console.log(err_message,counter);
            }
            if(this.projectdescrib.length === 0 || this.projectdescrib.length < 10 ){
                err_message = "The project description may not be empty or lower than 10";
                counter = 2;
            }
            if(this.projectsdate.length === 0 || new Date(this.projectsdate) < new Date().getDate()-1){
                err_message = "The project start date cannot be empty or earlier than present";
                counter = 3;
            }
            if(this.projectedate.length > 0 && new Date(this.projectedate)< new Date(this.projectsdate)){
                err_message = "The project completion date may not be earlier than the effective date.";
                counter = 4;
            }

            if(counter === 0){
                this.step1 = false;
                this.step2 = true;
                this.headermessage = "add team ";
            }else{
                this.$notify({
                        type:"error",
                        title: "Create Project Error ",
                        text: err_message,
                        position:"bottom right"
                    });
            }
            
            console.log(this.projectname,
                        this.projectdescrib,
                        this.projectsdate,
                        this.projectedate);
            
        }
    }
}
</script>




<style scoped>
/* rules that target nested elements */
.nested-enter-active,
.nested-leave-active {
  transition: all 3.5s ease-in-out;
}

.nested-enter-from,
.nested-leave-to {
  /*transform: translateX(500px);*/
  opacity: 0;
}




 .bounce-enter-active {
        animation: bounce-in 1.5s;
    }
    .bounce-leave-active {
        animation: bounce-in 0.5s reverse;
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
.projectname , .description, .Date, .projectteam{
    margin-bottom:10px;
    padding: 5px 10px;
    outline: none;
    background:transparent;
    color:#ccc;
    border:none;
    border-left: 5px solid #ccc;
}
.description{
    resize: none;
}
label{
    color:#eee;
}

.Date:hover{
    color-scheme: dark;
    cursor: pointer;
}
.btn{
    width:15%;
    text-align: right;
    align-items: center;
    margin: 0px 0px 0px auto;
    color:#ccc;
    border-color: #ccc;
    outline:none;
}
.btn:hover{
    background-color:#ccc;
    color:#fff;
    border-color: #fff;
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
</style>

