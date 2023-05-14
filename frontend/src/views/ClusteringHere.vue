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
        ></v-combobox>

        <v-card-title>Kategorien auswählen:</v-card-title>
        <v-combobox
          v-model="selectKategorie"
          :items="itemsKategorie"
          label="Kategorien"
          multiple
          chips
        ></v-combobox>

        <v-card-title>Clusteranzahl</v-card-title>
        <v-text-field
                   v-model="anzahl"
                   :rules="[
                       v=> v<64 || 'Die Anzahl muss 63 oder kleiner sein'
                   ]"
                   label="Anzahl"
                   variant="outlined"
                   class="px-5 pb-3"
                   type="number"
        ></v-text-field>


        
    </v-navigation-drawer>
    

    <main>
    
    
    
    <v-card rounded="0">
      
        <v-divider></v-divider>

        
      <!-- BubbleChart Diagramm -->
         <v-row class="ma-5">
           <v-col>
               <h2>Clustering mittels Künstlicher Intelligenz</h2>
               <v-card-text>Im folgenden Diagramm können Sie mehrere Ortsteile bezüglich von Ihnen gewählten Kategorien durch ein eingebautes Machine-Learning-Feature clustern lassen.                                                                                          
                Wählen Sie die Ortsteile, die Kategorien und ggf. die Clusteranzahl. Letztere können Sie alternativ auch vom Tool optimieren lassen.
                Bei zwei Kategorien können Sie das Ergebnis grafisch betrachten. Generell darf die Clusteranzahl die Anzahl ausgewähter Ortsteile nicht übersteigen.</v-card-text>
           </v-col>
         </v-row>



         <v-row class="ma-5">
           <v-col>
             <v-card class="BDiagramm" rounded="0" >
              <div class="bubble-chart-container">
             <BubbleChart
                   ref="bChart"
                   :anzahl="this.anzahl"
                   :orte="this.selectOrte"
                   :kategorie="this.selectKategorie"
                   @kategorie="handleKategorie" 
                   @orte="handleOrte" 
               ></BubbleChart> 
              </div>
             </v-card>
           </v-col>

         </v-row>


    </v-card>
    </main>

  </div>
</template>

<script>
import BubbleChart from "@/components/BubbleChart";
//import TestZwei from "@/components/TestZwei";
export default {
  components: { BubbleChart },
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
  max-width: 800px; /* Set the maximum width */
  max-height: 700px; /* Set the maximum height */
  margin: 0 auto; /* Center the chart horizontally */
}
</style>