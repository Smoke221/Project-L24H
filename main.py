from bs4 import BeautifulSoup
import requests


url = 'https://timesofindia.indiatimes.com/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find a common parent or container element
    containers = soup.find_all('div')  # Adjust 'div' to the actual parent/container element
    print(containers)
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')