from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "CvvApiBot API is running!"

@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    # यहाँ आप अपनी डाउनलोड logic डाल सकते हैं
    # फिलहाल यह सिर्फ संदेश भेजता है
    return jsonify({"message": f"Processing {url}"})

if __name__ == "__main__":
    app.run(debug=True)
