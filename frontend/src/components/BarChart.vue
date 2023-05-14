<template>
    <Bar class="barchart"
         
         :chartNumber="chartNumber"
         :chart-options="chartOptions"
         :chart-data="chartData"
         :chart-id="chartId"
         :dataset-id-key="datasetIdKey"
         :plugins="plugins"
         :css-classes="cssClasses"
         :styles="styles"
         :width="width"
         :height="height"
         
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
      },
      kategorie:{
        type: Array,
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
                
                //const colors = []

                let altenquote = []
                let elektroautos = []
                let durchschnittlicheHaushaltsgroesse = []
                let durchschnittsalter = []
                let jugendquote = []
                let kitaKinder = []
                let lebenszufriedenheitZufriedenheitsfaktor = []
                let persoenlichesEinkommen = []
                let straftaten = []
                let wirtschaftlicheLageZufriedenheitsfaktor = []
                let wohnviertelZufriedenheitsfaktor = []
                let zukunftsaussichtZufriedenheitsfaktor = []
                let ortsteil = [] //ist quasi rechnerName

                let kategorielist =["Altenquote","DurchschnittlicheHaushaltsgröße","Durchschnittsalter","Elektroautos",
                "Jugendquote","KitaKinder", "LebenszufriedenheitZufriedenheitsfaktor","PersönlichesEinkommen",
                "Straftaten","WirtschaftlicheLageZufriedenheitsfaktor", "WohnviertelZufriedenheitsfaktor",
                "ZukunftsaussichtZufriedenheitsfaktor"]

                for(b in newData){

                  altenquote.push(newData[b].Altenquote)
                  durchschnittlicheHaushaltsgroesse.push(newData[b].DurchschnittlicheHaushaltsgröße)
                  durchschnittsalter.push(newData[b].Durchschnittsalter)
                  elektroautos.push(newData[b].Elektroautos)
                  jugendquote.push(newData[b].Jugendquote)
                  kitaKinder.push(newData[b].KitaKinder)
                  lebenszufriedenheitZufriedenheitsfaktor.push(newData[b].LebenszufriedenheitZufriedenheitsfaktor)
                  persoenlichesEinkommen.push(newData[b].persoenlichesEinkommen)
                  straftaten.push(newData[b].straftaten)
                  wirtschaftlicheLageZufriedenheitsfaktor.push(newData[b].wirtschaftlicheLageZufriedenheitsfaktor)
                  wohnviertelZufriedenheitsfaktor.push(newData[b].WohnviertelZufriedenheitsfaktor)
                  zukunftsaussichtZufriedenheitsfaktor.push(newData[b].ZukunftsaussichtZufriedenheitsfaktor)
              
                  ortsteil.push(newData[b].Ortsteil)
              }
              
              this.chartData = {//setzt die Daten des Diagramms auf bestimmte Werte
                labels: ortsteil, //das ist meine x-Achse
                datasets: [ //das sind meine y-Achsen
                  { 
                    label: "altenquote",
                    data: altenquote,
                    backgroundColor: '#9BD0F5',
                    hidden: false,
                  },
                  {
                    label: "durchschnittlicheHaushaltsgroesse",
                    data: durchschnittlicheHaushaltsgroesse,
                    backgroundColor: '#ab1616',
                    hidden: false,
                  },
                  {
                    label: "durchschnittsalter",
                    data: durchschnittsalter,
                    backgroundColor: '#F44336',
                    hidden: false,
                  },
                  {
                    label: "elektroautos",
                    data: elektroautos,
                    backgroundColor: '#229924',
                    hidden: false,
                  },
                  {
                    label: "jugendquote",
                    data: jugendquote,
                    backgroundColor: '#E91E63',
                    hidden: false,
                  },
                  {
                    label: "kitaKinder",
                    data: kitaKinder,
                    backgroundColor: '#9C27B0',
                    hidden: false,
                  },
                  {
                    label: "lebenszufriedenheitZufriedenheitsfaktor",
                    data: lebenszufriedenheitZufriedenheitsfaktor,
                    backgroundColor: '#8E24AA',
                    hidden: false,
                  },
                  {
                    label: "persoenlichesEinkommen",
                    data: persoenlichesEinkommen,
                    backgroundColor: '#E65100',
                    hidden: false,
                  },
                  {
                    label: "straftaten",
                    data: straftaten,
                    backgroundColor: '#880E4F',
                    hidden: false,
                  },
                  {
                    label: "wirtschaftlicheLageZufriedenheitsfaktor",
                    data: wirtschaftlicheLageZufriedenheitsfaktor,
                    backgroundColor: '#9575CD',
                    hidden: false,
                  },
                  {
                    label: "wohnviertelZufriedenheitsfaktor",
                    data: wohnviertelZufriedenheitsfaktor,
                    backgroundColor: '#03A9F4',
                    hidden: false,
                  },
                  {
                    label: "zukunftsaussichtZufriedenheitsfaktor",
                    data: zukunftsaussichtZufriedenheitsfaktor,
                    backgroundColor: '#AED581',
                    hidden: false,
                  },
                ]
              }
              this.$emit("orte", ortsteil)
              this.$emit("kategorie", kategorielist)



    },

    data() {
      return {
        chartData:{
          labels: [],
          datasets:[]
        },//setzt die Diagramme erstmal auf 0, diese werden danach durch mounted auf einen Wert gesetzt
        chartOptions: {
          /*
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
          */
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