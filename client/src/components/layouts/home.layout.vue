<template>
  <a-layout style="min-height: 100vh">
    <a-layout-sider v-model:collapsed="collapsed" collapsible>
      <a-menu 
      v-model:selectedKeys="selectedKeys" 
      theme="dark" mode="inline"
      >
        <a-menu-item key="1">
          <pie-chart-outlined />
          <span>Home</span>
        </a-menu-item>
        <a-menu-item key="2">
          <desktop-outlined />
          <span>Project</span>
        </a-menu-item>
        <a-sub-menu key="sub1">
          <template #title>
            <span>
              <user-outlined />
              <span>Profile</span>
            </span>
          </template>
          <a-menu-item key="3">My Account</a-menu-item>
          <a-menu-item key="5">Logout</a-menu-item>
        </a-sub-menu>
        <a-menu-item key="sub2">
              <team-outlined />
              <span>Team</span>
        </a-menu-item>
        <a-menu-item key="9">
          <file-outlined />
          <span>Note</span>
        </a-menu-item>
        <a-menu-item key="10">
          <usergroupAddOutlined />
          <span>Invitaion</span>
        </a-menu-item>
        <a-menu-item key="11">
          <tagOutlined />
          <span>Ticket</span>
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
import { ref } from 'vue';
const collapsed = ref<boolean>(false);
const selectedKeys = ref<string[]>(['1']);
</script>
