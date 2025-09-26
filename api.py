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

    # Yahan apna real download/processing logic dalen
    # Example: agar URL valid hai, simple message return karenge
    try:
        # Placeholder for actual processing, e.g., requests.get(url)
        # yahan processing error handle karen
        message = f"Processing URL: {url}"
        return jsonify({"message": message})
    except Exception as e:
        return jsonify({"error": f"Failed to process URL: {str(e)}"}), 500

if __name__ == "__main__":
    # Heroku par gunicorn se run karenge, debug=False production ke liye
    app.run(debug=False, host='0.0.0.0', port=5000)
