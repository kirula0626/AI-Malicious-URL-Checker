import numpy as np
import tensorflow as tf
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences

# Sample paragraphs and corresponding URLs
paragraphs = [
    "This is a sample paragraph with URLs https://www.example1.com and https://www.example2.com.",
    "Another paragraph with a link https://www.example3.com.",
    "One more paragraph without any links."
]

urls = [
    ["https://www.example1.com", "https://www.example2.com"],
    ["https://www.example3.com"],
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

# Build and compile the model (same as before)
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Embedding(len(word_index) + 1, 128, input_length=maxlen))
model.add(tf.keras.layers.LSTM(64))
model.add(tf.keras.layers.Dense(max_num_urls, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(data, labels, epochs=10, batch_size=2)

# Now you can use the trained model to make predictions on new paragraphs and extract URLs.
new_paragraph = ["In today's digital age, the internet plays a pivotal role in our daily lives. We rely on it for various purposes, from staying informed about global events through news websites like https://www.bbc.com to connecting with friends and family on social media platforms such as https://www.facebook.com. Many of us also use it to enhance our knowledge and skills, often enrolling in online courses offered by platforms like https://www.coursera.org."]

# Tokenize and preprocess the new paragraph
new_sequences = tokenizer.texts_to_sequences([new_paragraph])
new_data = tf.keras.preprocessing.sequence.pad_sequences(new_sequences, maxlen=maxlen)

# Make predictions
predictions = model.predict(new_data)

# Threshold the predictions (you can adjust the threshold)
threshold = 0.5
url_present = [int(pred >= threshold) for pred in predictions[0]]

# Extract URLs based on predictions
predicted_urls = [urls[i] for i, is_present in enumerate(url_present) if is_present]

print("Predicted URLs:", predicted_urls)
