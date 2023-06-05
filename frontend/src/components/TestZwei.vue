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
        :data="chartData"
       
  />
</template>

<script>
import {Bar} from 'vue-chartjs'
import {BarElement, CategoryScale, Chart as ChartJS, Legend, PointElement, LinearScale, Title, Tooltip} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, PointElement)
//Minutendiagramm aus liniendiagramm berechnen, Überschriften
export default {
  name: 'BarChart',
  components: { Bar },
  props: {
    orte:{ 
      type: Array,
      default: function () {
      return ["Anger-Crottendorf"];
    },
    },
    kategorie:{
      type: Array,
      default: function () {
      return ["Anger-Crottendorf"];
    },
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
    async loadData(){ //async  wartet bis Fkt. durchläuft
    
          
          
            try {  
            console.log("Komme 1")   
            this.chartData =await (await fetch("http://127.0.0.1:5000/get/allData")).json();       
            console.log(this.chartData)
            console.log("Komme ich hier her?")
            this.updateDiagramm(this.chartData)


          } catch (e) {
            console.error(e)
          }

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
              let KitaKinder = []
              let LebenszufriedenheitZufriedenheitsfaktor = []
              let PersönlichesEinkommen = []
              let Straftaten = []
              let WirtschaftlicheLageZufriedenheitsfaktor = []
              let WohnviertelZufriedenheitsfaktor = []
              let ZukunftsaussichtZufriedenheitsfaktor = []
              let ortsteil = [] //ist quasi rechnerName
              let annot = []

              let kategorielist =["Altenquote","DurchschnittlicheHaushaltsgröße","Durchschnittsalter","Elektroautos",
              "Jugendquote","KitaKinder", "LebenszufriedenheitZufriedenheitsfaktor","PersönlichesEinkommen",
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
                KitaKinder.push(newData[b].KitaKinder)
                LebenszufriedenheitZufriedenheitsfaktor.push(newData[b].LebenszufriedenheitZufriedenheitsfaktor)
                PersönlichesEinkommen.push(newData[b].PersönlichesEinkommen)
                Straftaten.push(newData[b].Straftaten)
                WirtschaftlicheLageZufriedenheitsfaktor.push(newData[b].WirtschaftlicheLageZufriedenheitsfaktor)
                WohnviertelZufriedenheitsfaktor.push(newData[b].WohnviertelZufriedenheitsfaktor)
                ZukunftsaussichtZufriedenheitsfaktor.push(newData[b].ZukunftsaussichtZufriedenheitsfaktor)
            
                annot.push(newData[b].label) //anotation
                ortsteil.push(newData[b].Ortsteil)

                //war vorher innerhalb noch .toString()
              }

              console.log("Elektroautos:")
              console.log(Elektroautos)
              console.log("Jugendquote:")
              console.log(Jugendquote)
              console.log("KitaKinder:")
              console.log(KitaKinder)
            
            this.chartData = {//setzt die Daten des Diagramms auf bestimmte Werte
              labels: ortsteil, //das ist meine x-Achse
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
                  label: "KitaKinder",
                  data: KitaKinder,
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
            this.$emit("orte", ortsteillist)
            this.$emit("kategorie", kategorielist)



  },

  data() {
    return {
      chartData:{
        datasets:[]
      },//setzt die Diagramme erstmal auf 0, diese werden danach durch mounted auf einen Wert gesetzt
      chartOptions: {
        
        responsive: true,
        maintainAspectRatio: false,
        onClick: this.ClickHandeler,
        plugins: {
          legend:{
            display: false
          },
        },
        scales: {
          x: {
            display: true,
            title: {
              display: true,
              text: 'Gerätenummer'
            }
          },
          y: {
            display: true, title: {
              display: true,
              text: 'Energieverbrauch in W/s'
            }
          }
        }
        
      },
    }
  }
  },
  async mounted () {
    //lädt die Funktion für die Daten beim ersten Aufruf (des Reiters)
    await this.loadData()
  },

}
</script>

<style scoped>
</style>