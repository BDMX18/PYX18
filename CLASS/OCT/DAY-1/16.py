'''
Execution Time Logger with Custom Message

Question:
Write a decorator @time_logger(message) that takes a custom message string as an argument.
When the decorated function runs, print the message along with the function’s execution time.

Example:

@time_logger("Function finished!")
def process_data():
    # simulate processing time
    import time
    time.sleep(1)

process_data()


Expected output:

Function finished! Execution time: 1.0012 seconds
'''
import time

def timeLogger(message):
  def outerDecorator(func):
    def innerDecorator():
      start = time.time()
      result = func()
      end = time.time()
      time_taken = end-start
      print(f'{message} Execution Time: {round(time_taken, 2)}')
      return result
    return innerDecorator
  return outerDecorator

@timeLogger('Function Finished!')
def process_data():
  time.sleep(1)

process_data()
