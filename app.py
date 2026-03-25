from flask import Flask, render_template, request, jsonify
from features import extract_features
from predict import predict as get_prediction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    
    # Clean URL (optional)
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    # Extract features
    features = extract_features(url)
    
    # Get combined prediction (ML + Rules)
    prediction = get_prediction(url, features)
    
    return render_template('index.html', url=url, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
