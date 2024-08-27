from flask import Flask, render_template, request, jsonify

from llm_calls import askGPT, askClaude
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    prompt = data.get('text', '')
    response_text = askGPT(prompt)

    return jsonify({'response': response_text})


if __name__ == '__main__':
    app.run(debug=True)
