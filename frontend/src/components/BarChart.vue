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
        this.barCharData =await (await fetch("http://127.0.0.1:5000/get/allData")).json();       
        console.log(this.barCharData)
        this.updateDiagramm(this.barCharData)


      } catch (e) {
        console.error(e)
      }

      },
      updateDiagramm(newData){
        let b;
        
        //const colors = []

        let elektroautos = []
        let altenquote = []
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

        let kategorielist =["Elektroautos", "Altenquote","Durchschnittliche Haushaltsgröße","Durchschnittsalter",
        "Jugendquote","kitaKinder", "lebenszufriedenheitZufriedenheitsfaktor","persoenlichesEinkommen",
        "straftaten","wirtschaftlicheLageZufriedenheitsfaktor", "wohnviertelZufriedenheitsfaktor",
        "zukunftsaussichtZufriedenheitsfaktor","ortsteil"]

        for(b in newData){

          elektroautos.push(newData[b].elektroautos)
          altenquote.push(newData[b].altenquote)
          durchschnittlicheHaushaltsgroesse.push(newData[b].durchschnittlicheHaushaltsgroesse)
          durchschnittsalter.push(newData[b].durchschnittsalter)
          jugendquote.push(newData[b].jugendquote)
          kitaKinder.push(newData[b].kitaKinder)
          lebenszufriedenheitZufriedenheitsfaktor.push(newData[b].lebenszufriedenheitZufriedenheitsfaktor)
          persoenlichesEinkommen.push(newData[b].persoenlichesEinkommen)
          straftaten.push(newData[b].straftaten)
          wirtschaftlicheLageZufriedenheitsfaktor.push(newData[b].wirtschaftlicheLageZufriedenheitsfaktor)
          wohnviertelZufriedenheitsfaktor.push(newData[b].wohnviertelZufriedenheitsfaktor)
          zukunftsaussichtZufriedenheitsfaktor.push(newData[b].zukunftsaussichtZufriedenheitsfaktor)
      
          ortsteil.push(newData[b].Ortsteil)
      }
      
      this.chartData = {//setzt die Daten des Diagramms auf bestimmte Werte
        labels: ortsteil, //das ist meine x-Achse
        datasets: [ //das sind meine y-Achsen
          {
            label: "Altenquote",
            data: altenquote,
            backgroundColor: '#9BD0F5',
          },
          {
            label: "Elektroautos",
            data: elektroautos,
            backgroundColor: '#229924',
          },
          {
            label: "durchschnittlicheHaushaltsgroesse",
            data: durchschnittlicheHaushaltsgroesse,
            backgroundColor: '#ab1616',
          },
        ]
      }
      this.$emit("orte", ortsteil)
      this.$emit("kategorie", kategorielist)



    },

      
    async mounted () {
      //lädt die Funktion für die Daten beim ersten Aufruf (des Reiters)
      await this.loadData()
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

  }
  </script>
  
  <style scoped>
  </style>