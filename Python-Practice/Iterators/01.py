'''Custom iterator to fetch each and every line from a file in python'''

with open('Iterator.txt', 'w') as FO:
  FO.writelines(['Hi\n', 'Hello\n', 'Bye\n', 'How\n', 'Are\n', 'You?\n'])

class FileIterator:

  def __init__(self, filename):
    self.filename = filename
    self.FO = None

  def __iter__(self):
    if self.FO is None:
      try:
        self.FO = open(self.filename, 'r')
      except FileNotFoundError as error:
        print(error)
    return self

  def __next__(self):
    data = self.FO.readline()
    if data != '':
      return data
    else:
      self.FO.close()
      raise StopIteration
    
FIO = FileIterator('Iterator.txt')

for line in FIO:
  print(line)