# Sample new paragraph
import urltrain
new_paragraph = "This is a new paragraph with a URL https://www.example4.com."

# Tokenize and preprocess the new paragraph
new_sequences = tokenizer.texts_to_sequences([new_paragraph])
new_data = pad_sequences(new_sequences, maxlen=maxlen)

# Make predictions
predictions = model.predict(new_data)

# Threshold the predictions (you can adjust the threshold)
threshold = 0.5
url_present = [int(pred >= threshold) for pred in predictions[0]]

# Extract URLs based on predictions
predicted_urls = [urls[i] for i, is_present in enumerate(url_present) if is_present]

print("Predicted URLs:", predicted_urls)
