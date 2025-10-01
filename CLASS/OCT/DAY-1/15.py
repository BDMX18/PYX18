'''
Question:
Create a decorator @benchmark that measures execution time of any function and stores timing in a global dictionary benchmark_results.

Example:

benchmark_results = {}

@benchmark
def compute():
    sum(range(1000000))

compute()
print(benchmark_results)


Expected:

{'compute': 0.11238}
'''

import time

benchmark_results = {}

def benchmark(func):
  count = 1
  def decorator():
    nonlocal count
    global benchmark_results
    start = time.time()
    func()
    end = time.time()
    result = end - start
    key = f'computation-{count}'
    benchmark_results[key] = result
    count += 1
    return benchmark_results
  return decorator

@benchmark
def compute():
  sum(range(100))

compute()
compute()
compute()
compute()
print(benchmark_results)
