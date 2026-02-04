This project is a backend-focused community feed application built as part of the Playto Engineering Challenge.

## Features
- Posts with threaded (nested) comments
- Like system for posts and comments
- Karma-based leaderboard calculated for the last 24 hours
- Minimal React frontend to demonstrate API integration

----------------------------------------------------------------------------------------------------------------

## Tech Stack
- Backend: Django, Django REST Framework
- Frontend: React (Vite)
- Database: SQLite

----------------------------------------------------------------------------------------------------------------

## How to Run Locally

### Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

###Frontend
cd frontend
npm install
npm run dev

