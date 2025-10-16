class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __add__(self, other):
    sum_x = self.x + other.x
    sum_y = self.y + other.y
    return sum_x, sum_y
  
p1 = Point(2,3)
p2 = Point(3,4)
print(p1+p2)

