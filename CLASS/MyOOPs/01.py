class Book():

  book_count = 0

  def __init__(self, title, author):
    self.title = title
    self.author = author
    Book.book_count += 1

  def getInfo(self):
    return f'{self.title} by {self.author}'
  
  @classmethod
  def from_string(cls, title):
    cls.title = title


book_1 = Book('abc', 'def')
book_2 = Book('ghi', 'jkl')
book_3 = Book('mno', 'pqr')

print(Book.getInfo(book_1))
print(book_2.getInfo())
print(Book.book_count)
print(book_3.book_count)