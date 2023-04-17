<!-- MUSTER -->

<template>
    <v-card rounded="0">
      <!-- Systeminformationen -->
      <v-row class="ma-3 d-flex justify-center">
        <h2>Systeminformationen</h2>
      </v-row>
      <v-row class="ma-3 d-flex justify-center">
          <v-card  rounded="0">
            <v-row>
            <v-col class="v-col-auto ma-3">
              <h2 class="schriftmitte">erreichbare Topics</h2>
             <!-- <h3 v-for="item in this.topics">{{item}}</h3>-->
            </v-col>
            <v-col class="v-col-auto ma-3">
              <h2 class="schriftmitte">erreichbare Rechner</h2>
              <v-progress-circular
                  class="daten d-flex justify-center"
                  :rotate="360"
                  :size="100"
                  :width="15"
                  :model-value="(rechner.length)/(maxAnzahlRechner)*100"
                  color="#9c27b0"
              >
                {{ rechner.length }}/{{maxAnzahlRechner}}
              </v-progress-circular>
            </v-col>
              <v-col class="v-col-auto ma-3">
                <h2 class="schriftmitte">Zeitraum</h2>
                <h3>Von: {{this.allerAnfang}}</h3>
                <h3>Bis: {{this.today}}</h3>
              </v-col>
            </v-row>
          </v-card>
        </v-row>
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
                       v=> v<55 || 'Die Anzahl muss 54 oder kleiner sein'
                   ]"
                   label="Anzahl"
                   variant="outlined"
                   class="px-5 pb-3"
                   type="number"
                   v-model="anzahl"
                   bg-color="#282828FF"></v-text-field>
             </v-card>
             <v-card rounded="0">
               <v-card-title>Zeitraum</v-card-title>
               <v-text-field label="Anfang" variant="outlined" class="px-5 pb-3"  type="date" v-model="anfang" bg-color="#282828FF"></v-text-field>
               <v-text-field label="Ende" variant="outlined" class="px-5 pb-3"  type="date" v-model="ende" bg-color="#282828FF"></v-text-field>
             </v-card>
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
      anzahl:"3",
      anfang:"2023-01-25",
      ende:"2023-03-03",
      topics:[],
      rechner:[],
      maxAnzahlTopics:1,
      maxAnzahlRechner:56,
      today:"2023-03-03",
      allerAnfang:"25-01-2023"
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
    //erstellt die Systeminformationen
    async systeminformationen(){
      let b
      let x
      let c
      let v
      try {
        x = await (await fetch("http://192.168.34.150:8081/get/allStatisticsByDays?from="+this.today+"&to="+this.today)).json();
        this.topics.push(x[0].rechnerTopic)
        for (c in x){
          for(v in this.topics) {
            if (x[c].rechnerTopic !== this.topics[v]){
              this.topics.push(x[c].rechnerTopic)
            }
          }
        }
      }catch (e) {
        console.log(e)
      }
      try {
        b = await (await fetch("http://192.168.34.150:8081/get/allStatisticsByDays?from="+this.today+"&to="+this.today)).json();
        for (c in b){
          this.rechner.push(b[c].rechnerNummer)
        }
      }catch (e) {
        console.log(e)
      }
    },
  },
  watch:{
    //prüft, ob sich der Anfang ändert
    anfang(val){
      if(val >= this.ende){
        this.ende = this.anfang
      }
      this.reverseAnfang()
    },

    ende(val){
      if(val< this.anfang){
        this.anfang = this.ende
      }
      this.reverseEnde()
    },
  },
  //bevor die Seite geladen wird
  async beforeMount(){
    this.today = new Date().toJSON().slice(0,10)
    this.today= this.reverseToday()
    await this.systeminformationen()
  }
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