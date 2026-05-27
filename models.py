# models.py

class Book:
    def __init__(self, book_id: str, title: str, author: str, available: bool = True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

class Member:
    def __init__(self, member_id: str, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email

class Loan:
    def __init__(self, loan_id: str, book_id: str, member_id: str,
                 loan_date: str, return_date: str = None, is_active: bool = True):
        self.loan_id = loan_id
        self.book_id = book_id
        self.member_id = member_id
        self.loan_date = loan_date
        self.return_date = return_date
        self.is_active = is_active