CREATE TABLE IF NOT EXISTS Books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    genre_id INT,
    available BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (author_id) REFERENCES Authors(id),
    FOREIGN KEY (genre_id) REFERENCES Genres(id)
);

CREATE TABLE IF NOT EXISTS Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO Authors (name) VALUES
(1, 'Jane Austen'),
(2, 'George Orwell'),
(3, 'J.K. Rowling');

INSERT INTO Genres (name) VALUES
(1, 'Fiction'),
(2, 'Science Fiction'),
(3, 'Fantasy');

INSERT INTO Books (title, author_id, genre_id, available) VALUES
('Pride and Prejudice', 1, 1, TRUE),
('1984', 2, 2, TRUE),
('Harry Potter and the Philosopher''s Stone', 3, 3, TRUE);

INSERT INTO Users (name, email) VALUES
(1, 'John Doe', 'john@example.com'),
(2, 'Jane Smith', 'jane@example.com');
