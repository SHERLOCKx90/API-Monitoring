import pandas as pd
import random

# Define the ranges and categories for the dataset
def generate_data(num_samples=100):
    data = []
    for _ in range(num_samples):
        # Generate a random threat score (0 to 100)
        threat_score = random.randint(0, 100)
        
        # Generate a frequency of API access (1 to 200)
        frequency = random.randint(1, 200)
        
        # Randomly assign accessed ports (e.g., common ones)
        accessed_ports = random.choice(["80,443", "22,443", "80", "443", "22,80"])
        
        # Assign a historical risk level based on threat score
        if threat_score > 80:
            historical_risk = "High"
        elif 50 <= threat_score <= 80:
            historical_risk = "Medium"
        else:
            historical_risk = "Low"
        
        # Assign a label based on threat score and historical risk
        if historical_risk == "High" and frequency > 100:
            label = "Malicious"
        elif historical_risk == "Medium" or frequency > 50:
            label = "Suspicious"
        else:
            label = "Benign"
        
        # Append the generated data to the list
        data.append({
            "Threat_Score": threat_score,
            "Frequency": frequency,
            "Accessed_Ports": accessed_ports,
            "Historical_Risk": historical_risk,
            "Label": label
        })
    
    return data

# Generate 100 rows of data
dataset = generate_data(100)

# Create a DataFrame
df = pd.DataFrame(dataset)

# Save to a CSV file
csv_file = "mitigation_data.csv"
df.to_csv(csv_file, index=False)

print(f"Dataset with {len(dataset)} rows saved to '{csv_file}'.")
