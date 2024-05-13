from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from pyhive import hive
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Connect to Hive
connection = hive.Connection(host='localhost', port=10000, username='your_username')

nlp = spacy.load("en_core_web_sm")

# Function for semantic analysis
def analyze_semantics(text):
    doc = nlp(text)
    # Extract semantic information
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    # Extract noun chunks
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    return entities, noun_chunks

# Function to fetch search terms from Hive table and analyze semantics
def analyze_semantics_hive():
    query = "SELECT searchterms FROM flights"
    data = pd.read_sql(query, connection)
    content = " ".join(data['searchterms'])
    entities, noun_chunks = analyze_semantics(content)
    print("\nSemantic Entities:")
    print(entities)
    print("\nNoun Chunks:")
    print(noun_chunks)

# Function to execute a Hive query
def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# Function for keyword extraction
def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in word_tokenize(text) if word.isalpha() and word.lower() not in stop_words]
    return words

# Function for content optimization suggestions
def optimize_content(text):
    keywords = extract_keywords(text)
    optimized_content = " ".join(keywords)
    return optimized_content

# Function to fetch search terms from Hive table and optimize content
def optimize_content_hive():
    query = "SELECT searchterms FROM flights"
    data = pd.read_sql(query, connection)
    content = " ".join(data['searchterms'])
    optimized_content = optimize_content(content)
    print("\nOptimized Content based on search terms:")
    print(optimized_content)

# Function to analyze search terms
def analyze_search_terms():
    query = "SELECT searchterms FROM flights"
    data = pd.read_sql(query, connection)
    # Keyword Frequency Analysis
    all_words = [word.lower() for text in data['searchterms'] for word in word_tokenize(text) if word.isalpha()]
    word_freq = nltk.FreqDist(all_words)
    print("\nKeyword Frequency Analysis:")
    print(word_freq.most_common(10))

# Main function
def main():
    while True:
        print("\nChoose an option:")
        print("1. Analyze search terms")
        print("2. Optimize content based on search terms")
        print("3. Analyze semantics of search terms")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            analyze_search_terms()
        elif choice == '2':
            optimize_content_hive()
        elif choice == '3':
            analyze_semantics_hive()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    main()
