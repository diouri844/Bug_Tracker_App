import { createWebHistory, createRouter } from "vue-router"
import  LoginPage  from "../components/pages/login.page.vue";
import homePage from "../components/pages/home.page.vue";

const routes = [
    { path:"/", component: LoginPage },
    { path:"/home", component: homePage}
];


const appRouter = createRouter(
    {
        history: createWebHistory(),
        routes,
    }
);


export default  appRouter;