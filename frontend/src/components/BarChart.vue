<template>
    <Bar class="barchart"
         v-if="loaded"
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
  import {BarElement, CategoryScale, Chart as ChartJS, Legend, LinearScale, Title, Tooltip} from 'chart.js'
  
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
  //Minutendiagramm aus liniendiagramm berechnen, Überschriften
  export default {
    name: 'BarChart',
    components: { Bar },
    props: {
      anfang:{
        type: String,
        default:"",
      },
      ende:{
        type: String,
        default:"",
      },
      anzeige:{
        type: String,
        default: "",
      },
      gruppe:{
        type: String,
        default: "",
      },
      zeitraum:{
        type: String,
      },
      anfangZeit:{
        type: String,
      },
      endeZeit:{
        type: String,
      },
      datum:{
        type: String,
        default: "",
      },
      valideTage:{
        type: Array,
        default: [],
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
    methods: {
      //wenn auf das Diagramm geklickt wird
      ClickHandeler(evt, chartData){
        if (chartData.length != 0) {
          var position = chartData[0].index;
          this.$emit('clicked', position)
        }
      },
      //ändert zw. Maximal-, Durschnitts- und Idle-Werten
      toggleDiagramm(val){
        this.chartData.datasets.forEach(element => {
          element.hidden= true;
        });
        this.chartData.datasets[val].hidden = false;
      },
      //aktualisiert Diagramm
      updateDiagramm(barCharData){
        let b;
        
        /*
        let idleVerbrauch = []
        let maximalVerbrauch = []
        let durchschnittsVerbrauch = []
        let rechnerName = []
        */
        const colors = []
        
        let maxWerte = [1,1]
        let durchWerte = [1,1]
        let idleWerte = [1,1]

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



        for(b in barCharData){
          
          elektroautos.push(barCharData[b].elektroautos)
          altenquote.push(barCharData[b].altenquote)
          durchschnittlicheHaushaltsgroesse.push(barCharData[b].durchschnittlicheHaushaltsgroesse)
          durchschnittsalter.push(barCharData[b].durchschnittsalter)
          jugendquote.push(barCharData[b].jugendquote)
          kitaKinder.push(barCharData[b].kitaKinder)
          lebenszufriedenheitZufriedenheitsfaktor.push(barCharData[b].lebenszufriedenheitZufriedenheitsfaktor)
          persoenlichesEinkommen.push(barCharData[b].persoenlichesEinkommen)
          straftaten.push(barCharData[b].straftaten)
          wirtschaftlicheLageZufriedenheitsfaktor.push(barCharData[b].wirtschaftlicheLageZufriedenheitsfaktor)
          wohnviertelZufriedenheitsfaktor.push(barCharData[b].wohnviertelZufriedenheitsfaktor)
          zukunftsaussichtZufriedenheitsfaktor.push(barCharData[b].zukunftsaussichtZufriedenheitsfaktor)
      
          ortsteil.push(barCharData[b].Ortsteil)
          //rechnerName.push(barCharData[b].rechnerTopic+" "+barCharData[b].rechnerNummer.toString())
          
          if (barCharData[b].maximalVerbrauch>maxWerte[0]){ //gibt Maximalen Maximalverbrauch aus
            maxWerte[0] = barCharData[b].maximalVerbrauch
            maxWerte[1] = b
          }
          if (barCharData[b].durchschnittsVerbrauch>durchWerte[0]){ //gibt Maximalen Durchschnittsverbrauch aus
            durchWerte[0] = barCharData[b].durchschnittsVerbrauch
            durchWerte[1] = b
          }
          if (barCharData[b].idleVerbrauch>idleWerte[0]){ //gibt Maximalen Idleverbrauch aus
            idleWerte[0] = barCharData[b].idleVerbrauch
            idleWerte[1] = b
          }
        }
  
        this.chartData = {//setzt die Daten des Diagramms auf bestimmte Werte
          labels: rechnerName,
          datasets: [
            {
              label: "Idle-Verbrauch",
              data: idleVerbrauch,
              backgroundColor: '#9BD0F5',
              hidden: true,
            },
            {
              label: "Durchschnitts-Verbrauch",
              data: durchschnittsVerbrauch,
              backgroundColor: '#229924',
              hidden: true,
            },
            {
              label: "Maximal-Verbrauch",
              data: maximalVerbrauch,
              backgroundColor: '#ab1616',
              hidden: false,
            },
          ]
        }
  
        if(this.anzeige==="0"){
          this.chartData.datasets[0].hidden=false
          this.chartData.datasets[1].hidden=true
          this.chartData.datasets[2].hidden=true
        }else if (this.anzeige==="1"){
          this.chartData.datasets[0].hidden=true
          this.chartData.datasets[1].hidden=false
          this.chartData.datasets[2].hidden=true
        }else{
          this.chartData.datasets[0].hidden=true
          this.chartData.datasets[1].hidden=true
          this.chartData.datasets[2].hidden=false
        }
        colors.push(this.chartData.datasets[0].backgroundColor)
        colors.push(this.chartData.datasets[1].backgroundColor)
        colors.push(this.chartData.datasets[2].backgroundColor)
        this.$emit('colors', colors)
        this.$emit('maxWerte', maxWerte)
        this.$emit('durchWerte', durchWerte)
        this.$emit('idleWerte', idleWerte)
        this.$emit('listeRechner', rechnerName)
      },
      //Lädt die Daten aus der API in das Diagramm
      async loadData(){
        this.loaded = false
        this.$emit('loaded', this.loaded)
  
        let x
        let z1
        x = this.datum+"T"+this.anfangZeit+":00"
        z1 = Date.parse(x)+3600000
        z1 = z1.toString()
        z1 = z1.slice(0, -3)
  
  
  
        let z2
        x = this.datum+"T"+this.endeZeit+":00"
        z2 = Date.parse(x)+3600000
        z2 = z2.toString()
        z2 = z2.slice(0, -3)
  
        if(z1!==""&&z2!==""&&this.gruppe!==""){
          try {
            if(this.zeitraum==="Tag"){
              this.barCharData = await (await fetch("http://192.168.34.150:8081/get/balkenMinutenGroupRechner?from="+z1+"&to="+z2+"&group="+this.gruppe)).json()
            }else{
              this.barCharData = await (await fetch("http://192.168.34.150:8081/get/groupStatisticsByDays?from="+this.anfang+"&to="+this.ende+ "&group="+this.gruppe)).json()
            }
  
            this.updateDiagramm(this.barCharData)
            this.loaded = true
            this.$emit('loaded', this.loaded)
          } catch (e) {
            console.error(e)
          }
        }
      },
    },
    watch:{
      //prüft, ob sich der Anfang ändert
      anfang:function (){
        this.loadData()
      },
      //prüft, ob sich das Ende ändert
      ende:function (){
        this.loadData()
      },
      //prüft, ob sich die Gruppe ändert
      gruppe:function(){
        this.loadData()
      },
      zeitraum:function(){
        this.loadData()
      },
      datum:function(){
        if(this.valideTage.includes(this.datum)){
          this.loadData()
        }
      },
      anfangZeit:function(){
        this.loadData()
      },
      endeZeit:function(){
        this.loadData()
      },
    },
    data() {
      return {
        loaded: false,
        chartData: null,//setzt die Diagramme erstmal auf 0, diese werden danach durch mounted auf einen Wert gesetzt
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
    },
  
    async mounted () {
      //lädt die Funktion für die Daten beim ersten Aufruf
      await this.loadData()
    },
  }
  </script>
  
  <style scoped>
  </style>