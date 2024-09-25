#import torch
#from transformers import AutoTokenizer, AutoModelForSequenceClassification
from flask import Flask,request,jsonify
from flask_cors import CORS
from transformers import pipeline

pipe = pipeline("text-classification", model="idajikuu/AI-HUMAN-detector")
app=Flask(__name__)
CORS(app)
"""tokenizer = AutoTokenizer.from_pretrained("idajikuu/AI-HUMAN-detector")
model = AutoModelForSequenceClassification.from_pretrained("idajikuu/AI-HUMAN-detector")"""
@app.route("/ML",methods=['POST'])
def get_data():
    data=request.json.get('data')
    ip=data
    """inputs=tokenizer(ip,return_tensors="pt",padding=True)
    with torch.no_grad():
        logits=model(**inputs).logits
    predicted_realness = logits.argmax().item()"""
    predicted_realness=pipe(ip)
    if(predicted_realness[0]['label']=="Real" and predicted_realness[0]['score']>0.99):
        return jsonify({'val':"YES",'real':predicted_realness})
    else:
        return jsonify({'val':"NO",'real':predicted_realness})
    #return jsonify({'message':'Data recieved','rec_dat':ip})



if __name__=="__main__":
    app.run(debug=True)