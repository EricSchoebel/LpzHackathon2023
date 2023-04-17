<!-- MUSTER -->

<template>
    <v-card rounded="0">
      
        <v-divider></v-divider>

        
      <!-- BubbleChart Diagramm -->
         <v-row class="ma-5">
           <v-col>
               <h2>Clustering mittels Künstlicher Intelligenz</h2>
               <v-card-text>Im folgenden Diagramm können Sie alle Rechner durch ein eingebautes Machine-Learning-Feature clustern lassen, um einen ersten Überblick zu erhalten. Die Grundlage des Clusterings bildet der Durchschnitts- und der Maximalverbrauch der Rechner. Wählen Sie einfach die gewünschte Anzahl an Clustern sowie den zu betrachtenden Zeitraum aus. Die Clusteranalyse wird auf Grundlage des K-Means-Algorithmus durchgeführt.</v-card-text>
           </v-col>
         </v-row>

         <v-row class="ma-5">
           <v-col>
             <v-card class="BDiagramm" rounded="0" >
               <BubbleChart
                   ref="bChart"
                   :anzahl="this.anzahl"
                   :anfang="reverseAnfang()"
                   :ende="reverseEnde()"
               ></BubbleChart>
             </v-card>
           </v-col>
           <v-col class="align-right">
             <v-card>
               <v-card-title>Anzahl an Clustern</v-card-title>
               <v-text-field
                   :rules="[
                       v=> v<64 || 'Die Anzahl muss 64 oder kleiner sein'
                   ]"
                   label="Anzahl"
                   variant="outlined"
                   class="px-5 pb-3"
                   type="number"
                   v-model="anzahl"
                   bg-color="#282828FF"></v-text-field>
             </v-card>
            <!--   <v-card rounded="0">
               <v-card-title>Zeitraum</v-card-title>
               <v-text-field label="Anfang" variant="outlined" class="px-5 pb-3"  type="date" v-model="anfang" bg-color="#282828FF"></v-text-field>
               <v-text-field label="Ende" variant="outlined" class="px-5 pb-3"  type="date" v-model="ende" bg-color="#282828FF"></v-text-field>
             </v-card> -->
           </v-col>
         </v-row>


    </v-card>
</template>

<script>
import BubbleChart from "@/components/BubbleChart";
export default {
  components: {BubbleChart},
  data(){
    return{
      
    }
  },
  methods:{
    //gibt ein gedrehtes Datum vom Anfangszeitpunkt zurück
    reverseAnfang(){
      let t = this.anfang.split('-')
      t.reverse()
      return t.join('-')
    },
    //gibt ein gedrehtes Datum vom Endzeitpunkt zurück
    reverseEnde(){
      let t = this.ende.split('-')
      t.reverse()
      return t.join('-')
    },
    //gibt das gedrehte Datum von heute zurück
    reverseToday(){
      let t = this.today.split('-')
      t.reverse()
      return t.join('-')
    },
    
  },
  watch:{
  
  },
 
}
</script>
<style>
#bubble-chart{
  height: 45vh;
  width: 50%;
  padding: 5px;
}
h2{
  text-align: center;
  position: relative;
  margin:auto;
}
h3{
  text-align: center;
}
</style>