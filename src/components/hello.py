from flask import Flask, request
from flask_cors import CORS
import subprocess, json

app = Flask("ImageProcessingEngine")

CORS(app, resources={r'/*':{'origins':"*"}})

@app.route("/", methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello():
    if request.method == "POST":
        received = request.json
        process_image(received)
        return {'msg':'The image was received!'}
    else:
        return {'msg':'Heard a Get'}

def process_image(argument_vector):
    subprocess.call(["python3", "temp.py"]) #, json.dumps(argument_vector)])

if __name__ == "__main__":
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.run(host='0.0.0.0')
