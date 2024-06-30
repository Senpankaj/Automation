import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from transformers import pipeline

# Ensure required NLTK data packages are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    try:
        # Tokenization: Split the text into individual words (tokens)
        tokens = word_tokenize(text.lower())
        
        # Removing Stop Words: Remove common words that don't add much meaning
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
        
        # Lemmatization: Reduce words to their base form
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        
        return tokens
    except Exception as e:
        print(f"Error preprocessing text: {e}")
        return []

# Load question-answering pipeline
try:
    qa_pipeline = pipeline("question-answering")
except Exception as e:
    print(f"Error loading QA pipeline: {e}")
    qa_pipeline = None

# Example usage with your provided text
text = """
Albert Einstein was a theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics (alongside quantum mechanics). 
His work is also known for its influence on the philosophy of science. He was born in Germany in 1879 and moved to the United States in 1933, where he became a naturalized citizen. 
Einstein is best known to the general public for his mass energy equivalence formula E = mc^2, which has been dubbed "the world's most famous equation." 
He received the 1921 Nobel Prize in Physics for his "services to theoretical physics" and especially for his discovery of the law of the photoelectric effect.
"""

# Preprocess the text
preprocessed_text = preprocess_text(text)
context = " ".join(preprocessed_text)

# Perform question-answering if the pipeline is initialized
if qa_pipeline:
    question = "When did Albert Einstein move to the United States?"
    try:
        print("Context:", context)  # Debugging output
        result = qa_pipeline(question=question, context=context)
        print("Question:", question)
        print("Answer:", result['answer'])
    except Exception as e:
        print(f"Error during question-answering: {e}")
else:
    print("QA pipeline not initialized.")
