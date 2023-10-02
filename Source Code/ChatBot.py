import nltk
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize
from docx import Document

full_doc = Document('Alexander.docx')

full_text_content = []
for paragraph in full_doc.paragraphs:
    full_text_content.append(paragraph.text)
full_doc_text = '\n'.join(full_text_content)

# Tokenize the text into sentences
sentences = sent_tokenize(full_doc_text)

# Tokenize sentences into words and perform any necessary cleaning and stemming

# Create a TF-IDF vectorizer to convert text into numerical features
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)

def generate_response(user_input):
    # Transform user input into a TF-IDF vector
    user_tfidf = tfidf_vectorizer.transform([user_input])

    # Calculate cosine similarities between user input and sentences in the scraped text
    cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix)

    # Get the index of the most similar sentence
    max_similarity_idx = np.argmax(cosine_similarities)

    # Return the response (corresponding sentence)
    return sentences[max_similarity_idx]

print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    else:
        response = generate_response(user_input)
        print(f"Chatbot: {response}")