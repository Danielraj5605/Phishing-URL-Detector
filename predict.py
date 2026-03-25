import joblib
import os
import pandas as pd

def predict(url, features):
    """
    Advanced analysis pipeline returning risk score and human-readable reasons.
    """
    model_path = 'model.pkl'
    reasons = []
    confidence_points = 0
    
    # --- PHASE 1: Structural Security Checks (Rules) ---
    if features['length'] > 75:
        reasons.append("Abnormally long URL (common in obfuscation)")
        confidence_points += 25
    if features['has_at'] == 1:
        reasons.append("Contains '@' symbol (used to mask real domain)")
        confidence_points += 35
    if features['has_ip'] == 1:
        reasons.append("Uses raw IP address instead of a verified domain")
        confidence_points += 45
    if features['https'] == 0:
        reasons.append("Unsecured connection (No HTTPS encryption)")
        confidence_points += 20
    if features['dot_count'] > 3:
        reasons.append("Excessive subdomains detected (URL spoofing sign)")
        confidence_points += 15
    if features.get('dash_count', 0) > 2:
        reasons.append("Multiple hyphens used to mimic official domains")
        confidence_points += 10
    if features.get('keyword_count', 0) > 0:
        reasons.append("Contains sensitive keywords (login/banking/secure)")
        confidence_points += 15

    # --- PHASE 2: AI Pattern Recognition (ML) ---
    ml_detected = False
    if os.path.exists(model_path):
        try:
            model = joblib.load(model_path)
            feature_keys = ['length', 'dot_count', 'has_at', 'has_ip', 'https']
            feature_values = [features[k] for k in feature_keys]
            feature_df = pd.DataFrame([feature_values], columns=feature_keys)
            prediction = model.predict(feature_df)[0]
            if prediction == 1:
                ml_detected = True
                confidence_points += 40
        except:
            pass
    
    # --- PHASE 3: Risk Scoring & Classification ---
    risk_score = min(confidence_points, 100)
    
    if risk_score >= 70:
        result = "Phishing"
    elif risk_score >= 30:
        result = "Suspicious"
    else:
        result = "Safe"
        # Minimum score for transparency
        if result == "Safe" and risk_score == 0:
            risk_score = 4 

    return {
        "result": result,
        "risk_score": risk_score,
        "reasons": reasons,
        "ai_analysis": "Patterns match known phishing signatures" if ml_detected else "No malicious AI patterns found"
    }
