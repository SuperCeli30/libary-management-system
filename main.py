# main.py

from library_service import LibraryService

def display_menu() -> None:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")

def main():
    service = LibraryService()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        # Flowchart 1: Add Book
        if choice == '1':
            book_id = input("Input: Book ID: ")
            title = input("Input: Book Title: ")
            author = input("Input: Book Author: ")
            service.add_book(book_id, title, author)

        # Flowchart 2: Register Member
        elif choice == '2':
            member_id = input("Input: Member ID: ")
            name = input("Input: Member Name: ")
            email = input("Input: Member Email: ")
            service.register_member(member_id, name, email)

        # Flowchart 3: Borrow Book
        elif choice == '3':
            book_id = input("Input: Book ID: ")
            member_id = input("Input: Member ID: ")
            service.borrow_book(book_id, member_id)

        # Flowchart 4: Return Book
        elif choice == '4':
            book_id = input("Input: Book ID: ")
            service.return_book(book_id)

        # Flowchart 5: View Books
        elif choice == '5':
            books = service.view_books()
            if not books:
                print("Output: No books found.")
            else:
                print("Output: Books:")
                for book in books:
                    status = "Available" if book.available else "Borrowed"
                    print(f"  {book.book_id} - {book.title} by {book.author} [{status}]")

        # Flowchart 6: View Members
        elif choice == '6':
            members = service.view_members()
            if not members:
                print("Output: No members found.")
            else:
                print("Output: Members:")
                for member in members:
                    print(f"  {member.member_id} - {member.name} ({member.email})")

        # Flowchart 7: View Loans
        elif choice == '7':
            loans = service.view_loans()
            if not loans:
                print("Output: No loans found.")
            else:
                print("Output: Loans:")
                for loan in loans:
                    status = "Active" if loan.is_active else "Returned"
                    print(f"  {loan.loan_id} - Book: {loan.book_id}, Member: {loan.member_id}, Date: {loan.loan_date}, Status: {status}")

        # Flowchart 8: Exit
        elif choice == '8':
            print("Output: Program closed.")
            break  # Exit the while-True loop

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()