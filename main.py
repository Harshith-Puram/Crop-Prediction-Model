import numpy as np
import pickle
from flask import Flask, request,render_template,jsonify
#create flask app
app=Flask(__name__)
#load pickel model
model = pickle.load(open('model.pkl','rb'))
# crop names
crop_name=['Apple','Banana','Blackgram','Chickpea','Coconut','Cotton','Grape','Jute','Lentil','Maize','Mango','Muskmelon','Orange','Papaya','Pigeonpeas','Pomegranate','Rice','Watermelon']

@app.route('/') #home page
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
##prediction function
def predict():
    
    float_features=[float(x) for x in request.form.values()] ##con
    features=[np.array(float_features)]
    prediction=model.predict(features)
   
    prediction_name=crop_name[prediction[0]]
    return render_template("index.html",prediction_text=prediction_name+" is the best crop to grow for the above conditions.")

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.get_jsonify(force=True)
    prediction=model.predict([np.array(list(data.values))])
    prediction_name=crop_name[prediction[0]]
    return jsonify(prediction_name)

if __name__=="__main__":
    app.run(debug=True)