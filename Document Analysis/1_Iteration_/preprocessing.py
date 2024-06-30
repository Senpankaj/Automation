import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Ensure required NLTK data packages are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    try:
        # Tokenization: Split the text into individual words (tokens)
        tokens = word_tokenize(text.lower())
        # Debugging output to check tokens
        print("Tokens after tokenization:", tokens[:50])
        
        # Removing Stop Words: Remove common words that don't add much meaning
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
        # Debugging output to check tokens after stop word removal
        print("Tokens after stop word removal:", tokens[:50])
        
        # Lemmatization: Reduce words to their base form
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        # Debugging output to check tokens after lemmatization
        print("Tokens after lemmatization:", tokens[:50])
        
        return tokens
    except Exception as e:
        print(f"Error preprocessing text: {e}")
        return []

# Example usage
text = """
We present the first deep learning model to successfully learn control policies directly from high-dimensional sensory input using reinforcement learning. The
model is a convolutional neural network, trained with a variant of Q-learning,
whose input is raw pixels and whose output is a value function estimating future
rewards. We apply our method to seven Atari 2600 games from the Arcade Learning Environment, with no adjustment of the architecture or learning algorithm. We
find that it outperforms all previous approaches on six of the games and surpasses
a human expert on three of them.
"""
preprocessed_text = preprocess_text(text)
print("Preprocessed text:", preprocessed_text)
