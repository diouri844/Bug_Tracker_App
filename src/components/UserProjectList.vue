<template>
    <div class="container">
        <ul class="responsive-table">
            <li class="table-header">
                <div class="col col-1"> Id</div>
                <div class="col col-2"><i class="fa-solid fa-user-tie"></i> Owner </div>
                <div class="col col-3"><i class="fa-solid fa-people-group"></i> Team </div>
                <div class="col col-4"><i class="fa-solid fa-spinner"></i> Status</div>
            </li>
            <li class="table-row">
                <div class="col col-1" data-label="Job Id">42235</div>
                <div class="col col-2" data-label="Customer Name">John Doe</div>
                <div class="col col-3 team-name" data-label="Amount" >Google-azur-closed-team</div>
                <div class="col col-4" data-label="Payment Status">in deployment</div>
            </li>
            <li class="table-row">
                <div class="col col-1" data-label="Job Id">42655</div>
                <div class="col col-2" data-label="Customer Name">Chopen</div>
                <div class="col col-3 team-name" data-label="Amount" >Py_charp</div>
                <div class="col col-4" data-label="Payment Status">in deployment</div>
            </li>
        </ul>
</div>
</template>

<script>
    export default{
    methode:{
        click_table_row(){
            console.log("row click detected ");
        }
    }
    }
</script>


<style scoped>
.content-side{
    margin:0;
    padding:5px 15px;
    border: 1px solid #537895;
    background:linear-gradient(to right,#E8126B,#0e0e0e);
    border-radius: 18px;
    color:#fff;

}

body {
  font-family: 'lato', sans-serif;
}
.container {
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 10px;
  padding-right: 10px;
}
/*
    <div class="col col-5" data-label="Payment Status">
                    <button class=" btn btn-outline-info fa-solid fa-circle-info me-2"></button>
                    <button class="btn btn-outline-light fa-solid fa-pen"></button>
                </div>
*/

.responsive-table li {
    border-radius: 3px;
    padding: 25px 30px;
    display: flex;
    justify-content: space-between;
    margin-bottom: 25px;
  }
.responsive-table  .table-header {
    color:#fff;/* #95A5A6;*/
    background:linear-gradient(to right,#E8126B,#0e0e0e);
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 0.03em;
  }
.responsive-table  .table-row {
    background:linear-gradient(to right, #95A5A6,#000);
    color:#fff;
    box-shadow: 0px 0px 9px 0px rgba(0,0,0,0.1);
  }
.table-row:hover{
    box-shadow: 0px 0px 9px 0px #fff;
}

.team-name{
    background-color:#537895;
    color: #fff;
    width:auto;
    text-align: center;
    border-radius: 25px;
    padding:2px 1px;
    margin-right:25px;
}


.responsive-table .col-1 {
    flex-basis: 10%;
}
.responsive-table .col-2 {
    flex-basis: 20%;
}
.responsive-table .col-3 {
    flex-basis: 25%;
  }
.responsive-table .col-4 {
    flex-basis: 25%;
}

  
.table-header {
    display: none;
}

li {
    display: block;
}
.col {
flex-basis: 100%;      
}

</style>