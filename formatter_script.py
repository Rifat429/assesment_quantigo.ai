import json

# Load the original JSON data from "pos_0.png.json"
with open('pos_0.png.json', 'r') as json_file:
    original_data = json.load(json_file)

# Initialize dictionaries to store the formatted data
annotation_objects = {}
annotation_attributes = {}

# Loop through objects in the original data
for obj in original_data['objects']:
    annotation_type = obj['classTitle'].lower()
    annotation_type = annotation_type.replace(" ", "_")
    bbox = obj['points']['exterior']

    # Create a dictionary for annotation_objects
    annotation_objects[annotation_type] = {
        "presence": 1,
        "bbox": [bbox[0][0], bbox[0][1], bbox[1][0], bbox[1][1]]
    }

    # Create a dictionary for annotation_attributes
    annotation_attributes[annotation_type] = {}

    # Extract attributes from tags
    for tag in obj['tags']:
        attribute_name = tag['name']
        attribute_value = tag['value']

        if attribute_name == "Difficulty Score":
            attribute_value = int(attribute_value)

        annotation_attributes[annotation_type][attribute_name] = attribute_value

# Add "Occlusion" attribute to "license_plate" if it's missing
if "license_plate" in annotation_attributes and "Occlusion" not in annotation_attributes["license_plate"]:
    annotation_attributes["license_plate"]["Occlusion"] = 0



# Create the final formatted data
formatted_data = [{
    "dataset_name": "pos_0.png.json",
    "image_link": "",
    "annotation_type": "image",
    "annotation_objects": annotation_objects,
    "annotation_attributes": annotation_attributes
}]

# Save the formatted data to "formatted_pos_0.png.json"
with open('new_formatted_pos_0.png.json', 'w') as formatted_file:
    json.dump(formatted_data, formatted_file, indent=4)

print("Conversion completed. Formatted data saved to formatted_pos_0.png.json.")
