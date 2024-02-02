# Project Title: CIRBE Data Extractor
This project is designed to extract specific data from a PDF file provided by the "Banco de España" about enterprises. The file is known as CIRBE.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Project Structure
The project consists of several Python scripts:

- `definitive.py`: This is the main script that orchestrates the data extraction process.
- `intro_func.py`: This script contains functions for getting the PDF file and extracting text from it.
- `support_regex.py`: This script contains regular expressions used for parsing the extracted text.
- `output.py`: This script contains functions for writing the extracted data to an Excel file.