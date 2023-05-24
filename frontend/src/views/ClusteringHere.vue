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
                       //v=> v<11 || 'Die Anzahl muss 10 oder kleiner sein',
                       v=> v>0 || 'Die Anzahl muss größer 0 sein'
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
               <v-card-text>Im Folgenden können Sie mehrere Ortsteile bezüglich von Ihnen gewählten Kategorien durch ein eingebautes Machine-Learning-Feature clustern lassen.                                                                                          
                Wählen Sie die Ortsteile, die Kategorien und ggf. die Clusteranzahl. Letztere können Sie alternativ auch vom Tool optimieren lassen.                                                      
                <p>Bei <strong>zwei Kategorien</strong> können Sie das Ergebnis graphisch betrachten. Generell darf die Clusteranzahl die Ortsteilanzahl nicht übersteigen.</p></v-card-text>
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
  max-width: 800px; 
  max-height: 600px; 
  margin: 0 auto; /* Center the chart horizontally */ 
}
</style>