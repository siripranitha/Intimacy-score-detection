from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)


API_URL = "https://api-inference.huggingface.co/models/siripranitha/iter1"
ACCESS_TOKEN = "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"


def query(payload):
    HEADERS = {"Authorization": "Bearer "+ACCESS_TOKEN}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()
	

#https://github.com/melozap/Flask-Language-Detector-App/blob/master/templates/result.html
@app.route('/')
def home(): 
        return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == "POST":
        message = request.form["message"] 
        print(message)
        output = query({"inputs": message,"options":{ 'wait_for_model':True}})
        output = output[0][0]['score']
        output = output*4+1
        output = round(output,2)
        
        return render_template("result.html",prediction = output)

if __name__ == "__main__": 
         app.run(debug=False)