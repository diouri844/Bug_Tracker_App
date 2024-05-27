<template>
  <a-layout style="min-height: 150vh">
    <a-layout-sider v-model:collapsed="collapsed" collapsible>
      <a-menu 
      v-model:selectedKeys="selectedKeys" 
      theme="dark" mode="inline"
      >
        <a-menu-item key="/home">
        <RouterLink to="/home">
          <pie-chart-outlined class="mx-1 px-1" />
          <span>Home</span>
        </RouterLink>
        </a-menu-item>
        <a-menu-item key="/projects">
        <RouterLink to="/projects">
          <desktop-outlined class="mx-1 px-1"/>
          <span>Project</span>
        </RouterLink>
        </a-menu-item>
        <a-sub-menu key="sub1">
          <template #title>
            <span>
              <user-outlined class="mx-1 px-1" />
              <span>Profile</span>
            </span>
          </template>
          <a-menu-item key="3">My Account</a-menu-item>
          <a-menu-item key="5">Logout</a-menu-item>
        </a-sub-menu>
        <a-menu-item key="/teams">
        <RouterLink to="/teams">
          <team-outlined class="mx-1 px-1"/>
          <span>Team</span>
        </RouterLink>
        </a-menu-item>
        <a-menu-item key="9">
          <file-outlined class="mx-2" />
          <span>Note</span>
        </a-menu-item>
        <a-menu-item key="/invitations">
        <RouterLink to="/invitations">
          <usergroupAddOutlined class="mx-1 px-1"/>
          <span>Invitaion</span>
          </RouterLink>
        </a-menu-item>
        <a-menu-item key="/tickets">
        <RouterLink to="/tickets">
          <tagOutlined class="mx-1 px-1" />
          <span>Ticket</span>
        </RouterLink>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-content class="m-7">
          <slot />
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>
<script lang="ts" setup>
import {
  PieChartOutlined,
  DesktopOutlined,
  UserOutlined,
  TeamOutlined,
  FileOutlined,
  UsergroupAddOutlined,
  TagOutlined
} from '@ant-design/icons-vue';
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';
const collapsed = ref<boolean>(true);
const selectedKeys = ref<string[]>(['/home']);

// setup use router api call :
const route = useRoute();
// time to watch :
watch(
  () => route.path,
  (newPath) => {
    selectedKeys.value = [newPath];
  },
  { immediate: true } // Run the watcher immediately on component mount
);
</script>
