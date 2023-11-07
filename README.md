# Web Scraping with Python: Houzz.com Scraper

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to the **Web Scraping with Python: Houzz.com Scraper** project. This repository contains a Python web scraping script that extracts data from business websites on [www.houzz.com](https://www.houzz.com). The scraper is built on Scrapy and BeautifulSoup and is designed to collect information from business sites on Houzz.com, allowing you to store the data in a CSV file for further analysis or usage.

![Houzz.com](https://yourimageurl.com/here)

## Output

- **Business Name**: The name of the business.
- **Location**: The location of the business.
- **Phone Number**: The contact phone number of the business.
- **Website URL**: The website URL of the business.
- **Email**: If emails available on website

## Installation

Follow these steps to get started with the Houzz.com Scraper:

### Prerequisites

- Python 3.x
- Pip (Python Package Installer)

### Instructions

1. Clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/adil6572/houzz-scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd houzz-scraper
   ```

3. Install the required Python packages:
   ```bash
   pip install scrapy beautifulsoup4
   ```

## Usage

To use the Houzz.com Scraper, follow these steps:

To modify the `start_urls` and `custom_settings` in the Houzz.com scraper, follow these instructions:

### Changing `start_urls`:

1. Open the `houzz_scraper/spiders/houzz_spider.py` file in your project directory.

2. Locate the `start_urls` variable, which is defined as a list of URLs. You can change the URL to the one you want to scrape.

3. Replace the existing URL with the new URL you want to scrape (The URL should be similar to Example URL). For example:

   ```python
   start_urls = ["https://www.houzz.com/professionals/interior-designer/carter-lake-ia-us-probr0-bo~t_11785~r_4850531"]
   ```

### Changing `custom_settings`:

1. In the same `houzz_scraper/spiders/houzz_spider.py` file, find the `custom_settings` dictionary.

2. Within the `custom_settings` dictionary, you can customize various settings related to the scraper's behavior. To change the output file format and overwrite behavior, modify the values accordingly.

   - To change the output file format to JSON:

     ```python
     'FEEDS': {
         'output.json': {
             'format': 'json',
             'overwrite': True,  # Set to True to overwrite the file if it already exists
         },
     }
     ```

   - To set the scraper to append data to the existing file instead of overwriting:

     ```python
     'FEEDS': {
         'output.csv': {
             'format': 'csv',
             'overwrite': False,  # Set to False to append data to the existing file
         },
     }
     ```

3. Save the `houzz_scraper/spiders/houzz_spider.py` file with your changes.

Now, your scraper will start with the modified `start_urls` and follow the settings you've configured in the `custom_settings` dictionary.

4. Start the scraper using the following command:

   ```bash
   scrapy crawl houzz_scraper
   ```

5. The scraper will begin extracting information from Houzz.com business websites and store it in a CSV file.

You can now use this data for your intended purposes, such as analysis, data processing, or any other creative project.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository to your own GitHub account.

2. Clone the forked repository to your local machine.

3. Create a new branch with a descriptive name for your feature or bug fix.

4. Make your changes and commit them.

5. Push your branch to your GitHub repository.

6. Create a pull request to the main repository, explaining your changes and improvements.

We welcome your contributions and ideas to make this project even better!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for using the Houzz.com Scraper! Happy web scraping and data extraction! If you have any questions or need assistance, feel free to open an issue or contact the maintainers.
