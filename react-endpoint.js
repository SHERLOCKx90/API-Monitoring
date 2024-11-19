const fetchPrediction = async (apiKey) => {
    const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ api_key: apiKey })
    });

    const data = await response.json();
    if (data.status === "success") {
        console.log("Predicted Label:", data.predicted_label);
        return data.predicted_label;
    } else {
        console.error("Error:", data.message);
    }
};
