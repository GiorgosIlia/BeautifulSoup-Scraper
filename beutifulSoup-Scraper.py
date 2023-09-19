import requests
from bs4 import BeautifulSoup
import csv
import os
import re
import time

# Define the base URL of the web page you want to scrape
base_url = "https://example.com/page/{}/"

# Create a directory to store downloaded images
image_dir = "images"
os.makedirs(image_dir, exist_ok=True)

# Define the directory path and file name
directory_path = 'path/to/save/the/file.csv'
file_name = 'file.csv'

# Full file path
file_path = os.path.join(directory_path, file_name)

# Create a CSV file to store the data
with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Product Name', 'Product Details', 'Sale Price', 'Link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  # Write the header row

    # Iterate through multiple pages
    page_number = 1  # Start with the first page
    max_pages = 12  # Define the maximum number of pages to scrape (you can adjust this as needed)

    while page_number <= max_pages:
        # Construct the URL for the current page
        url = base_url.format(page_number)
        print(f"Scraping page {page_number}: {url}")  # Debugging statement

        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find product title elements, product description elements, and price elements
            product_title_tags = soup.find_all('h3', class_='product-title-class')
            product_details_tags = soup.find_all('p', class_='product-description-class')
            product_price_tags = soup.find_all('span', class_='product-price-class')
            product_link_tags = soup.find_all('a', class_='product-link-class')

            # Iterate through products on the current page and write to CSV
            for name_tag, details_tag, price_tag, link_tag in zip(product_title_tags, product_details_tags, product_price_tags, product_link_tags):
                product_name = name_tag.text
                details = " ".join(re.split(r'\s+', details_tag.text))
                final_price = price_tag.text
                link = link_tag.get('href')

                details_one_line = " ".join(re.split(r'\s+', details))
                writer.writerow({
                    'Product Name': product_name,
                    'Product Details': details_one_line,
                    'Sale Price': final_price,
                    'Link': link
                })

        else:
            print("Failed to retrieve the web page. Status code:", response.status_code)

        # Increment the page number
        page_number += 1

        # Introduce a delay (e.g., 10 seconds) between requests to avoid overloading the website
        time.sleep(10)

print("Data has been written to file.csv")
