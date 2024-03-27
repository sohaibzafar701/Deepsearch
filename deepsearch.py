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
    The author is not responsible for any misuse of DeepSearch 
    in this world and the next. 
    Stay Blessed. 
'''

# Define constants
DEEPSEARCH_API = "https://ahmia.fi/search/?q="
REQUESTS_SUCCESS_CODE = 200
MIN_DATA_RETRIEVE_LENGTH = 1

# deepsearch_api = "https://ahmia.fi/search/?q="
# proxy_api = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=elite"


#colors
class Colors:
    # Console colors
    W = '\033[0m'  # white (normal)
    R = '\033[31m'  # red
    G = '\033[32m'  # green
    O = '\033[33m'  # orange
    B = '\033[34m'  # blue
    P = '\033[35m'  # purple
    C = '\033[36m'  # cyan
    GR = '\033[37m'  # gray
    BOLD = '\033[1m'  # bold
    END = '\033[0m'  # reset

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


class Platform(object):

    def __init__(self, execpltf):
        self.execpltf = execpltf

    def operating_system(self):
        clr = Colors()
    
        print(clr.BOLD + "Starting Services in:", clr.G + sys.platform + clr.END )
        return
        operating_system()

    def clean_screen(self):
        if self.execpltf:
            if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
                os.system('clear')
            else: os.system('cls')
        else: pass




# Function to perform the search
def DEEPSEARCH(query, amount, use_proxy=False):
    
    clr = Colors()
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
                print(f"[{i + 1}]Website: {descriptions[i]}\n{clr.R}Onion Link: {clr.G} {urls[i]}\n\n" + clr.END)
        else:
            print("[!] No results found.")
    else:
        print("[!] Failed to retrieve search results.")


# Main function
def main():
    clr = Colors() 
    bn = Banner() 

    Platform(True).clean_screen()
    Platform(True).operating_system()
    bn.LoadDeepSearchBanner()
    print(clr.O + note + clr.END)
    time.sleep(1.3)

    parser = argparse.ArgumentParser(description= clr.G + "DeepSearch is a tool for searching the deep web for specific keywords.")
    parser.add_argument("-q", "--query", help="the keyword or string you want to search on the deep web", type=str)
    parser.add_argument("-a", "--amount", help="the amount of results you want to retrieve (default: 5)", type=int)
    parser.add_argument("-p", "--proxy", help="use DEEPSEARCH proxy to increase anonymity", action="store_true") 
    
    # Parse the arguments
    args = parser.parse_args()

    # Check if query is provided, if not, ask the user to enter it
    if not args.query:
        args.query = input(clr.B + "Enter the keyword or string you want to search on the deep web: " + clr.END)

    # Check if amount is provided, if not, ask the user to enter it
    if args.amount is None:
        try:
            args.amount = int(input(clr.B + "Enter the amount of results you want to retrieve (default: 5): " + clr.END))
        except ValueError:
            args.amount = 5

    print(clr.B + "Searching for:", args.query + clr.END)
    print(clr.B + "Showing", args.amount, "results...\n" + clr.END)

    DEEPSEARCH(args.query, args.amount, args.proxy)


if __name__ == "__main__":
    main()
