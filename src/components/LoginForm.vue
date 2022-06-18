<template>
    <div class="form">
        <div class="header">
            <h1>login <span>now</span></h1>
        </div>
        <div class="form_body">
            <div class="body-item">
                <label><i class="fa-solid fa-user"></i> user <span>name</span></label>
                <input type="text" placeholder="Ch__open866">
            </div>
            <div class="body-item">
                <label><i class="fa-solid fa-envelope"></i> user <span>email</span></label>
                <input type="email" placeholder="Ch__open866@gmail.com">
            </div>
            <div class="body-item">
                <label><i class="fa-solid fa-key"></i> user <span>password</span></label>
                <input type="password" placeholder="****************">
            </div>
            <button class="login-btn">login <i class="fa-solid fa-arrow-right-to-bracket"></i> </button>
        </div>
    </div>
</template>


<style scoped>
    .form{
        font-family: Times, "Times New Roman", Georgia, serif;
        background-color:#80827d;
        padding:2px;
        font-size: 14px;
        margin:auto auto;
        border:1px solid #c6d9dc;
        border-radius: 15px;
        width:300px;
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
        align-items: left;
        margin:10px 0;
    }
    input{
        width:80%;
        margin-left:5%;
        border-radius:25px;
        border: 1px solid #c6d9dc;
        padding: 10px 10px;
        background-color:#80827d;/*
        background-color:#c6d9dc;*/
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