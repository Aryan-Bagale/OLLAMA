import ollama  # Import the Ollama Python library to interact with local LLMs

# ===========================
# 📌 1. List all local models
# ===========================
response = ollama.list()  # Lists all models installed in your Ollama environment
# print(response)  # Uncomment to see the available models

# ================================
# 📌 2. Chat example (non-streaming)
# ================================
res = ollama.chat(
    model="deepseek-r1",  # Changed from 'llama3.2' to 'deepseek-r1'
    messages=[
        {"role": "user", "content": "why is the sky blue?"},  # User message
    ],
)
# print(res["message"]["content"])  # Uncomment to see the full assistant response

# ===================================
# 📌 3. Chat example (with streaming)
# ===================================
res = ollama.chat(
    model="deepseek-r1",  # Streaming chat with 'deepseek-r1'
    messages=[
        {
            "role": "user",
            "content": "why is the ocean so salty?",
        },
    ],
    stream=True,  # Enable streaming output
)

# Stream and print the assistant's reply in real time
for chunk in res:
    print(chunk["message"]["content"], end="", flush=True)  # Output chunks immediately

# =========================================
# 📌 4. Generate text without chat history
# =========================================
res = ollama.generate(
    model="deepseek-r1",  # Use direct prompt with 'deepseek-r1'
    prompt="why is the sky blue?",
)
# print(res["response"])  # Uncomment to see the result

# ========================================
# 📌 5. Create a custom model with system prompt
# ========================================
modelfile = """
FROM deepseek-r1  # Base model changed to 'deepseek-r1'
SYSTEM You are a very smart assistant who knows everything about oceans. You are very succinct and informative.
PARAMETER temperature 0.1  # Lower temperature = more factual, less creative
"""

# Create a new custom model based on 'deepseek-r1'
ollama.create(model="knowitall", modelfile=modelfile)

# Generate a response using the new "knowitall" model
res = ollama.generate(
    model="knowitall",
    prompt="why is the ocean so salty?",
)
print("\n\n🧠 KnowItAll says:", res["response"])  # Output response from custom model

# ============================
# 📌 6. Delete the custom model
# ============================
ollama.delete("knowitall")  # Clean up by deleting the custom model
