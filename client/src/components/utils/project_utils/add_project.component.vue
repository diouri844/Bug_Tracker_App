<template>
    <a-form ref="formRef" :model="formState" :rules="rules" :label-col="labelCol" :wrapper-col="wrapperCol">
        <a-form-item ref="name" label="Activity name" name="name">
            <a-input v-model:value="formState.name" />
        </a-form-item>
        <a-form-item label="Activity zone" name="region">
            <a-select v-model:value="formState.region" placeholder="please select your zone">
                <a-select-option value="shanghai">Zone one</a-select-option>
                <a-select-option value="beijing">Zone two</a-select-option>
            </a-select>
        </a-form-item>
        <a-form-item label="Activity time" required name="date1">
            <a-date-picker v-model:value="formState.date1" show-time type="date" placeholder="Pick a date"
                style="width: 100%" />
        </a-form-item>
        <a-form-item label="Instant delivery" name="delivery">
            <a-switch v-model:checked="formState.delivery" />
        </a-form-item>
        <a-form-item label="Activity type" name="type">
            <a-checkbox-group v-model:value="formState.type">
                <a-checkbox value="1" name="type">Online</a-checkbox>
                <a-checkbox value="2" name="type">Promotion</a-checkbox>
                <a-checkbox value="3" name="type">Offline</a-checkbox>
            </a-checkbox-group>
        </a-form-item>
        <a-form-item label="Resources" name="resource">
            <a-radio-group v-model:value="formState.resource">
                <a-radio value="1">Sponsor</a-radio>
                <a-radio value="2">Venue</a-radio>
            </a-radio-group>
        </a-form-item>
        <a-form-item label="Activity form" name="desc">
            <a-textarea v-model:value="formState.desc" />
        </a-form-item>
        <a-form-item :wrapper-col="{ span: 14, offset: 4 }">
            <a-button type="primary" @click="onSubmit">Create</a-button>
            <a-button style="margin-left: 10px" @click="resetForm">Reset</a-button>
        </a-form-item>
    </a-form>
</template>



<script lang="ts" setup>
import { Dayjs } from 'dayjs';
import type { UnwrapRef } from 'vue';
import { reactive , ref, toRaw } from "vue";
interface FormState {
  name: string;
  region: string | undefined;
  date1: Dayjs | undefined;
  delivery: boolean;
  type: string[];
  resource: string;
  desc: string;
}
const formState: UnwrapRef<FormState> = reactive({
  name: '',
  region: undefined,
  date1: undefined,
  delivery: false,
  type: [],
  resource: '',
  desc: '',
});
const formRef = ref();

const onSubmit = () => {
  formRef.value
    .validate()
    .then(() => {
      console.log('values', formState, toRaw(formState));
    })
    .catch(
        (error:Error) => {
            console.log('error', error);
    });
};
const resetForm = () => {
  formRef.value.resetFields();
};



</script>
