# Python Socket Authentication System

A simple client-server authentication system built using Python, SQLite, Socket Programming, Multithreading, and SHA-256 password hashing.

## Features

- User login authentication
- TCP client-server communication
- SQLite database for storing user credentials
- SHA-256 password hashing
- Multi-client support using threading
- SQL Injection protection using parameterized queries

## Technologies Used

- Python 3
- SQLite3
- Socket Programming
- Threading
- Hashlib (SHA-256)

## Project Structure

```
.
├── server.py          # Authentication server
├── client.py          # Client application
├── samples.py         # Creates the SQLite database and inserts users
├── userdata.db        # SQLite database
└── README.md
```

## How It Works

1. The server starts and listens for client connections.
2. The client connects to the server.
3. The server requests the username.
4. The client sends the username.
5. The server requests the password.
6. The client sends the password.
7. The server hashes the password using SHA-256.
8. The server compares the username and hashed password with the SQLite database.
9. If the credentials match, login is successful.
10. Otherwise, login fails.

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/socket-authentication.git
```

Move into the project folder:

```bash
cd socket-authentication
```

## Requirements

Python 3.x

No external libraries are required.

The project only uses Python's built-in modules:

- sqlite3
- socket
- threading
- hashlib

## Database Setup

Run the database creation script:

```bash
py samples.py
```

This creates:

```
userdata.db
```

with sample users.

## Running the Server

```bash
py server.py
```

Example Output:

```
Server is running on port 50000...
```

## Running the Client

Open another terminal and run:

```bash
py client.py
```

Example:

```
Username: Mike
Password: mikepassword
Login successful!
```

## Sample Users

| Username | Password |
|----------|----------|
| Mike | mikepassword |
| Jhon | mycatisgreat |
| striker999 | ilikestriking |
| neuralnine | neuralpassword |

> Passwords are stored in the database as SHA-256 hashes, not plain text.

## Security Features

- SHA-256 password hashing
- Parameterized SQL queries to prevent SQL Injection
- Multi-threaded client handling
- Passwords are never stored in plain text

## Learning Concepts

This project demonstrates:

- Socket Programming
- Client-Server Architecture
- SQLite Database
- Password Hashing
- SQL Queries
- SQL Injection Prevention
- Python Threading
- Authentication Systems

## Future Improvements

- User Registration
- Password Reset
- SSL/TLS Encryption
- AES Encrypted Communication
- Graphical User Interface (Tkinter or PyQt)
- Logging System
- Role-Based Authentication
- Session Management

## Author

Created by **S. Md. Nihaal**

