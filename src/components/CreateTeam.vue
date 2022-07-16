<template>
    <div class="modal-overlay open-modal">
            <div class="modal-container">
                <div class="modal-header">
                    <div v-show="step1" class="update">
                        <h3 class="header">
                            <i class="fa-solid fa-plus"></i>
                            Create Team  
                        </h3>
                    </div>
                    <button type="button" class="btn-close btn-light bg-light" 
                    aria-label="Close"
                    @click="CloseMe"></button>
                </div>
                    <div v-if="step1" class="modal-body">
                        <input type="text" class="Nameteam" id="team" placeholder="Team-Name" v-model="teamName">
                    </div>
                    <div v-if="step2" class="modal-body">
                         <h1>step2</h1>   
                    </div>
            </div>
        </div>
</template>




<script>
export default {
    props:{
      User:{
        type: String,
        required: true
      }
    },
    data(){
        return{
            'step1':true,
            'step2':false,
            'teamName':''
        }
    },
    methods:{
        CloseMe(){
            this.$emit("closeModal");
        },
    }
    
}
</script>

<style scoped>
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
.Nameteam{
    margin-bottom:10px;
    padding: 5px 10px;
    outline: none;
    background:transparent;
    color:#ccc;
    border:none;
    border-left: 5px solid #ccc;
}
</style>