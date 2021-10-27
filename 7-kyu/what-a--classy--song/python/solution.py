class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = set()
    
    def how_many(self, todays_listeners):
        ret = 0
        for listener in todays_listeners:
            if listener.lower() not in self.listeners:
                ret += 1
                self.listeners.add(listener.lower())
        return ret
