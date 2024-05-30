# Recipe Meal Planner

This project is a Recipe Meal Planner built with Django. It allows users to register, log in, and manage recipes. Users can perform CRUD (Create, Read, Update, Delete) operations on recipes and generate a PDF of their meal plan.

## Features

- User registration and authentication
- CRUD operations for recipes
- Generate PDF for meal plans
- User-specific data management

## Requirements

- Python 3.x
- Django 3.x or 4.x
- ReportLab (for PDF generation)

## Setup Instructions

### 1. Clone the Repository

```sh
 git clone https://github.com/yourusername/recipe-meal-planner.git
 cd recipe-meal-planner
```

### 2. Create and Activate a Virtual Environment

```sh
 python -m venv venv
 source venv/Scripts/activate  # On Mac use `venv\bin\activate`
```

### 3. Install Dependencies

```sh
 pip install -r requirements.txt
```

### 4. Apply Migrations

```sh
 python manage.py migrate
```

### 5. Create a Superuser

```sh
 python manage.py createsuperuser
```

### 6. Run Development Server

```sh
 python manage.py runserver
``` 

### 7. Access the Application

```sh
 Open web browser and go to `http://127.0.0.1:8000`.
``` 