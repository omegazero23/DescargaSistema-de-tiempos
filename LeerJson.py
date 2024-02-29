import json


class ReadJson:
    def __init__(self, filename):
        with open(filename) as f:
            self.secretdata = json.load(f)
        
