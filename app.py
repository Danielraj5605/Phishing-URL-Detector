from flask import Flask, render_template, request, jsonify, session
from features import extract_features
from predict import predict as get_prediction
import os

app = Flask(__name__)
app.secret_key = os.urandom(24) # For session management

# Global list for demonstration (in a real app, use a database)
RECENT_SCANS = []

@app.route('/')
def index():
    return render_template('index.html', recent_scans=RECENT_SCANS[:5])

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get('url', '').strip()
    if not url:
        return jsonify({"error": "Please enter a URL"}), 400
    
    # Simple normalization
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    # 1. Feature Extraction
    features = extract_features(url)
    
    # 2. Hybrid Analysis (ML + Rules)
    prediction = get_prediction(url, features)
    
    # 3. Update Recent Scans
    scan_entry = {
        "url": url,
        "result": prediction['result'],
        "score": prediction['risk_score']
    }
    
    # Avoid duplicate consecutive entries
    if not RECENT_SCANS or RECENT_SCANS[0]['url'] != url:
        RECENT_SCANS.insert(0, scan_entry)
    
    return render_template('index.html', 
                           url=url, 
                           prediction=prediction, 
                           recent_scans=RECENT_SCANS[:5])

if __name__ == '__main__':
    app.run(debug=True)
