class Calculator:
    @staticmethod
    def average(*args):
        return sum(args) / len(args) if args else 0