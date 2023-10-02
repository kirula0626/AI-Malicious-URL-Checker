from urllib.parse import urlparse
import subprocess
import time

def extract_urls(paragraph):
    # Split the paragraph into words and check each word as a potential URL
    words = paragraph.split()
    allowed_special_chars = "@/,.:="  # Allow "@" and "/"
    urls = []
    for word in words:
        # Remove special characters except "@" and "/"
        cleaned_word = ''.join(char for char in word if char.isalnum() or char in allowed_special_chars)
         #Remove trailing period if it exists
        cleaned_word = cleaned_word.rstrip('.')
        parsed_url = urlparse(cleaned_word)
        if parsed_url.scheme and parsed_url.netloc:
            urls.append(cleaned_word)
    return urls


# Predefined paragraph with various types of URLs

paragraph_with_urls = """
 "Visit our website: http://www.example-site.com for more details.",
    "Check out this product on our e-commerce platform: https://shop.example-store.com/product123/ For news and updates, follow us on Twitter: @example_twitter and visit our blog at https://blog.example-company.org/.",
    "Join our community forum: https://community.example-forum.net/discussion/1234/    dsq.",
    "Explore the world with our travel app: https://travel.example-app.io/  cscs.",
    "Click here for the latest video: https://www.youtube.com/watch?v=9H_kz71MGwE/ CDWW.",
    "Learn new skills with our online courses: https://courses.example-education.com/course123/.",
    "Need help? Reach out to our support team: support@example-service.com or visit https://support.example-service.com/.",
    "Visit our secure portal for sensitive information: https://secure.example-portal.net/login/.",
    

"""

# Extract URLs from the input paragraph using urllib.parse
extracted_urls = extract_urls(paragraph_with_urls)

# Print extracted URLs
print("Extracted URLs:")
for url in extracted_urls:
    print(url)

# Time to wait between requests (in seconds)
wait_time = 5  # You can adjust this value according to your needs

for url in extracted_urls:
    try:
        # Call request.py script with the extracted URL as a command-line argument
        result = subprocess.run(["python", "request.py", "-u", url], capture_output=True, text=True)
        output = result.stdout.strip()  # Get the output from the subprocess
        print(f"\nPhishing probability for {url}: {output}\n\n")

        # Wait for the specified duration before making the next request
        time.sleep(wait_time)

    except Exception as e:
        print(f"Error processing URL {url}: {e}")