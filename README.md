# WebCashier

WebCashier is a Django-based web application for managing cashier transactions and products.

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
