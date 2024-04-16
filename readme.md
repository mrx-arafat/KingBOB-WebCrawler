# KingBOB Web Crawler

Welcome to the KingBOB Web Crawler repository. This Python script allows systematic browsing and extraction of links from websites up to a specified depth. It is ideal for SEO analysis, site audit, and exploring web structures.

## Features

- **Multithreading**: Speeds up the crawling process by utilizing multiple threads.
- **Configurable Depth**: Users can specify how deep the crawler should go into the website.
- **Custom HTTP Headers**: Supports passing custom headers for HTTP requests.
- **Flexible Output**: Options to output results in plain text or JSON format.
- **Detailed Link Information**: Shows the source tag and the exact page of each discovered link.

## Prerequisites

Make sure you have Python 3.8 or higher installed. If not, download it from [Python&#39;s official site](https://www.python.org/downloads/).

Required Python packages:

```bash
pip install requests beautifulsoup4
```

## Usage

To run the web crawler, you can use the command line to pass URLs into the script. Here's how to execute the crawler with basic settings:

```
echo "http://example.com" | python crawler.py
```

### Command Line Arguments

- `-d` or `--depth`: Specifies the crawling depth (default is 1).
- `-H` or `--headers`: Allows custom headers for HTTP requests, formatted as a string separated by semicolons.
- `--json`: Outputs the results in JSON format.
- `-s` or `--source`: Indicates whether to show the HTML source of each link.
- `-w` or `--where`: Indicates the page URL where each link is found.
- `-t` or `--threads`: Determines the number of threads to use for crawling (default is 4).

### Detailed Run Example

Run the crawler starting from "http://example.com", at a depth of 2, using 4 threads, with output in JSON format:

```
echo "http://example.com" | python crawler.py --depth 2 --threads 4 --json
```
