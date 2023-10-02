import subprocess
import json
import flask
from flask import request
import validators
import tkinter as tk
from tkinter import messagebox
import tensorflow as tf
import label_data
import numpy as np
from flask import request, render_template


app = flask.Flask(__name__)

model_pre ='models/bi-lstmchar256256128.h5'
model = tf.keras.models.load_model(model_pre)

def prepare_url(url):

    urlz = label_data.main()

    samples = []
    labels = []
    for k, v in urlz.items():
        samples.append(k)
        labels.append(v)

    #print(len(samples))
    #print(len(labels))

    maxlen = 128
    max_words = 20000

    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=max_words, char_level=True)
    tokenizer.fit_on_texts(samples)
    sequences = tokenizer.texts_to_sequences(url)
    word_index = tokenizer.word_index
    #print('Found %s unique tokens.' % len(word_index))

    url_prepped = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=maxlen)
    return url_prepped

@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}

    if flask.request.method == "POST":
        incoming = flask.request.get_json()
        url = incoming.get("url")

        if not url or not validators.url(url):
            data["error"] = "Invalid URL format. Please provide a valid URL."
            return flask.jsonify(data)

        try:
            url_prepped = prepare_url([url])
            prediction = model.predict(url_prepped)

            result = "URL is probably malicious." if prediction > 0.50 else "URL is probably NOT malicious."
            data["result"] = result
            data["success"] = True
        except Exception as e:
            data["error"] = f"Error processing URL: {str(e)}"

    return flask.jsonify(data)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]

        if not url or not validators.url(url):
            return render_template("index.html", error="Invalid URL format. Please provide a valid URL.")

        try:
            result = subprocess.run(["python", "request.py", "-u", url], capture_output=True, text=True)
            output = result.stdout.strip()
            return render_template("index.html", result=output, url=url)
        except Exception as e:
            return render_template("index.html", error=f"Error processing URL: {str(e)}")

    return render_template("index.html", result=None, error=None, url=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=45000)