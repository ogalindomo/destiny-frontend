from flask import Flask, request
from flask_cors import CORS

app = Flask("ImageProcessingEngine")

CORS(app, resources={r'/*':{'origins':'*'}})

@app.route("/", methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello():
    if request.method == "POST":
        print(request.json)
        return {'msg':'The image was received!'}
    else:
        return {'msg':'Heard a Get'}

if __name__ == "__main__":
    app.run()
