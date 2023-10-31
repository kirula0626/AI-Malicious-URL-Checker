#!/usr/bin/env python
"""
This file will make a simple request to the Flask API for URL processing.
"""
import argparse
import requests
import validators

def main(url_list):
    # Check if the URL starts with "http://" or "https://", and add "http://" if not.

    responses = []
    for url in url_list:
        # Check if the URL is valid.
        # if not validators.url(url):
        #     print("Invalid URL format. Please provide a valid URL.")
        #     return -1
        


        # Define URL for Flask API endpoint.
        KERAS_REST_API_URL = "http://127.0.0.1:5000/predict"

        # Set the payload to JSON format.
        payload = {"url": url}

        try:
            # Submit the POST request.
            r = requests.post(KERAS_REST_API_URL, json=payload)
            r.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)

            response = r.json()

            # Ensure the request was successful.
            if response["success"]:
                # Extract and display specific information from the response.
                predictions = response['predictions']
                # print(predictions[0])
                responses.append(predictions[0])
                # for prediction in predictions:
                #     print(prediction)
            else:
                print("Request failed")

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
    
    print(responses)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Make a request to the Flask API for URL processing.')
    parser.add_argument(
        '-u',
        dest='urls',
        action='store',
        nargs='+',  # Accept multiple URLs
        required=True,
        help="The URL(s) to be processed."
    )

    args = parser.parse_args()

    main(args.urls)  # Pass the list of URLs to the main function