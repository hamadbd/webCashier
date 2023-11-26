# WebCashier

# Project Name

## Overview
This project is a RESTful API built using Django and Django Rest Framework, allowing users to interact with the system through endpoints. It includes user authentication, product management, and transaction handling. The code has been tested and successfully executes.

## Setup
To run this project, ensure you have Django and Django Rest Framework installed. If not, use the following pip commands:

```bash
pip install django
pip install djangorestframework
```


Make sure to update the `settings.py` file according to your local environment configurations, such as database settings or any additional installed apps.

## Usage
To execute the project, create a virtual environment and install the required packages. Then, run the Django development server and use tools like Postman or Python requests to interact with the available APIs.

## Structure
The project contains models for CustomUser, Product, Transaction, along with corresponding serializers and views for API endpoints.




## Prerequisites

Make sure you have Python and pip installed.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/WebCashier.git
    cd WebCashier
    ```

2. Create a virtual environment:

    ```bash
    python -m venv myenv
    ```

3. Activate the virtual environment:

    - **Windows**:

        ```bash
        myenv\Scripts\activate
        ```

    - **Unix or MacOS**:

        ```bash
        source myenv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Setting Up the Database

1. Create a MySQL database:

    ```sql
    CREATE DATABASE webcashier_db;
    ```

2. Update the settings.py file in the WebCashier folder with your MySQL database details:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'webcashier_db',
            'USER': 'yourusername',
            'PASSWORD': 'yourpassword',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

3. Run migrations to create database tables:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Running the Server

To start the development server, run:

```bash
python manage.py runserver
