import subprocess
import flask
from flask import request, render_template, jsonify
import validators
import tensorflow as tf
import label_data
import numpy as np

app = flask.Flask(__name__)

# Load the pre-trained Keras model
model_pre = 'models/bi-lstmchar256256128V2.h5'
model = tf.keras.models.load_model(model_pre)

# Modified function to prepare URL for prediction
def prepare_url(url):
    urlz = label_data.main()
    samples = []
    labels = []
    for k, v in urlz.items():
        # Check if the URL is a string and not a float
        if isinstance(k, str):
            samples.append(k)
            labels.append(v)

    maxlen = 128
    max_words = 20000

    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=max_words, char_level=True)
    tokenizer.fit_on_texts(samples)
    sequences = tokenizer.texts_to_sequences(url)
    url_prepped = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=maxlen)
    return url_prepped


@app.route("/predict", methods=["POST"])
def predict():
    # Initialize the dictionary for the response.
    data = {"success": False}

    # Check if POST request.
    if flask.request.method == "POST":
        # Grab and process the incoming json.
        incoming = flask.request.get_json()
        urlz = []
        url = incoming["url"]

        urlz.append(url)

        # Process and prepare the URL.
        url_prepped = prepare_url(urlz)

        # Classify the URL and make the prediction.
        prediction = model.predict(url_prepped)
        
        data["predictions"] = []  # Initialize predictions list
        
        # Determine the result and format response data.
        if prediction > 0.90:
            result = "URL is probably malicious and Dangerous!"
        elif prediction > 0.50:
            result = "URL is probably malicious."
        else:
            result = "URL is probably NOT malicious."
        
        # Check for base URL. Accuracy is not as great.
        split = url.split("//")
        split2 = split[1]
        if "/" not in split2:
            result = "Base URLs cannot be accurately determined."
        
        # Processes prediction probability.
        prediction_percentage = float(prediction) * 100
        
        if result == "Base URLs cannot be accurately determined.":
            r = {"result": result, "url": url}
        else:
            r = {"result": result, "malicious percentage": prediction_percentage, "url": url}
        data["predictions"].append(r)

        # Show that the request was a success.
        data["success"] = True

    # Return the data as a JSON response.
    return flask.jsonify(data)

# Web interface route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]

        # Check if the URL starts with "http://" or "https://", and add "http://" if not.
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
    # Check if the URL is valid.
        if not validators.url(url):
            print("Invalid URL format. Please provide a valid URL.")
            return -1
        try:
            result = subprocess.run(["python", "request.py", "-u", url], capture_output=True, text=True)
            output = result.stdout.strip()
            return render_template("index.html", result=output, url=url)
        except Exception as e:
            return render_template("index.html", error=f"Error processing URL: {str(e)}")

    return render_template("index.html", result=None, error=None, url=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    