import re

# Example response
response = "The bar graph of average sales for 5 unique stores has been saved as 'average_sales.png'."

# Regular expression to find the filename with .png extension
pattern = r"'([^']+\.png)'"
match = re.search(pattern, response)

if match:
    filename = match.group(1)
    print(f"Extracted filename: {filename}")
else:
    print("No filename found.")
