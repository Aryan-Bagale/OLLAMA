import ollama
import os

model = "deepseek-r1:1.5b"

input_file = "./data/travel_essentials.txt"

output_file = "./data/categorized_travel_essentials.txt"


if not os.path.exists(input_file):
    print(f"Error {input_file} not found")
    exit(1)

with open(input_file, "r") as f:
    items = f.read().strip()


prompt = f"""
You are an assistant that categorizes and organizes travel-related items.

Here is a list of travel essentials:

{items}

Please:

1. Categorize these items into appropriate categories such as Documents, Luggage & Bags, Personal Care, Electronics, Health & Safety, Clothing, Accessories, and Miscellaneous.
2. Sort the items alphabetically within each category.
3. Present the categorized list in a clear and organized manner, using bullet points or numbering.
"""

try:
    response = ollama.generate(model = model , prompt = prompt)
    generated_text = response.get("response", "")
    print("==== Categorized List: ===== \n")
    print(generated_text)
    with open(output_file, "w") as f:
        f.write(generated_text.strip())
        print(f"Categorized grocery list has been saved to '{output_file}'.")
except Exception as e:
    print("An error occurred:", str(e))

