<template>
    <div>
    <!-- Navigations-Bar rechts zum einstellen der Diagramme -->
      <v-navigation-drawer
      location="right"
      v-model="drawer"
      >   

      <v-card-title>Ortsteile auswählen:</v-card-title>
        <v-combobox
          v-model="selectOrte"
          :items="itemsOrte"
          label="Ortsteile"
          multiple
          chips
          >
                  <template v-slot:prepend-item>
                  <v-checkbox
                    v-model="selectAll"
                    label="alle auswählen"
                    @click ="toggleSelectAll"
                  ></v-checkbox>
                  </template>
        </v-combobox>

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
                   
            >

            </BarChart>
      
     

    </main>
              <!--
                :anzahl="this.anzahl"
                   
                   @kategorie="handleKategorie" 
                   @orte="handleOrte" 
                :orte="this.selectOrte"
                   :kategorie="this.selectKategorie"-->
    
    </div>

</template>

<script>
    import BarChart from "@/components/BarChart"
    
    export default{
        components: { BarChart },
        data () {
            return {
               drawer:true,
               selectOrte: [],
               itemsOrte: ["hi"],
               selectKategorie: [],
               itemsKategorie: [],
               anzahl:"2",
            }
        },
        methods:{
          handleKategorie(data){
                this.itemsKategorie=data
            },
          handleOrte(data){
                this.itemsOrte=data
            },

        }
        
    }

</script>