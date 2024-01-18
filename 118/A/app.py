from flask import Flask, render_template, request, jsonify
from model_prediction import *

app = Flask(__name__)

text=""
predicted_emotion=""
predicted_emotion_img_url=""

@app.route("/")
def home():
    entries = show_entry()
    return render_template("index.html", entries=entries)
    

@app.route("/predict-emotion", methods=["POST"])
def predict_emotion():
    input_text = request.json.get("text")
    if not input_text:
        return jsonify({
            "status": "error",
            "message": "Digite um texto para prever a emoção!"
        }), 400
    else:
        predicted_emotion, predicted_emotion_img_url = predict(input_text)                         
        return jsonify({
            "data": {
                "predicted_emotion": predicted_emotion,
                "predicted_emotion_img_url": predicted_emotion_img_url
            },
            "status": "success"
        }), 200
        
#Escreva o código da API aqui
@app.route("/save-entry", methods=["POST"])
def save_entry():
    date = request.json.get("date")
    save_text = request.json.get("text")
    save_text=save_text.replace("\n"," ")
    emotion = request.json.get("emotion")
    

    entry = f'{date},{save_text},{emotion}\n'

    with open('./static/assets/datafiles/data_entry.csv','a') as f:
        f.write(entry)
    return jsonify("Success")
                
if __name__ == "__main__":
    app.run(debug=True)

