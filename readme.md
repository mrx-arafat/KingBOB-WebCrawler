# Web Crawler in Python

This project contains a Python script for a web crawler that systematically browses and extracts links from websites up to a specified depth. It is built using Python and employs libraries such as `requests` for making HTTP requests and `BeautifulSoup` for parsing HTML.

## Features

- **Multithreading**: Utilizes multiple threads to speed up the crawling process.
- **Custom Depth**: Allows the user to specify the depth of the crawl.
- **Custom Headers**: Supports custom HTTP headers for requests.
- **Output Formatting**: Provides options for JSON output and details about the source and location of each link.
- **User-Agent Configuration**: Can be set to mimic different devices/browsers.

## Getting Started

### Prerequisites

Ensure Python 3.8 or higher is installed on your machine. You can download it from [Python&#39;s official site](https://www.python.org/downloads/).

You will also need the following Python packages:

```bash
pip install requests beautifulsoup4
```
