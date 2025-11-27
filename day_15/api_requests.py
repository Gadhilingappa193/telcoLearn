import requests
import yaml
import json

url = "https://forge.3gpp.org/rep/all/5G_APIs/-/raw/REL-19/TS24283_Lms_Information.yaml"


response = requests.get(url)


# Step 2: Convert YAML text → Python dictionary
yaml_data = yaml.safe_load(response.text)

# Step 3: Convert dictionary → JSON string
json_data = json.dumps(yaml_data, indent=4)

# Step 4: Print JSON
print(json_data)

# Step 5 (optional): Save to a JSON file
with open("output.json", "w") as f:
    f.write(json_data)
