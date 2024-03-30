IPL Cricket Stats Scraper
This Python script collects statistics and player information from the IPL (Indian Premier League) website for a specific year. It utilizes web scraping techniques with BeautifulSoup and Selenium libraries to extract data from the IPL website.

Features
Retrieves batting statistics for the specified year from the IPL website.
Scrapes player names, images, and profile links.
Saves the collected data into CSV files for further analysis.
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/ipl-cricket-stats-scraper.git
Install the required libraries using pip:

bash
Copy code
pip install -r requirements.txt
Make sure you have Chrome WebDriver installed and it's in your system's PATH.

Usage
Run the script collect_cricinfo.py:

bash
Copy code
python collect_cricinfo.py
The script will open a Chrome browser, scrape the data, and save it into CSV files named ipl201.csv (for statistics) and ipl202.csv (for player information).

File Descriptions
collect_cricinfo.py: Python script to scrape IPL cricket statistics and player information.
requirements.txt: Contains the list of required Python libraries.
README.md: Documentation file providing information about the project.
Contributions
Contributions to improve the functionality, efficiency, or documentation of this project are welcome. Feel free to submit pull requests or open issues for any bugs or feature requests.

License
This project is licensed under the Apache License - see the LICENSE file for details.
