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
We present the first deep learning model to successfully learn control policies directly from high-dimensional sensory input using reinforcement learning. The
model is a convolutional neural network, trained with a variant of Q-learning,
whose input is raw pixels and whose output is a value function estimating future
rewards. We apply our method to seven Atari 2600 games from the Arcade Learning Environment, with no adjustment of the architecture or learning algorithm. We
find that it outperforms all previous approaches on six of the games and surpasses
a human expert on three of them.
"""

# Preprocess the text
preprocessed_text = preprocess_text(text)
context = " ".join(preprocessed_text)

# Perform question-answering if the pipeline is initialized
if qa_pipeline:
    question = "What does the model learn directly from high-dimensional sensory input?"
    try:
        result = qa_pipeline(question=question, context=context)
        print(result['answer'])  # Print only the answer
    except Exception as e:
        print(f"Error during question-answering: {e}")
else:
    print("QA pipeline not initialized.")
