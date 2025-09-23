'''
2. Multiple Decorators

Write two decorators:

One that prints "Start"

Another that prints "End"
Use them on a single function to print:

Start
Function is running
End
'''

def startOuter(arg):
  def startInner(*args, **kwargs):
    print('start')
    return arg(*args, **kwargs)
  return startInner

@startOuter # endOuter = startOuter(endOuter)
def endOuter(args):
  def endInner():
    args()
    print('End')
  return endInner

@endOuter # decoratedFunc = endOuter(decoratorFunc)
def decoratedFunc():
  print('Function is running')

decoratedFunc()