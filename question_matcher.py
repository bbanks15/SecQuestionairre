import difflib
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Ensure stopwords are downloaded
nltk.download('stopwords')

class QuestionMatcher:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.stop_words = set(stopwords.words('english'))

    def fuzzy_match(self, question):
        best_match = difflib.get_close_matches(question, self.knowledge_base, n=1)
        if best_match:
            return best_match[0], difflib.SequenceMatcher(None, question, best_match[0]).ratio()
        return None, 0.0

    def semantic_match(self, question):
        tfidf_matrix = self.vectorizer.fit_transform(self.knowledge_base + [question])
        cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
        max_sim_index = cosine_sim.argmax()
        return self.knowledge_base[max_sim_index], cosine_sim[0][max_sim_index]

    def match_question(self, question):
        fuzzy_match, fuzzy_score = self.fuzzy_match(question)
        semantic_match, semantic_score = self.semantic_match(question)
        return {
            'fuzzy_match': fuzzy_match,
            'fuzzy_score': fuzzy_score,
            'semantic_match': semantic_match,
            'semantic_score': semantic_score
        }

# Example knowledge base
knowledge_base = [
    "What is your name?",
    "How can I reset my password?",
    "What is your refund policy?",
]

# Create an instance of the matcher
matcher = QuestionMatcher(knowledge_base)

# Test the matcher
incoming_question = "How do I reset my password?"
matching_results = matcher.match_question(incoming_question)
print(matching_results)