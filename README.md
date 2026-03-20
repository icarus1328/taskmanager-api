# Task Manager API

A RESTful Task Manager API built using **FastAPI** and **SQLAlchemy**, supporting user management and task operations.  
This project demonstrates backend development fundamentals including CRUD operations, relational database design, and API structuring.

---

## 🚀 Features

### User Management
- Create a new user
- Get all users
- Get user by ID
- Delete a user

### Task Management
- Create a task
- Get task by ID
- Get all tasks for a specific user
- Update a task
- Delete a task

---

## 🛠 Tech Stack

- **Backend Framework:** FastAPI  
- **Database:** SQLite  
- **ORM:** SQLAlchemy  
- **Migrations:** Alembic  
- **Validation:** Pydantic  
- **Server:** Uvicorn  

---

## 📂 Project Structure
task-manager-api/
│
├── app/
│ ├── main.py # FastAPI application & routes
│ ├── database.py # DB connection & session setup
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│
├── alembic/ # Database migrations
├── alembic.ini
├── requirements.txt
└── README.md


---

## 🧱 Database Design

### Users Table
| Column      | Type    | Description          |
|------------|--------|----------------------|
| id         | Integer | Primary Key         |
| username   | String  | Unique              |
| email      | String  | Unique              |
| created_at | DateTime | Timestamp           |

### Tasks Table
| Column      | Type     | Description                  |
|------------|----------|------------------------------|
| id         | Integer  | Primary Key                  |
| title      | String   | Required                     |
| description| String   | Optional                     |
| completed  | Boolean  | Default: False               |
| priority   | String   | low / medium / high          |
| due_date   | DateTime | Optional                     |
| created_at | DateTime | Timestamp                    |
| updated_at | DateTime | Timestamp                    |
| user_id    | Integer  | Foreign Key → Users.id       |

---

## ⚙️ Setup & Installation

### 1. Clone the repository
git clone https://github.com/icarus1328/taskmanager-api.git
cd task-manager-api

### 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run database migrations
alembic upgrade head

### 5. Start the server
uvicorn app.main:app --reload


---

## 🌐 API Documentation

Once the server is running, access:

- Swagger UI:  http://127.0.0.1:8000/docs


---

## 📌 API Endpoints

### Users

| Method | Endpoint        | Description        |
|--------|----------------|--------------------|
| POST   | /users         | Create user        |
| GET    | /users         | Get all users      |
| GET    | /users/{id}    | Get user by ID     |
| DELETE | /users/{id}    | Delete user        |

### Tasks

| Method | Endpoint                  | Description                 |
|--------|---------------------------|-----------------------------|
| POST   | /tasks                    | Create task                 |
| GET    | /tasks/{id}               | Get task by ID              |
| GET    | /tasks/user/{user_id}     | Get tasks by user           |
| PUT    | /tasks/{id}               | Update task                 |
| DELETE | /tasks/{id}               | Delete task                 |

---

## 🧠 Learning Outcomes

- Designed and built a RESTful API using FastAPI  
- Implemented CRUD operations with SQLAlchemy  
- Structured backend using models, schemas, and routes  
- Managed database migrations using Alembic  
- Built relational database design with foreign keys  
- Practiced request validation and response modeling  

---

## 🔮 Future Improvements

- Add authentication (JWT-based login system)  
- Implement filtering (by status, priority, due date)  
- Add pagination for large datasets  
- Introduce role-based access control  

---

## 📄 License

This project is for learning and educational purposes.