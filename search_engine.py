import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download the NLTK stopwords data if not already present
import nltk
nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove non-alphabetic characters
    text = re.sub(r'[^a-z\s]', '', text)

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Join the tokens back into a single string
    processed_text = ' '.join(tokens)

    return processed_text


def build_reverse_index(data):
    reverse_index = {}
    for index, row in data.iterrows():
        text = preprocess_text(row['text'])
        for word in text.split():
            if word not in reverse_index:
                reverse_index[word] = set()
            reverse_index[word].add(row['filename'])
    print('Length of reverse index -',str(len(reverse_index)))
    return reverse_index

def search(query, reverse_index):
    # Implement your search logic here
    
    query = preprocess_text(query)
    query_words = set(query.split())

    # Initialize the result with the documents containing the first query word
    result = reverse_index.get(query_words.pop(), set())

    # Intersect with the sets of documents containing the other query words
    for word in query_words:
        result = result.intersection(reverse_index.get(word, set()))

    return list(result)