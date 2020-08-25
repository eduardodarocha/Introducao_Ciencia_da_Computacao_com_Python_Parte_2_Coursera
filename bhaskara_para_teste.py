import math

class Bhaskara:

    def deltafunc(self, a, b, c):
        return (b**2) - (4 * a * c)

    def calc_x1_x2(self, a, b, c):
        deltaval = self.deltafunc(a, b, c)
        if deltaval < 0:
            return 0
        if deltaval == 0:
            xs = (-b - math.sqrt(deltaval)) / (2 * a)
            return 1, xs
        if deltaval > 0:
            xp = (-b + math.sqrt(deltaval)) / (2 * a)
            xs = (-b - math.sqrt(deltaval)) / (2 * a)
            return 2, xp, xs
        else:
            return None

