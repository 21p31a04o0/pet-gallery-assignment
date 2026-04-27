Pet Gallery Assignment
Project Overview

Pet Gallery is a Django REST API project that allows users to authenticate using JWT tokens, fetch random dog images from an external API, and manage favorite dogs.

Features
JWT Authentication (Login / Refresh Token)
Fetch Random Dog Image
Save Favorite Dogs
View Favorite Dogs
Delete Favorite Dogs
Django Admin Panel

Tech Stack
Python
Django
Django REST Framework
Simple JWT
SQLite
External Dog API (dog.ceo)

Installation & Setup
1. Clone Repository
           git clone https://github.com/21p31a04o0/pet-gallery-assignment.git
           cd pet-gallery-assignment
2. Create Virtual Environment
           python -m venv env
3.Activate Virtual Environment
           source env/Scripts/activate (windows i use so..)
4.install django
          pip install djangoframework
5.Run Migrations
          python manage.py makemigrations
          python manage.py migrate
6.Run server
          python manage.py runserver
   
API ENDPOINTS
Authentication
Login

Request Body:

{
  "username": "your_username",
  "password": "your_password"
}

Response:

{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}


Refresh Token
POST /api/refresh/

Request Body:

{
  "refresh": "your_refresh_token"
}


Random Dog
Get Random Dog
GET /api/dogs/random/

Response:

{
  "breed": "husky",
  "image_url": "https://..."
}
Favorites
Get All Favorites
GET /api/favorites/
Add Favorite
POST /api/favorites/

Request Body:

{
  "breed": "husky",
  "image_url": "https://..."
}
Delete Favorite
DELETE /api/favorites/{id}/

Admin Access
http://127.0.0.1:8000/admin/

Author
Harika

---
