from flask import Flask, request
from flask_cors import CORS
import subprocess, json, os, base64

app = Flask("ImageProcessingEngine")

CORS(app, resources={r'/*':{'origins':"*"}})

@app.route("/", methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello():
    if request.method == "POST":
        received = request.json
        process_json(received)
        return {'msg':'The image was received!'}
    else:
        return {'msg':'Heard a Get'}

def process_json(vector):
    #Description of the image format.
    image_type = vector['image'].split(';',1)
    #Format of the image (e.g. png, jpeg)
    image_format = image_type[0].split('/')[1]
    #Image in base64 encoding.
    image_description = image_type[1].split(',',1)[1]
    #ImageID
    image_ID = vector['imageID']
    save_img(image_description, image_ID, image_format)
    vector.pop("image")
    short_vector = vector
    send_to_processing_module(short_vector)
    
def save_img(img,image_ID, image_format):
    f = open("Gallery/"+image_ID+'.'+image_format, "wb")
    i = base64.b64decode(img)
    f.write(i)
    f.close()

def send_to_processing_module(short_vector):
    short_vector = json.dumps(short_vector)
    subprocess.run(['python3','temp.py',short_vector])

if __name__ == "__main__":
    if os.path.isdir('./Gallery') == False:
        os.mkdir('./Gallery')
    app.run(host='0.0.0.0')
