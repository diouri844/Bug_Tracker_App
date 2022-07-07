<template> 
        <Transition name="bounce" appear>
        <div class="modal-overlay open-modal">
            <div class="modal-container">
                <div class="modal-header">
                    <h3 class="header"><i class="fa-solid fa-plus"></i> Create New Project  </h3>
                    <button type="button" class="btn-close btn-light bg-light" 
                    aria-label="Close"
                    @click="CloseMe"></button>
                </div>
                <div class="modal-body">
                        <input type="text" placeholder="Project Name" class="projectname" v-model="projectname">
                        <textarea placeholder="describe your project " cols="50" rows="5" class="description"></textarea>
                        <label for="startedDate"> Start date </label>
                        <input type="date" class="Date" id="startedDate">
                        <label for="endedDate"> Expected end  date </label>
                        <input type="date" class="Date" id="endedDate">
                </div>
                <button class="btn btn-outline-info">
                    Next
                    <i class="fa-solid fa-circle-arrow-right"></i>
                </button>
            </div>
        </div>
        </Transition>
</template>

<script>
export default {
    methods:{
        CloseMe(){
            this.$emit("closeModal");
        }
    }
}
</script>




<style scoped>
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
.projectname , .description, .Date{
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
}
</style>

