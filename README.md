# Hackathon E-Library

Hackathon E-Library is a web application designed to manage and browse digital book collections efficiently. The project is developed to provide an easy-to-use platform for users to access and manage their e-books.

## Project Structure

- `backend/` — Contains the backend logic built with Django.
- `frontend/` — React-based frontend for an interactive UI.
- `database/` — Stores information about books, users, and transactions.
- `.env` — Configuration file with sensitive environment variables.
- `requirements.txt` — Lists dependencies for the backend.
- `package.json` — Manages frontend dependencies.

## Features

### Backend (Django)
1. **User Authentication**
    - Register, login, and manage user sessions.
2. **Book Management**
    - Add, update, delete, and browse digital books.
3. **Search and Filtering**
    - Search books by title, author, or category.

### Frontend (React)
1. **User-Friendly Interface**
    - Intuitive UI for browsing and managing books.
2. **Responsive Design**
    - Optimized for mobile and desktop.
3. **Interactive Components**
    - Dynamic elements for enhanced user experience.

## Setup and Execution

### Install Backend Dependencies
```bash
pip install -r requirements.txt
```

### Start the Backend Server
```bash
python manage.py runserver
```

### Install Frontend Dependencies
```bash
cd frontend
npm install
```

### Start the Frontend
```bash
npm start
```

### Environment Variables Setup
Create a `.env` file and add:
```
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
REACT_APP_API_URL=your_backend_url
```

## Technologies Used
- **Django** — Backend framework
- **React** — Frontend framework
- **SQLite/PostgreSQL** — Database
- **dotenv** — Environment variable management

## Author
Hackathon E-Library — A digital book management system developed for efficient library handling.

