import urllib.request
from bs4 import BeautifulSoup

# Replace this URL with your own URL
url = 'http://py4e-data.dr-chuck.net/comments_1980846.html'

try:
    html = urllib.request.urlopen(url).read()
except Exception as e:
    print(f"Error fetching URL: {e}")
    exit()

soup = BeautifulSoup(html, 'html.parser')

# Find all span tags and calculate the sum of numbers
tags = soup.find_all('span')
total_sum = 0
count = 0

for tag in tags:
    try:
        number = int(tag.text)
        total_sum += number
        count += 1
    except ValueError:
        print(f"Skipping non-integer value: {tag.text}")
        continue

print("Count", count)
print("Sum", total_sum)
