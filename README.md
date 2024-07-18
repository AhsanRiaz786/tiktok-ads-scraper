# TikTok Ads Scraper

This is a tool for scraping TikTok ads data using Playwright and Python. The tool logs into TikTok Ads, scrapes data for specified brands, and saves the data to an Excel file. It also downloads the ad videos.

## Features
- Login to TikTok Ads
- Scrape ads data for specified brands
- Save data to an Excel file
- Download ad videos

## Installation

1. **Clone the repository:**
   ```sh
   git clonehttps://github.com/AhsanRiaz786/tiktok-ads-scraper.git/
   cd tiktok-ads-scraper

2. **Create a virtual environment and activate it:**
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install dependencies:**
    ```
    pip install -r requirements.txt

4. **Install Playwright and its browser dependencies:**
    ```
    playwright install

## Usage

1. **Run the application:**
    ```
    python main.py

2. **Login:**

    If this is your first time using the tool, click the "Login" button and enter your TikTok Ads credentials.
    After a successful login, your session will be saved, and you won't need to log in again unless the session expires.

3. **Scrape Ads:**

    Click the "Scrape Ads" button.
    Select the Excel file containing the list of brands you want to scrape data for.
    The scraping process will start, and you will see progress updates on the screen.
    Once completed, the data will be saved to an Excel file named tiktok_ads_data.xlsx in the project directory.

