<template>
<div class="form-area">
      <b-row>
        <b-col style="text-align: right;">Sample:</b-col>
        <b-col style="text-align: left;">Miners ID:</b-col>
      </b-row>
      <b-row>
        <b-col><textarea v-model="ID" style="resize: none; text-align: right;" cols="12" rows="1"></textarea></b-col>
        <b-col><textarea v-model="MinersID" style="resize: none; text-align: left;" cols="12" rows="1" disabled></textarea></b-col>
      </b-row>    
      <b-row>
        <b-col class="text-center">
          <h2>Input</h2>
        </b-col>
      </b-row>
      <b-row>
        <textarea id="input" style="resize: none; text-align:center;" class="input-area;" v-model="formula" cols="30" rows="3"></textarea>
      </b-row>
      <b-row>
        <b-col class="text-center">
          <h2>Result</h2>
        </b-col>
      </b-row>
      <b-row>
        <div style="height: 200px;">
          <vue-mathjax style="font-size: var(--fontSize)" :formula="formula"></vue-mathjax>
        </div>
      </b-row>
  </div>
</template>

<script>
import { VueMathjax } from 'vue-mathjax'
export default {
  components: {
    'vue-mathjax': VueMathjax,
  },
  mounted() {
    ///////////////Make LaTex Engine Work///////////////
    let latexScript = document.createElement('script');
    latexScript.setAttribute('src', "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS_HTML");
    document.head.appendChild(latexScript);
    ////////////////////////////////////////////////////
    this.display();
    this.calculateCols();
    alert("Here: "+this.cols);
    document.documentElement.style.setProperty('--size', this.calculateFontSize()+'em');
    document.documentElement.style.setProperty('--fontSize', this.calculateFontSize()+'em');
    // let variable = getComputedStyle(document.documentElement).getPropertyValue('--size');
  },
  methods:{
    display(){
      var s = screen.height;
      var w = screen.width;
      alert(s+"x"+w)
    },
    calculateCols(){
      this.cols = parseInt(screen.width/56);
      //alert(this.cols);
      document.getElementById("input").cols = String(Math.max(parseInt(screen.width/56),20));
    },
    calculateFontSize(){
      var calc = Math.max(((screen.width/1680)*2), 0.75);
      alert("Calc: "+calc);
      return calc;
    }
  },
  name: 'FormTex',
  data () {
    return {
      input:"",
      formula: '$$x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}$$',
      msg: 'Welcome to Your Vue.js App',
      ID: null,
      MinersID:'ogalindomo',
      cols:0,
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.input-area{
  font-size: var(--size);
}
div{
  margin-left:15%;
  margin-right:15%;
  border: 1px solid red;
}
.form-area{
  outline: 3px solid black;
}
textarea{
  font-size: 1em;
  text-align:left;
}
h1,h2 {
  font-weight: normal;
}
.text-center{
  text-align: center;
}
</style>