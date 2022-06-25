<template>
    <transition name="bounce" appear>
        <div class="form">
            <div class="header">
                <h1>create account <span>now</span></h1>
            </div>
            <div class="form_body">
                <div class="body-item">
                    <input type="text" placeholder="Ferst Name" v-model="user_fname">
                </div>
                <div class="body-item">
                    <input type="text" placeholder="Last Name" v-model="user_lname">
                </div>
                <div class="body-item">
                    <input type="email" placeholder="Email address" v-model="user_email">
                </div>
                <div class="body-item">
                    <input type="date" v-model="user_Bdate">
                </div>
                <div class="body-item">
                    <input type="password" placeholder="Password" v-model="user_password">
                </div>
                <div class="body-item">
                    <input type="password" placeholder="Confirm your password" v-model="user_password_confirmation">
                </div>
                <button class="login-btn" id="login-btn" v-on:click="check_user_registration"> {{ this.login_button_body }} 
                <i class='fa-solid fa-plus'></i></button>
            </div>
        </div>
    </transition>
</template>

<script scoped>

import axios from "axios"

export default {
    data(){
        return{
            "user_fname":"",
            "user_lname":"",
            "user_email":"",
            "user_Bdate":"",
            "user_password":"",
            "user_password_confirmation":"",
            "login_button_body":"create account "
        }
    },
    methods:{
        check_user_registration(){
            this.login_button_body = "Creating a new account .....";
            let counter_ckeck = 0;
            if(this.user_fname.length>3){
                counter_ckeck+=1;
            }
            if(this.user_lname.length>5){
                counter_ckeck+=1;
            }
            if(this.user_email.length>10){
                counter_ckeck+=1;
            }
            if(new Date(this.user_Bdate).getFullYear()<=2004){
                counter_ckeck+=1;
            }
            if(this.user_password.length>8){
                counter_ckeck+=1;
            }
            if(this.user_password_confirmation.length>8){
                counter_ckeck+=1;
            }
            if(this.user_password===this.user_password_confirmation){
                counter_ckeck+=1;
                if(counter_ckeck===7){
                /* regstration protocole :  */
                let user_registration_data = new FormData();
                user_registration_data.append("FerstName",this.user_fname);
                user_registration_data.append("LastName",this.user_lname);
                user_registration_data.append("Email",this.user_email);
                user_registration_data.append("Password",this.user_password);
                /* show data :  */
                axios.post("http://127.0.0.1:5000/get-registration",user_registration_data).then(response => {
                    console.log(response);
                    if(response.data.RegistrationState===1){
                        this.$notify({
                        type:"succses",
                        title: "Creating New account ",
                        text: response.data.message,
                        position:"bottom right"
                    });
                    // send custom event to the main component (app):
                    this.$emit("toogletologin");
                    }else{
                        this.$notify({
                        type:"error",
                        title: "Creating New account ",
                        text: response.data.message,
                        position:"bottom right"
                    });
                    }
                }).catsh(error => {
                    console.err(error);
                });
                }else{
                    this.$notify({
                        type:"error",
                        title: "Error !!",
                        text: "all fields must be completed !!",
                        position:"bottom right"
                    });
                }
            }else{
                this.$notify({
                    type:"error",
                    title: "Error !!",
                    text: "Password and confirmation password must be the same !!",
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
        animation: bounce-in 1.5s;
    }
    .bounce-leave-active {
        opacity:0;
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
        width:500px;
        vertical-align: middle;
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
        margin-left:25%;
        width: 50%;
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
    label{
        font-size:17px;
        text-transform: capitalize;
        text-align: center;
        margin-bottom: 10px;
        color:#c6d9dc;
    }
</style>