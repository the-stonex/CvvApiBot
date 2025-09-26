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
    # Yahan aap apna real download/processing logic daal sakte hain
    return jsonify({"message": f"Processing {url}"})

if __name__ == "__main__":
    app.run(debug=True)
