<template>
  <div class="main-menu">
    <div>
      <b-row class="d-sm-none">
        <div class="head-space-small"></div>
      </b-row>
      <b-row class="d-none d-sm-block">
        <div class="head-foot-large"></div>
      </b-row>
    </div>
    <div class="d-sm-none small-form-area">
      <div class="inner-form-area">
        <b-row>
          <div class="row1-space-small"></div>
        </b-row>
        <b-row>
          <b-col>Sample:</b-col>
        </b-row>
        <b-row>
          <b-col><textarea class= "id-overflow" v-model="ID" style="resize: none; text-align: right;" cols="12" rows="1"></textarea></b-col>
        </b-row>
        <b-row>
          <div class="row3-space-small"></div>
        </b-row>
        <b-row>
          <b-col>Miners ID:</b-col>
        </b-row>
        <b-row>
          <b-col><textarea v-model="MinersID" style="resize: none; text-align: left;" cols="12" rows="1" disabled></textarea></b-col>
        </b-row>
        <b-row>
          <div class="row2-space-small"></div>
        </b-row>
        <b-row>
          <b-col class="line-divider"></b-col>
        </b-row>
        <b-row>
          <div class="row2-space-small"></div>
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
          <div class="row1-space-small"></div>
        </b-row>
        <b-row>
          <b-col class="text-center">
            <h2>Result</h2>
          </b-col>
        </b-row>
        <b-row>
          <b-col class="text-center">
            <div class="result-display">
              <vue-mathjax  style="font-size: var(--fontSize)" :formula="formula"></vue-mathjax>
            </div>
          </b-col>
        </b-row>
        <b-row>
          <div class="row1-space-small"></div>
        </b-row>
      </div>
    </div>

    <div class="form-area d-none d-sm-block">
      <div class="inner-form-area">
        <b-row>
          <div class="row1-space-large"></div>
        </b-row>
        <b-row>
          <b-col class="text-center">Sample:</b-col>
          <b-col class="text-center">Miners ID:</b-col>
        </b-row>
        
        <b-row>
          <b-col><textarea class= "id-overflow" v-model="ID" style="resize: none; text-align: right;" cols="12" rows="1"></textarea></b-col>
          <b-col><textarea v-model="MinersID" style="resize: none; text-align: left;" cols="12" rows="1" disabled></textarea></b-col>
        </b-row>  
        <b-row>
          <div class="row2-space-large"></div>
        </b-row>
        <b-row>
          <b-col class="line-divider"></b-col>
        </b-row>
        <b-row>
          <div class="row2-space-large"></div>
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
          <div class="row1-space-large"></div>
        </b-row>
        <b-row>
          <b-col class="text-center">
            <h2>Result</h2>
          </b-col>
        </b-row>
        <b-row>
          <b-col class="text-center">
            <div class="result-display">
              <vue-mathjax style="font-size: var(--fontSize)" :formula="formula"></vue-mathjax>
            </div>
          </b-col>
        </b-row>
        <b-row>
          <div class="row1-space-large"></div>
        </b-row>
      </div>
    </div>
    <div>
      <b-row class="d-sm-none">
        <div class="foot-space-small"></div>
      </b-row>
      <b-row class="d-sm-none">
        <div class="foot-space-small"></div>
      </b-row>
    </div>
  </div>
</template>

<script>
import { VueMathjax } from 'vue-mathjax'
export default {
  components: {
    'vue-mathjax': VueMathjax,
  },
  mounted() {
  
    // Function expression that resizes the input div height based on the amount of text.
    var inputExpand = function(element){
      // Takes height of parent. Downsizes if text is deleted.
      element.style.height = "inherit";
      
      // Retrieves object with all css properities of the element.
      var elementProperties = window.getComputedStyle(element);
      
      // Calculates new height based on current border, padding, and scroll height.
      var borderHeight = parseInt(elementProperties.getPropertyValue('border-top-width'), 10) 
          + parseInt(elementProperties.getPropertyValue('border-bottom-width'), 10);
          
      var paddingHeight = parseInt(elementProperties.getPropertyValue('padding-top'), 10)
          + parseInt(elementProperties.getPropertyValue('padding-bottom'), 10)
          
      var height = borderHeight + element.scrollHeight + paddingHeight;
      
      // Sets new height
      element.style.height = height + "px";
    };
  
    ///////////////Make LaTex Engine Work///////////////
    let latexScript = document.createElement('script');
    latexScript.setAttribute('src', "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS_HTML");
    document.head.appendChild(latexScript);
    ////////////////////////////////////////////////////
    
    this.display();
    this.calculateCols();
    //alert("Here: "+this.cols);
    
    document.addEventListener("input", function(event){
      if(event.target.id.toLowerCase() != "input"){
        return;
      }
      inputExpand(event.target);
    }, false);
    
    document.documentElement.style.setProperty('--size', this.calculateFontSize()+'em');
    document.documentElement.style.setProperty('--fontSize', this.calculateFontSize()+'em');
    // let variable = getComputedStyle(document.documentElement).getPropertyValue('--size');
  },
  methods:{
    display(){
      //var s = screen.height;
      //var w = screen.width;
      //alert(s+"x"+w)
    },
    calculateCols(){
      this.cols = parseInt(screen.width/56);
      //alert(this.cols);
      document.getElementById("input").cols = String(Math.max(parseInt(screen.width/56),20));
    },
    calculateFontSize(){
      var calc = Math.max(((screen.width/1680)*2), 0.75);
      //alert("Calc: "+calc);
      return calc;
    },
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
.main-menu{
  width: 100%;
  margin:0;
  //border: 1px solid orange;
  /*display: flex;
  flex-direction: column;
  justify-content: space-between;*/
}
.input-area{
  font-size: var(--size);
}
div{
  margin-left:5%;
  margin-right:5%;
  //border: 1px solid red;
}
.small-form-area{
  outline: 3px solid black;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: repeating-linear-gradient(
    45deg,
    rgb(240, 139, 62),
    rgb(240, 139, 62) 5px,
    rgb(255, 209, 168) 5px,
    rgb(255, 209, 168) 10px
  );
  overflow-y: hidden;
  
}

.form-area{
  outline: 3px solid rgb(12,36,73);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: repeating-linear-gradient(
    45deg,
    rgb(240, 139, 62),
    rgb(240, 139, 62) 10px,
    rgb(255, 209, 168) 10px,
    rgb(255, 209, 168) 20px
  );
}

textarea{
  font-size: 1em;
  text-align:left;
  border-radius: 5px;
  //border: 1px solid blue;
}
h1,h2 {
  font-weight: normal;
}
.text-center{
  text-align: center;
}
.result-display{
  white-space: nowrap;
  overflow-x: auto;
}

/*TODO: Delete when done. For testing only*/
.col{
  //border: 2px solid green;
  background-color: white;
  width: 90%;
}
.inner-form-area{
  background-color: white;
  //border: 1px solid red;
}
.id-overflow{
  white-space: nowrap;
  overflow: hidden;
}
#input{
  width: 90%;
}
.head-space-small{
  margin-top: 5%;
}
.head-space-large{
  margin-top: 2%;
}
.row1-space-large{
  margin-top: 3%;
}
.row2-space-large{
  margin-top: 2%;
}

.line-divider{
  margin-top: 1px;
  border: 1px solid rgb(240, 139, 62);
}
.foot-space-small{
  margin-top: 3%;
}
.foot-space-large{
  margin-bottom: 2%;
}

.row1-space-small{
  margin-top: 8%;
}
.row2-space-small{
  margin-top: 4%;
}
.row3-space-small{
  margin-top: 2%;
}
</style>