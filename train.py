import pandas as pd
from features import extract_features
from sklearn.linear_model import LogisticRegression
import joblib
import os

def train_model(data_path='data.csv', model_path='model.pkl'):
    # Load dataset
    df = pd.read_csv(data_path)
    
    # Extract features for each URL
    print("Extracting features...")
    feature_list = []
    for url in df['url']:
        feature_list.append(extract_features(url))
    
    X = pd.DataFrame(feature_list)
    y = df['label']
    
    # Train Logistic Regression model
    print("Training model...")
    model = LogisticRegression()
    model.fit(X, y)
    
    # Save the model
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model()
