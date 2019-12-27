<template>
  <div class="main-menu">
    <div class="d-sm-none">
      <div class="photo-area">
          <b-row>
            <b-col class="text-center">
              <picture-input 
                ref="pictureInput" 
                @change="onChange" 
                width="300" 
                height="300" 
                margin="8" 
                accept="image/jpeg,image/png" 
                size="10" 
                buttonClass="btn"
                hideChangeButton="true"
                crop="true"
                :customStrings="{
                  upload: '<h1>Bummer!</h1>',
                  drag: 'Import an image'
                }">
              </picture-input>
            </b-col>
          </b-row>
      </div>
      <b-row>
        <b-col>Sample:</b-col>
      </b-row>
      <b-row>
        <b-col><textarea class= "id-overflow" v-model="ID" style="resize: none; text-align: right;" cols="12" rows="1"></textarea></b-col>
      </b-row>
      <b-row>
        <b-col>Miners ID:</b-col>
      </b-row>
      <b-row>
        <b-col><textarea v-model="MinersID" style="resize: none; text-align: left;" cols="12" rows="1" disabled></textarea></b-col>
      </b-row>
      <b-row>
          <b-col class="text-center">
            <h2>Input</h2>
          </b-col>
        </b-row>
        <b-row>
          <b-col class="text-center">
            <textarea id="input" style="resize: none; text-align:center;" class="input-area;" v-model="formula"></textarea>
          </b-col>
        </b-row>
        <b-row>
          <b-col class="text-center">
            <h2>Result</h2>
          </b-col>
        </b-row>
        <b-row>
          <b-col class="text-center">
            <div style="height: 200px;">
              <vue-mathjax style="font-size: var(--fontSize)" :formula="formula"></vue-mathjax>
            </div>
          </b-col>
        </b-row>
    </div>

    <div class="form-area d-none d-sm-block">
      <div class="photo-area" style="margin-top: 1%;">
          <b-row>
            <b-col class="text-center">
              <picture-input 
                ref="pictureInput" 
                @change="onChange" 
                width="300" 
                height="300" 
                margin="8" 
                accept="image/jpeg,image/png" 
                size="10" 
                buttonClass="btn"
                hideChangeButton="true"
                crop="true"
                :customStrings="{
                  upload: '<h1>Bummer!</h1>',
                  drag: 'Import an image'
                }">
              </picture-input>
            </b-col>
          </b-row>
      </div>
        <b-row>
          <b-col class="text-center">Sample:</b-col>
          <b-col class="text-center">Miners ID:</b-col>
        </b-row>
        <b-row>
          <b-col><textarea class= "id-overflow" v-model="ID" style="resize: none; text-align: right;" cols="12" rows="1"></textarea></b-col>
          <b-col><textarea v-model="MinersID" style="resize: none; text-align: left;" cols="12" rows="1" disabled></textarea></b-col>
        </b-row>    
        <b-row>
          <b-col class="text-center">
            <h2>Input</h2>
          </b-col>
        </b-row>
        <b-row>
          <b-col class="text-center">
            <textarea id="input" style="resize: none; text-align:center;" class="input-area;" v-model="formula"></textarea>
          </b-col>
        </b-row>
        <b-row>
          <b-col class="text-center">
            <h2>Result</h2>
          </b-col>
        </b-row>
        <b-row>
          <b-col class="text-center">
            <div style="height: 200px;">
              <vue-mathjax style="font-size: 2em;" :formula="formula"></vue-mathjax>
            </div>
          </b-col>
        </b-row>
    </div>
  </div>
</template>

<script>
import { VueMathjax } from 'vue-mathjax'
import PictureInput from 'vue-picture-input'
export default {
  components: {
    'vue-mathjax': VueMathjax,
    PictureInput
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
    // this.calculateCols();
    document.documentElement.style.setProperty('--size', this.calculateFontSize()+'em');
    document.documentElement.style.setProperty('--fontSize', this.calculateFontSize()+'em');
    // let variable = getComputedStyle(document.documentElement).getPropertyValue('--size');
  },
  methods:{
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
      hasImage: false
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.photo-area{
}
.main-menu{
  height: 100%;
  width: 100%;
  margin:0;
  /* border: 1px solid orange; */
}
.input-area{
  font-size: var(--size);
}
div{
  margin-left:5%;
  margin-right:5%;
  /* border: 1px solid white; */
}
.form-area{
  outline: 3px solid black;
}
textarea{
  font-size: 1em;
  text-align:left;
  /* border: 1px solid blue; */
}
h1,h2 {
  font-weight: normal;
}
.text-center{
  text-align: center;
}

/*TODO: Delete when done. For testing only*/
.col{
  /* border: 2px solid green; */
  width: 90%;
}
.id-overflow{
  white-space: nowrap;
  overflow: hidden;
}
#input{
  width: 90%;
}
/*
.med_screen_html{
  display: none;
}
@media only screen and (max-width: 600px) {
  .med_screen_html{
    border: 5px solid yellow;
    display: inline-block;
  }
  .form-area{
    display: none;
  }
}
*/


</style>