from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indexs.html')

@app.route('/process_urls', methods=['POST'])
def process_urls():
    data = request.json
    input_text = data.get('text', '')
    url_pattern = r'https?://\S+|www\.\S+'
    extracted_urls = re.findall(url_pattern, input_text)
    # Process the extracted URLs here if needed
    return jsonify({'extracted_urls': extracted_urls})

if __name__ == '__main__':
    app.run(debug=True)
