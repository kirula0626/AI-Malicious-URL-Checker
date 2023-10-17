from flask import Flask, render_template, request, jsonify
import re

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('indexs.html')

@app.route('/process_urls', methods=['POST'])
def process_urls():
    data = request.json

    input_text = data.get('text', '')
    url_pattern = r'https?://\S+|www\.\S+(?=\W|$)'
    extracted_urls = re.findall(url_pattern, input_text)

    # Remove quotation marks from the extracted URLs
    cleaned_urls = [url.rstrip('.').rstrip('/').rstrip('"') for url in extracted_urls] 

    # Process the extracted URLs here if needed
    return jsonify({'extracted_urls': cleaned_urls})

if _name_ == '_main_':
    app.run(debug=True)