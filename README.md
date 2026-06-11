# PRODIGY_BD_02

## Persistent Storage with Database Integration

This project is the second task of the Backend Web Development Internship at Prodigy InfoTech.

The goal of this task is to extend a basic REST API by integrating a relational database for persistent storage. The application uses PostgreSQL as the database management system and Django ORM for database operations.

---

## Features

* Create User
* Retrieve All Users
* Retrieve User by ID
* Update User Information
* Delete User
* UUID-based User Identification
* Input Validation
* PostgreSQL Integration
* Django ORM
* Database Migrations
* Environment Variables Configuration
* Persistent Data Storage
* Connection Reuse using `CONN_MAX_AGE`
* Swagger API Documentation

---

## Technologies Used

* Python
* Django
* Django REST Framework
* PostgreSQL
* Django ORM
* drf-spectacular
* python-decouple

---

## Project Structure

```text
PRODIGY_BD_02
│
├── config/
├── users/
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
├── README.md
└── PRODIGY_BD_02.postman_collection.json
```

---

## API Endpoints

| Method | Endpoint                     | Description       |
| ------ | ---------------------------- | ----------------- |
| GET    | `/api/users/`                | Get all users     |
| POST   | `/api/users/`                | Create a new user |
| GET    | `/api/users/<uuid:user_id>/` | Get a user by ID  |
| PUT    | `/api/users/<uuid:user_id>/` | Update a user     |
| DELETE | `/api/users/<uuid:user_id>/` | Delete a user     |

---

## User Schema

```json
{
  "id": "uuid",
  "name": "John Doe",
  "email": "john@example.com",
  "age": 25,
  "created_at": "2026-06-18T10:00:00Z",
  "updated_at": "2026-06-18T10:00:00Z"
}
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/X-hor/PRODIGY_BD_02.git
cd PRODIGY_BD_02
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
DB_NAME=prodigy_bd_02
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## Database Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE prodigy_bd_02;
```

Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Running the Project

```bash
python manage.py runserver
```

Server URL:

```text
http://127.0.0.1:8000/
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/api/docs/
```

OpenAPI Schema:

```text
http://127.0.0.1:8000/api/schema/
```

---

## Testing

The project can be tested using:

* Postman
* Swagger UI
* Browser requests for GET endpoints

A Postman collection is included in the repository.

---

## What I Learned

* Integrating PostgreSQL with Django
* Working with Django ORM
* Creating and applying database migrations
* Managing configuration using environment variables
* Implementing persistent storage
* Understanding database connections and connection reuse
* Building scalable REST APIs with Django REST Framework

---

## Author

Abdennour Lachab

Backend Web Development Intern at Prodigy InfoTech
