class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def short_title(self):
        return self.title[:10]


b1 = Book("to kill a mocking bird","Harper Lee")
b2 = Book("The Alchemist","Paulo Coelho")
b3 = Book("Atomic Habits","James Clear")

print(b1.short_title())
print(b2.short_title())
print(b3.short_title())