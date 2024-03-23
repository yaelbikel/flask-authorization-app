# User Authentication and Authorization with Flask

This Flask application provides a simple user authentication and authorization system with token-based access control.

## Features

- **Registration**: Users can register with a unique username and password.
- **Login**: Registered users can login to obtain an access token.
- **Token-based Authentication**: The application uses JWT (JSON Web Tokens) for token-based authentication.
- **Role-based Authorization**: Users are assigned roles (e.g., USER) upon registration, and certain endpoints are restricted based on these roles.
- **File Permissions**: Users can request file permissions based on their roles.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yaelbikel/flask-authorization-app.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:

   ```bash
   python3 main.py
   ```

2. Access the endpoints using a tool like cURL or Postman.

    - `/register` (POST): Register a new user with a unique username and password.
    - `/login` (POST): Log in with registered credentials to obtain an access token.
    - `/user` (GET): Get user information (requires valid token).
    - `/file_permissions` (GET): Get file permissions for a specific file (requires valid token and file parameter).

## Endpoints

- **POST `/register`**
    - Register a new user.
    - Request Body: JSON with `username` and `password`.
    - Returns:
        - Success (201): User registered successfully.
        - Error (400): User already exists.

- **POST `/login`**
    - Log in to obtain an access token.
    - Authentication: Basic Auth with `username` and `password`.
    - Returns:
        - Success (200): JSON with access token.
        - Error (401): Invalid credentials.

- **GET `/user`**
    - Get user information.
    - Authentication: Bearer Token.
    - Returns:
        - Success (200): JSON with user information.
        - Error (401): Unauthorized.

- **GET `/file_permissions`**
    - Get file permissions for a specific file.
    - Query Parameters: `file` (name of the file).
    - Authentication: Bearer Token.
    - Returns:
        - Success (200): JSON with file permissions.
        - Error (400): File parameter missing.
        - Error (401): Unauthorized.
        - Error (404): File not found.

## Code Examples

A working code example can be found in example.py