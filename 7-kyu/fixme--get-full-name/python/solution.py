class Dinglemouse(object):
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
    def get_full_name(self):
        if not self.last_name:
            return self.first_name
        elif not self.first_name:
            return self.last_name
        elif not self.first_name and not self.last_name:
            return ''
        return self.first_name + ' ' + self.last_name