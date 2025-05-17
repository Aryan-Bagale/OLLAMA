#Interact with DeepSeek-R1 in Python using Ollama REST API

# Import necessary libraries
import requests  # Used to send HTTP requests (core part of interacting with REST APIs)
import json      # Used to parse JSON data (commonly used format in REST APIs)

# Define the REST API endpoint provided by the local Ollama server
# This is the URL we're sending the HTTP request to
# "localhost" means the server is running on your own computer
# "/api/generate" is the specific REST endpoint for generating model output
url = "http://localhost:11434/api/generate"

# Define the data (JSON payload) to send in the POST request
data = {
    "model": "deepseek-r1",   # Name of the AI model to use
    "prompt": "1+ 1"          # The user input or prompt to send to the model
}

# Send a POST request to the REST API with the specified URL and data
# stream=True means we want to receive the response as a stream (useful for real-time generation)
# This is the actual REST API call using the HTTP POST method
response = requests.post(url, json=data, stream=True)

# Check if the response was successful (HTTP status code 200 = OK)
if response.status_code == 200:
    print("Generated Text:", end=" ", flush=True)

    # Loop through each line of the streamed response
    # The model will send output line-by-line as it generates text
    for line in response.iter_lines():
        if line:  # Skip empty lines
            # Decode the byte string to a normal string (UTF-8 format)
            decoded_line = line.decode("utf-8")
            
            # Parse the JSON-formatted line into a Python dictionary
            result = json.loads(decoded_line)
            
            # Extract the generated text from the 'response' field
            generated_text = result.get("response", "")
            
            # Print the generated text in real-time (without newlines)
            print(generated_text, end="", flush=True)

else:
    # If something went wrong, print the error status and message
    print("Error:", response.status_code, response.text)
