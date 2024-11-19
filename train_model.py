import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Load the dataset
df = pd.read_csv("data/mitigation_data.csv")

# Load the label encoder
with open("models/label_encoder.pkl", "rb") as file:
    label_encoder = pickle.load(file)

# Prepare the features and labels
X = df[["Threat_Score", "Frequency"]]  # Adjust to your feature columns
y = label_encoder.transform(df["Label"])  # Encode labels using the encoder

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test the model and check accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Save the trained model in the models folder
with open("models/model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved as 'models/model.pkl'.")
