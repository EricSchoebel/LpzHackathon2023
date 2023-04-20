<template>
  <v-app id="inspire">


    <!--Navigation-Drawer-Links-->
    <v-navigation-drawer
        v-model="drawer"
        app
        image="https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg"
        permanent
        theme="dark"
      >
      <v-tabs
          v-model="tab"
          direction="vertical"
          :hide-slider="false"
        >
          <v-tab to="/" value="zero" :prepend-icon="(tab === 'zero') ? 'mdi-home': 'mdi-home'" :color="(tab === 'zero') ? 'teal-darken-1': 'default'">
            Startseite
          </v-tab>

          <v-tab to="/Wertevergleich" value="one" :prepend-icon="(tab === 'one') ? 'mdi-chart-areaspline': 'mdi-chart-areaspline'" :color="(tab === 'one') ? 'teal-darken-1': 'default'">
            Wertevergleich
          </v-tab>

          <v-tab to="/Clustering" value="two" :prepend-icon="(tab === 'two') ? 'mdi-chart-scatter-plot': 'mdi-chart-scatter-plot'" :color="(tab === 'two') ? 'teal-darken-1': 'default'">
            Clustering
          </v-tab>

          <v-tab to="/Anomalieerkennung" value="three" :prepend-icon="(tab === 'three') ? 'mdi-magnify': 'mdi-magnify'" :color="(tab === 'three') ? 'teal-darken-1': 'default'">
            Anomalieerkennung
          </v-tab>
          <v-divider></v-divider>
      
        </v-tabs>


      </v-navigation-drawer>


    <v-app-bar>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>KI-Analysetool für die Stadt Leipzig</v-toolbar-title>
    </v-app-bar>

    <v-main>
      
      <router-view></router-view>
      <!--  -->
    </v-main>
  </v-app>
</template>

<script>
import { useTheme } from 'vuetify';
import '@mdi/font/css/materialdesignicons.css'
//import { RouterView } from "vue-router";

//import Vue from 'vue';
//import VueRouter from 'vue-router';
//Vue.use(VueRouter);
//import { useRouter } from 'vue-router'
//import router from './router/index.js';


export default {
  data () {
    return {
      drawer: null,
      tab: "zero",
    }
  },
  setup () {
    const theme = useTheme()
    return {
      theme,
      toggleTheme: () => {
        theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
      }
    }
  },
}

</script>

