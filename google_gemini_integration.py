import requests

def fetch_google_gemini_data(api_key):
    # Example endpoint, replace with actual Google Gemini endpoint
    url = "https://google-gemini-api.example.com/data"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")
