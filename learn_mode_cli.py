import json
import os

class KnowledgeBase:
    def __init__(self, data_file='knowledge_base.json'):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                self.data = json.load(file)
        else:
            self.data = {}

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_q_a_pair(self, question, answer):
        self.data[question] = answer
        self.save_data()

    def get_answers(self):
        return self.data.items()

class CLI:
    def __init__(self):
        self.kb = KnowledgeBase()

    def run(self):
        print('Welcome to the Knowledge Base CLI!')
        while True:
            command = input('\nEnter a command (view, add, exit): ').strip().lower()
            if command == 'view':
                self.view_answers()
            elif command == 'add':
                self.add_pair()
            elif command == 'exit':
                print('Exiting the CLI.')
                break
            else:
                print('Invalid command. Please try again.')

    def view_answers(self):
        answers = self.kb.get_answers()
        if not answers:
            print('No Q/A pairs found.')
            return
        for question, answer in answers:
            print(f'Q: {question}\nA: {answer}\n')

    def add_pair(self):
        question = input('Enter your question: ')
        answer = input('Enter the answer: ')
        self.kb.add_q_a_pair(question, answer)
        print('Q/A pair added!')

if __name__ == '__main__':
    cli = CLI()
    cli.run()