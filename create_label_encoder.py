import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

# Load the dataset
df = pd.read_csv("data/mitigation_data.csv")

# Encode the labels
label_encoder = LabelEncoder()
df["Label_Encoded"] = label_encoder.fit_transform(df["Label"])

# Save the label encoder in the models folder
with open("models/label_encoder.pkl", "wb") as file:
    pickle.dump(label_encoder, file)

print("Label encoder saved as 'models/label_encoder.pkl'.")
