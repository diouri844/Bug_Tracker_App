<template>
    <div class="form">
        <div class="header">
            <h1>create account <span>now</span></h1>
        </div>
        <div class="form_body">
            <div class="body-item">
                <label><i class="fa-solid fa-user"></i> ferst <span>name</span></label>
                <input type="text" placeholder="Ch__open866" v-model="user_fname">
            </div>
            <div class="body-item">
                <label><i class="fa-solid fa-user"></i> last <span>name</span></label>
                <input type="text" placeholder="Ch__open866" v-model="user_lname">
            </div>
            <div class="body-item">
                <label><i class="fa-solid fa-envelope"></i> <span>email</span></label>
                <input type="email" placeholder="Ch__open866@gmail.com" v-model="user_email">
            </div>
            <div class="body-item">
                <label><i class="fa-solid fa-envelope"></i> birth-<span>day</span></label>
                <input type="date" v-model="user_Bdate">
            </div>
            <div class="body-item">
                <label><i class="fa-solid fa-key"></i> user <span>password</span></label>
                <input type="password" placeholder="****************" v-model="user_password">
            </div>
            <div class="body-item">
                <label><i class="fa-solid fa-key"></i> confirme <span>password</span></label>
                <input type="password" placeholder="****************" v-model="user_password_confirmation">
            </div>
            <button class="login-btn" v-on:click="check_user_registration">create account <i class="fa-solid fa-plus"></i> </button>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            "user_fname":"",
            "user_lname":"",
            "user_email":"",
            "user_Bdate":"",
            "user_password":"",
            "user_password_confirmation":""
        }
    },
    methods:{
        check_user_registration(){
            let counter = 0;
            if(this.user_fname.length>3){
                counter++;
            }
            if(this.user_lname.length>5){
                counter++;
            }
            if(this.user_email.length>10){
                counter++;
            }
            if(new Date(this.user_Bdate).getFullYear()<2004){
                counter++;
            }
            if(this.user_password.length>8){
                counter++;
            }
            if(this.user_password_confirmation.length>8){
                counter++;
            }
            if(this.user_password===this.user_password_confirmation){
                counter++;
            }
            console.log(counter);
        }
    }
}
</script>



<style scoped>
    .form{
        font-family: Times, "Times New Roman", Georgia, serif;
        background:transparent;
        padding:2px;
        font-size: 14px;
        margin:auto auto;
        border:1px solid #c6d9dc;
        border-radius: 15px;
        width:700px;
    }
    .header{
        text-transform: capitalize;
        color:#0d0f0c;
    }
    span{
        color:#CCCA0D;
    }
    .login-btn{
        padding: 10px 10px;
        margin-bottom: 10px;
        width: 250px;
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
        grid-template-columns:repeat(2,1fr);
        align-items: left;
        margin:10px 0;
    }
    input{
        width:80%;
        margin-left:5%;
        border-top: 0;
        border-bottom: 0;
        border-right: 0;
        border-left: 5px solid #c6d9dc;
        padding: 10px 10px;
        background:transparent;
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