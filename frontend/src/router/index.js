import { createWebHistory, createRouter } from "vue-router"
// import EinzelneGruppe from "@/views/EinzelneGruppe"
import Test from "@/views/Test"
/*
import MehrereGruppen from "@/views/MehrereGruppen"
import LastSequenzen from "@/views/LastSequenzen"
import GruppenBearbeiten from "@/views/GruppenBearbeiten"
import Home from "@/views/Home"
*/

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home, //it's called "component" here but it is actually in views
    },
  /*  {
        path: "/EinzelneGruppe",
        name: "Einzelne Gruppe",
        component: EinzelneGruppe,
        alias: "/EinzelneGruppe",
    },  */
    {
        path: "/Test",
        name: "Test",
        component: Test,
        alias: "/Test",
    },
    /*
    {
        path: "/MehrereGruppen",
        name: "MehrereGruppen",
        component: MehrereGruppen,
        alias: "/MehrereGruppen",
    },
    {
        path: "/LastSequenzen",
        name: "Last-Sequenzen",
        component: LastSequenzen,
        alias: "/LastSequenzen",
    },
    {
        path: "/GruppenBearbeiten",
        name: "Gruppen bearbeiten",
        component: GruppenBearbeiten,
        alias: "/GruppenBearbeiten",
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