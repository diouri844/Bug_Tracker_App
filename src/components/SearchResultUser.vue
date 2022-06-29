<template>
        <div class="container" v-for="(item,index) in Data" :key="index">
            <div class="header">
                <h5 class="project-title"><i class="fa-solid fa-folder"></i> {{ item.Name }}</h5>
                <h4 class="project-contributors_number"> {{ item.Contributors.length }} contributors </h4>
            </div>
            <div class="body">
                <p class="description">
                    {{ item.Discription }}
                </p>
            </div>
            <div class="footer">
                <h5 class="project-details"> started : {{ item.S-date }}</h5>
                <h5 class="project-state"> {{ item.State }}</h5>
                <h5 class="project-details"> ended : {{ item.E-date }}</h5>
            </div>
        </div>
</template>


<script>
export default {
    props: ["Data"]
}
</script>


<style scoped>
.container {
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
  margin-top:15px;
  padding-left: 10px;
  padding-right: 10px;
  padding-top: 15px;
  grid-column: 2/ span 10 ;
  grid-row: 4/ span 5;
  border:1px solid #ccc;
  border-radius:25px;
}
.header{
    display: grid;
    grid-template-columns: repeat(12,1fr);
}
.project-title{
    color:#fff;
    text-decoration: underline;
    text-transform: capitalize;
    grid-column:1/ span 5;
}
.project-contributors_number{
    text-transform: capitalize;
    color:#537895;
    grid-column: 10/ span 2;
}
.description{
    color:#fff;
    text-transform: capitalize;
    text-justify: newspaper;
    font-family: monospace;
    font-size: 20px;
}

</style>