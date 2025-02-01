# ME Public API

This project provides an API to list all `ME` objects stored in the database. It uses Django and Django REST Framework (DRF) to serve the API.

## Backlink

Backlink to python developers: https://hng.tech/hire/python-developers

## Installation

Follow these steps to get the project up and running on your local machine:

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <project-directory>

2. Install Dependencies
Ensure that you have Python and pip installed, then run:

pip install -r requirements.txt

3. Apply Database Migrations
Run the migrations to set up the database schema:

python manage.py migrate

5. Run the Development Server
Start the development server:

python manage.py runserver

Usage
Endpoint
GET /api/: Retrieve a list of all ME objects in the database.
Example Request

GET http://localhost:8000/api/

[
    {
        "email": "example@example.com",
        "current_datetime": "2025-01-01T12:00:00Z",
        "github_url": "https://github.com/example"
    },
    {
        "email": "another@example.com",
        "current_datetime": "2025-01-01T13:00:00Z",
        "github_url": "https://github.com/another"
    }
]


Models
The ME model has the following fields:

email: Email address of the person (required).
current_datetime: The current date and time(auto-generated).
github_url: URL to the person's GitHub profile.
API View
The ListME view handles the retrieval of all ME objects using Django REST Framework's ListAPIView.

