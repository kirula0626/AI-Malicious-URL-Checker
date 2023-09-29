from urllib.parse import urlparse
import subprocess

# Function to extract URLs from a paragraph using urllib.parse
def extract_urls(paragraph):
    # Split the paragraph into words and check each word as a potential URL
    words = paragraph.split()
    urls = []
    for word in words:
        parsed_url = urlparse(word)
        if parsed_url.scheme and parsed_url.netloc:
            urls.append(word)
    return urls

# Predefined paragraph with various types of URLs
paragraph_with_urls = """
 In today's digital age, the internet has become an indispensable part of our lives. We use it for everything from education to entertainment, from communication to commerce. Here are 1000 words on the marvels of the internet, peppered with diverse examples of URLs from around the world.

Exploring the World Wide Web

The World Wide Web, often simply called the web, is a vast system of interlinked hypertext documents accessed via the internet. It has transformed how we gather information, connect with people, and conduct business.

One of the earliest and most influential websites is the http://info.cern.ch, which was the world's first-ever website. Created by Sir Tim Berners-Lee, this site marks the beginning of our online journey.

Educational Resources

Education has been revolutionized by the internet. Online learning platforms like https://www.coursera.org and https://www.edx.org offer courses from universities worldwide. Students can enhance their knowledge at their own pace.

Connecting People

Social media platforms have brought people from different corners of the world together. https://www.facebook.com allows us to connect with friends and family, sharing our lives through posts and photos. For professional networking, https://www.linkedin.com is the go-to platform.

E-Commerce

Online shopping has witnessed an exponential rise, with sites like https://www.amazon.com offering a vast array of products. For handmade and unique items, https://www.etsy.com is a haven for artisans and craft enthusiasts.

Entertainment Galore

YouTube, a platform for sharing and viewing videos, has become a household name. Many talented content creators showcase their skills here. https://www.youtube.com has indeed redefined entertainment.

Travel and Exploration

When it comes to travel, https://www.booking.com helps in finding accommodations worldwide. If you're an adventurer seeking authentic experiences, https://www.airbnb.com offers unique stays hosted by locals.

Staying Informed

For news from around the globe, https://www.bbc.com provides comprehensive coverage. Additionally, https://edition.cnn.com keeps us updated on the latest events, making sure we are never out of the loop.

Culinary Adventures

Food lovers can rejoice with platforms like https://www.allrecipes.com/llfvejbfgvbvgfva, offering a plethora of recipes catering to various cuisines. Craving restaurant food at home? https://www.ubereats.com delivers your favorite meals to your doorstep.

Health and Wellness

Taking care of our health is easier with apps like https://www.myfitnesspal.com, helping us track our meals and workouts. For mental health support, https://www.betterhelp.com offers online therapy sessions.

Conclusion

The internet, with its myriad of URLs, has undoubtedly transformed our lives. It has bridged gaps, opened doors to new opportunities, and brought the world to our fingertips. As we continue to surf the web, discovering new URLs and exploring the endless possibilities, let's do so responsibly, making the most of this incredible digital age.


"""

# Extract URLs from the input paragraph using urllib.parse
extracted_urls = extract_urls(paragraph_with_urls)

# Print extracted URLs
print("Extracted URLs:")
for url in extracted_urls:
    print(url)

for url in extracted_urls:
    try:
        # Call request.py script with the extracted URL as a command-line argument
        result = subprocess.run(["python", "request.py", "-u", url], capture_output=True, text=True)
        output = result.stdout.strip()  # Get the output from the subprocess
        print(f"Phishing probability for {url}: {output}")
    except Exception as e:
        print(f"Error processing URL {url}: {e}")