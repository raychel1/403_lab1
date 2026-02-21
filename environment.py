import random

class DisasterEnvironment:
    def __init__(self):
        self.disasters = ["None", "Flood", "Fire", "Earthquake"]

    def sense(self):
        """Randomly selects a disaster and severity"""
        event = random.choice(self.disasters)
        severity = random.randint(1, 10)
        return event, severity
