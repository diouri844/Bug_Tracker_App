<template> 
        <Transition name="bounce" appear>
        <div class="modal-overlay open-modal">
            <div class="modal-container">
                <div class="modal-header">
                    <h3 class="header"> Contributors </h3>
                    <button type="button" class="btn-close btn-light bg-light" aria-label="Close" @click="close_modal"></button>
                </div>
                <div class="modal-body">
                        <ul v-for="(item,index) in Project" :key="index">
                            <li class="contrib-item">
                                <i class="fa-solid fa-user"></i>
                                {{ item }}</li>
                        </ul>
                    </div>
            </div>
        </div>
        </Transition>
</template>



<script scoped>
export default {
    props:{
      Project:{
        type: [],
        required: true
      }
    },
    data(){
        return{
        }
    },
    methods:{
        close_modal(){
            this.$emit("CloseModal");
        }
    }
    
}
</script>



<style scoped>
/* animation */
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
  color:#eee;
  box-shadow: 0 15px 50px #00000080;
}
.modal-header{
    display:flex;
    max-width:500px;
    min-width:500px;
}
.header{
    color:#ccc;
    margin-right:15px;
}

.btn-close{
    padding: 10px 10px;
    border-radius: 15px;
    outline:none;
}

.contrib-item{
    list-style: none;
    text-transform: capitalize;
}

</style>
