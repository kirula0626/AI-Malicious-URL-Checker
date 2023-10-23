import pandas as pd
import requests
import time

VIRUSTOTAL_API_KEY = '8cdc3b3d6b91d294b3f0a8d3fe994a752505d2b320aa55ea15d966086366600b'

# Function to extract URL from a CSV row
def extract_url_from_csv_row(row):
    # Assuming URLs are in the second column and in the specified format
    url = row[1].strip(',')
    return url

# Function to get VirusTotal label for a URL
def get_virustotal_label(url):
    params = {
        'apikey': VIRUSTOTAL_API_KEY,
        'resource': url
    }

    response = requests.get('https://www.virustotal.com/vtapi/v2/url/report', params=params)
    json_response = response.json()

    if json_response['response_code'] == 1:
        if json_response['positives'] > 0:
            return 'Malicious'
        else:
            return 'Non-Malicious'
    else:
        return 'Unknown'

# Main function to process the CSV file
def main():
    blacklist_file = 'phishing_database.csv'
    urls_to_check = 100  # Number of URLs to check
    processed_urls = 0  # Counter for processed URLs

    try:
        blacklist = pd.read_csv(blacklist_file, header=None)  # Read without headers

        # Print URLs along with their labels from VirusTotal
        for index, row in blacklist.iterrows():
            url = extract_url_from_csv_row(row)
            label = get_virustotal_label(url)
            print(f"URL: {url}, Label: {label}")
            processed_urls += 1

            if processed_urls >= urls_to_check:
                break  # Stop processing after 100 URLs

            # Pause for 1 minute after making 4 requests (to comply with the rate limit)
            if processed_urls % 4 == 0:
                print("Waiting for 1 minute to comply with VirusTotal API rate limit...")
                time.sleep(60)  # Pause for 1 minute (60 seconds)

    except FileNotFoundError:
        print(f"Error: {blacklist_file} not found. Make sure the file exists.")

# Call the main function if the script is run
if __name__ == "__main__":
    main()
