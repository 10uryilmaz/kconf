import json
import os

def modify_layersfor_k11(data):
    def add_kc_no(layer, line_numbers):
        offset = 0
        for original_line_number in line_numbers:
            adjusted_line_number = original_line_number + offset
            layer.insert(adjusted_line_number, "KC_NO")
            offset += 1


    def delete_lines(layer, line_numbers):
        offset = 0
        for original_line_number in line_numbers:
            adjusted_line_number = original_line_number - offset
            del layer[adjusted_line_number - 1]
            offset += 1
    
    for layer in data['layers']:
        add_kc_no(layer, [14])
        add_kc_no(layer, [30])
        delete_lines(layer, [39])
        add_kc_no(layer, [44])
        add_kc_no(layer, [46])
        add_kc_no(layer, [60])
        add_kc_no(layer, [71])
        add_kc_no(layer, [71])
        add_kc_no(layer, [71])
        delete_lines(layer, [78])
        delete_lines(layer, [78])
        
    return data


def modify_layersfor_q8(data):
    def add_kc_no(layer, line_numbers):
        offset = 0
        for original_line_number in line_numbers:
            adjusted_line_number = original_line_number + offset
            layer.insert(adjusted_line_number, "KC_NO")
            offset += 1


    def delete_lines(layer, line_numbers):
        offset = 0
        for original_line_number in line_numbers:
            adjusted_line_number = original_line_number - offset
            del layer[adjusted_line_number - 1]
            offset += 1
    
    for layer in data['layers']:
        delete_lines(layer, [15])
        delete_lines(layer, [30])
        add_kc_no(layer, [36])
        delete_lines(layer, [44])
        delete_lines(layer, [45])
        delete_lines(layer, [58])
        delete_lines(layer, [68])
        delete_lines(layer, [68])
        delete_lines(layer, [68])
        add_kc_no(layer, [70])
        add_kc_no(layer, [70])

    return data

def process_file(input_file_path, output_file_path, new_name, new_vendor_product_id, layer_mod_func):
    if os.path.exists(input_file_path):
        with open(input_file_path, 'r') as file:
            data = json.load(file)
        
        data['name'] = new_name
        data['vendorProductId'] = new_vendor_product_id
        data = layer_mod_func(data)
        
        with open(output_file_path, 'w') as file:
            json.dump(data, file, indent=2)
            
        print(f"\n\n\n BINGO! 🎯🎯🎯🎯🎯  \n\n\n your new config is created. \n\n >>>>>>>>>>      {output_file_path}       <<<<<<<<<<\n")

        print("Did this slice of code gift you some extra ticks on the clock? \n\nDrop me a line "
              "at: \n\n      onuryilmaz@onuryilmaz.com      \n\nit'd totally make my day to hear it did!"
              )

# Configuration for each possible file
configurations = {
    "keychron_q8_max_ansi_knob.layout.json": {
        "output": "converted_keychron_k11_pro_ansi_rgb_knob.layout.json",
        "new_name": "Keychron K11 Pro ANSI RGB Knob",
        "vendorProductId": 875823798,
        "layer_mod_func": modify_layersfor_k11
    },
    "keychron_k11_pro_ansi_rgb_knob.layout.json": {
        "output": "converted_keychron_q8_max_ansi_knob.layout.json",
        "new_name": "Keychron Q8 Max ANSI Knob",
        "vendorProductId": 875825280,
        "layer_mod_func": modify_layersfor_q8
    }
}

# Check for each file and process accordingly
for input_file, config in configurations.items():
    if os.path.exists(input_file):
        process_file(input_file, config["output"], config["new_name"], config["vendorProductId"], config["layer_mod_func"])
        break
else:
    print(
    "No valid configuration files found to process. You should have either "
    "keychron_q8_max_ansi_knob.layout.json or keychron_k11_pro_ansi_rgb_knob.layout.json "
    "within the directory"
    "for more information visit https://github.com/10uryilmaz/keychorn-layout-config-converter"
)