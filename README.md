# TikTok Ads Scraper

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Playwright](https://img.shields.io/badge/playwright-latest-red.svg)

A powerful tool for scraping TikTok ads data using Playwright and Python. This tool provides a user-friendly GUI to log into TikTok Ads Manager, scrape comprehensive ad data for specified brands, and save the results to Excel files with automatic video downloads.

## ✨ Features

- 🔐 **Secure Login**: Automated login to TikTok Ads Manager with session persistence
- 📊 **Comprehensive Data Scraping**: Extract detailed ad performance metrics including:
  - Industry and brand information
  - Ad captions and creative content
  - Performance metrics (likes, comments, shares, CTR)
  - Budget information
  - Landing page URLs
- 📹 **Video Downloads**: Automatically download ad videos to local storage
- 📱 **User-Friendly GUI**: Intuitive interface built with Tkinter
- 📈 **Excel Export**: Save all scraped data to organized Excel files
- 🔄 **Progress Tracking**: Real-time progress updates during scraping operations

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AhsanRiaz786/tiktok-ads-scraper.git
   cd tiktok-ads-scraper
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**
   ```bash
   playwright install chromium
   ```

### Usage

1. **Start the application:**
   ```bash
   python main.py
   ```

2. **First-time setup:**
   - Click the "Login" button
   - Enter your TikTok Ads Manager credentials
   - Your session will be saved for future use

3. **Scraping ads:**
   - Click "Scrape Ads"
   - Select an Excel file containing brand names (see [Input Format](#input-format))
   - Monitor progress in real-time
   - Results will be saved as `tiktok_ads_data.xlsx`

### Input Format

Your Excel file should contain a column named "Brand Name" with the brands you want to scrape:

| Brand Name |
|------------|
| Nike       |
| Adidas     |
| Apple      |

## 📂 Output Structure

The tool generates:
- `tiktok_ads_data.xlsx`: Comprehensive ad data in Excel format
- `videos/`: Directory containing downloaded ad videos
- `state.json`: Saved login session (auto-generated)

## 🛠️ Technical Details

- **Browser Automation**: Uses Playwright with Chromium for reliable scraping
- **Data Processing**: Pandas for efficient data manipulation and Excel export
- **GUI Framework**: Tkinter for cross-platform compatibility
- **Async Operations**: Threading for non-blocking UI during scraping

## 📋 Requirements

See [`requirements.txt`](requirements.txt) for a complete list of dependencies.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and contribute to the project.

## 🔒 Security

If you discover a security vulnerability, please see our [Security Policy](SECURITY.md) for instructions on responsible disclosure.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is intended for educational and research purposes only. Users are responsible for ensuring compliance with TikTok's Terms of Service and applicable laws. The developers are not responsible for any misuse of this tool.

## 🐛 Issues and Support

- Found a bug? [Open an issue](https://github.com/AhsanRiaz786/tiktok-ads-scraper/issues)
- Have a feature request? [Start a discussion](https://github.com/AhsanRiaz786/tiktok-ads-scraper/discussions)
- Need help? Check our [FAQ](https://github.com/AhsanRiaz786/tiktok-ads-scraper/wiki/FAQ) or open an issue

## 🙏 Acknowledgments

- Built with [Playwright](https://playwright.dev/) for robust browser automation
- Data processing powered by [Pandas](https://pandas.pydata.org/)
- UI created with Python's built-in [Tkinter](https://docs.python.org/3/library/tkinter.html)

