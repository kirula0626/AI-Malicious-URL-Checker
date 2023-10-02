import numpy as np
import tensorflow as tf
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences

# Sample paragraphs and corresponding URLs with additional complexity
paragraphs = [
    "Visit our website: http://www.example-site.com for more details.",
    "Check out this product on our e-commerce platform: https://shop.example-store.com/product123.",
    "For news and updates, follow us on Twitter: @example_twitter and visit our blog at https://blog.example-company.org.",
    "Join our community forum: https://community.example-forum.net/discussion/1234.",
    "Explore the world with our travel app: https://travel.example-app.io.",
    "Click here for the latest video: https://www.youtube.com/watch?v=exampleVideo123.",
    "Learn new skills with our online courses: https://courses.example-education.com/course123.",
    "Need help? Reach out to our support team: support@example-service.com or visit https://support.example-service.com.",
    "Visit our secure portal for sensitive information: https://secure.example-portal.net/login.",
    "This paragraph contains no URLs."
]

urls = [
    ["http://www.example-site.com"],
    ["https://shop.example-store.com/product123"],
    ["https://blog.example-company.org", "https://twitter.com/example_twitter"],
    ["https://community.example-forum.net/discussion/1234"],
    ["https://travel.example-app.io"],
    ["https://www.youtube.com/watch?v=exampleVideo123"],
    ["https://courses.example-education.com/course123"],
    ["support@example-service.com", "https://support.example-service.com"],
    ["https://secure.example-portal.net/login"],
    []  # An empty list for a paragraph without links
]

# Tokenize and preprocess the paragraphs
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(paragraphs)
sequences = tokenizer.texts_to_sequences(paragraphs)
word_index = tokenizer.word_index
maxlen = 200  # Max length of input paragraph
data = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=maxlen)

# Create labels for URL presence (binary classification)
max_num_urls = max(len(url_list) for url_list in urls)
labels = []
for paragraph, paragraph_urls in zip(paragraphs, urls):
    label = [1 if url in paragraph else 0 for url in paragraph_urls]
    label += [0] * (max_num_urls - len(label))
    labels.append(label)

labels = np.array(labels)

# Build and compile the model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Embedding(len(word_index) + 1, 128, input_length=maxlen))
model.add(tf.keras.layers.LSTM(64))
model.add(tf.keras.layers.Dense(max_num_urls, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(data, labels, epochs=100, batch_size=2)

# Now you can use the trained model to make predictions on new paragraphs and extract URLs.

# Assuming you have already trained and have the 'model' object

# New paragraphs for which you want to extract URLs
new_paragraphs = [
    "Visit our website: http://www.example-site.com for more details.",
    "Check out this product on our e-commerce platform: https://shop.example-store.com/product123.",
    "For news and updates, follow us on Twitter: @example_twitter and visit our blog at https://blog.example-company.org.",
    "Join our community forum: https://community.example-forum.net/discussion/1234.",
    "Explore the world with our travel app: https://travel.example-app.io.",
    "Click here for the latest video: https://www.youtube.com/watch?v=exampleVideo123.",
    "Learn new skills with our online courses: https://courses.example-education.com/course123.",
    "Need help? Reach out to our support team: support@example-service.com or visit https://support.example-service.com.",
    "Visit our secure portal for sensitive information: https://secure.example-portal.net/login.",
    
]

# Tokenize and preprocess the new paragraphs
new_sequences = tokenizer.texts_to_sequences(new_paragraphs)
new_data = tf.keras.preprocessing.sequence.pad_sequences(new_sequences, maxlen=maxlen)

# Make predictions using the trained model
predictions = model.predict(new_data)

# Threshold for considering a URL prediction
threshold = 0.5

# Padding URLs list to match prediction length
urls_padded = [url_list + [''] * (len(prediction) - len(url_list)) for url_list, prediction in zip(urls, predictions)]

# Extract URLs based on predictions
extracted_urls = []
for i, prediction in enumerate(predictions):
    print(f"Length of URLs for paragraph {i}: {len(urls_padded[i])}")
    print(f"Length of predictions for paragraph {i}: {len(prediction)}")
    min_length = min(len(urls_padded[i]), len(prediction))
    urls_in_paragraph = [urls_padded[i][j] for j in range(min_length) if prediction[j] > threshold]
    extracted_urls.append(urls_in_paragraph)

# Print extracted URLs
for i, urls in enumerate(extracted_urls):
    print(f"Extracted URLs from paragraph {i + 1}:")
    for url in urls:
        print(url)

