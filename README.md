#  My Home Workout API

A secure, RESTful API built with Flask to help users plan and manage home workout routines. Supports user authentication, workout tracking, and exercise assignments.

---

## Live Link

 Deployed on Render:  https://home-workout-backend-server.onrender.com

---

##  Features

 User Registration & Login 
 JWT-based Authentication 
 Create, View, and Delete Workouts 
 Assign Exercises to Workouts 
 PostgreSQL for persistent data 
 CORS enabled for frontend integration 
 MVC structure 
 Seed script for testing data 

---

## Authentication Flow

- `POST /api/auth/register`: Create a new user 
- `POST /api/auth/login`: Returns a JWT token 
- For protected routes, include the JWT in the header:

```http
Authorization: Bearer <your_token>
```

---

##  Technologies Used

- Python 3
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Flask-JWT-Extended
- psycopg2-binary
- Pipenv
- PostgreSQL
- Render for deployment

---

##  Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/phase4-workout-team/Home-Workout-Backend.git
cd Home-Workout-Backend
```

### 2. Install Dependencies

```bash
pipenv install
pipenv shell
```

### 3. Configure the Database

Create your PostgreSQL DB locally or on Render (if testing locally):

```sql
CREATE DATABASE my_home_workout;
```

### 4. Set Up Environment Variables

Create a `.env` file and add:

```env
DATABASE_URI=postgresql://<user>:<password>@localhost:5432/my_home_workout
JWT_SECRET_KEY=your_secret_key
```

(Or add these to Render's environment variables panel)

### 5. Run Migrations and Seed

```bash
export FLASK_APP=wsgi.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

---

##  Deployment on Render

- Add your GitHub repo to Render
- Set Root Directory = `.`
- Set Build Command = `pip install pipenv && pipenv install`
- Set Start Command = `gunicorn wsgi:app`
- Add Environment Variables:
  - `DATABASE_URI`
  - `JWT_SECRET_KEY`
- Click “Deploy”

---

##  Example Requests

### Register

```http
POST /api/auth/register
Content-Type: application/json

{
  "username": "brian",
  "email": "brian@example.com",
  "password": "password123"
}
```

### Login

```http
POST /api/auth/login
Content-Type: application/json

{
  "username": "brian",
  "password": "password123"
}
```

Response:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUz..."
}
```

---

##  Postman / Thunder Client Setup

1. Import your live API URL.
2. Test `/register` and `/login`.
3. Save the JWT token from `/login` and use it in the `Authorization` header as:
   ```
   Bearer <your_token>
   ```
4. Then access protected routes like `/api/workouts/`.

---

##  Notes

- All workout routes are tied to the current logged-in user.
- You must be logged in to create, view, or delete workouts.
- Seed data includes users, exercises, and example workouts.

---
