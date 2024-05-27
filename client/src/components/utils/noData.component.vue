<template>
    <div class="flex flex-col items-center justify-center w-full my-[10%]">
        <a-empty :image="simpleImage" />
        <a-button type="primary">Start new project</a-button>
    </div>
  </template>
  <script lang="ts" setup>
  import { Empty } from 'ant-design-vue';
  const simpleImage = Empty.PRESENTED_IMAGE_SIMPLE;
  </script>
  
  