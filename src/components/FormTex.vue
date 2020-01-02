<template>
  <div class="main-menu">
    <div>
      <b-row class="d-sm-none">
        <div class="head-space-small"></div>
      </b-row>
      <b-row class="d-none d-sm-block">
        <div class="head-space-large"></div>
      </b-row>
    </div>
    <div class="d-sm-none small-form-area">
      <div class="inner-form-area">
        <b-row>
          <div class="row1-space-small"></div>
        </b-row>
        <b-row>
          <b-col class="text-center"> 
              <picture-input 
                style="width: 100%"
                ref="pictureInput" 
                @change="onChange" 
                width="400" 
                height="400" 
                :autoToggleAspectRatio="true" 
                margin="0"
                accept="image/jpeg,image/png" 
                size="10" 
                buttonClass="btn"
                :hideChangeButton="true"
                :crop="false"
                :customStrings="{
                  upload: '<h1>Bummer!</h1>',
                  drag: 'Import an image',
                  tap: 'Tap to upload an image'
                }">
            </picture-input>
          </b-col>
        </b-row>
        <b-row>
          <div class="row1-space-small"></div>
        </b-row>
        <b-row>
          <b-col>Sample:</b-col>
        </b-row>
        <b-row>
          <b-col>
            <textarea class= "sample-field id-overflow" style="resize: none;" v-model="ID" cols="12" rows="1" disabled></textarea>
          </b-col>
        </b-row>
        <b-row>
          <div class="row3-space-small"></div>
        </b-row>
        <b-row>
          <b-col>Class:</b-col>
        </b-row>
        <b-row>
          <b-col>
            <select v-model="option">
              <option>Matrix Algebra</option>
              <option>Calculus III</option>
              <option>Foundations of Logic</option>
            </select>
          </b-col>
        </b-row>
        <b-row>
          <div class="row2-space-small"></div>
        </b-row>
        <b-row>
          <b-col>Miners ID:</b-col>
        </b-row>
        <b-row>
          <b-col><textarea class="id-field id-overflow" v-model="MinersID" style="resize: none;" cols="12" rows="1"></textarea></b-col>
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
            <textarea id="input" style="resize: none; text-align:center; font-size: var(--size);" v-model="formula"></textarea>
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
          <b-col><b-button block pill variant="dark" style="font-size: var(--fontSize); margin-top: 2.5%;" @click="submissionClicked">Submit</b-button></b-col>
        </b-row>
        <b-row>
          <div class="row1-space-small"></div>
        </b-row>
      </div>
    </div>
<!-- Division between styles of screen -->
    <div class="form-area d-none d-sm-block">
      <div class="inner-form-area">
        <b-row>
          <div class="row2-space-small"></div>
        </b-row>
        <b-row>
          <b-col class="photo-area">
                <picture-input 
                  ref="pictureInput" 
                  @change="onChange" 
                  width="720" 
                  height="300" 
                  :autoToggleAspectRatio="true" 
                  margin="0" 
                  accept="image/jpeg,image/png" 
                  size="10" 
                  buttonClass="btn"
                  :hideChangeButton="true"
                  :crop="false"
                  :customStrings="{
                    upload: '<h1>Bummer!</h1>',
                    drag: 'Import an image',
                    tap: 'Tap to upload an image'
                  }">
                </picture-input>
          </b-col>
        </b-row>
        <b-row>
          <div class="row2-space-small"></div>
        </b-row>
        <b-row>
          <b-col class="text-center">Sample:</b-col>
          <b-col class="text-center">Class:</b-col>
          <b-col class="text-center">Miners ID:</b-col>
        </b-row>
        <b-row>
          <b-col><textarea class="sample-field id-overflow user-selection" v-model="ID" style="resize: none;" cols="12" rows="1" disabled></textarea></b-col>
          <b-col align-self="center">
            <select v-model="option" class="user-selection">
              <option>Matrix Algebra</option>
              <option>Calculus III</option>
              <option>Foundations of Logic</option>
            </select>
          </b-col>
          <b-col>
            <textarea class="id-field id-overflow user-selection" v-model="MinersID" style="resize: none;" cols="12" rows="1"></textarea>
          </b-col>
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
            <textarea id="input" style="resize: none; text-align:center; font-size: var(--size)" class="input-area;" v-model="formula"></textarea>
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
              <vue-mathjax style="font-size: var(--fontSize);" :formula="formula"></vue-mathjax>
            </div>
          </b-col>
        </b-row>
        <b-row>
          <b-col><b-button block pill variant="dark" style="font-size: var(--fontSize); margin-top: 2.5%;" @click="submissionClicked">Submit</b-button></b-col>
        </b-row>
        <b-row>
          <div class="row1-space-large"></div>
        </b-row>
        <b-row>
          <div class="foot-space"></div>
        </b-row>
      </div>
    </div>

  </div>
</template>

<script>
import { VueMathjax } from 'vue-mathjax'
import PictureInput from 'vue-picture-input'
import {uuid} from 'vue-uuid';
export default {
  components: {
    'vue-mathjax': VueMathjax,
    PictureInput,
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
  
    // Makes LaTex engine work 
    let latexScript = document.createElement('script');
    latexScript.setAttribute('src', "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS_HTML");
    document.head.appendChild(latexScript);
    ////////////////////////////////////////////////////
    document.addEventListener("input", function(event){
      if(event.target.id.toLowerCase() != "input"){
        return;
      }
      inputExpand(event.target);
    }, false);
    
    // Adjust the size of CSS elements that need text
    document.documentElement.style.setProperty('--size', this.calculateFontSize()+'em');
    document.documentElement.style.setProperty('--fontSize', this.calculateFontSize()+'em');
    
    this.ID = this.$uuid.v4();
    this.copyID = this.ID;
    this.retrieveInfo();
  },
  methods:{
    calculateCols(){
      this.cols = parseInt(screen.width/56);
      document.getElementById("input").cols = String(Math.max(parseInt(screen.width/56),20));
    },
    calculateFontSize(){
      var calc = Math.max(((screen.width/1680)*2), 0.75);
      return calc;
    },
    onChange(img){
      if (img != null){
        this.img = img;
      }
      else{
        alert("Please upload an image.");
      }
    },
    retrieveInfo(){
        var retrievedMinersID = localStorage.getItem("ID");
        var retrievedOption = localStorage.getItem("class");
        if(retrievedMinersID != null)
          this.MinersID = retrievedMinersID;
        if(retrievedOption != null || retrievedOption != '')
          this.option = retrievedOption;
    },
    submissionClicked(){
      if(this.img != null){
        if(this.MinersID != ''){
          if(this.option != ''){
            // The miners id and the options are saved before the website is re uploaded.
            localStorage.setItem("ID", this.MinersID);
            localStorage.setItem("class", this.option);
            // Forces a reload of the website.
            window.location.reload(false); 
          }
          else{
            alert("Please select a class.")
          }
        }
        else{
          alert("Please write your Miners ID.")
        }
      }
      else{
        alert("Please upload an image")
      }
    }
  },
  name: 'FormTex',
  data () {
    return {
      input:"",
      formula: '$$x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}$$',
      MinersID:'',
      ID: "",
      copyID: "",
      uuid: uuid.v1(),
      option: '',
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* .photo-area{
} */

.btn-dark{
  background-color: rgb(18,41,79);
  color: rgb(240, 139, 62);
}

.btn-dark:hover{
  background-color: rgb(18,41,79);
}

.btn-dark::after{
  background-color: rgb(18,41,79);
}

.main-menu{
  width: 100%;
  height: 100%;
  margin:0;
}
.input-area{
  font-size: var(--size);
}
div{
  margin-left:5%;
  margin-right:5%;
  /* border: 1px solid white; */
  /* border: 10px solid red; */
}
.small-form-area{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow-y: hidden;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  background: rgb(231, 230, 225);
}
.form-area{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  background: rgb(231, 230, 225);
}
textarea{
  font-size: 1em;
  text-align:left;
  border-radius: 5px;
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
.col{
  background-color: white;
  width: 90%;
}
.inner-form-area{
  background-color: white;
}
.id-overflow{
  white-space: nowrap;
  overflow: hidden;
}
.sample-field{
  resize: none; 
  text-align: right;
}
.id-field{
  resize: none; 
  text-align: left;
}
#input{
  width: 90%;
  resize: none; 
  text-align:center;
}
.head-space-small{
  margin-top: 5%;
}
.head-space-large{
  margin-top: 4%;
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
.foot-space{
  margin-top: 3%;
}
.row1-space-small{
  border: 1px solid red;
  margin-top: 8%;
}
.row2-space-small{
  margin-top: 4%;
}
.row3-space-small{
  margin-top: 2%;
}
@media (max-width: 952px) and (min-width: 900px){
  .user-selection{
    width: 120px;
  }
}
@media (max-width: 899px) and (min-width: 765px){
  .user-selection{
    width: 100px;
  }
}
@media (max-width: 764px) and (min-width: 706px){
  .user-selection{
    width: 90px;
  }
}
@media (max-width: 705px) and (min-width: 651px){
  .user-selection{
    width: 80px;
  }
}
@media (max-width: 650px) and (min-width: 589px){
  .user-selection{
    width: 70px;
  }
}
@media (max-width: 588px) and (min-width: 574px){
  .user-selection{
    width: 65px;
  }
}
</style>
