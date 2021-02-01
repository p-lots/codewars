class Dictionary():
    def __init__(self):
        self.lookup = dict()
        
    def newentry(self, word, definition):
        self.lookup[word] = definition
        
    def look(self, key):
        return self.lookup.get(key, f"Can't find entry for {key}")