# HospitalDemo

HospitalDemo is a Django-based web application for managing hospital operations, including patient records, appointments, and staff information.

## Features

- Patient management
- Appointment scheduling
- Staff management
- User authentication
- Responsive design using Bootstrap 5

## Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/hospitaldemo.git
    cd hospitaldemo
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open your browser and go to `http://127.0.0.1:8000`.