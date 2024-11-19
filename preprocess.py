# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# import pickle

# def preprocess_input(threat_score, frequency):
#     # Convert input into DataFrame
#     input_data = pd.DataFrame({
#         "Threat_Score": [threat_score],
#         "Frequency": [frequency],
#         # Add other features if necessary
#     })
#     return input_data

import pandas as pd

def preprocess_gemini_data(gemini_data):
    # Extract and map Gemini data to required features
    preprocessed_data = {
        "ip_type": gemini_data.get("ip_type", "public"),
        "geolocation": gemini_data.get("geolocation", "unknown"),
        "threat_score": gemini_data.get("threat_score", 0),
        "api_behavior": gemini_data.get("api_behavior", 0),
        "ioc": gemini_data.get("ioc", 0),
    }
    
    # Convert to a DataFrame for model compatibility
    return pd.DataFrame([preprocessed_data])
