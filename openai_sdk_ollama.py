# We can run DeepSeek R1 locally using Ollama. Ollama gives us an endpoint we can talk to. Instead of using OpenAI’s cloud API,
# we point our code to this local endpoint. This way, we use the same code patterns but with local, open-source models.


# Import the OpenAI SDK (used here to connect with the local Ollama server)
from openai import OpenAI

# Define a function that takes user input (prompt) and sends it to the model
def chat_with_model(prompt):
    # Create a client to talk to the local Ollama server
    # Note: The OpenAI SDK needs an api_key, but for Ollama we just pass a dummy value
    client = OpenAI(
        api_key="ollama",  # not used, but required by the SDK
        base_url="http://localhost:11434/v1"  # this must match your running Ollama server
    )

    # Define the messages to send to the model
    # 'system' sets the behavior of the assistant
    # 'user' is the actual question or command given by you
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}  # use the user's actual input here
    ]

    try:
        # Send the messages to the model and request a streaming response
        response = client.chat.completions.create(
            model="deepseek-r1:1.5b",  # Make sure this model is available locally via Ollama
            messages=messages,
            stream=True,  # receive response in chunks as it's being generated
        )

        # Loop through each chunk as it comes and print it immediately
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:  # make sure there is something to print
                print(content, end="", flush=True)  # print without newline

    except Exception as e:
        # If something goes wrong (e.g., model not found or server not running), print the error
        print(f"\n❌ Error: {e}")

# Ask the user for input and send it to the function
chat_with_model(input("Type here: "))
