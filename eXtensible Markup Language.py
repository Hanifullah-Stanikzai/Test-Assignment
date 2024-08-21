import urllib.request
import xml.etree.ElementTree as ET

# Prompt for URL
url = input('Enter location: ')
print('Retrieving', url)

# Open URL and read XML data
response = urllib.request.urlopen(url)
data = response.read()
print('Retrieved', len(data), 'characters')

# Parse XML data
tree = ET.fromstring(data)

# Find all 'count' elements
counts = tree.findall('.//count')

# Extract and sum the counts
total = 0
for count in counts:
    total += int(count.text)

# Output results
print('Count:', len(counts))
print('Sum:', total)