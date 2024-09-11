# Web-Scraper

A simple web scraper built using Python and Flask to extract email addresses from user-provided URLs (up to 5 URLs). The application crawls all pages within the domain, saves the scraped emails in a CSV file, and automatically downloads the file via the browser.

## Features
* Accepts up to 5 URLs for email scraping
* Cralws all pages and subdomains within each domain
* Automatically downloads the scraped emails as a CSV file
* Real-time loading bar and logs during the scraping process
* Simple and user-friendly interface for non-programmers

## Crawler
* Identifies and extracts emails using pattern matching
* Parses Sitemap if it exists
* Follows links within the same domain to discover subpages
* Handle JavaScript-based pages with libraries like Selenium or Playwright
* Manage cookie blocks and sessions during scraping
* Rotate user agents and proxies to prevent IP blocking
* Option to respect or bypass the restrictions based on the user's preference
* Implement delays between requests to avoid being blocked
* Concurrently scrape multiple URLs for efficiency
* Pagination handling for websites with long lists of pages
* Use headless browsers like Selenium to simulate a real browser session and bypass bot detection
* Randomize delay between requests to avoid detection and blocking

* Real-time progress bar to show scraping status
* Log display for each step of the scraping progress
