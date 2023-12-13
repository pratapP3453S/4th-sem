# Write a program for tokenization of given input

import nltk
from nltk.tokenize import WhitespaceTokenizer

def tokenize_text(text):
    # Use WhitespaceTokenizer for tokenization
    tokenizer = WhitespaceTokenizer()
    tokens = tokenizer.tokenize(text)
    return tokens

# Example usage:
input_text = "This is a simple example sentence. Tokenization is an important step in natural language processing."
tokenized_text = tokenize_text(input_text)

# Print the tokenized text
print("Input Text:")
print(input_text)
print("\nTokenized Text:")
print(tokenized_text)
