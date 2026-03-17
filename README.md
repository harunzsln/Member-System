# Member Management System (Python & JSON)

A simple, local member management system built with Python that utilizes **JSON** for data persistence. This project demonstrates basic CRUD operations, user authentication, and a simulated activation code logic.

## 🚀 Features

* **Sign In (Login):** Authenticates existing users based on their credentials stored in the JSON database.
* **Log In (Sign Up):** Handles new user registration with password confirmation and a simulated activation code verification.
* **Forget Password:** Allows users to reset their passwords by verifying an activation code sent to a local text file.
* **Data Persistence:** All user records are stored in a structured `users.json` file.

## 🛠️ Setup and Usage

1.  **Clone or Download:** Ensure you have the project files in a directory.
2.  **Run the Application:** Execute the script using Python 3:
    ```bash
    python3 system.py
    ```
3.  **Interaction:** Follow the on-screen menu to navigate between options (Sign In, Sign Up, etc.).

## 📁 File Structure

* `system.py`: The main application logic containing the `System` class and flow control.
* `users.json`: The local database file where user information (username, password, email) is stored.
* `activation.txt`: A temporary file used to store generated activation codes for registration and password resets.

## 📝 Important Note

> [!WARNING]
> This system is developed for educational purposes. Passwords are currently stored as **plain text** in the JSON file. For a production-ready application, password hashing (e.g., using `bcrypt`) is highly recommended.

## 🛠️ Requirements
* Python 3.x
* `json` and `random` (Standard Python libraries)
