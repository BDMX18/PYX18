'''
Overload Arithmetic Operators for Time Calculation
Implement a Time class where:

+ adds two time objects (e.g., 1hr 30min + 2hr 45min = 4hr 15min)

Automatically adjusts minutes > 60.
'''

class Time:

  def __init__(self, hour, minute):
    self.hour = hour
    self.minute = minute

  def __add__(self, other):
    hours = self.hour + other.hour
    minutes = self.minute + other.minute
    if minutes >= 60:
      hours += minutes // 60
      minutes = minutes % 60
    return f'{hours} Hours : {minutes} Minutes'
  
T1 = Time(5, 43)
T2 = Time(4, 27)

print(T1 + T2)