# Player class
class Player(object):
    def __init__(self, name, point, score):
        self.name = name
        self.point = point
        self.score = score

    def get_name(self):
        return self.name
