'''
> Singleton class is a design pattern wherein a class will have a single object throughout its entire lifecycle. In-order to create a singleton class we've to use the concept of decoration.
> The process of singleton class is mainly used when we're dealing with booking application.

> Flow Of Execution:
  -> At first, singleTonDecorator function gets created which will take one arguement.
  -> We've created a class by the name of 'Multiplex'.
  -> 
'''

def singleTonDecporator(cls):
  Obj_List = []
  def innerFunc():
    if(len(Obj_List) == 0):
      Obj_List.append(cls())
    return Obj_List[0]
  return innerFunc

@singleTonDecporator # Multiplex = singleTonDecorator(MultiplexCA) || After decorator function gets executed, Multiplex = innerFunc FA.
class Multiplex:

  def __init__(self):
    self.count = 500

  def booking(self, n):
    if n <= self.count:
      self.count -= n
      print('Tickets Booked!')
    else:
      print('Tickets Limit Exceeded!')
    print('Available Tickets:', self.count)
    print('-'*50)

Rajesh = Multiplex()
Rajesh.booking(120)
print(Rajesh)
Suresh = Multiplex()
Suresh.booking(110)
print(Suresh)
Mahesh = Multiplex()
Mahesh.booking(444)
print(Mahesh)