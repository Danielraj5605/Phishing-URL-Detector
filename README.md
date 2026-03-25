# 🛡️ Phishing URL Detector

A deployed web application that identifies safe, suspicious, and phishing URLs using a hybrid approach of rule-based analysis and machine learning.

## 🎯 Problem
Phishing attacks often use deceptive URLs to trick users. This tool helps users quickly identify potential threats before clicking.

## 🚀 Features
- **URL Feature Extraction:** Analyzes length, dots, presence of '@', IP addresses, and HTTPS status.
- **Hybrid Detection:** Combines rule-based logic with a Logistic Regression machine learning model.
- **Explainable Results:** Provides clear reasons for classification (e.g., "URL is unusually long").
- **Responsive UI:** Clean, modern interface with color-coded results.

## 🧱 Project Structure
- `app.py`: Flask backend.
- `features.py`: URL feature extraction logic.
- `predict.py`: Combined ML and rule-based prediction engine.
- `train.py`: Machine learning model training script.
- `model.pkl`: Trained Logistic Regression model.
- `templates/`: HTML interface.
- `static/`: CSS styling.

## 🛠️ Tech Stack
- **Frontend:** HTML5, CSS3 (Vanilla CSS), Inter Fonts.
- **Backend:** Flask (Python).
- **Machine Learning:** Scikit-Learn (Logistic Regression), Pandas, Joblib.
- **Deployment:** Render (Procfile included).

## 📌 Resume Point
> Built a phishing URL detection system using rule-based and machine learning approaches, achieving accurate classification and providing explainable results to improve user awareness.

## 📸 Screenshots
*(Add screenshots here after deployment)*

---
Built with ❤️ for Security Awareness.
