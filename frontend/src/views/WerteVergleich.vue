<template>
    <div>
    <!-- Navigations-Bar rechts zum einstellen der Diagramme -->
      <v-navigation-drawer
      location="right"
      v-model="drawer"
      >   

        <v-combobox
          v-model="selectOrte"
          :items="itemsOrte"
          label="Ortsteile"
          multiple
          chips
        ></v-combobox>

        <v-combobox
          v-model="selectKategorie"
          :items="itemsKategorie"
          label="Kategorien"
          multiple
          chips
        ></v-combobox>


      </v-navigation-drawer>

    <main>
        
            <BarChart
                    ref="barChart"
                   :anzahl="this.anzahl"
                   :orte="this.selectOrte"
                   :kategorie="this.selectKategorie"
                   @kategorie="handleKategorie" 
                   @orte="handleOrte" 
            >

            </BarChart>
      
     

    </main>

    
    </div>

</template>

<script>
    import BarChart from "@/components/BarChart"
    
    export default{
        components: {BarChart },
        data () {
            return {
               drawer:true,
               selectOrte: [],
               itemsOrte: ["hi"],
               selectKategorie: [],
               itemsKategorie: [],
            }
        },
        methods:{
            kategorie(data){
                this.itemsKategorie=data
            },
            orte(data){
                this.itemsOrte=data
            }

        }
        
    }

</script>