# deepsearch.py

import sys
import os
import time
import argparse
import random
import requests
from bs4 import BeautifulSoup
from banner import Banner

note = '''
Note: 
    This tool is not to be used for illegal purposes.
    The author is not responsible for any misuse of DeepSearch. 
'''

# Define constants
DEEPSEARCH_API = "https://ahmia.fi/search/?q="
REQUESTS_SUCCESS_CODE = 200
MIN_DATA_RETRIEVE_LENGTH = 1

# Function to retrieve user agent headers
def get_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    ]
    return random.choice(user_agents)




class Configuration:
    DARKDUMP_ERROR_CODE_STANDARD = -1
    DARKDUMP_SUCCESS_CODE_STANDARD = 0

    DARKDUMP_MIN_DATA_RETRIEVE_LENGTH = 1
    DARKDUMP_RUNNING = False
    DARKDUMP_OS_UNIX_LINUX = False
    DARKDUMP_OS_WIN32_64 = False
    DARKDUMP_OS_DARWIN = False

    DARKDUMP_REQUESTS_SUCCESS_CODE = 200
    DARKDUMP_PROXY = False

    descriptions = []
    urls = []

    __deepsearch_api__ = "https://ahmia.fi/search/?q="
    __proxy_api__ = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=elite"

class Platform(object):
    def __init__(self, execpltf):
        self.execpltf = execpltf

    def get_operating_system_descriptor(self):
        cfg = Configuration()



    def clean_screen(self):
        cfg = Configuration()
        if self.execpltf:
            if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
                os.system('clear')
            else: os.system('cls')
        else: pass




# Function to perform the search
def darkdump(query, amount, use_proxy=False):
    headers = {'User-Agent': get_user_agent()}
    proxies = None
    
    if use_proxy:
        # You can implement proxy assignment logic here if needed
        pass

    response = requests.get(DEEPSEARCH_API + query, headers=headers, proxies=proxies)

    if response.status_code == REQUESTS_SUCCESS_CODE:
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find(id='ahmiaResultsPage')
        second_results = results.find_all('li', class_='result')
        
        descriptions = []
        urls = []

        for result in second_results:
            description = result.find('p').text
            url = result.find('cite').text
            descriptions.append(description)
            urls.append(url)

        # Remove duplicates
        descriptions = list(set(descriptions))
        urls = list(set(urls))

        if len(descriptions) >= MIN_DATA_RETRIEVE_LENGTH:
            for i in range(min(amount, len(descriptions))):
                print(f"[+] Website: {descriptions[i]}\n\t> Onion Link: {urls[i]}\n")
        else:
            print("[!] No results found.")
    else:
        print("[!] Failed to retrieve search results.")

# Main function
def main():
    cfg = Configuration()
    bn = Banner() 

    Platform(True).clean_screen()
    Platform(True).get_operating_system_descriptor()
    bn.LoadDeepSearchBanner()
    print(note)
    time.sleep(1.3)
    parser = argparse.ArgumentParser(description="DeepSearch is a tool for searching the deep web for specific keywords.")
    parser.add_argument("-q", "--query", help="the keyword or string you want to search on the deep web", type=str, required=True)
    parser.add_argument("-a", "--amount", help="the amount of results you want to retrieve (default: 10)", type=int, default=5)
    parser.add_argument("-p", "--proxy", help="use darkdump proxy to increase anonymity", action="store_true")
    
    args = parser.parse_args()

    print("Searching for:", args.query)
    print("Showing", args.amount, "results...\n")

    darkdump(args.query, args.amount, args.proxy)

if __name__ == "__main__":
    main()
