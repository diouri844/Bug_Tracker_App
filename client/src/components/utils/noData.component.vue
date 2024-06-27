<template>
    <div class="flex flex-col items-center justify-center w-full my-[10%]">
        <a-empty :image="simpleImage" />
        <a-button @click="showModal" type="primary">Start new project</a-button>
        <a-modal v-model:open="isOpen" title="Basic Modal" @ok="handleOk">
            <add_projectComponent />
        </a-modal>
    </div>
</template>
<script lang="ts" setup>
import { Empty } from 'ant-design-vue';
import add_projectComponent  from './project_utils/add_project.component.vue';
const simpleImage = Empty.PRESENTED_IMAGE_SIMPLE;
import {  ref } from 'vue';

const isOpen = ref<boolean>(false);
const showModal = () => {
    isOpen.value = true;
};
const handleOk = (e: MouseEvent) => {
    e.preventDefault;
    console.log(e);
    isOpen.value = false;
    return;
}
</script>