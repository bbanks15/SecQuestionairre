# conflict_resolver.py

class ConflictResolver:
    def __init__(self):
        self.answers = []  # Store answers with their sources and timestamps

    def add_answer(self, source: str, answer: str, timestamp: str):
        self.answers.append({'source': source, 'answer': answer, 'timestamp': timestamp})

    def resolve_conflicts(self):
        # Sort answers based on source and timestamp
        sorted_answers = sorted(self.answers, key=lambda x: (x['source'], x['timestamp']))
        resolved_answers = []

        # Resolve conflicts by official source prioritization
        last_source = None
        for entry in sorted_answers:
            if last_source != entry['source']:
                resolved_answers.append(entry)
                last_source = entry['source']

        return resolved_answers

# Example Usage
if __name__ == '__main__':
    resolver = ConflictResolver()
    resolver.add_answer('sourceA', 'Answer 1', '2026-03-04 18:20:00')
    resolver.add_answer('sourceB', 'Answer 2', '2026-03-04 18:21:00')
    resolver.add_answer('sourceA', 'Answer 3', '2026-03-04 18:22:00')
    
    resolved = resolver.resolve_conflicts()
    for r in resolved:
        print(f"Source: {r['source']}, Answer: {r['answer']}, Timestamp: {r['timestamp']}")