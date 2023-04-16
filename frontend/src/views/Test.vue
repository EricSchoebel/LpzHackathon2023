<template>
   <div> 
    <h1>Hello Vue + Vuetify!</h1>
  </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        // Data for your component
      };
    },
    methods: {
      // Method for sending GET request to backend
      fetchData() {
        axios.get('/api/data')
          .then(response => {
            // Handle response from backend
            console.log(response.data);
          })
          .catch(error => {
            // Handle error
            console.error(error);
          });
      },
      // Method for sending POST request to backend
      sendData() {
        const data = { key: 'value' };
        axios.post('/api/data', data)
          .then(response => {
            // Handle response from backend
            console.log(response.data);
          })
          .catch(error => {
            // Handle error
            console.error(error);
          });
      },
      // Other methods for your component
    },
    computed: {
      // Computed properties for your component
    },
  };
  </script>
  
  <style scoped>
  /* Styling for your component */
  </style>
  