# Data Visualization Tool

![Project Logo](res/logo.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Introduction
The Data Visualization Tool is a desktop application designed to help users visualize data from Excel files. It allows users to load datasets, select columns for the X and Y axes, and generate plots to analyze relationships within the data. The tool aims to make data analysis more accessible and intuitive through a user-friendly graphical interface.

## Features
- **Load Excel Files**: Easily load Excel files and process the data.
- **Column Management**: Add, remove, and clear columns for plotting.
- **Dynamic Plotting**: Generate plots with user-selected columns and customizable axis labels.
- **Interactive Interface**: User-friendly interface for managing and visualizing data.

## Installation
Describe the steps required to install and set up your project.

### Prerequisites
Ensure you have the following prerequisites installed:
- Python 3.x
- pip (Python package installer)

### Installation Steps
Follow these steps to set up the project:

```sh
# Clone the repository
git clone https://github.com/Mank1941/DataVisualisationTool dataviz-tool

# Navigate to the project directory
cd dataviz-tool

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

## Usage
With the virtual environment activated, you can run the application using:
```sh
python main.py
```

1. **Load Data**: Click on "Add File" to select and load an Excel file.
2. **Manage Columns**: Use the "Add", "Remove", and "Clear" buttons to manage columns.
3. **Configure Plot**: Select columns for the X and Y axes and set axis titles.
4. **Plot Data**: Click "PLOT!" to generate and view the plot.

## Configuration
The application configuration is minimal and primarily handled through the graphical user interface. Ensure that the `requirements.txt` file includes all necessary dependencies:

```txt
pandas
matplotlib
pyqt5
openpyxl
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or inquiries, please contact:
- **Project Lead**: Prosper Manyele - [your.email@example.com]

## Acknowledgements
- **PyQt5**: For providing the graphical user interface framework.
- **pandas**: For data manipulation and analysis.
- **matplotlib**: For plotting and data visualization.
- **Excel**: For the file format used in data input.

