<template>
    <div class="container">
        <button 
            @mouseenter="hover1 = true"
            @mouseleave="hover1 = false"
            @click="sendCustomProjectEvent"
            class="btn btn-sm btn-outline-info item">
            <i class="fa-solid fa-plus"></i>
        </button>
        <button 
            @mouseenter="hover2 = true"
            @mouseleave="hover2 = false"
            @click="sendCustomContribEvent"
            class="btn btn-sm btn-outline-light item">
            <i class="fa-solid fa-code-pull-request"></i>
        </button>
        <button
            @mouseenter="hover3 = true"
            @mouseleave="hover3 = false"
            @click="sendCustomUpdateEvent"
            class="btn btn-sm btn-outline-primary item">
            <i class="fa-solid fa-pen-to-square"></i>
        </button>
        <button
            @mouseenter="hover4 = true"
            @mouseleave="hover4 = false"
            @click="sendCustomTeamEvent"
            class="btn btn-sm btn-outline-danger item">
            <i class="fa-solid fa-people-group"></i>
        </button>
    </div>
    <h6 class="details-msg-1" v-show="hover1">{{ msg1 }}</h6>
    <h6 class="details-msg-2" v-show="hover2">{{ msg2 }}</h6>
    <h6 class="details-msg-3" v-show="hover3">{{ msg3 }}</h6>
    <h6 class="details-msg-4" v-show="hover4">{{ msg4 }}</h6>
</template>



<script>
export default {
    data(){
        return{
            "hover1":false,
            "hover2":false,
            "hover3":false,
            "hover4":false,
            "msg1":'create new project',
            "msg2":'invite contributor',
            "msg3":'update project info',
            "msg4":'create new team'
        }
    },
    methods:{
        sendCustomProjectEvent(){
            this.$emit("addProject");
        },
        sendCustomContribEvent(){
            this.$emit("addContrib");
        },
        sendCustomUpdateEvent(){
            this.$emit("UpdateProject");
        },
        sendCustomTeamEvent(){
            this.$emit("addTeam");
        }
    }
    
}

</script>



<style  scoped>
@keyframes rotate {
  0% {
    transform: rotate(-45deg);
    opacity:1.5;
  }
  100% {
    transform: rotate(180deg);
    opacity:1;
  }
}




.container{
    margin: auto;
    position: fixed;
    left: 0;
    bottom: 1%;
    width: 100%;
    display: flex;
    justify-content: center;
}
.item{
    margin-left:5px;
    margin-right:5px;
}
.details-msg-1,.details-msg-2 ,.details-msg-3, .details-msg-4{
    color:#ececec;
    margin:15px auto;
    position: fixed;
    left: 38%;
    bottom: 5%;
    display:flex;
    justify-content: center;
    border-bottom: 1px solid #ececec;
    text-transform: capitalize;
}

.btn:hover{
    animation: rotate 2s infinite;
}




</style>