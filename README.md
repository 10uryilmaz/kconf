# Keychorn Layout Config Converter

This project provides a Python script for converting saved layout configuration files of Keychron Q8 Max to Keychron K11 Pro and vice versa.
Works with QMK VIA web app.

## Background

Crafted through a detailed comparison of layout files between the Keychron Q8 Max and K11 Pro, this converter addresses the challenge of differing exported configuration file formats. It provides a solution for adapting and transferring layouts without necessitating firmware resets or risking compatibility issues.

## Features

- Seamlessly reads and converts configuration files from the Q8 Max to the K11 Pro and potentially vice versa.
- Maintains custom key mappings for all layouts, macros, and functionalities across conversions.
- Designed with the flexibility to support additional keyboard models with compatible physical layouts in the future.

## Getting Started

### Prerequisites

Ensure Python 3.x is installed on your machine.

### Installation

1. Clone the repository:

git clone https://github.com/10uryilmaz/keychron-layout-converter.git

Navigate to the cloned repository:

cd keychron-layout-converter

# Usage
Export and place your exported configuration file in the root directory make sure its file name is not modified as its downloaded a few times etc.

Run the conversion script:

python kconv.py

If all goes well the script will generate the new config file in the root directory, which contains the K11 Pro compatible configuration.

# Known Limitations

Its tested and working fine for converting:
  Keychron Q8 Max config to Keychron K11 Pro. 
  Keychron K11 Pro to Keychron Q8 Max.
  (Both are rgb hot swappable models)

I believe it should be working fine for converting:
  Any Keychron Q8 model to any Keychorn K11.
  Any Keychorn K11 model to any Keychorn Q8 model.
  (I am not a keyboard enthusiast so I am not %100 sure wether the vendorproductids are same for all models sharing the same model family so if you try please let     me know the results)

## Contributing and Further Improvements
Your contributions are encouraged and welcome! If you have ideas for enhancing this tool or extending its compatibility to other models, please fork the repository and submit a pull request. While the initial focus has been on converting from and to Q8 and K11 due to available configurations, the goal is to eventually support bidirectional conversions between any two keyboards sharing the same physical layout.

If you have suggestions for improving this tool, feel free to fork the repository and submit a pull request. Potential areas for expansion include supporting different keyboard model config conversions. 
As I did not have the fresh Q8 Max config file I did not try this but I believe a general approach would be possible in order to convert the config files of 
keyboards which have the same physical key layouts. So the next step can be to update the code to convert any keyboard config to another if they have the same 
physical layout.

## Questions or Suggestions?

Feel free to reach out if you have any questions, suggestions, or just want to share your experience with the project. I'm always happy to connect with fellow enthusiasts and learn from your feedback.

📧 Email: onuryilmaz@onuryilmaz.com
