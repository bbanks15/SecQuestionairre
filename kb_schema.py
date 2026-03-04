# Enhanced KB Schema

class KBEntry:
    def __init__(self, question: str, answer: str, version: int, source: str, timestamp: str, confidence_score: float, conflict_resolution: str):
        self.question = question
        self.answer = answer
        self.version = version
        self.source = source
        self.timestamp = timestamp
        self.confidence_score = confidence_score
        self.conflict_resolution = conflict_resolution

# Example usage:
kb_entry = KBEntry(
    question="What is the capital of France?",
    answer="Paris",
    version=1,
    source="trusted_source",
    timestamp="2026-03-04 18:25:19",
    confidence_score=0.95,
    conflict_resolution="Reviewed and approved"
)