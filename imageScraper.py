# An application that connects to a site and pulls all https links,
# saving them to a searchable index file.

# Import HTML request library
import requests
# Import Beautiful Soup for parsing HTML
from bs4 import BeautifulSoup

# User inputs a URL
URL = input('Please enter a URL to find all links that start with https://: ')

# If the URL does not begin with HTTP, try to add it
if 'http://' not in URL and 'https://' not in URL:
    URL = 'http://' + URL

# Attempt to request info from provided URL
try:
    page = requests.get(URL)
except:
    print('URL invalid.')
else:
    # Use BS to parse content
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find all 'a' tags
    results = soup.findAll("a")

    # Define link list to hold info
    off_page_links = []

    # Add the href of every link beginning with 'https://' to list
    for link in results:
        if 'https://' in link.attrs['href']:
            off_page_links.append({'href':link.attrs['href']})


    print(soup.title.string)
    for link in off_page_links:
        print(link['href'])
