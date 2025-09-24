# BUDGET101 
A RESTful API for managing personal expenses and budget categories. This is my first API project, focused on learning how to use Python and Django for an API. 

## Tech Stack
- Python 
- Django
- Django REST Framework
- PostgreSQL

## Features
- User registration and login
- Create categories for expenses
- Define a budget for each category
- Register expenses including amount, date, description and category
- See total expenses amount and available spending amount for each category
- List, Create, Update and Delete categories and expenses

## Installation for Local Development
1. Clone the repository 
    ```bash
    `git clone https://github.com/isabeleguimaraes/budget101`

2. Navigate to the folder
    `cd budget101`

3. Create a virtual environment
```bash
    python -m venv venv
    ### Windows PowerShell
    .\venv\Scripts\Activate.ps1

    ### Linux/Mac
    source venv/bin/activate
```
4. Install dependencies
    `pip install -r requirements.txt`

5. Set environment variables
```bash
    $env:DB_NAME="budget101"
    $env:DB_USER="your_username"
    $env:DB_PASSWORD="your_password"
    $env:DB_HOST="localhost"
    $env:DB_PORT="5432"
```
6. Run migrations to create database tables:
    `python manage.py migrate`

7. Start the local development server:
    `python manage.py runserver`

## Available Endpoints

### Expenses
```bash
GET /api/expenses/ - Retrieve all expenses related to the user (name, amount, description, date, category)
POST /api/expenses/ - Register a new expense
PUT /api/expenses/{id}/ - Update an existing expense
PATCH /api/expenses/{id}/ - Partially update an existing expense
DELETE /api/expenses/{id}/ - Delete an existing expense
GET /api/expenses/{id}/ - Retrieve an specific expense
```
### Categories
```bash
GET /api/categories/ - Retrieve all existing categories related to the user (name, budget, total expenses, available amount)
POST /api/categories/ - Create a new category
GET /api/categories/{id}/ - Retrieve an specific category
PUT /api/categories/{id}/ - Update an existing category
PATCH /api/categories/{id}/ - Partially update an existing category
DELETE /api/categories/{id}/ - Delete an existing category
 ```
 ### Authentication
 ```bash
 GET /api/signup/ - Register a user to use the application
 GET /api/login/ - Login with a registered user
```
## Authentication

This API uses token-based authentication. Include your token in the Authorization header:
`Authorization: Bearer YOUR_TOKEN_HERE`
To obtain a token, register through the sign up endpoint.
