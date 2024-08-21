import urllib.request
from bs4 import BeautifulSoup

def find_last_name(url, count, position):
    # Start at the initial URL
    for _ in range(count):
        # Fetch the HTML content from the URL
        html = urllib.request.urlopen(url).read()
        
        # Parse the HTML content
        soup = BeautifulSoup(html, 'html.parser')
        
        # Find all anchor tags
        tags = soup('a')
        
        # Check if the position is valid
        if position > len(tags) or position < 1:
            print("Position is out of range.")
            return
        
        # Find the URL at the given position
        url = tags[position - 1].get('href', None)
        
        # Print the current URL being retrieved
        print("Retrieving:", url)
    
    # Print the final URL which contains the last name
    print("The answer to the assignment is:", url.split('_')[-1].replace('.html', ''))

# Input parameters for the assignment
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Find and print the last name
find_last_name(url, count, position)