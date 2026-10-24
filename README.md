# Python Course Management System

A terminal-based Course Management System developed using Python, Object-Oriented Programming (OOP), and MySQL. The application provides user registration and login functionality along with operations to manage course records.

## Features

- **User Registration:** Register users to access the application.
- **User Login:** Authenticate users using their login credentials.
- **View Courses:** Display available courses and their details.
- **Add Course:** Add new courses to the database.
- **Edit Course:** Update existing course information.
- **Delete Course:** Remove courses from the database.
- **Database Integration:** Store and manage course and user records using MySQL.
- **Menu-Driven Interface:** Perform operations through an interactive terminal menu.

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- MySQL
- MySQL Connector/Python
- SQL
- Visual Studio Code

## Project Structure

```text
python-course-management-system/
│
├── course_management-oops_terminal.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
    ├── main-menu.png
    ├── course-list.png
    └── course-management.png
```

## Prerequisites

Before running the application, ensure that you have:

- Python 3.10 or later
- MySQL Server
- A MySQL account with the required database permissions

## Installation and Setup

### 1. Download the Project

Clone the repository or download the project files from GitHub.

### 2. Install Dependencies

Open the project folder in VS Code and install the required Python package:

```bash
python -m pip install -r requirements.txt
```

### 3. Configure MySQL

Ensure that the MySQL server is running.

Create the database required by the application if it does not already exist.

The application currently uses the `cms` database. Verify the database name and connection settings in the Python source code.

Configure the MySQL hostname, username, and password appropriately for your local environment.

**Security note:** Never publish database passwords or other secret credentials in this repository.

### 4. Run the Application

Run the following command from the project directory:

```bash
python course_management-oops_terminal.py
```

The application should display its terminal interface, allowing you to register, log in, and manage course records.

## Screenshots

Screenshots demonstrating the application's interface and functionality will be added here.

### Main Menu

![Course Management System Main Menu](screenshots/main-menu.png)

### Course List

![Course List](screenshots/course-list.png)

### Course Management

![Course Management Operations](screenshots/course-management.png)

## Security Considerations

This project is intended as a learning application. Database credentials should be configured securely, and user passwords should be stored using an appropriate password-hashing mechanism rather than as plain text.

## Future Enhancements

- Implement secure password hashing.
- Improve input validation and exception handling.
- Add course search functionality.
- Introduce role-based access control.
- Develop a graphical user interface.

## Author

Developed as a Python programming project.
