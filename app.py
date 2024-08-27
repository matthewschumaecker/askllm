from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/process', methods=['POST'])
def process_text():
    data = request.json
    input_text = data.get('text', '')
    
    # Process the text (for this example, we'll just reverse it)
    processed_text = input_text[::-1]
    
    return jsonify({'response': f"Processed text: {processed_text}"})

if __name__ == '__main__':
    app.run(debug=True)
