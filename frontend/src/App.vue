<template>
  <div>
    <h1>My Data from Flask API:</h1>
    <ul>
      <li v-for="item in data" :key="item.id">
        {{ item.name }} - {{ item.value }} <!-- Access the properties of the received data object -->
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Test',
  data() {
    return {
      data: [] // Initialize an empty array to store the received data
    };
  },
  mounted() {
    // Fetch data from Flask API endpoint using Axios or Fetch API
    // and update the 'data' property when data is received
    fetch('/jsontest')
      .then(response => response.json())
      .then(data => this.data = data)
      .catch(error => console.error(error));
  }
}
</script>

<style scoped>
/* Add any scoped styles for your Test.vue component */
</style>
