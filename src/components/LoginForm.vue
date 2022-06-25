<template>
    <Transition name="bounce" appear>
        <div class="form">
            <div class="header">
                <h1>login <span>now</span></h1>
            </div>
            <div class="form_body">
                <div class="body-item">
                    <input type="text" placeholder=" user name " v-model="user_name">
                </div>
                <div class="body-item">
                    <input type="email" placeholder=" email" v-model="user_email">
                </div>
                <div class="body-item">
                    <input type="password" placeholder=" Password " v-model="user_password">
                </div>
                <button class="login-btn" v-on:click="check_user_input">login <i class="fa-solid fa-arrow-right-to-bracket"></i> </button>
            </div>
        </div>
    </Transition>
</template>

<script>
import axios from "axios";

export default {
    data(){
        return{
            "user_name":'',
            "user_email":'',
            "user_password":'',
            "checked_counter":0
        }
    },
    methods:{
        check_user_input(){
            //check if all required is failed :
            if (this.user_name.length>3 && this.user_email.length>10 && this.user_password.length>5){
                this.checked_counter=3;
            }
            // check if counter == 3
            if(this.checked_counter===3){
                let login_data = new FormData() 
                login_data.append("name",this.user_name);
                login_data.append("email",this.user_email);
                login_data.append("pswd",this.user_password);
                axios.post("http://127.0.0.1:5000/get-auth",login_data).then(response => {
                    if(response.data.statelogin===1){
                        this.$notify({
                        type:"succses",
                        title: "Login ",
                        text: response.data.message,
                        position:"bottom right"
                    });
                    // send custom event to the main component (app):
                    this.$emit("toogleComponent",this.user_name);
                    }else{
                        this.$notify({
                        type:"error",
                        title: "Login ",
                        text: response.data.message,
                        position:"bottom right"
                    });
                    }
                    
                }).catsh(error => {
                    console.err(error);
                });
            }else{
                console.log(this.checked_counter);
                this.$notify({
                type:"error",
                title: "Error !!",
                text: "all fields must be completed !!",
                position:"bottom right"
            });
            }
        }
    }
}
</script>




<style scoped>
    /* animation setup  */
    .bounce-enter-active {
        animation: bounce-in 2.5s;
    }
    .bounce-leave-active {
        opacity:0;
    }
    @keyframes bounce-in {
        0% {
            transform: scale(0);
        }
        50% {
            transform: scale(1.25);
        }
        100% {
            transform: scale(1);
        }
    }
    .form{
        font-family: Times, "Times New Roman", Georgia, serif;
        background:#fff;
        padding:2px;
        font-size: 14px;
        margin-left:auto;
        margin-right: auto;
        margin-top: 60px;
        border:1px solid #E8126B;
        border-radius: 15px;
        width:300px;
    }
    .header{
        text-transform: capitalize;
        color:#c6d9dc;
        text-align:center;
        align-items: center;
    }
    span{
        color:#CCCA0D;
    }
    .login-btn{
        padding: 10px 10px;
        margin-bottom: 10px;
        margin-left:10%;
        width: 80%;
        text-align: center;
        text-transform: capitalize;
        border-radius: 5px;
        border: 1px solid #c6d9dc;
        background-color:#fff;
        color: #ccca0d;
    }
    .login-btn:hover{
        background-color:#ccca0d;
        color:#fff;
        border: 1px solid #ccca0d; 
    }
    .body-item{
        display:grid;
        grid-template-rows: 1fr;
        align-items: left;
        margin:10px 0;
    }
    input{
        width:70%;
        margin:10px 12%;
        border-top: 0;
        border-bottom: 0;
        border-right: 0;
        border-left: 5px solid #c6d9dc;
        padding: 10px 10px;
        color:#c6d9dc;
    }
</style>