#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Book:
    def __init__(self, book_id, title, author, level, availability=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.level = level
        self.availability = availability


class Member:
    def __init__(self, member_id, name, email, level):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.level = level
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def delete_member(self, member_id):
        member = self.find_member_by_id(member_id)
        if member:
            self.members.remove(member)

    def display_members(self):
        if self.members:
            print("Members in the library:")
            for member in self.members:
                print(f"Member ID: {member.member_id}, Name: {member.name}, Email: {member.email}, Level: {member.level}")
        else:
            print("No members found in the library.")

    def display_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                availability = "Available" if book.availability else "Not Available"
                print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Level: {book.level}, Availability: {availability}")
        else:
            print("No books found in the library.")

    def borrow_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        if member:
            book = self.find_book_by_id(book_id)
            if book and book.availability:
                member.borrow_book(book)
                book.availability = False
                print("Book borrowed successfully.")
            else:
                print("Book not available.")
        else:
            print("Member not found.")

    def return_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        if member:
            book = self.find_book_by_id(book_id)
            if book and book not in member.borrowed_books:
                print("Book is not borrowed by the member.")
            elif book:
                member.return_book(book)
                book.availability = True
                print("Book returned successfully.")
            else:
                print("Book not found.")
        else:
            print("Member not found.")

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None


class LibrarySystem:
    def __init__(self):
        self.library = Library()

    def display_menu(self):
        print("-------📚 welcom in lama’s library 📚--------")
        print("1. Add Member")
        print("2. Edit Member")
        print("3. Show Members")
        print("4. Delete Member")
        print("5. Add Book")
        print("6. Show Books")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Exit")
        print("---------------------------------------------")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-9): ")

            if choice == "1":
                self.add_member()

            elif choice == "2":
                self.edit_member()

            elif choice == "3":
                self.show_members()

            elif choice == "4":
                self.delete_member()

            elif choice == "5":
                self.add_book()

            elif choice == "6":
                self.show_books()

            elif choice == "7":
                self.borrow_book()

            elif choice == "8":
                self.return_book()

            elif choice == "9":
                print("Good bye 👋")
                break

            else:
                print("Invalid choice can Please try again.")

    def add_member(self):
        member_id = int(input("Enter the member ID: "))
        name = input("Enter the member name: ")
        email = input("Enter the member email: ")
        level = input("Enter the member level (A, B, C): ")
        member = Member(member_id, name, email, level)
        self.library.add_member(member)
        print("Member added successfully.")

    def edit_member(self):
        member_id = int(input("Enter the member ID: "))
        member = self.library.find_member_by_id(member_id)
        if member:
            name = input("Enter the new member name: ")
            email = input("Enter the new member email: ")
            level = input("Enter the new member level (A, B, C): ")
            member.name = name
            member.email = email
            member.level = level
            print("Member updated successfully.")
        else:
            print("Member not found.")

    def show_members(self):
        self.library.display_members()

    def delete_member(self):
        member_id = int(input("Enter the member ID: "))
        self.library.delete_member(member_id)
        print("Member deleted successfully.")

    def add_book(self):
        book_id = int(input("Enter the book ID: "))
        title = input("Enter the book title: ")
        author = input("Enter the author name: ")
        level = input("Enter the book level (A, B, C): ")
        book = Book(book_id, title, author, level)
        self.library.add_book(book)
        print("Book added successfully.")

    def show_books(self):
        self.library.display_books()

    def borrow_book(self):
        member_id = int(input("Enter the member ID: "))
        book_id = int(input("Enter the book ID: "))
        self.library.borrow_book(member_id, book_id)

    def return_book(self):
        member_id = int(input("Enter the member ID: "))
        book_id = int(input("Enter the book ID: "))
        self.library.return_book(member_id, book_id)


library_system = LibrarySystem()
library_system.run()


# In[ ]:




