class Harshad:
    @staticmethod
    def is_valid(number):
        if number == 0:
            return False
        return number % sum(map(int, str(number))) == 0
    
    @staticmethod
    def get_next(number):
        number += 1
        while not Harshad.is_valid(number):
            number += 1
        return number
    
    @staticmethod
    def get_series(count, start=0):
        series = []
        start += 1
        while len(series) < count:
            if Harshad.is_valid(start):
                series.append(start)
            start += 1
        return series