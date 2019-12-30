<template>
  <div id="app">
    
    <div class="banana">
      <header></header>
      <div class="main-b">
        <div class="form-area d-none d-sm-block large-image-area">
          <img alt="UTEP logo" height='156' width='200' src="./assets/UTEP.png">
        </div>
        <div class="d-sm-none small-image-area">
          <img alt="UTEP logo" height='117' width='150' src="./assets/UTEP.png">
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
/*img{
  margin-bottom:7%
}*/

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
   /* border: 5px solid black; */
   min-height: 70vh;
   display: flex;
   flex-direction: column;
   justify-content: center;
   overflow-y: hidden;
  background: linear-gradient(rgb(240, 139, 62) 5%, rgb(255, 157, 82) 40%, rgb(246, 246, 246) 30%, white 55%);
  
  /*Maybe*/
  /*background: linear-gradient(rgb(240, 139, 62) 5%, rgb(255, 157, 82) 40%, rgb(241,241,241) 30%, rgb(241,241,241) 55%);*/
   /*background: linear-gradient(rgb(18,41,79), rgb(203, 208, 212) 65%);*/
   /*background-color: rgb(21, 37, 89); */
   
}
.banana{
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

</style>
