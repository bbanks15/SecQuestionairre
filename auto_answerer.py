class AutoAnswerer:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def get_best_match(self, question):
        # This function retrieves the best-match answer from the knowledge base
        # For the sake of this example, let's assume knowledge_base is a dictionary
        # with questions as keys and a tuple of (answer, confidence_score, citation) as values.
        best_match = None
        best_confidence = 0
        citation = ""

        for q, (answer, confidence_score, cite) in self.knowledge_base.items():
            if question.lower() in q.lower() and confidence_score > best_confidence:
                best_match = answer
                best_confidence = confidence_score
                citation = cite

        return best_match, best_confidence, citation

# Example usage
knowledge_base = {
    'What is Python?': ('Python is a programming language.', 0.95, 'Wikipedia'),
    'What is the capital of France?': ('The capital of France is Paris.', 0.98, 'Geography Books')
}
auto_answerer = AutoAnswerer(knowledge_base)
question = 'What is Python?'
answer, confidence, source = auto_answerer.get_best_match(question)
print(f'Answer: {answer}, Confidence: {confidence}, Source: {source}')