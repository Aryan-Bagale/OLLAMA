import ollama
import os

model = "deepseek-r1:1.5b"

# Paths to input and output files
input_file = "./data/grocery_list.txt"
output_file = "./data/categorized_grocery_list.txt"

# Check if the input file exists
if not os.path.exists(input_file):
    print(f"Input file '{input_file}' not found")
    exit(1)

# Read the uncategorized grocery items from the input file
with open(input_file,"r") as f:
    items = f.read().strip()
# open(input_file, "r"): Opens the file in read mode.
# f.read(): Reads the entire content.
# .strip(): Removes any extra spaces or newlines at the beginning or end.

# Prepare the prompt for the model
prompt = f"""
You are an assistant that categorizes and sorts grocery items.

Here is a list of grocery items:

{items}

Please:

1. Categorize these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, etc.
2. Sort the items alphabetically within each category.
3. Present the categorized list in a clear and organized manner, using bullet points or numbering.
"""

# Send the prompt and get the response
try:
    response = ollama.generate(model=model, prompt=prompt)  # Ask the model
    generated_text = response.get("response", "")  # Get the actual text from response

    print("==== Categorized List: ===== \n")
    print(generated_text)  # Show it on screen

    # Write the categorized list to the output file

    with open(output_file, "w") as f:
        f.write(generated_text.strip())
    print(f"Categorized grocery list has been saved to '{output_file}'.")
except Exception as e:
    print("An error occurred:", str(e))


