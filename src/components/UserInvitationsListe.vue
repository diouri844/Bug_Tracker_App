<template>
    <div class="container">
        <div v-show="isloading" class="loading_message">
            <h4> Hum something loud while others stare ....... </h4>
        </div>
        <div class="container" v-show="has_invitations">
            <div class="header">
                <h5>{{ invitations.length }} Invitations for you </h5>
                <button class="btn-close btn-light bg-light" aria-label="Close" @click="CloseMe"></button>
            </div>

            <!--   show liste of last notifications : -->
            <perfect-scrollbar class="body_tab">
                <div v-for="(item,index) in invitations" :key="index" class="item">
                    <div class="invitation-header">
                        <h5 class="invitaion-sender"><i class="fa-solid fa-user-tag"></i> {{ item.From}} </h5>
                        <h7 class="invitation-type"> {{ item.Type }} : {{ item.Target }}
                            <i class="fa-solid fa-lightbulb"></i>
                        </h7>
                    </div>
                    <div class="invitation-body">
                        <p class="description">
                            {{ item.Subject }}
                        </p>
                    </div>
                    <div class="invitation-footer" v-if="item.State === 'Sended'">
                        <button class="accept-invit" @click="accept(index)"><i class="fa-solid fa-check"></i></button>
                        <button class="refuse-invit" @click="refuse(index)"><i class="fa-solid fa-ban"></i></button>
                    </div>
                </div>
            </perfect-scrollbar>
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
                this.invitations = response.data.reponse_data;
                console.log(this.invitations);
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
            // clear all notifications : 
            axios.delete("http://127.0.0.1:5000/update/Invitation/"+this.User)
            .then(response => {
                console.log(response.data);
            }).catch(error => { console.error(error);})
        },
        accept(index){
            console.log(index, "accept invitation from ", this.invitations[index]);
            let invit_data  = new FormData();
            invit_data.append("From", this.invitations[index]['From']);
            invit_data.append("Type", this.invitations[index]['Type']);
            invit_data.append("To", this.invitations[index]['To']);
            invit_data.append("Target", this.invitations[index]['Target']);
            if(this.invitations[index]['Type'] === 'Project'){
                // we have some meta data : 
                invit_data.append('TeamName', this.invitations[index]['TeamName']);
            }
            console.log("send :  ",invit_data);
            // sendrequest to back-end end-point
            axios.post("http://127.0.0.1:5000/update/Invitation/Accept",invit_data)
            .then(response => {
                console.log(response.data);
                this.$notify({
                    type: response.data.state,
                    title: "Notification ",
                    text: response.data.message,
                    position: "bottom right"
                });
            })
            .catch(error => {
                console.error(error);
            })
            // filter array :
            let i = 0;
            this.invitations = this.invitations.filter((invit)=>{
                return invit.Target != this.invitations[i].Target;
            })
            this.has_invitations = false;
            this.isloading = true;
            setTimeout(()=>{
                this.isloading = false;
                this.has_invitations = true;
            },500);
        },
        refuse(index){
            let invit_data = new FormData();
            invit_data.append("From", this.invitations[index]['From']);
            invit_data.append("Type", this.invitations[index]['Type']);
            invit_data.append("To", this.invitations[index]['To']);
            invit_data.append("Target", this.invitations[index]['Target']);
            // send refuse request to the end-point :
            axios.post("http://127.0.0.1:5000/update/Invitation/Refuse",invit_data)
            .then(response => {
                console.log(response.data);
                this.$notify({
                    type: response.data.state,
                    title: "Notification ",
                    text: response.data.message,
                    position: "bottom right"
                });
            })
            .catch(error => {
                console.error(error);
            });
            // update ui :
            let i = 0;
            this.invitations = this.invitations.filter((invit) => {
                return invit.Target != this.invitations[i].Target;
            })
            this.has_invitations = false;
            this.isloading = true;
            setTimeout(() => {
                this.isloading = false;
                this.has_invitations = true;
            }, 500);
        }
    }
}
</script>



<style scoped>

.body_tab{
    height: 400px;
}

.item{
    margin-top: 15px;
    border-top: 1px solid #ccc;
    padding: 10px 10px;
    height:auto;
}

.invitaion-sender, .invitaion-type{
    color:#fff;
}

.description{
    border-left: 5px solid #fff;
    text-align: left;
    text-transform: capitalize;
    font-weight:bold;
    padding-left: 3px;
}

.invitation-body{
    margin-top:7px;
}

.header , .invitation-header, .invitation-footer {
    display: flex;
    justify-content: space-between;
    font-weight: bold;
}
.invitation-footer{
    justify-content: right;
}



.accept-invit{
    background-color:transparent;
    border:1px solid #fff;
    color:#ccc;
    border-radius: 5px;
    margin-right:5px;
    padding-left:15px;
    padding-right:15px;
}
.accept-invit:hover{
    background-color:#ccc;
    color:#fff;
    border:none;
}
.refuse-invit{
    background-color: #202131;
    color:#eee;
    border:none;
    outline:none;
    border-radius: 5px;
    padding-left: 15px;
    padding-right: 15px;
}
.refuse-invit:hover{
    background-color: transparent;
    border: 1px solid #ccc;
    color: #ccc;
}

.container {
    max-width: 900px;
    padding: 10px 10px;
    margin-top: 8px;
    left:0;
    border-radius: 15px;
    color:#ccc;
    background-color: transparent;
}
.error_message{
    width: 1000px;
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