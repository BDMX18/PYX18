'''
1️⃣ Question: Execution Time Decorator

Write a decorator @timer that:

Measures how long a function takes to execute.

Prints the execution time in seconds.

Works on any function, regardless of its arguments.

Then, use this decorator on a sample function that:

Takes a list of numbers and returns their squares.

Example:

@timer
def square_numbers(numbers):
    return [n ** 2 for n in numbers]

square_numbers(list(range(1_000_000)))


Output:

Execution time: 0.25 seconds
'''

import time

# agr here holds the square_numbers function address
def timer(arg):
  def innerTimer(numbers):
    start = time.time()

    # Herein, we're calling the square_numbers function.
    arg(numbers)

    end = time.time()
    print('Execution Time: ', end-start)
  return innerTimer

@timer # square_numbers = timer(square_numbers)
def square_numbers(numbers):
  return [n**2 for n in numbers]

square_numbers(list(range(100)))

'''
Flow Of Execution:

1. We've at first imprted the 'time' module.
2. The function 'timer' is defined with one positional arguement 'arg'.
3. We've decorated the 'square_numbers' function with timer function '@timer'.
4. The function 'square_numbers' is defined with one positional arguement 'numbers'.
5. 'square_numbers' function is called with value 'list(range(100))'.
6. As we call the function 'square_numbers', The control goes to the line where we've     defined the decorator (i.e : @timer)
  -> Herein, internally a variable by the name 'square_numbers' gets created which calls
    the 'timer' function and passes the 'square_numbers' function address as a value.
7. Now, with the timer function being called, control goes inside 'timer' function.
8. In 'timer' function, an 'innerTimer' function is defined with one positional arguement 'numbers'.
9. The 'timer' function now returns the 'innerTimer' function address.
10. The return statement returns the output and the control from 'timer' function to 'square_numbers' variable.
11. The square_number variable now holds the function address of 'innerTimer'.
12. The square_number function starts executing and the control goes for square_number function to innerTimer function.
13. Now, innerTimer function starts executing.
    -> We've defined a variable start which calls the time() function from time module.
    -> Now 'arg' is called as a function, which primarily calls the square_number function, as it holds its address.
    -> The square_number function completes its execution.
    -> The control again comes into innerTimer function.
    -> We've defined a variable end which calls the time() function from time module.
    -> Further we're printing the difference between start and end.
14. With this, innerTimer() function completes its execution and prints the execution time.

'''