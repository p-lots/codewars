class CircularList():
    def __init__(self, *args):
        if len(args) == 0:
            raise Exception
        self.internal_list = list(args)
        self.idx = 0
        self.first_next = None
        
    def next(self):
        if self.first_next == None:
            self.first_next = True
            self.idx = -1
        self.idx += 1
        return self.internal_list[self.idx % len(self.internal_list)]
    
    def prev(self):
        if self.first_next == None:
            self.first_next = False
        self.idx -= 1
        return self.internal_list[self.idx % len(self.internal_list)]
