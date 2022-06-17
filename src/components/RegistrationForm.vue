<template>
    <div class="form">
        <div class="header">
            <h1>create account <span>now</span></h1>
        </div>
        <div class="form_body">
            <div class="body-item">
                <label><i class="fa-solid fa-user"></i> ferst <span>name</span></label>
                <input type="text" placeholder="Ch__open866">
            </div>
            <div class="body-item">
                <label><i class="fa-solid fa-user"></i> last <span>name</span></label>
                <input type="text" placeholder="Ch__open866">
            </div>
            <div class="body-item">
                <label><i class="fa-solid fa-envelope"></i> <span>email</span></label>
                <input type="email" placeholder="Ch__open866@gmail.com">
            </div>
            <div class="body-item">
                <label><i class="fa-solid fa-envelope"></i> birth-<span>day</span></label>
                <input type="date">
            </div>
            <div class="body-item">
                <label><i class="fa-solid fa-key"></i> user <span>password</span></label>
                <input type="password" placeholder="****************">
            </div>
            <div class="body-item">
                <label><i class="fa-solid fa-key"></i> confirme <span>password</span></label>
                <input type="password" placeholder="****************">
            </div>
            <button class="login-btn">create account <i class="fa-solid fa-arrow-right-to-bracket"></i> </button>
        </div>
    </div>
</template>


<style scoped>
    .form{
        font-family: Times, "Times New Roman", Georgia, serif;
        background:transparent;
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
        color:#238636;
    }
    .login-btn{
        padding: 10px 10px;
        margin-bottom: 10px;
        width: 250px;
        text-align: center;
        text-transform: capitalize;
        border-radius: 5px;
        border: 1px solid #c6d9dc;
        background-color:#238636;
        color: #c6d9dc;
    }
    .login-btn:hover{
        background-color:#0d0f0c;
        color:#c6d9dc;
        border: 1px solid #c6d9dc; 
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