<!-- MUSTER -->

<template>
    <div>
      <v-navigation-drawer
        location="right"
        v-model="drawer"
        >   
  
          <v-card-title>Ortsteile auswählen:</v-card-title>
          <v-combobox
            v-model="selectOrte"
            :items="itemsOrte"
            label="Ortsteile"
            multiple
            chips
            :rules="[
                       v=> selectOrte.length >3 || 'mindestens 4 Ortsteile auswählen'
                   ]"
           
          ></v-combobox>
  
          <v-card-title>Kategorien auswählen:</v-card-title>
          <v-combobox
            v-model="selectKategorie"
            :items="itemsKategorie"
            label="Kategorien"
            multiple
            chips
            :rules="[
                       v=> selectKategorie.length >0 || 'mindestens eine Kategorie auswählen'
                   ]"
          ></v-combobox>
  
            
  
          
      </v-navigation-drawer>
      
  
      <main>
      
      
      
      <v-card rounded="0">
        
          <v-divider></v-divider>
  
          
        <!-- BubbleChart Diagramm -->
           <v-row class="ma-5">
             <v-col>
                 <h2>Anomalieerkennung mittels Künstlicher Intelligenz</h2>
                 <v-card-text>.... Im Folgenden können Sie über Anomalieerkennung Aureißer ....mehrere Ortsteile bezüglich von Ihnen gewählten Kategorien durch ein eingebautes Machine-Learning-Feature clustern lassen.                                                                                          
                  Wählen Sie die Ortsteile, die Kategorien.                                                      
                  <p>Bei <strong>zwei Kategorien</strong> können Sie das Ergebnis graphisch betrachten. Generell darf die Clusteranzahl die Ortsteilanzahl nicht übersteigen.</p></v-card-text>
             </v-col>
           </v-row>
          
           <!-- 
           <div v-if="this.selectKategorie.length != 2">
              <p>Text Length of itemsKategorie: {{ this.selectKategorie.length }}</p>
            </div>
          -->
  
           <v-row class="ma-5">
             <v-col>
               <v-card class="BDiagramm" rounded="0" >
                <div class="bubble-chart-container">
               <AnomalieChart
                     ref="bChart"
                     :anzahl="this.anzahl"
                     :orte="this.selectOrte"
                     :kategorie="this.selectKategorie"
                     @kategorie="handleKategorie" 
                     @orte="handleOrte" 
                 ></AnomalieChart> 
                </div>
               </v-card>
             </v-col>
  
           </v-row>
  
  
      </v-card>
      </main>
  
    </div>
  </template>
  
  <script>
  import AnomalieChart from "@/components/AnomalieChart";
  //import TestZwei from "@/components/TestZwei";
  export default {
    components: { AnomalieChart },
    data(){
      return{
        drawer:true,
        selectOrte: [],
        itemsOrte: ["hi"],
        selectKategorie: [],
        itemsKategorie: [],
        anzahl:"3",
      }
    },
    methods:{
      handleKategorie(data){
                  this.itemsKategorie=data
              },
      handleOrte(data){
                  this.itemsOrte=data
              }
  
    },
    watch:{
    
    },
   
  }
  </script>
  <style>
  h2{
    text-align: center;
    position: relative;
    margin:auto;
  }
  h3{
    text-align: center;
  }
  .bubble-chart-container {
    max-width: 800px; 
    max-height: 600px; 
    margin: 0 auto; /* Center the chart horizontally */ 
  }
  </style>