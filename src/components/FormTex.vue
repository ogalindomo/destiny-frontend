<template>
  <div class="main-menu">
    <div>
      <b-row class="d-md-none">
        <div class="head-space-small"></div>
      </b-row>
      <b-row class="d-none d-md-block">
        <div class="head-space-large"></div>
      </b-row>
    </div>
    <div class="d-md-none small-form-area">
      <div class="inner-form-area">
        <b-row>
          <div class="row1-space-small"></div>
        </b-row>
        <b-row>
          <b-col class="text-center"> 
              <picture-input
                v-if="showImageArea"
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
          <div class="row2-space-small"></div>
        </b-row>
        <b-row>
          <b-col>Sample:</b-col>
        </b-row>
        <b-row>
          <b-col>
            <textarea class= "sample-field id-overflow" v-model="ID" rows="1" disabled></textarea>
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
          <div class="row3-space-small"></div>
        </b-row>
        <b-row>
          <b-col>Instructor:</b-col>
        </b-row>
        <b-row>
          <b-col>
            <select v-model="instructor">
              <option>Dr. Urenda</option>
            </select>
          </b-col>
        </b-row>
        <b-row>
          <div class="row3-space-small"></div>
        </b-row>
        <b-row>
          <b-col>Miners Username:</b-col>
        </b-row>
        <b-row>
          <b-col><textarea class="id-field text-center id-overflow" v-model="MinersID" rows="1"></textarea></b-col>
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
        <div>
          <b-modal class="confirmation-modal" id="bv-modal-confirmation" data-backdrop="true" hide-footer no-close-on-esc no-close-on-backdrop hide-header-close>
            <template v-slot:modal-title>
              Please Confirm Your Submission
            </template>
            <div class="d-block text-center">
              <h6>Your Submission Text Is: </h6>
              <vue-mathjax :formula="formula"></vue-mathjax>
              <img class="modal-container" v-if="this.img" :src="`${this.img}`" align="middle" height="auto" width="auto"/>
            </div>
            <b-row>
              <b-col>
                <b-button variant="outline-dark" class="mt-3" block @click="confirmedSubmission">Confirm</b-button>
              </b-col>
              <b-col>
                <b-button variant="danger" class="mt-3" block @click="canceledSubmission">Cancel</b-button>
              </b-col>
            </b-row>
          </b-modal>
        </div>
        <b-row>
          <b-col><b-button block pill variant="dark" style="font-size: var(--fontSize); margin-top: 2.5%;" @click="submissionClicked">Submit</b-button></b-col>
        </b-row>
        <b-row>
          <div class="row1-space-small"></div>
        </b-row>
      </div>
    </div>
<!-- Division between styles of screen -->
    <div class="form-area d-none d-md-block">
      <div class="inner-form-area">
        <b-row>
          <div class="row2-space-small"></div>
        </b-row>
        <b-row>
          <b-col class="photo-area" id="imgInput">
                <picture-input 
                  v-if="showImageArea"
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
          <b-col class="text-center zero-margin">Sample:</b-col>
          <b-col class="text-center zero-margin">Class:</b-col>
          <b-col class="text-center zero-margin">Instructor:</b-col>
          <b-col class="text-center zero-margin">Miners Username:</b-col>
        </b-row>
        <b-row>
          <b-col class="zero-margin"><textarea class="sample-field id-overflow user-selection" v-model="ID" rows="1" disabled></textarea></b-col>
          <b-col class="zero-margin">
            <select v-model="option" class="user-selection">
              <option>Matrix Algebra</option>
              <option>Calculus III</option>
              <option>Foundations of Logic</option>
            </select>
          </b-col>
          <b-col class = "zero-margin">
            <select v-model="instructor" class="user-selection">
              <option>Dr. Urenda</option>
            </select>
          </b-col>
          <b-col class="zero-margin">
            <textarea class="id-field text-center id-overflow user-selection" v-model="MinersID" rows="1"></textarea>
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
        <div>
          <b-modal class="confirmation-modal" id="bv-modal-confirmation" data-backdrop="true" hide-footer no-close-on-esc no-close-on-backdrop hide-header-close>
            <template v-slot:modal-title>
              Please Confirm Your Submission
            </template>
            <div class="d-block text-center">
              <h6>Your Submission Text Is: </h6>
              <vue-mathjax :formula="formula"></vue-mathjax>
              <img class="modal-container" v-if="this.img" :src="`${this.img}`" align="middle" height="auto" width="auto"/>
            </div>
            <b-row>
              <b-col>
                <b-button variant="outline-dark" class="mt-3" block @click="confirmedSubmission">Confirm</b-button>
              </b-col>
              <b-col>
                <b-button variant="danger" class="mt-3" block @click="canceledSubmission">Cancel</b-button>
              </b-col>
            </b-row>
          </b-modal>
        </div>
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
import axios from 'axios';
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
        var retrievedInstructor = localStorage.getItem("instructor");
        if(retrievedMinersID != null)
          this.MinersID = retrievedMinersID;
        if(retrievedOption != null || retrievedOption != '')
          this.option = retrievedOption;
        if(retrievedInstructor != null || retrievedInstructor != 'null')
          this.instructor = retrievedInstructor;
    },
    submissionClicked(){
      if(this.instructor == 'null')
        alert("Please choose an instructor.")
      else if(this.formula == '')
        alert("Please write something.")
      else if(this.img == null)
        alert("Please upload an image")
      else if(this.MinersID == '')
        alert("Please write your Miners Username.")
      else if(this.option == '')
        alert("Please select a class.")
      else
        this.toogleImageDisplayFlag();
    },
    storeInfo(){
        localStorage.setItem("ID", this.MinersID);
        localStorage.setItem("class", this.option);
        localStorage.setItem("instructor", this.instructor);
    },
    toogleImageDisplayFlag(){
      this.showImageArea = false;
      this.$bvModal.show('bv-modal-confirmation')
    },
    confirmedSubmission(){
      this.showImageArea = true;
      this.$bvModal.hide('bv-modal-confirmation')
      this.storeInfo();
      this.sendImageToScript();
    },
    canceledSubmission(){
      this.showImageArea = true;
      this.$bvModal.hide('bv-modal-confirmation');
    },
    sendImageToScript(){
      // Posts info to localhost on port 5000
      // Sanity check can be seen if navigated to that url
      alert("Please wait for a confirmation, do not click the submit again until a message is received.")
      axios.post('http://129.108.156.19:5000/', {
        id: this.MinersID,
        imageID: this.copyID,
        class: this.option,
        input_text: this.formula,
        image: this.img
      })
      .then((res) => {
        alert(res.data.msg);
        window.location.reload(false);
      },(error) => {
        alert(error);
        alert(error.response);
        alert(error.code);});
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
      instructor: '',
      showImageArea: true,
      img: null
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
.modal-container{
  height: 350px;
  width: 350px;
  object-fit:contain;
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
.zero-margin{
  margin: 0px;
}
@media (max-width: 1169px) and (min-width: 953px){
  .user-selection{
    width: 110px;
  }
}
@media (max-width: 952px) and (min-width: 900px){
  .user-selection{
    width: 100px;
  }
}
@media (max-width: 899px) and (min-width: 771px){
  .user-selection{
    width: 100px;
  }
}
.modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
  }

  .modal-footer {
    border-top: 1px solid #eeeeee;
    justify-content: flex-end;
  }

  .modal-body {
    position: relative;
    padding: 20px 10px;
  }

  .btn-close {
    border: none;
    font-size: 20px;
    padding: 20px;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
  }

  .btn-green {
    color: white;
    background: #4AAE9B;
    border: 1px solid #4AAE9B;
    border-radius: 2px;
  }
</style>
