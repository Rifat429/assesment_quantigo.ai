import json

# Load the three JSON files
with open('Pos_0.png.json', 'r') as json_file:
    data1 = json.load(json_file)

with open('Pos_10010.png.json', 'r') as json_file:
    data2 = json.load(json_file)

with open('Pos_10492.png.json', 'r') as json_file:
    data3 = json.load(json_file)

# Define a mapping of class name changes
class_name_mapping = {
    "Vehicle": "car",
    "License Plate": "number",
}

# Create a dictionary to hold the combined data
combined_data = {
    "description": "",
    "tags": [],
    "size": {"height": 720, "width": 1280},
    "objects": [],
}

# Iterate through the data in each file
for data in [data1, data2, data3]:
    for obj in data["objects"]:
        class_title = obj["classTitle"]
        if class_title in class_name_mapping:
            obj["classTitle"] = class_name_mapping[class_title]
        combined_data["objects"].append(obj)

# Save the combined and modified data to a new JSON file
with open('combined_data.json', 'w') as json_file:
    json.dump(combined_data, json_file, indent=4)

print("Combining and modifying completed. Combined data saved to combined_data.json.")
