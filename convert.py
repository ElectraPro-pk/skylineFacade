# # Open the original file and read it
# with open('data.json', 'rb') as file:
#     content = file.read()

# # Try decoding using a fallback encoding (e.g., latin-1)
# content = content.decode('latin-1')

# # Re-encode the content in UTF-8
# with open('data_utf8.json', 'w', encoding='utf-8') as file:
#     file.write(content)


import json

# Load the dumped data
with open('data.json', 'r') as file:
    data = json.load(file)

# Remove the app prefix (e.g., 'appname.')
for entry in data:
    model = entry['model']
    app_name = model.split('.')[0]  # Extract app name from the model
    entry['model'] = model[len(app_name) + 1:]  # Remove the app name prefix

# Write the cleaned data back to the file
with open('data_cleaned.json', 'w') as file:
    json.dump(data, file, indent=4)
