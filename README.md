# BeautifulSoup Scraper

This Python script is a web scraper that fetches data from a specified website and stores it in a CSV file. It is designed to extract product information, including product name, details, sale price, and links.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your system.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/GiorgosIlia/BeautifulSoup-Scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd web-scraper
   ```

3. Install the required Python libraries from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

This will install the necessary libraries, including `requests` for making HTTP requests, `beautifulsoup4` for parsing HTML, and `csv` for handling CSV files.

## Usage

1. Open the `scraper.py` file and update the `base_url` variable with the URL of the website you want to scrape.

2. Update the HTML structure and class names used in `find_all` to match the structure of the website you're scraping.

3. Run the script:

   ```bash
   python scraper.py
   ```

The script will make requests to the specified website, extract product data, and save it to a CSV file named `file.csv`.

## Output

The script will create a CSV file `file.csv` in the project directory, containing the following columns:

- `Product Name`: The name of the product.
- `Product Details`: Additional details about the product.
- `Sale Price`: The sale price of the product.
- `Link`: The link to the product page.

## Contributing

If you'd like to contribute to this project, please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear and concise messages.
4. Push your branch to your fork.
5. Create a pull request to merge your changes into the main repository.

## Issues

If you encounter any issues or have suggestions for improvements, please open an issue on the [Issues](https://github.com/GiorgosIlia/BeautifulSoup-Scraper/issues) page.

Happy scraping!
