

import requests

API_KEY = '8cdc3b3d6b91d294b3f0a8d3fe994a752505d2b320aa55ea15d966086366600b'
url_to_check = 'https://verfolgen.sie.die.paketdetails.4-232-168-189.cprapid.com/dpd/update.php'

params = {
    'apikey': API_KEY,
    'resource': url_to_check
}\

response = requests.get('https://www.virustotal.com/vtapi/v2/url/report', params=params)
json_response = response.json()

# Check the response from VirusTotal
if json_response['response_code'] == 1:
    # The URL was scanned before
    if json_response['positives'] > 0:
        print('The URL is malicious!')
    else:
        print('The URL is not malicious.')
else:
    print('Error occurred while scanning the URL.')
