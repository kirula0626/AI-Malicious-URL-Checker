from flask import Flask, render_template, request, jsonify
import re
import flask
import validators
import tensorflow as tf
import label_data
import numpy as np
import subprocess
from flask import Response
import json
# NEW UPDATES
def clean_string(s):
    chars_to_remove = ",'.\""
    cleaned_string = s.rstrip(chars_to_remove)
    return cleaned_string

def add_trailing_slash_if_missing(url):
    # Check if the URL ends with a slash
    if not url.endswith('/'):
        # Add a trailing slash to the URL
        url += '/'
    return url

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/process_urls', methods=['POST'])
def process_urls():
    data = request.json

    input_text = data.get('text', '')
    url_pattern = r'https?://\S+|www\.\S+(?=\W|$)'
    extracted_urls = re.findall(url_pattern, input_text)

    # Remove quotation marks from the extracted URLs
    cleaned_urls = [url.rstrip('."').rstrip('///').rstrip('"') for url in extracted_urls] 
    cleaned_urls = [clean_string(url) for url in cleaned_urls]
        
    print("cleaned_urls", cleaned_urls)

    # validate URLs
    validated_urls = []
    for url in cleaned_urls:
        url = url.replace("'", "")
        print("URL", url)

        if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
        
        # Add a trailing slash to the URL if missing
        url = add_trailing_slash_if_missing(url)
        
        # Check if the URL is valid.
        # print(url)
        if not validators.url(url):
            print("Invalid URL format. Please provide a valid URL.")
            return Response('-1', status=400, content_type='text/plain')

        validated_urls.append(url)
    
    print("validated URLs", validated_urls)
    try:
        print("Before subprocess.run")
        result = subprocess.run(["python", "request.py", "-u"] + validated_urls, capture_output=True, text=True)
        output = result.stdout.strip()

        fixed_json_string = output.replace("'", '"')
        parsed_output = json.loads(fixed_json_string)

        print("After subprocess.run")
        print("OUTPUT_123", parsed_output)

        # return render_template("indexs.html", data=parsed_output)
        return jsonify({'extracted_urls': parsed_output})
    except Exception as e:
        return render_template("indexs.html", data=f"Error processing URL: {str(e)}")


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

        print("INCOMING URL", url)

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

if __name__ == '__main__':
    app.run(debug=True)
    