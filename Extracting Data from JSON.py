import urllib.request
import json

def main():
    # Prompt the user for the URL
    url = input('Enter location: ')
    
    try:
        # Retrieve the JSON data from the URL
        print(f'Retrieving {url}')
        response = urllib.request.urlopen(url)
        data = response.read().decode()
        print(f'Retrieved {len(data)} characters')
        
        # Parse the JSON data
        js = json.loads(data)
        
        # Extract the counts
        counts = js['comments']
        
        # Calculate the sum of all count values
        total_sum = 0
        for comment in counts:
            total_sum += comment['count']
        
        # Output the count and sum
        print(f'Count: {len(counts)}')
        print(f'Sum: {total_sum}')
        
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()