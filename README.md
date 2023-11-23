# AI-Malicious-URL-Checker

Requirements
------------

This code was created with Python 3.8 Other versions of Python 3 might also work.  You can have multiple Python
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

GUI START
---------
Open a separate tab or window and run:

    $ python3 GUI_URL_Paragraph_Checker.py

    Output :     
    2023-11-03 00:01:07.718791: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
    To enable the following instructions: SSE SSE2 SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
    * Serving Flask app 'GUI_URL_Paragraph_Checker'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    * Restarting with stat
    2023-11-03 00:01:17.654420: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
    To enable the following instructions: SSE SSE2 SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
    * Debugger is active!
    * Debugger PIN: 926-147-486
    127.0.0.1 - - [03/Nov/2023 00:01:19] "GET / HTTP/1.1" 200 -
    cleaned_urls ['https://www.cisco.com/c/en/us/solutions/enterprise-networks/sd-wan/idc-business-value-white-paper.html?oid=anretr030044', 'https://www.cisco.com/site/us/en/products/networking/sdwan-    routers/catalyst-8200-series-platforms/index.html', 'https://tinyurl.com/megafonedigitalcombr?_user=abc@abc.com.br']
    URL https://www.cisco.com/c/en/us/solutions/enterprise-networks/sd-wan/idc-business-value-white-paper.html?oid=anretr030044
    URL https://www.cisco.com/site/us/en/products/networking/sdwan-routers/catalyst-8200-series-platforms/index.html
    URL https://tinyurl.com/megafonedigitalcombr?_user=abc@abc.com.br
    validated URLs ['https://www.cisco.com/c/en/us/solutions/enterprise-networks/sd-wan/idc-business-value-white-paper.html?oid=anretr030044', 'https://www.cisco.com/site/us/en/products/networking/sdwan-    routers/catalyst-8200-series-platforms/index.html', 'https://tinyurl.com/megafonedigitalcombr?_user=abc@abc.com.br']
    Before subprocess.run
    INCOMING URL https://www.cisco.com/c/en/us/solutions/enterprise-networks/sd-wan/idc-business-value-white-paper.html?oid=anretr030044
    1/1 [==============================] - 4s 4s/step
    127.0.0.1 - - [03/Nov/2023 00:01:33] "POST /predict HTTP/1.1" 200 -
    INCOMING URL https://www.cisco.com/site/us/en/products/networking/sdwan-routers/catalyst-8200-series-platforms/index.html
    1/1 [==============================] - 0s 354ms/step
    127.0.0.1 - - [03/Nov/2023 00:01:36] "POST /predict HTTP/1.1" 200 -
    INCOMING URL https://tinyurl.com/megafonedigitalcombr?_user=abc@abc.com.br
    1/1 [==============================] - 0s 386ms/step
    127.0.0.1 - - [03/Nov/2023 00:01:39] "POST /predict HTTP/1.1" 200 -
    After subprocess.run
    OUTPUT_123 [{'malicious percentage': 0.5930278915911913, 'result': 'URL is probably NOT malicious.', 'url': 'https://www.cisco.com/c/en/us/solutions/enterprise-networks/sd-wan/idc-business-value-white-paper.html?oid=anretr030044'}, {'malicious percentage': 3.097047284245491, 'result': 'URL is probably NOT malicious.', 'url': 'https://www.cisco.com/site/us/en/products/networking/sdwan-routers/catalyst-8200-series-platforms/index.html'}, {'malicious percentage': 94.33512687683105, 'result': 'URL is probably malicious and Dangerous!', 'url': 'https://tinyurl.com/megafonedigitalcombr?_user=abc@abc.com.br'}]
    127.0.0.1 - - [03/Nov/2023 00:01:39] "POST /process_urls HTTP/1.1" 200 -

Screenshot of GUI browser interface 
![GUI](https://github.com/kirula0626/AI-Malicious-URL-Checker/assets/84916544/3cb0c530-19a2-4b70-8acf-5d688d13fbda)
