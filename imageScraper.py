# An application that connects to a site and pulls all https links,
# saving them to a searchable index file.

# Import HTML request library
import requests
# Import Beautiful Soup for parsing HTML
from bs4 import BeautifulSoup


def URL_input():
    # User inputs a URL
    URL = input('Please enter a URL to find all links that start with https://: ')

    # If the URL does not begin with HTTP, try to add it
    if 'http://' not in URL and 'https://' not in URL:
        URL = 'http://' + URL

    return URL


def get_data(address):
    # Attempt to request info from provided URL
    try:
        page = requests.get(address)
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

        return soup, off_page_links


def write_to_file(data, links, url):
    # Output data to file
    f = open('web_links.txt', 'w')
    f.write(f'URL USED:\n    {url}')
    f.write(f'\nSITE:\n    {data.title.string}')
    f.write('\nLINKS:')
    for link in links:
        f.write('\n    {}'.format(link['href']))
    f.close()

    # Alert user
    print("\nNo errors detected. Please check the current directory for web_links.txt.")

# Run functions
URL = URL_input()
site_data, site_links = get_data(URL)
write_to_file(site_data, site_links, URL)
