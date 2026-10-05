""""""""""""""""
Julie Murphy- Base level

#Test output includes five fields plus available
=== Full Collection ===
978-0689853234 | Alanna: The First Adventure  | Tamora Pierce        | 1983 | Fantasy          | Available
978-0593336823 | The Love Hypothesis          | Ali Hazelwood        | 2021 | Romance          | Available
978-1728289731 | Done and Dusted              | Lyla Sage            | 2023 | Contemporary     | Available
978-0451227431 | Vision in White              | Nora Roberts         | 2009 | Romance          | Available
978-0451408655 | Naked in Death               | J.D. Robb            | 1995 | Mystery/Sci-Fi   | Available
978-1649374042 | Fourth Wing                  | Rebecca Yarros       | 2023 | Fantasy          | Available

#Test checkout books
'Alanna: The First Adventure' checked out to Julie.
'The Love Hypothesis' checked out to Adam.
'Alanna: The First Adventure' is already checked out.

'The Love Hypothesis' has been returned and is now available.

#Test sorted display
=== Collection Sorted by Title ===
978-0689853234 | Alanna: The First Adventure  | Tamora Pierce        | 1983 | Fantasy          | Checked out to Julie
978-1728289731 | Done and Dusted              | Lyla Sage            | 2023 | Contemporary     | Available
978-1649374042 | Fourth Wing                  | Rebecca Yarros       | 2023 | Fantasy          | Available
978-0451408655 | Naked in Death               | J.D. Robb            | 1995 | Mystery/Sci-Fi   | Available
978-0593336823 | The Love Hypothesis          | Ali Hazelwood        | 2021 | Romance          | Available
978-0451227431 | Vision in White              | Nora Roberts         | 2009 | Romance          | Available

#Test available books
=== Available Books ===
978-0593336823 | The Love Hypothesis          | Ali Hazelwood        | 2021 | Romance          | Available
978-1728289731 | Done and Dusted              | Lyla Sage            | 2023 | Contemporary     | Available
978-0451227431 | Vision in White              | Nora Roberts         | 2009 | Romance          | Available
978-0451408655 | Naked in Death               | J.D. Robb            | 1995 | Mystery/Sci-Fi   | Available
978-1649374042 | Fourth Wing                  | Rebecca Yarros       | 2023 | Fantasy          | Available

"""""""""""""""""
class Book:
    def __init__(self, title, author, isbn, year, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.genre = genre
        self.available = True
        self.borrower = None

    def __str__(self):
        return f"{self.isbn:<14} | {self.title:<28} | {self.author:<20} | {self.year:<4} | {self.genre:<16} | {self.get_status()}"

    def check_out(self, patron_name):
        if self.available:
            self.available = False
            self.borrower = patron_name
            return True
        return False

    def return_book(self):
        self.available = True
        self.borrower = None
        return f"'{self.title}' has been returned and is now available."

    def get_status(self):
        if self.available:
            return "Available"
        return f"Checked out to {self.borrower}"


#Display collection
if __name__ == "__main__":
    collection = [
        Book("Alanna: The First Adventure", "Tamora Pierce", "978-0689853234", 1983, "Fantasy"),
        Book("The Love Hypothesis", "Ali Hazelwood", "978-0593336823", 2021, "Romance"),
        Book("Done and Dusted", "Lyla Sage", "978-1728289731", 2023, "Contemporary"),
        Book("Vision in White", "Nora Roberts", "978-0451227431", 2009, "Romance"),
        Book("Naked in Death", "J.D. Robb", "978-0451408655", 1995, "Mystery/Sci-Fi"),
        Book("Fourth Wing", "Rebecca Yarros", "978-1649374042", 2023, "Fantasy"),
    ]

    print("=== Full Collection ===")
    for book in collection:
        print(book)
    print()

#Checkout books
    if collection[0].check_out("Julie"):
        print(f"'{collection[0].title}' checked out to Julie.")
    else:
        print(f"'{collection[0].title}' is already checked out.")

    if collection[1].check_out("Adam"):
        print(f"'{collection[1].title}' checked out to Adam.")
    else:
        print(f"'{collection[1].title}' is already checked out.")

    # Try checking out a book that's already checked out
    if not collection[0].check_out("Melissa"):
        print(f"'{collection[0].title}' is already checked out.")
    print()

    # Return one of the checked out books
    print(collection[1].return_book())
    print()

    #Display sorted collection by title
    sorted_collection = sorted(collection, key=lambda b: b.title)
    print("=== Collection Sorted by Title ===")
    for book in sorted_collection:
        print(book)
    print()

    #Display available books
    available_books = [b for b in collection if b.available]
    print("=== Available Books ===")
    for book in available_books:
        print(book)
