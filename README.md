# Employee Management REST API
This project is a Django REST Framework based Employee Management API.
It supports CRUD operations, JWT authentication, filtering, pagination,
and proper RESTful error handling.

## Features
- JWT Authentication (secured APIs)
- Create, Read, Update, Delete Employees
- Filtering by department and role
- Pagination (10 records per page)
- Validation and proper HTTP status codes
- Unit testing support

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (default)
- JWT Authentication
<!-- requirment.text file install -->
asgiref==3.11.0
Django==5.1
django-cors-headers==4.9.0
djangorestframework==3.16.1
python-dotenv==1.2.1
sqlparse==0.5.5
tzdata==2025.3


## Setup Instructions

1. Clone the repository
```bash
git clone <repo-url>
cd employee_api
# Create virtual environment and install dependencies
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
# Run migrations
python manage.py makemigrations
python manage.py migrate
# Create superuser
python manage.py createsuperuser
# Run the server
python manage.py runserver
#Authentication (JWT)
POST /api/token/
# if  Request Body:
{
    "username":"Rajendra",
    "password":"admin@123"
}
# then get responce 
{
  "access": "jwt-access-token",
  "refresh": "jwt-refresh-token"
}
#  Use the access token in headers,then access all api endpoint
# example like 
# Create Employee
POST /api/employees/
# get data for employee and filter and pagination
GET /api/employees/
GET /api/employees/?page=2
GET /api/employees/?department=HR
GET /api/employees/?role=Developer
# Update Employee
PUT /api/employees/{id}/
# Delete Employee
DELETE /api/employees/{id}/
# if  Running Tests
python manage.py test employees
