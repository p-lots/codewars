class Journey:
    def __init__(self, weight, crew, balloons):
        self.weight = weight['weight']
        self.crew = crew
        self.balloons = balloons
        self.CREW_WEIGHT = 80
        self.BALLOON_LIFT = 0.0048
    
    def isPossible(self):
        return self.weight + self.crew * self.CREW_WEIGHT <= self.balloons * self.BALLOON_LIFT
