<template>
  <Bar class="barchart"
       
       :options="chartOptions"
       :id="chartId"
       :dataset-id-key="datasetIdKey"
       :plugins="plugins"
       :css-classes="cssClasses"
       :styles="styles"
       :width="width"
       :height="height"
       :data="chartData" />
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },

  props: {
    orte:{ 
      type: Array,
      default: null,
    },
    kategorie:{
      type: Array,
      default: null,
    },
    anzahl: {
      type: String,
      default: "2",
    },
    chartNumber:{
      type: Number,
      default: 1,
    },
    chartId: {
      type: String,
      default: 'bar-chart'
    },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    width: {
      type: Number,
      default: 1000
    },
    height: {
      type: Number,
      default: 1000,
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Object,
      default: () => {}
    },
    
  },

  methods:{
    async loadData(){

      try {  
            console.log("Komme 1")
            /* Idee signifikant anders als bei CLustering und Anomalieerkennung:
            Es gibt einen allgemeinen API-Call und im Frontend wird dann bloß ausgewählt was genutzt wird.
            Bei Clustering wird mit Auswahl von Ortsteilen, Kategorien o. ä. der API-Call beeinflusst */   
            this.chartData =await (await fetch("http://127.0.0.1:5000/get/allData")).json();       
            console.log(this.chartData)
            console.log("Komme ich hier her?")
            this.updateDiagramm(this.chartData)
            console.log("ortsteile asugewählt:")
            console.log(this.orte)  // dat kommt erstmal an
            console.log("kategorien asugewählt:")
            console.log(this.kategorie)


          } catch (e) {
            console.error(e)
          }

      /*
      let a =[1,2,3,4,5,6,7,8,9,10]
      let b =[1,2,3,4,5,6,7,8,9,10]
      this.chartData={
        labels: a,
        datasets:[{
          label: 'test',
          data: b
        }]
      }
      */

    },
    updateDiagramm(newData){
              let b;

              console.log("test")
              //const colors = []

              let Altenquote = []
              let DurchschnittlicheHaushaltsgröße = []
              let Durchschnittsalter = []
              let Elektroautos = []
              let Jugendquote = []
              let KinderInTagesbetreuung = []
              let LebenszufriedenheitZufriedenheitsfaktor = []
              let PersönlichesEinkommen = []
              let Straftaten = []
              let WirtschaftlicheLageZufriedenheitsfaktor = []
              let WohnviertelZufriedenheitsfaktor = []
              let ZukunftsaussichtZufriedenheitsfaktor = []
              let ortsteil = [] 

              let kategorielist =["Altenquote","DurchschnittlicheHaushaltsgröße","Durchschnittsalter","Elektroautos",
              "Jugendquote","KinderInTagesbetreuung", "LebenszufriedenheitZufriedenheitsfaktor","PersönlichesEinkommen",
              "Straftaten","WirtschaftlicheLageZufriedenheitsfaktor", "WohnviertelZufriedenheitsfaktor",
              "ZukunftsaussichtZufriedenheitsfaktor"]
      
              let ortsteillist =['Althen-Kleinpösna', 'Altlindenau', 'Anger-Crottendorf', 'Baalsdorf',
                          'Burghausen-Rückmarsdorf', 'Böhlitz-Ehrenberg', 'Connewitz', 'Dölitz-Dösen',
                          'Engelsdorf', 'Eutritzsch', 'Gohlis-Mitte', 'Gohlis-Nord', 'Gohlis-Süd',
                          'Großzschocher', 'Grünau-Mitte', 'Grünau-Nord', 'Grünau-Ost',
                          'Grünau-Siedlung', 'Hartmannsdorf-Knautnaundorf', 'Heiterblick',
                          'Holzhausen', 'Kleinzschocher', 'Knautkleeberg-Knauthain', 'Lausen-Grünau',
                          'Leutzsch', 'Liebertwolkwitz', 'Lindenau', 'Lindenthal', 'Lößnig',
                          'Lützschena-Stahmeln', 'Marienbrunn', 'Meusdorf', 'Miltitz', 'Mockau-Nord',
                          'Mockau-Süd', 'Möckern', 'Mölkau', 'Neulindenau', 'Neustadt-Neuschönefeld',
                          'Paunsdorf', 'Plagwitz', 'Plaußig-Portitz', 'Probstheida',
                          'Reudnitz-Thonberg', 'Schleußig', 'Schönau', 'Schönefeld-Abtnaundorf',
                          'Schönefeld-Ost', 'Seehausen', 'Sellerhausen-Stünz', 'Stötteritz',
                          'Südvorstadt', 'Thekla', 'Volkmarsdorf', 'Wahren', 'Wiederitzsch', 'Zentrum',
                          'Zentrum-Nord', 'Zentrum-Nordwest', 'Zentrum-Ost', 'Zentrum-Süd',
                          'Zentrum-Südost', 'Zentrum-West']


              //put API-Data into variables 
              for(b in newData){
                //console.log("nun")
                Altenquote.push(newData[b].Altenquote)
                DurchschnittlicheHaushaltsgröße.push(newData[b].DurchschnittlicheHaushaltsgröße)
                Durchschnittsalter.push(newData[b].Durchschnittsalter)
                Elektroautos.push(newData[b].Elektroautos)
                Jugendquote.push(newData[b].Jugendquote)
                KinderInTagesbetreuung.push(newData[b].KinderInTagesbetreuung)
                LebenszufriedenheitZufriedenheitsfaktor.push(newData[b].LebenszufriedenheitZufriedenheitsfaktor)
                PersönlichesEinkommen.push(newData[b].PersönlichesEinkommen)
                Straftaten.push(newData[b].Straftaten)
                WirtschaftlicheLageZufriedenheitsfaktor.push(newData[b].WirtschaftlicheLageZufriedenheitsfaktor)
                WohnviertelZufriedenheitsfaktor.push(newData[b].WohnviertelZufriedenheitsfaktor)
                ZukunftsaussichtZufriedenheitsfaktor.push(newData[b].ZukunftsaussichtZufriedenheitsfaktor)
            
                //annot.push(newData[b].label) //anotation
                ortsteil.push(newData[b].Ortsteil)

                //war vorher innerhalb noch .toString()
              }

              /*hilft binarylist (mit 1 wenn Ortsteil selected) ? */
              const desired_ortsteile = this.orte
              const ortsteillist_standard = ortsteillist
              const ortsteileBinaryList = ortsteillist_standard.map(u => desired_ortsteile.includes(u) ? 1 : 0);
              console.log("ortsteileBinaryList:")
              console.log(ortsteileBinaryList)

              //FALSCH const filteredOrtsteil = ortsteil.filter((_, index) => ortsteileBinaryList[index] === 1);
              //const filteredOrtsteil = ortsteil.map((el, index) => (ortsteileBinaryList[index] === 1 ? el : null));
              //FIXME HIER WIRD NOCH DAS FALSCH ANGEZEIGT!

              console.log(typeof(ortsteil))
              /*Ortsteil einkürzen auf das was angezeigt werden soll */




              console.log("Elektroautos:")
              console.log(Elektroautos)
              console.log("Jugendquote:")
              console.log(Jugendquote)
              console.log("KinderInTagesbetreuung:")
              console.log(KinderInTagesbetreuung)


            
            this.chartData = {//setzt die Daten des Diagramms auf bestimmte Werte
              labels: filteredOrtsteil, //das ist meine x-Achse
              datasets: [ //das sind meine y-Achsen
                { 
                  label: "Altenquote",
                  data: Altenquote,
                  backgroundColor: '#9BD0F5',
                  hidden: false,
                },
                {
                  label: "DurchschnittlicheHaushaltsgröße",
                  data: DurchschnittlicheHaushaltsgröße,
                  backgroundColor: '#ab1616',
                  hidden: false,
                },
                {
                  label: "Durchschnittsalter",
                  data: Durchschnittsalter,
                  backgroundColor: '#F44336',
                  hidden: false,
                },
                {
                  label: "Elektroautos",
                  data: Elektroautos,
                  backgroundColor: '#229924',
                  hidden: false,
                },
                {
                  label: "Jugendquote",
                  data: Jugendquote,
                  backgroundColor: '#E91E63',
                  hidden: false,
                },
                {
                  label: "KinderInTagesbetreuung",
                  data: KinderInTagesbetreuung,
                  backgroundColor: '#9C27B0',
                  hidden: false,
                },
                {
                  label: "LebenszufriedenheitZufriedenheitsfaktor",
                  data: LebenszufriedenheitZufriedenheitsfaktor,
                  backgroundColor: '#8E24AA',
                  hidden: false,
                },
                {
                  label: "PersönlichesEinkommen",
                  data: PersönlichesEinkommen,
                  backgroundColor: '#E65100',
                  hidden: false,
                },
                {
                  label: "Straftaten",
                  data: Straftaten,
                  backgroundColor: '#880E4F',
                  hidden: false,
                },
                {
                  label: "WirtschaftlicheLageZufriedenheitsfaktor",
                  data: WirtschaftlicheLageZufriedenheitsfaktor,
                  backgroundColor: '#9575CD',
                  hidden: false,
                },
                {
                  label: "WohnviertelZufriedenheitsfaktor",
                  data: WohnviertelZufriedenheitsfaktor,
                  backgroundColor: '#03A9F4',
                  hidden: false,
                },
                {
                  label: "ZukunftsaussichtZufriedenheitsfaktor",
                  data: ZukunftsaussichtZufriedenheitsfaktor,
                  backgroundColor: '#AED581',
                  hidden: false,
                },
              ]
            }

            /* HIER HIN FOR ANGEHAKTE KATEGORIE LABEL ANZEIGEN ODER NICHT */
            //setzt das dataset.hidden auf den gegenteiligen Wahrheitswert des Vorkommens in this.kategorie-Prop
            this.chartData.datasets.forEach((dataset) => {dataset.hidden = !this.kategorie.includes(dataset.label);}); 


            this.$emit("orte", ortsteillist)
            this.$emit("kategorie", kategorielist)

  },
    
  },

  watch:{ 
      orte:function(){
        this.loadData()
      },
      kategorie:function(){
        this.loadData()
      },
 
    },

  data() {
    return {
      chartData: {
        //labels: [ 'January', 'February', 'March'],
        datasets: []
      },
      chartOptions: {
        plugins: {
          legend:{
            display: false
          },
        },
      },

   



    }
  },
  //lädt die Funktion für die Daten beim ersten Aufruf (des Reiters)
  async mounted(){
    await this.loadData()
  }
}
</script>
