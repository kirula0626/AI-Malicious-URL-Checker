# AI-Phishing

Requirements
------------

This code was created with Python 3.6.7. Other versions of Python 3 might also work.  You can have multiple Python
versions (2.x and 3.x) installed on the same system without problems.

Make sure to install all requirements:

    $ pip install -r requirements.txt


Quick start
-----------

Ensure the model has been downloaded from the above link.

Open a separate tab or window and run:

    $ python3 flaskrestapi.py

Now go back to the original tab or window and run:

    $ python3 request.py -u https://www.google.com/about

    Output:

    $ [{'malicious percentage': 2.552182786166668, 'result': 'URL is probably NOT malicious.', 'url': 'https://www.google.com/about'}]
