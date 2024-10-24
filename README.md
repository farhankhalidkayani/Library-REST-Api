
# Library Management System API

This project is a RESTful API for managing a library's book collection using Django and Django Rest Framework (DRF). It allows users to perform CRUD operations on books, search for books by various fields, and filter the book list.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete books in the library.
- **Search Functionality**: Search for books by title, author, and genre.

## Technologies Used

- Python
- Django
- Django Rest Framework
- SQLite (default database)

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Django
- Django Rest Framework

### Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install django djangorestframework
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (optional)**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the server**:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Books

- **List all books**:  
  `GET /book/`

- **Create a new book**:  
  `POST /book/`  
  **Request Body**:
  ```json
  {
      "title": "Book Title",
      "author": "Author Name",
      "genre": "Book Genre",
      "publication_year": "YYYY-MM-DD",
      "availability_status": true
  }
  ```

- **Retrieve a specific book**:  
  `GET /book/{id}/`

- **Update a specific book**:  
  `PUT /book/{id}/`  
  **Request Body** (example):
  ```json
  {
      "title": "Updated Title",
      "author": "Updated Author",
      "genre": "Updated Genre",
      "publication_year": "YYYY-MM-DD",
      "availability_status": false
  }
  ```

- **Delete a specific book**:  
  `DELETE /book/{id}/`

### Search and Filter

You can search and filter books using query parameters:

- **Search**:  
  `GET /book/?search=keyword`  
  Searches in title, author, and genre.

## Project Structure

```
library_project/
│
├── main/                  # Main application directory
│   ├── migrations/        # Database migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          # Model definitions
│   ├── serializers.py     # Serializer definitions
│   └── views.py           # View definitions
│
├── library_project/       # Project settings directory
│   ├── __init__.py
│   ├── settings.py        # Settings configuration
│   ├── urls.py            # Root URL routing
│   └── wsgi.py
│
└── manage.py              # Project management script
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/) - The web framework used.
- [Django Rest Framework](https://www.django-rest-framework.org/) - Toolkit for building Web APIs.
