<template>
  <div id="app">
    <img alt="UTEP logo" height='156' width='200' src="./assets/UTEP.jpeg">
    <FormTex msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import FormTex from './components/FormTex.vue'

export default {
  name: 'app',
  components: {
    FormTex
  }
}
</script>

<style>
img{
  margin-bottom:3%
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
