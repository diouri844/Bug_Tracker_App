<template>
    <homeLayout>
        <projectHeaderComponent />
        this is the project page :
        <noData />
    </homeLayout>
</template>


<script lang="ts" setup>
import homeLayout from "../layouts/home.layout.vue";
//import projectTable from "../utils/project_utils/project_table.component.vue";
import noData from "../utils/noData.component.vue";
import projectHeaderComponent from "../utils/project_utils/project_header.component.vue";
</script>