<template>
    <div class="container">
        <div v-show="isloading" class="loading_message">
            <h4> Hum something loud while others stare ....... </h4>
        </div>
        <div class="header" v-show="has_invitations">
            <h5>{{ invitations.length }} Invitations for you </h5>
            <button class="btn-close btn-light bg-light" aria-label="Close" @click="CloseMe"></button>
            <!--   show liste of last notifications : -->
        </div>
        <div class="error_message" v-show="no_invitations">
            <h1> No notification found at the moment. </h1>
            <i class="fa-solid fa-face-sad-tear"></i>
        </div>
    </div>
</template>





<script>
import axios from "axios"
export default {
    props: {
        User: {
            type: String,
            required: true
        }
    },
    mounted(){
        //send get request to load all notification(invitations for now ):
        axios.get("http://127.0.0.1:5000/get-all-project/Invitation/"+this.User)
        .then(response => {
            this.isloading = false;
            if(response.data.reponse_data.length === 0){
                this.no_invitations = true;
                setTimeout(() => {
                    this.CloseMe();
                }, 2500);
            }else{
                // we have invitations to display:
                console.log(response.data);
                this.invitations = response.data.reponse_data;
                this.has_invitations = true;
            }
        })
        .catch(error => {
            console.error(error);
        });
        
    },
    data(){
        return{
            'invitations':[],
            'isloading':true,
            'has_invitations':false,
            'no_invitations':false,
        }
    },
    methods:{
        CloseMe(){
            this.$emit("closeMe");
        }
    }
}
</script>



<style scoped>









.header{
    display: flex;
    justify-content: space-between;
    font-weight: bold;
}
.container {
    max-width: 700px;
    padding: 10px 10px;
    margin-top: 8px;
    margin-left:17%;
    left:0;
    border-radius: 15px;
    color:#ccc;
    background-color: transparent;
}
.error_message{
    width: 4000px;
    padding: 10px 10px;
    margin-top: 8px;
    display: flex;
    text-align: left;
    align-content: center;
    color: #ccc;
}
.error_message h1 {
    display: flex;
    font-size: 20px;
    text-transform: capitalize;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}

.error_message .fa-face-sad-tear {
    font-size: 20px;
    margin-left: 10px;
}
.loading_message {
    width: 500px;
    padding: 10px 10px;
    font-size: 20px;
    margin-top: 8px;
    display: flex;
    text-align: left;
    align-content: center;
    color: #fff;
}

.btn-close {
    margin-bottom: 5px;
    margin-top: 1px;
    padding: 5px 5px;
    grid-column: 9/ span 3;
    background-color: #202131;
    border-radius: 15px;
    outline: none;
}
</style>