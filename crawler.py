import requests
from bs4 import BeautifulSoup
import argparse
from urllib.parse import urljoin, urlparse
import threading
import queue
import sys
import json

def extract_hostname(url):
    try:
        return urlparse(url).hostname
    except Exception as e:
        raise ValueError("Invalid URL") from e

def parse_headers(raw_headers):
    headers = {}
    if raw_headers:
        for part in raw_headers.split(";;"):
            if ':' in part:
                key, value = part.split(':', 1)
                headers[key.strip()] = value.strip()
    return headers

def crawl(url, depth, headers, show_json, show_source, show_where):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links:
            href = link['href']
            abs_link = urljoin(url, href)
            if show_json:
                result = json.dumps({"source": "href", "URL": abs_link, "Where": url if show_where else ""})
            else:
                source = f"[href] " if show_source else ""
                where = f"[{url}] " if show_where else ""
                result = f"{where}{source}{abs_link}"
            print(result)
            if depth > 1:
                crawl(abs_link, depth-1, headers, show_json, show_source, show_where)
    except Exception as e:
        print(f"Error crawling {url}: {str(e)}", file=sys.stderr)

def worker(url_queue, depth, headers, show_json, show_source, show_where):
    while True:
        url, depth = url_queue.get()
        if url is None:
            break
        crawl(url, depth, headers, show_json, show_source, show_where)
        url_queue.task_done()

def main():
    parser = argparse.ArgumentParser(description="Simple Web Crawler")
    parser.add_argument('-d', '--depth', type=int, default=1, help="Depth to crawl.")
    parser.add_argument('-H', '--headers', type=str, help="Custom headers separated by two semi-colons.")
    parser.add_argument('--json', action='store_true', help="Output as JSON.")
    parser.add_argument('-s', '--source', action='store_true', help="Show the source of URL.")
    parser.add_argument('-w', '--where', action='store_true', help="Show at which link the URL is found.")
    parser.add_argument('-t', '--threads', type=int, default=4, help="Number of threads to utilise.")
    args = parser.parse_args()

    headers = parse_headers(args.headers)
    urls = [line.strip() for line in sys.stdin if line.strip()]

    url_queue = queue.Queue()
    threads = []

    for url in urls:
        url_queue.put((url, args.depth))

    for _ in range(args.threads):
        thread = threading.Thread(target=worker, args=(url_queue, args.depth, headers, args.json, args.source, args.where))
        thread.start()
        threads.append(thread)

    url_queue.join()

    for _ in range(args.threads):
        url_queue.put((None, None))

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
