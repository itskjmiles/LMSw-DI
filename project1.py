import pymysql

# Database connection parameters
HOST = 'localhost'
USER = ''
PASSWORD = ''
DATABASE = 'library_db'

# Function to establish a database connection
def connect_to_database():
    try:
        conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
        return conn
    except pymysql.Error as e:
        print("Error:", e)
        return None

# Main menu function
def main_menu():
    print("Welcome to the Library Management System with Database Integration!")
    print("****")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Genre Operations")
    print("5. Quit")

    choice = input("Enter your choice: ")
    if choice == '1':
        book_menu()
    elif choice == '2':
        user_menu()
    elif choice == '3':
        author_menu()
    elif choice == '4':
        genre_menu()
    elif choice == '5':
        print("Exiting...")
    else:
        print("Invalid choice!")

# Book menu function
def book_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")

    choice = input("Enter your choice: ")
    if choice == '1':
        add_new_book()
    elif choice == '2':
        borrow_book()
    elif choice == '3':
        return_book()
    elif choice == '4':
        search_book()
    elif choice == '5':
        display_all_books()
    else:
        print("Invalid choice!")

# User menu function
def user_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")

    choice = input("Enter your choice: ")
    if choice == '1':
        add_new_user()
    elif choice == '2':
        view_user_details()
    elif choice == '3':
        display_all_users()
    else:
        print("Invalid choice!")

# Author menu function
def author_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")

    choice = input("Enter your choice: ")
    if choice == '1':
        add_new_author()
    elif choice == '2':
        view_author_details()
    elif choice == '3':
        display_all_authors()
    else:
        print("Invalid choice!")

# Genre menu function
def genre_menu():
    print("Genre Operations:")
    print("1. Add a new genre")
    print("2. View genre details")
    print("3. Display all genres")

    choice = input("Enter your choice: ")
    if choice == '1':
        add_new_genre()
    elif choice == '2':
        view_genre_details()
    elif choice == '3':
        display_all_genres()
    else:
        print("Invalid choice!")

# Function to add a new book
def add_new_book():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            genre = input("Enter the genre of the book: ")
            # Execute SQL query to insert the new book into the database
            query = "INSERT INTO Books (title, author, genre) VALUES (%s, %s, %s)"
            cursor.execute(query, (title, author, genre))
            conn.commit()
            print("Book added successfully!")
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

# Function to borrow a book
def borrow_book():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            book_id = input("Enter the ID of the book to borrow: ")
            user_id = input("Enter your user ID: ")
            # Execute SQL query to update book status and borrower ID
            query = "UPDATE Books SET status = 'Borrowed', borrower_id = %s WHERE id = %s"
            cursor.execute(query, (user_id, book_id))
            conn.commit()
            print("Book borrowed successfully!")
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

# Function to return a book
def return_book():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            book_id = input("Enter the ID of the book to return: ")
            # Execute SQL query to update book status and borrower ID
            query = "UPDATE Books SET status = 'Available', borrower_id = NULL WHERE id = %s"
            cursor.execute(query, (book_id,))
            conn.commit()
            print("Book returned successfully!")
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

# Function to search for a book
def search_book():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            title = input("Enter the title of the book to search for: ")
            # Execute SQL query to search for the book by title
            query = "SELECT * FROM Books WHERE title LIKE %s"
            cursor.execute(query, ('%' + title + '%',))
            books = cursor.fetchall()
            if books:
                print("Search results:")
                for book in books:
                    print("ID:", book[0])
                    print("Title:", book[1])
                    print("Author:", book[2])
                    print("Genre:", book[3])
                    print("Status:", book[4])
                    print("Borrower ID:", book[5])
                    print("----------------------")
            else:
                print("No matching books found.")
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

# Function to display all books
def display_all_books():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            # Execute SQL query to fetch all books
            query = "SELECT * FROM Books"
            cursor.execute(query)
            books = cursor.fetchall()
            if books:
                print("All Books:")
                for book in books:
                    print("ID:", book[0])
                    print("Title:", book[1])
                    print("Author:", book[2])
                    print("Genre:", book[3])
                    print("Status:", book[4])
                    print("Borrower ID:", book[5])
                    print("----------------------")
            else:
                print("No books available.")
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

# Function to add a new user
def add_new_user():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            name = input("Enter the name of the user: ")
            email = input("Enter the email of the user: ")
            # Execute SQL query to insert the new user into the database
            query = "INSERT INTO Users (name, email) VALUES (%s, %s)"
            cursor.execute(query, (name, email))
            conn.commit()
            print("User added successfully!")
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

# Function to view user details
def view_user_details():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            user_id = input("Enter the ID of the user: ")
            # Execute SQL query to retrieve user details based on the user ID
            query = "SELECT * FROM Users WHERE id = %s"
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
            if user:
                print("User details:")
                print("ID:", user[0])
                print("Name:", user[1])
                print("Email:", user[2])
            else:
                print("User not found.")
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

# Function to display all users
def display_all_users():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            # Execute SQL query to fetch all user details
            query = "SELECT * FROM Users"
            cursor.execute(query)
            users = cursor.fetchall()
            if users:
                print("All Users:")
                for user in users:
                    print("ID:", user[0])
                    print("Name:", user[1])
                    print("Email:", user[2])
                    print("----------------------")
            else:
                print("No users available.")
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

# Function to add a new author
def add_new_author():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            name = input("Enter the name of the author: ")
            # Execute SQL query to insert the new author into the database
            query = "INSERT INTO Authors (name) VALUES (%s)"
            cursor.execute(query, (name,))
            conn.commit()
            print("Author added successfully!")
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

# Function to view author details
def view_author_details():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            author_id = input("Enter the ID of the author: ")
            # Execute SQL query to retrieve author details based on the author ID
            query = "SELECT * FROM Authors WHERE id = %s"
            cursor.execute(query, (author_id,))
            author = cursor.fetchone()
            if author:
                print("Author details:")
                print("ID:", author[0])
                print("Name:", author[1])
            else:
                print("Author not found.")
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

# Function to display all authors
def display_all_authors():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            # Execute SQL query to fetch all author details
            query = "SELECT * FROM Authors"
            cursor.execute(query)
            authors = cursor.fetchall()
            if authors:
                print("All Authors:")
                for author in authors:
                    print("ID:", author[0])
                    print("Name:", author[1])
                    print("----------------------")
            else:
                print("No authors available.")
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

# Function to add a new genre
def add_new_genre():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            name = input("Enter the name of the genre: ")
            # Execute SQL query to insert the new genre into the database
            query = "INSERT INTO Genres (name) VALUES (%s)"
            cursor.execute(query, (name,))
            conn.commit()
            print("Genre added successfully!")
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

# Function to view genre details
def view_genre_details():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            genre_id = input("Enter the ID of the genre: ")
            # Execute SQL query to retrieve genre details based on the genre ID
            query = "SELECT * FROM Genres WHERE id = %s"
            cursor.execute(query, (genre_id,))
            genre = cursor.fetchone()
            if genre:
                print("Genre details:")
                print("ID:", genre[0])
                print("Name:", genre[1])
            else:
                print("Genre not found.")
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

# Function to display all genres
def display_all_genres():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            # Execute SQL query to fetch all genre details
            query = "SELECT * FROM Genres"
            cursor.execute(query)
            genres = cursor.fetchall()
            if genres:
                print("All Genres:")
                for genre in genres:
                    print("ID:", genre[0])
                    print("Name:", genre[1])
                    print("----------------------")
            else:
                print("No genres available.")
        except pymysql.Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main_menu()
