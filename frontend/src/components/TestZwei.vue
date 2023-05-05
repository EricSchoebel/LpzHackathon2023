<template>
    <Bubble :data="chartData" />
  </template>
  
  <script>
  import { Bubble } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, PointElement, BarElement, CategoryScale, LinearScale } from 'chart.js'
  
  ChartJS.register(Title, Tooltip, PointElement, Legend, BarElement, CategoryScale, LinearScale)
  
  export default {
    name: 'BubbleChart',
    components: { Bubble },
    data() {
      return {
    
        

       
        chartData: {datasets: [
          {
            label: 'dataset1',
            data:[
                  {
                    x:1,
                    y:2,
                    r:10,
                  },
                  {
                    x:3,
                    y:4,
                    r:10,
                  }
                ],
            backgroundColor: '#9BD0F5',
            hidden: false,
          },
        ] } ,
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
    }
  }
  </script>
  