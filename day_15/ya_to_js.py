import yaml, json

with open("nrf.yaml") as f:
    y = yaml.safe_load(f)
    
json_data= json.dumps(y, indent=2)
print(json_data)