import { createWebHistory, createRouter } from "vue-router"
// import EinzelneGruppe from "@/views/EinzelneGruppe"
import HomeStart from "@/views/HomeStart"

//Chat
import Vue from 'vue';
import VueRouter from 'vue-router';

/*
import WerteVergleich from "@/views/WerteVergleich"
import Clustering from "@/views/Clustering"
import AnomalieErkennung from "@/views/AnomalieErkennung"

import MehrereGruppen from "@/views/MehrereGruppen"
import LastSequenzen from "@/views/LastSequenzen"
import GruppenBearbeiten from "@/views/GruppenBearbeiten"
import Home from "@/views/Home"
*/

//Chat
Vue.use(VueRouter);


const routes = [
    {
        path: "/",
        name: "Home",
        component: HomeStart, //it's called "component" here but it is actually in views
    },
    /*
    {
        path: "/Wertevergleich",
        name: "Wertevergleich",
        component: WerteVergleich,
        alias: "/Wertevergleich",
    },
    {
        path: "/Clustering",
        name: "Clustering",
        component: Clustering,
        alias: "/Clustering",
    },
    {
        path: "/Anomalieerkennung",
        name: "Anomalieerkennung",
        component: AnomalieErkennung,
        alias: "/Anomalieerkennung",
    },
    */
    {
        path: "/:pathMatch(.*)*",
        redirect: "/",
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
  export default router;