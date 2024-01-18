import json, os
class analyze_response:
    def __init__(self, model):
        self.model = model
    
    def context(self):
        pass

    def find_similar(self):
        pass

    def identify_type(self, q):
        pass

    def load_database(self):
        db = []
        for file in os.listdir('memory/'):
            print(file)


    def queue(self, token):
        response = None
        if self.model == "no-context":
            db = self.load_database()
        return response