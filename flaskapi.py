import tensorflow as tf
import label_data
import flask
import json
import numpy as np

app = flask.Flask(__name__)

# Load the Keras model.
model_pre ='models/bi-lstmchar256256128.h5'
model = tf.keras.models.load_model(model_pre)

# List to store processed URLs and their results.
processed_urls = []

def prepare_url(url):

    urlz = label_data.main()

    samples = []
    labels = []
    for k, v in urlz.items():
        samples.append(k)
        labels.append(v)

    maxlen = 128
    max_words = 20000

    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=max_words, char_level=True)
    tokenizer.fit_on_texts(samples)
    sequences = tokenizer.texts_to_sequences(url)
    word_index = tokenizer.word_index

    url_prepped = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=maxlen)
    return url_prepped

@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}

    if flask.request.method == "POST":
        incoming = flask.request.get_json()
        urlz = []
        url = incoming["url"]

        urlz.append(url)

        url_prepped = prepare_url(urlz)
        prediction = model.predict(url_prepped)

        result = ""
        malicious = False

        if prediction > 0.50:
            result = "URL is probably malicious."
            malicious = True
        else:
            result = "URL is probably NOT malicious."

        split = url.split("//")
        split2 = split[1]
        if "/" not in split2:
            result = "Base URLs cannot be accurately determined."

        prediction_percentage = float(prediction) * 100

        processed_url = {
            "url": url,
            "malicious": malicious,
            "percentage": prediction_percentage
        }

        # Add processed URL to the list.
        processed_urls.append(processed_url)

        data["result"] = result
        data["success"] = True

    return flask.jsonify(data)

@app.route("/processed_urls", methods=["GET"])
def get_processed_urls():
    # Return the list of processed URLs.
    return flask.jsonify({"processed_urls": processed_urls})

if __name__ == "__main__":
    print("Starting the server and loading the model...")
    app.run(host='0.0.0.0', port=45000)
