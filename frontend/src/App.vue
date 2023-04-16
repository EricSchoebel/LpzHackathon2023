<template>
  <v-app id="inspire">


    <v-navigation-drawer
        v-model="drawer"
        app
        image="https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg"
        permanent
        theme="dark"
      >
        <v-list nav>
          <v-list-item prepend-icon="mdi-home" title="Startseite" value="Startseite"></v-list-item>
          <v-list-item prepend-icon="mdi-chart-areaspline" title="Wertevergleich" value="Wertevergleich"></v-list-item>
          <v-list-item prepend-icon="mdi-chart-scatter-plot" title="Clustering" value="Clustering"></v-list-item>
          <v-list-item prepend-icon="mdi-magnify" title="Anomalieerkennung" value="Anomalieerkennung"></v-list-item>
        </v-list>
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
  export default {
    data: () => ({ drawer: null }),
  }
</script>