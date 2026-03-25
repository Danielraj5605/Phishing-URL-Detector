import joblib
import os
import pandas as pd

def predict(url, features):
    """
    Combines ML prediction with rule-based explanation.
    """
    model_path = 'model.pkl'
    reasons = []
    
    # 1. Rule-based analysis for reasons (The "Explanation Engine")
    if features['length'] > 75:
        reasons.append("URL is unusually long")
    if features['has_at'] == 1:
        reasons.append("Contains '@' symbol (often used to mask real domain)")
    if features['has_ip'] == 1:
        reasons.append("Uses an IP address instead of a domain name")
    if features['https'] == 0:
        reasons.append("Does not use HTTPS")
    if features['dot_count'] > 3:
        reasons.append("Contains too many dots")

    # 2. Prediction logic
    if os.path.exists(model_path):
        # Load the model
        model = joblib.load(model_path)
        # Prepare features for model (ensure correct order)
        # Expected order: length, dot_count, has_at, has_ip, https
        feature_df = pd.DataFrame([features])
        prediction = model.predict(feature_df)[0]
        
        if prediction == 1:
            result = "Phishing" if len(reasons) >= 2 else "Suspicious"
        else:
            result = "Safe"
    else:
        # Fallback to rule-based logic
        score = len(reasons)
        if score == 0:
            result = "Safe"
        elif score == 1:
            result = "Suspicious"
        else:
            result = "Phishing"
            
    return {
        "result": result,
        "reasons": reasons
    }

if __name__ == "__main__":
    from features import extract_features
    test_url = "http://192.168.1.1/login@secure.com"
    features = extract_features(test_url)
    print(f"Prediction for {test_url}: {predict(test_url, features)}")
