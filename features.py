import re
from urllib.parse import urlparse

def extract_features(url):
    """
    Extracts features from a URL for phishing detection.
    """
    features = {}
    
    # Feature 1: URL Length
    features['length'] = len(url)
    
    # Feature 2: Count of "."
    features['dot_count'] = url.count('.')
    
    # Feature 3: Presence of "@"
    features['has_at'] = 1 if '@' in url else 0
    
    # Feature 4: Presence of IP address
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    features['has_ip'] = 1 if re.search(ip_pattern, url) else 0
    
    # Feature 5: HTTPS or not
    features['https'] = 1 if url.startswith('https') else 0

    # Feature 6: Count of "-" (Often used in phishing)
    features['dash_count'] = url.count('-')

    # Feature 7: Presence of "login", "secure", "verify"
    keywords = ['login', 'secure', 'verify', 'update', 'account', 'banking', 'service']
    features['keyword_count'] = sum(1 for kw in keywords if kw in url.lower())
    
    return features

if __name__ == "__main__":
    # Test extraction
    test_url = "http://192.168.1.1/login@secure.com/index.php?id=123"
    print(f"Features for {test_url}:")
    print(extract_features(test_url))
