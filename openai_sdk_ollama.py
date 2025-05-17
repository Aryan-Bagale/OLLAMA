def chat_with_model(prompt):
    from openai import OpenAI  # ✅ required for using the OpenAI client interface

    # Create a client for interacting with a locally hosted Ollama model
    client = OpenAI(
        api_key="ollama",  # dummy value; required by SDK but unused for Ollama
        base_url="http://localhost:11434/v1/"  # point to local Ollama server
    )

    # Define the chat messages
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},  # fixed typo in 'assistant'
        {"role": "user", "content": prompt }
    ]

    # Try streaming a response
    try:
        response = client.chat.completions.create(
            model="deepseek-r1:1.5b",  # model must exist in your local Ollama
            messages=messages,
            stream=True,
        )

        for chunk in response:
            if chunk.choices[0].delta.content:  # safe check for streaming content
                print(chunk.choices[0].delta.content, end="", flush=True)

    except Exception as e:
        print(f"\n❌ Error: {e}")

chat_with_model(input("Type Here: "))