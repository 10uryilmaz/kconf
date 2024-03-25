# Keychron Layout Converter

This project provides a Python script for converting saved layout configuration files from Keychron Q8 Max to Keychron K11 Pro. It enables users to transfer their custom layouts from Q8 Max to K11 Pro, preserving the user's preferred key mappings and functionalities and Macros.

## Background

The Keychron Q8 Max and K11 Pro are popular mechanical keyboards among enthusiasts for their build quality, customizable layouts, and distinctive features. However, transitioning custom layouts from the Q8 Max to the K11 Pro can be challenging due to differences in their exported configuration file formats.

This tool was developed by manually comparing layout files from both models. Given that the Keychron Q8's official website advises against firmware modifications unless necessary, this tool provides a safe alternative to adjust and transfer layouts without the need to reset the firmware or risk potential incompatibilities.

## Features

- Reads configuration from exported Q8 Max layout files.
- Generates compatible configuration files for the K11 Pro.
- Preserves custom key mappings and functionalities.
- Supports potential expansion for converting configuration files between different keyboard models with the same physical layout.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository to your local machine:

git clone https://github.com/10uryilmaz/keychron-layout-converter.git

Navigate to the cloned repository:

cd keychron-layout-converter

# Usage
Place your exported Q8 Max layout configuration file in the root directory of the project and name it input.json.

Run the conversion script:

python kconv.py

The script will generate a new file named output.json in the root directory, which contains the K11 Pro compatible configuration.

## Contributing
Contributions are welcome! If you have suggestions for improving this tool, feel free to fork the repository and submit a pull request. Potential areas for expansion include supporting different keyboard model config conversions.In the time of writing this I did not have the config export from fresh Q8 Max so I implemented only converter from Q8 to K11 but it should be possible to write conver which will make this conversion in between any different keyboards which share the same physical layout.
