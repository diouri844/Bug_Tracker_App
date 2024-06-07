<template>
    <div class="demo-page-header" style="background-color: #f5f5f5; padding: 24px">
      <a-page-header
        title="My Project List : "      
      >
        <template #extra>
          <a-button key="1" type="primary">Start new project</a-button>
        </template>
        <a-descriptions class="mt-3"  size="small" :column="3">
          <a-descriptions-item>
            <a-select
              v-model:value="filterValue"
              show-search
              placeholder="Project State"
              style="width: 200px"
              :options="options"
              :filter-option="filterOption"
              @focus="handleFocus"
              @blur="handleBlur"
              @change="handleChange"
            ></a-select>
          </a-descriptions-item>
          <a-descriptions-item >
            <a-select
              v-model:value="filterTeamValue"
              show-search
              placeholder="Team"
              style="width: 200px"
              :options="teams"
              :filter-option="filterTeam"
              @focus="handleFocus"
              @blur="handleBlur"
              @change="handleChange"
            ></a-select>
          </a-descriptions-item>


          <a-descriptions-item>
            <a-input-search
            v-model:value="value"
            placeholder="find a project"
            style="width: 250px"
            @search="onSearch"
          />
          </a-descriptions-item>
        
        </a-descriptions>
        
      </a-page-header>
    </div>
  </template>
  <script lang="ts" setup>
    import { ref } from 'vue';
    import type { SelectProps } from 'ant-design-vue';
    const options = ref<SelectProps['options']>([
      { value: 'created', label: 'Created' },
      { value: 'Pending', label: 'Pending' },
      { value: 'Finished', label: 'Finished' },
    ]);
    const teams = ref<SelectProps['teams']>([
      { value: 'Ch_Team', label: 'Ch_Team' }
    ]);
    const handleChange = (value: string) => {
      console.log(`selected ${value}`);
    };
    const handleBlur = () => {
      console.log('blur');
    };
    const handleFocus = () => {
      console.log('focus');
    };
    const filterOption = (input: string, option: any) => {
      return option.value.toLowerCase().indexOf(input.toLowerCase()) >= 0;
    };
    const filterTeam = (input: string, team: any) => {
      return team.value.toLowerCase().indexOf(input.toLowerCase()) >= 0;
    };
    const filterValue = ref<string | undefined>(undefined);
    const filterTeamValue = ref<string | undefined>(undefined);
    const value = ref<string>('');
    const onSearch = ()=>{};
  </script>
  <style scoped>
  .demo-page-header :deep(tr:last-child td) {
    padding-bottom: 0;
  }
  </style>
  