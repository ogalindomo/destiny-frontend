<template>
<div class="form-area">
      <image-uploader
        :preview="true"
        :className="['fileinput', { 'fileinput--loaded': hasImage }]"
        capture="environment"
        :debug="1"
        doNotResize="gif"
        :autoRotate="true"
        outputFormat="verbose"
        @input="setImage"
      >
        <label for="fileInput" slot="upload-label">
            <figure>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="32"
                height="32"
                viewBox="0 0 32 32"
              >
                <path
                  class="path1"
                  d="M9.5 19c0 3.59 2.91 6.5 6.5 6.5s6.5-2.91 6.5-6.5-2.91-6.5-6.5-6.5-6.5 2.91-6.5 6.5zM30 8h-7c-0.5-2-1-4-3-4h-8c-2 0-2.5 2-3 4h-7c-1.1 0-2 0.9-2 2v18c0 1.1 0.9 2 2 2h28c1.1 0 2-0.9 2-2v-18c0-1.1-0.9-2-2-2zM16 27.875c-4.902 0-8.875-3.973-8.875-8.875s3.973-8.875 8.875-8.875c4.902 0 8.875 3.973 8.875 8.875s-3.973 8.875-8.875 8.875zM30 14h-4v-2h4v2z"
                ></path>
              </svg>
            </figure>
            <span class="upload-caption">{{
              hasImage ? "Replace" : "Click to upload"
            }}</span>
        </label>
      </image-uploader>
      <b-row class="justify-content-md-center">
        <b-col cols="2" md="auto" style="text-align: left; font-size:1.75em;">Sample:  </b-col>
        <b-col cols="2" md="auto" style="text-align: right; font-size:1.75em;">Miners ID:</b-col>
      </b-row>
      <b-row >
        <b-col cols="2" md="auto" style="text-align: left;" ><textarea v-model="ID" style="resize: none;" cols ="13" rows="1"></textarea></b-col>
        <b-col cols="2" md="auto" style="text-align: right;" ><textarea v-model="MinersID" style="resize: none;" cols ="13" rows="1" disabled></textarea></b-col>
      </b-row>    
      <b-row>
        <h2>Input</h2>
      </b-row>
      <b-row>
        <textarea id="input" style="resize: none; text-align:center;" class="input-area;" v-model="formula" cols="30" rows="3"></textarea>
      </b-row>
      <b-row>
        <h2>Result</h2>
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
    let uploaderScript = document.createElement('script');
    uploaderScript.setAttribute('src', "https://unpkg.com/vue-image-upload-resize");
    document.head.appendChild(uploaderScript);
    ////////////////////////////////////////////////////
    this.display();
    this.calculateCols();
    document.documentElement.style.setProperty('--size', this.calculateFontSize()+'em');
    document.documentElement.style.setProperty('--fontSize', this.calculateFontSize()+'em');
    // let variable = getComputedStyle(document.documentElement).getPropertyValue('--size');
  },
  methods:{
    display(){
      var s = screen.height;
      var w = screen.width;
    },
    calculateCols(){
      this.cols = parseInt(screen.width/56);
      document.getElementById("input").cols = String(Math.max(parseInt(screen.width/56),20));
    },
    calculateFontSize(){
      var calc = Math.max(((screen.width/1680)*2), 0.75);
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
.col1{
  background-color: red;
}
.col2{
  background-color: yellow;
}
.input-area{
  font-size: var(--size);
}
div{
  margin-left:15%;
  margin-right:15%;
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
</style>
