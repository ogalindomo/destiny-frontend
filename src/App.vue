<template>
  <div id="app">
    
    <div class="page">
      <header></header>
      <div class="main-b">
        <div class="form-area d-none d-sm-block large-image-area">
          <img alt="UTEP logo" src="./assets/UTEP.png">
        </div>
        <div class="d-sm-none small-image-area">
          <img alt="UTEP logo" src="./assets/UTEP.png">
        </div>
        <div class="bar-spacing">
        </div>
        <div class="small-bar-spacing">
        </div>
        <div id="form-tex-area">
          <FormTex></FormTex>
        </div>
      </div>
      <footer>
      </footer>
    </div>
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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 99.9vh;
  background-color: white;
  /*orange*/
  /*background-color: rgb(240, 139, 62);*/
}
.confirmation-modal{
  z-index: -1;
}
.small-image-area{
  padding-top: 20px;
  height: 150px;
  background-color: rgb(18, 41, 79);
}
.large-image-area{
  padding-top: 30px;
  height: 215px;
  background-color: rgb(18, 41, 79);
}
#form-tex-area{
   min-height: 70vh;
   display: flex;
   flex-direction: column;
   justify-content: center;
   overflow-y: hidden;
    background: linear-gradient(rgb(240, 139, 62) 5%, rgb(255, 157, 82) 40%, rgb(246, 246, 246) 30%, white 55%);
}
.page{
    min-height: 100%;
    display: flex;
    flex-direction: column;
    align-items: stretch;
}
.main-b{
  flex-grow: 1;
  flex-shrink: 0;
}
footer{
  flex-shrink: 0;
  border: 5px solid rgb(240, 139, 62);
  bottom: 0;
}
header{
  flex-shrink: 0;
  border: 5px solid white;
  bottom: 0;
}
.bar-spacing{
  margin-bottom: 1%;
  border: 5px solid rgb(215, 215, 215);
}
.large-image-area img{
  height: 156px;
  width: 200px;
}
.small-image-area img{
  height: 117px;
  width: 150px;
}
</style>
