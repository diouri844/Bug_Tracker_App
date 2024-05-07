<template>
    <context-holder />
    <a-form 
      class="w-[700px] m-[3%]"
      :model="formState"
      name="basic"
      :label-col="{ span: 8 }"
      :wrapper-col="{ span: 16 }"
      autocomplete="off"
      @finish="onFinish"
      @finishFailed="onFinishFailed"
    >
      <a-form-item
        label="Username"
        name="username"
        :rules="[{ required: true, message: 'Please input your username!' }]"
      >
        <a-input v-model:value="formState.username" />
      </a-form-item>
  
      <a-form-item
        label="Password"
        name="password"
        :rules="[{ required: true, message: 'Please input your password!' }]"
      >
        <a-input-password v-model:value="formState.password" />
      </a-form-item>
  
      <a-form-item name="remember" :wrapper-col="{ offset: 8, span: 16 }">
        <a-checkbox v-model:checked="formState.remember">Remember me</a-checkbox>
      </a-form-item>
  
      <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
        <a-button type="primary" html-type="submit">Send</a-button>
      </a-form-item>
    </a-form>
  </template>
  <script lang="ts" setup>
  import { reactive } from 'vue';
  import { message } from 'ant-design-vue';
  import { useRouter } from "vue-router";
  import IFormState from "../../commun/types/formState.type";
  const [messageApi, contextHolder] = message.useMessage();
  const myRouter = useRouter();
  
  const formState = reactive<IFormState>({
    username: '',
    password: '',
    remember: true,
  });


  const onFinish = (values:IFormState ):void =>{
    console.log('Success:', values);
    // popup response : 
    messageApi.success(`Welcome back ${values.username} !`);
    myRouter.push("/home");
    return;
  };
  

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo);
  };
  </script>