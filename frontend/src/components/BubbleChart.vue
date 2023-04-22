<template>
    <Bubble class="bubblechart"
          v-if="loaded"
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
  import { Bubble } from 'vue-chartjs'
  import {
    Chart as ChartJS,  Title,  Tooltip,  Legend,  LineElement,  LinearScale,  PointElement,  CategoryScale,} from 'chart.js'
  ChartJS.register(Title, Tooltip, Legend, LineElement, LinearScale, PointElement, CategoryScale)
  
  export default {
    name: 'BubbleChart',
    components: {Bubble},
    props: {
      chartId: {
        type: String,
        default: 'bubble-chart'
      },
      /*anfang:{
        type: String,
        default:"",
      },
      ende:{
        type: String,
        default:"",
      },
      */
      anzahl: {
        type: String,
        default: "3",
      },
      rechnerSelect:{
        type: Array,
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
      }
    },
    methods:{
      //aktualisiert das Diagramm
      updateDiagramm(newData){
        let b;
        let x;

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

        let anzahlDia = [] //labels?
        let ortsteilName = []

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
      
          anzahlDia.push(newData[b].label) 
          ortsteilName.push(newData[b].rechnerTopic+" "+newData[b].rechnerNummer.toString())
        }
        this.chartData = {
          datasets:[]
        }
        for (x in ortsteilName){
          this.chartData.datasets.push(
              {
                label: ortsteilName[x],
                backgroundColor: this.colors[anzahlDia[x]],
                data:[
                  {
                    x:durchschnittlicheHaushaltsgroesse[x],
                    y:altenquote[x],
                    r:10,
                  }
                ]
              }
          )
        }
      },
      //lädt die Daten von der API
      async loadData(){
        this.loaded = false
        try {

          //needs to deliver which categories and how many clusters (or)
          this.bubbleChartData = await (await fetch(
            //"http://127.0.0.1:5000/get/kmeansByTimespan?clusteranzahl=" + this.anzahl)).json();
            "http://127.0.0.1:5000//get/kmeansAllDataTwoClusters")).json();
            this.updateDiagramm(this.bubbleChartData)
          this.loaded = true
        }catch (e){
          console.error(e)
        }
      },
    },
    watch:{
      //prüft, ob sich der Anfang ändert
     /*
      anfang:function(){
        this.loadData()
      },
      //prüft, ob sich das Ende ändert
      ende:function(){
        this.loadData()
      },
      */
      //prüft, ob sich die Gruppe ändert
      anzahl:function(){
        this.loadData()
      },
    },
  
    data(){
      return{
        loaded:false,
        colors: ['#F44336', '#E91E63', '#9C27B0', '#673AB7', '#3F51B5', '#B71C1C', '#880E4F', '#4A148C', '#311B92', '#1A237E', '#C62828', '#AD1457', '#6A1B9A', '#4527A0', '#283593', '#D32F2F', '#C2185B', '#7B1FA2', '#512DA8', '#303F9F', '#E53935', '#D81B60', '#8E24AA', '#5E35B1', '#3949AB', '#EF5350', '#EC407A', '#AB47BC', '#7E57C2', '#5C6BC0', '#E57373', '#F06292', '#BA68C8', '#9575CD', '#7986CB', '#EF9A9A', '#F48FB1', '#CE93D8', '#B39DDB', '#9FA8DA', '#2196F3', '#03A9F4', '#00BCD4', '#009688', '#4CAF50', '#0D47A1', '#01579B', '#006064', '#004D40', '#1B5E20', '#1565C0', '#0277BD', '#00838F', '#00695C', '#2E7D32', '#1976D2', '#0288D1', '#0097A7', '#00796B', '#388E3C', '#1E88E5', '#039BE5', '#00ACC1', '#00897B', '#43A047', '#42A5F5', '#29B6F6', '#26C6DA', '#26A69A', '#66BB6A', '#64B5F6', '#4FC3F7', '#4DD0E1', '#4DB6AC', '#81C784', '#90CAF9', '#81D4FA', '#80DEEA', '#80CBC4', '#A5D6A7', '#8BC34A', '#CDDC39', '#FFEB3B', '#FFC107', '#FF9800', '#33691E', '#827717', '#F57F17', '#FF6F00', '#E65100', '#558B2F', '#9E9D24', '#F9A825', '#FF8F00', '#EF6C00', '#689F38', '#AFB42B', '#FBC02D', '#FFA000', '#F57C00', '#7CB342', '#C0CA33', '#FDD835', '#FFB300', '#FB8C00', '#9CCC65', '#D4E157', '#FFEE58', '#FFCA28', '#FFA726', '#AED581', '#DCE775', '#FFF176', '#FFD54F', '#FFB74D'],
        chartData:null,
        chartOptions:{
          responsive:true,
          maintainAspectRatio: false,
          plugins:{
            legend: {
              display: false,
            },
            title:{
              display: false,
            },
          },
          scales: {
            x: {
              display: true,
              title: {
                display: true,
                text:'durchschnittlicheHaushaltsgroesse'
              },
              suggestedMin: 0,
            },
            y: {
              display: true,
              title: {
                display: true,
                text: 'altenquote'
              },
              suggestedMin: 0,
            }
          }
        }
      }
    },
    //bevor das Diagramm lädt
    async mounted(){
      await this.loadData()
    }
  }
  </script>
  
  <style scoped>
  </style>