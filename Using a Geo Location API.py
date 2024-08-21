import urllib.request
import urllib.parse
import json

def main():
    # Prompt the user for the location
    location = input('Enter location: ')
    
    # URL encode the location parameter
    params = {'q': location}
    url = 'http://py4e-data.dr-chuck.net/opengeo?' + urllib.parse.urlencode(params)
    
    try:
        # Retrieve the JSON data from the URL
        print(f'Retrieving {url}')
        response = urllib.request.urlopen(url)
        data = response.read().decode()
        print(f'Retrieved {len(data)} characters')
        
        # Parse the JSON data
        js = json.loads(data)
        
        # Debugging: Print the parsed JSON to check structure
        print('Parsed JSON data:')
        print(js)
        
        # Extract the plus_code
        features = js.get('features', [])
        if features:
            properties = features[0].get('properties', {})
            plus_code = properties.get('plus_code', 'No plus_code found')
        else:
            plus_code = 'No plus_code found'
        
        print(f'Plus code {plus_code}')
        
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
    