import datetime
from models import Book, Member, Loan


class LibraryService:
    def __init__(self):
        self._books = {}  
        self._members = {} 
        self._loans = {}  
        self._loan_id_counter = 0

  
    def add_book(self, book_id: str, title: str, author: str) -> None:
        if book_id in self._books:
            print("Error: Book ID already exists.")
            return
        book = Book(book_id, title, author, available=True)
        self._books[book_id] = book
        print(f"Book added: {title}")

   
    def register_member(self, member_id: str, name: str, email: str) -> None:
        if member_id in self._members:
            print("Error: Member ID already exists.")
            return
        member = Member(member_id, name, email)
        self._members[member_id] = member
        print(f"Member registered: {name}")

  
    def borrow_book(self, book_id: str, member_id: str) -> None:
        book = self._books.get(book_id)
        if book is None:
            print("Error: Book not found.")
            return

        member = self._members.get(member_id)
        if member is None:
            print("Error: Member not found.")
            return

        if not book.available:
            print("Error: Book is not available.")
            return

       
        self._loan_id_counter += 1
        loan_id = f"L{self._loan_id_counter:04d}"
        loan_date = datetime.date.today().strftime("%Y-%m-%d")
        loan = Loan(loan_id, book_id, member_id, loan_date)
        self._loans[loan_id] = loan


        book.available = False
        print(f"Book borrowed: {book.title}")

    
    def return_book(self, book_id: str) -> None:
        book = self._books.get(book_id)
        if book is None:
            print("Error: Book not found.")
            return

      
        active_loan = None
        for loan in self._loans.values():
            if loan.book_id == book_id and loan.is_active:
                active_loan = loan
                break

        if active_loan is None:
            print("Error: No active loan for this book.")
            return

       
        active_loan.is_active = False
        active_loan.return_date = datetime.date.today().strftime("%Y-%m-%d")
        book.available = True
        print(f"Book returned: {book.title}")

   
    def view_books(self) -> list:
        return list(self._books.values())

   
    def view_members(self) -> list:
        return list(self._members.values())

   
    def view_loans(self) -> list:
        return list(self._loans.values())
