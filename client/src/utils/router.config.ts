import { createWebHistory, createRouter } from "vue-router"
import  LoginPage  from "../components/pages/login.page.vue";
import homePage from "../components/pages/home.page.vue";
import teamPage from "../components/pages/team.page.vue";
import projectPage from "../components/pages/project.page.vue";
import invitationPage from "../components/pages/invitation.page.vue";
import ticketPage from "../components/pages/ticket.page.vue";


const routes = [
    { path:"/", component: LoginPage },
    { path:"/home", component: homePage},
    // add project page route link :
    { path:"/projects", component:projectPage },
    // add the team page route link :
    { path:"/teams", component: teamPage},
    // add the invitation page route link :
    { path:"/invitations", component: invitationPage },
    // add tickets page route link : 
    { path:"/tickets", component: ticketPage }
];


const appRouter = createRouter(
    {
        history: createWebHistory(),
        routes,
    }
);


export default  appRouter;