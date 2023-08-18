# Classification of Social Media Posts 
Classification of social media posts using SVM and XGB classifiers. API endpoint exposed using FastAPI.

## API Documentation

- Endpoint: /api/theme
- Method: POST
- Description: Get theme probabilities for input text.
- Parameters (Body-json):
  -- text: (required) The social media post text for which you want to predict the probabilities.
- Response example:
```
{
  "personal": 0.123,
  "medical": 0.456,
  "lifestyle": 0.789
}
```

## test_script.py
```
import requests

# Replace with the URL of FastAPI server
url = "http://localhost:8000/api/theme"

# The JSON payload with the "text" field
data = {
    "text": "What is your BHAG? Mine is changing the standard of care for multiple sclerosis patients."
}

# Send the POST request
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    output_probs = response.json()
    print("Predicted probabilities:")
    print(output_probs)
else:
```

