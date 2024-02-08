import json
import re

# def traverse_json(json_obj, keys_dict):
#     # Check if the input is a dictionary
#     if isinstance(json_obj, dict):
#         # Create a new dictionary to store the mapped keys and values
#         mapped_dict = {}

#         # Iterate through each key-value pair in the input dictionary
#         for key, value in json_obj.items():
#             # If the key is present in the keys dictionary
#             if key in keys_dict:
#                 # Assign the value to the corresponding keys
#                 for sub_key in keys_dict[key]:
#                     mapped_dict[sub_key] = value
#             else:
#                 # Recursively traverse nested dictionaries
#                 mapped_dict[key] = traverse_json(value, keys_dict)
        
#         return mapped_dict
    
#     # If the input is a list, recursively traverse each element
#     elif isinstance(json_obj, list):
#         mapped_list = []
#         for item in json_obj:
#             mapped_list.append(traverse_json(item, keys_dict))
#         return mapped_list
    
#     # Base case: return the value as is if it's not a dictionary or a list
#     else:
#         return json_obj

# # Example usage:
# json_object = {
#     "rule_name": "Sample Rule",
#     "rule_type": "Type 1",
#     "rule_description": "This is a sample rule description",
#     "deployment_status": {
#         "display_name": "Deployed",
#         "data_type": "string",
#         "id": 123,
#         "created_on": "2024-02-07",
#         "created_by": "Admin",
#         "field_name": "Status",
#         "db_key": "status"
#     }
# }

# # Define the keys dictionary
keys_dict = {
    "rule_type": ["display_name", "data_type", "id", "created_on", "created_by", "field_name", "db_key"],
    "logic_complexity": ["display_name", "data_type", "id", "created_on", "created_by", "field_name", "db_key"],
    "rule_definition_type": ["display_name", "data_type", "id", "created_on", "created_by", "field_name", "db_key"],
    "deployment_status": ["display_name", "data_type", "id", "created_on", "created_by", "field_name", "db_key"],
    "json_keys": ["rule_name", "rule_type", "rule_description", "impact", "suggested_fix", "active_flag",
                  "logic_complexity", "rule_unique_identifier", "identifier", "rule_definition_type",
                  "dsl_version_no", "id", "created_on", "updated_on", "created_by", "version_no", "org_id",
                  "created_by_id", "can_deploy", "dsl", "inputs", "deployment_status", "platforms",
                  "security_controls", "tags", "suppression_flag", "vul_id", "stig_id", "rule_id", "cci_id",
                  "legacy_id", "rule_definition_type_display_name", "can_edit", "sdp_version_no"]
}

# Traverse the JSON object
    
def read_json_file(file_path):
    """
    Read a JSON file and return its contents as a Python dictionary.

    Args:
    - file_path (str): The path to the JSON file.

    Returns:
    - dict: The contents of the JSON file as a Python dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            json_string = file.read()
            # print(json_string)
            # json_data = json.load(file)
        return json_string
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file '{file_path}': {e}")
        return None

# Example usage:
# file_path = 'example.json'
# json_data = read_json_file(file_path)
# if json_data:
#     print(json_data)


def get_main_nodes(json_string:str)->dict:
    main_json_nodes = json_string.split('": {"200": [{"request": {')
    main_nodes = {}
    ex_path=""
    update_main_node=""

    for i in range(1, len(main_json_nodes)):
        current_node = main_json_nodes[i]
        split_node = current_node.split("}}}]}, ")        
            
        start_index = current_node.find('/api/v1')
        end_index = current_node.find('", "ip')
        # Extract the substring from the start index to the end of the string
        path = current_node[start_index:end_index]
        
        final_node = f"{split_node[0]}}}}}}}]}}"
        main_nodes[path] = f'{{"200": [{{"request": {{{final_node}'
    
    # print(main_nodes)
    return main_nodes

def get_all_child_nodes(main_nodes:dict)->dict:
    converted_json_objects = []
    
    for path, json_string in main_nodes.items():
        print(f"endpoint = {path}")

        # json_string = json_string.rstrip("]}")
        split_str = json_string.split('{"request":')
        modified_items = []
        errors = {}
        
        length_split_str = len(split_str)
        for index in range(1, length_split_str):
            current_node_string = split_str[index]
            if index == (length_split_str-1):
                current_node_string = current_node_string[:-2]
            new_item = '{"request":' + current_node_string
            # Remove the last characters ", "
            new_item = new_item.rstrip(", ")

            # print(f"index = {index}")
            modified_items.append(new_item)

            try:
                json_obj = json.loads(new_item)
                converted_json_objects.append(json_obj)
            except json.decoder.JSONDecodeError as err:
                # print(err)
                errors[index] = err

        # print(len(modified_items))
        # print(type(modified_items))
        print(f"errors for converting to json = {len(errors)}")
        print(f"count - converted to json = {len(converted_json_objects)}")
        
    return converted_json_objects


if __name__ == "__main__":
    json_string = read_json_file("rules.json")
    
    main_nodes = get_main_nodes(json_string)

    child_nodes = get_all_child_nodes(main_nodes)

    file_path = "converted_data.json"

    # Write JSON data to the file
    with open(file_path, "w") as json_file:
        json.dump(child_nodes, json_file)

    # print(child_nodes)





    # split_str = json_string.split('{"request":')
    # modified_items = []
    # errors = {}
    # converted_json_objects = []
    # for index in range(1, len(split_str)):
    #     new_item = '{"request":' + split_str[index]
    #     # Remove the last characters ", "
    #     new_item = new_item.rstrip(", ")

    #     # print(f"index = {index}")
    #     modified_items.append(new_item)

    #     try:
    #         json_obj = json.loads(new_item)
    #         converted_json_objects.append(json_obj)
    #     except json.decoder.JSONDecodeError as err:
    #         print(err)
    #         errors[index] = err

    # print(len(modified_items))
    # print(type(modified_items))
    # print(f"errors for converting to json = {len(errors)}")
    # print(f"count - converted to json = {len(converted_json_objects)}")

    # print(modified_items[1])
    # mapped_json = traverse_json(json_obj, keys_dict)
    # print(mapped_json)