class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def __str__(self):
        return f"Book: '{self.title}' by {self.author} , and its cost is {self.price}"
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price})"
book1 = Book("Python Basics", "Manasa", 499)
book2 = Book("OOP Concepts", "Rahul", 599)
print(book1)
print(book2)
