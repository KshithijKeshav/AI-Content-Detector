import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from flask import Flask,request,jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
tokenizer = AutoTokenizer.from_pretrained("idajikuu/AI-HUMAN-detector")
model = AutoModelForSequenceClassification.from_pretrained("idajikuu/AI-HUMAN-detector")
@app.route("/ML",methods=['POST'])
def get_data():
    data=request.json.get('data')
    ip=list(data.split('\n'))
    inputs=tokenizer(ip,return_tensors="pt",padding=True,truncation=True)
    with torch.no_grad():
        logits=model(**inputs).logits
    predicted_realness = logits.argmax().item()
    
    if(predicted_realness<2):
        return jsonify({'val':"YES"})
    else:
        return jsonify({'val':"NO"})
    #return jsonify({'message':'Data recieved','rec_dat':ip})



if __name__=="__main__":
    app.run(debug=True)