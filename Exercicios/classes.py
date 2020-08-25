class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def print_point(self):
        print("({0}, {1})".format(self.x, self.y))
        
    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my).to_string()



p1 = Point(3, 4)
target = Point(10, 6)
teste = p1.halfway(target)
print(teste)

