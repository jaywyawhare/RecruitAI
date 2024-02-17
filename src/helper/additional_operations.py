import re
import nltk

try:
    nltk.data.find('corpora/stopwords.zip')
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')

class AdditionalAnalyzer:
    def __init__(self, text: str):
        self.text = text

    def remove_special_characters(self) -> str:
        """Cleans text by removing special characters."""
        return re.sub(r"[^a-zA-Z0-9]+", ' ', self.text)

    def text_cleaning(self) -> str:
        """Cleans text by removing stopwords."""
        stop_words = set(nltk.corpus.stopwords.words('english'))
        word_tokens = nltk.word_tokenize(self.text)
        filtered_sentence = [w for w in word_tokens if w.lower() not in stop_words]
        return ' '.join(filtered_sentence)
