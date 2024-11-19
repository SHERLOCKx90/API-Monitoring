# import pandas as pd
# import pickle
# from preprocess import preprocess_input

# # Load the label encoder and model
# with open("models/label_encoder.pkl", "rb") as le_file:
#     label_encoder = pickle.load(le_file)

# with open("models/model.pkl", "rb") as model_file:
#     model = pickle.load(model_file)

# # Example input data (replace with real-time inputs)
# threat_score = 85  # Replace with real Threat_Score
# frequency = 120    # Replace with real Frequency

# # Preprocess the input
# input_data = preprocess_input(threat_score, frequency)

# # Predict the label
# prediction = model.predict(input_data)
# predicted_label = label_encoder.inverse_transform(prediction)

# # Display the result
# print(f"Predicted label: {predicted_label[0]}")


from flask import Flask, request, jsonify
import pickle
from preprocess import preprocess_gemini_data
from google_gemini_integration import fetch_google_gemini_data

app = Flask(__name__)

# Load model and label encoder
model = pickle.load(open("models/model.pkl", "rb"))
label_encoder = pickle.load(open("models/label_encoder.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Fetch Google Gemini data
        api_key = request.json.get("api_key")
        gemini_data = fetch_google_gemini_data(api_key)

        # Preprocess the data
        preprocessed_data = preprocess_gemini_data(gemini_data)

        # Predict
        prediction = model.predict(preprocessed_data)
        predicted_label = label_encoder.inverse_transform(prediction)[0]

        # Return prediction as JSON
        return jsonify({
            "status": "success",
            "predicted_label": predicted_label
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)
