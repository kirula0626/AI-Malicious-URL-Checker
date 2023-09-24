#!/usr/bin/env python
"""
This file gathers data to be used for pre-processing in training and prediction.
"""
import pandas as pd

def main():
    urls = {}

    blacklist_file = 'phishing_database.csv'
    whitelist_file = 'whitelist.txt'

    try:
        blacklist = pd.read_csv(blacklist_file)
        
        # Assign 0 for non-malicious and 1 as malicious for supervised learning.
        for url in blacklist['url']:
            urls[url] = 1
    except FileNotFoundError:
        print(f"Error: {blacklist_file} not found. Make sure the file exists.")

    try:
        with open(whitelist_file, 'r') as f:
            lines = f.read().splitlines()
            for url in lines:
                urls[url] = 0
    except FileNotFoundError:
        print(f"Error: {whitelist_file} not found. Make sure the file exists.")

    return urls

if __name__ == "__main__":
    data = main()
    print(f"Total URLs collected: {len(data)}")
