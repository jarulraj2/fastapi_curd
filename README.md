FastAPI CRUD Project

Overview

This project is a FastAPI-based CRUD application that includes two modules: items and users. It allows users to create, read, update, and delete data using a RESTful API.

Features

Item Module: Manage items with full CRUD operations

User Module: Manage users with full CRUD operations

SQLAlchemy ORM: Database integration

Pydantic Models: Data validation

Uvicorn: ASGI server for running FastAPI

Dependency Injection: Using FastAPI's Depends

Installation

1. Clone the Repository

 git clone https://github.com/YOUR_USERNAME/fastapi_crud.git
 cd fastapi_crud

2. Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Configure Database

Modify database.py to set up your SQLAlchemy database connection.

5. Run the Application

uvicorn main:app --host 127.0.0.1 --port 8000 --reload


Running with Docker (Optional)

To run the application inside a Docker container:

docker build -t fastapi_app .
docker run -p 8000:8000 fastapi_app

Testing the API

You can test the API using:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

License

This project is licensed under the MIT License.

Author

Developed by [jarulraj2![fastapi_swagger](https://github.com/user-attachments/assets/4a1cc58f-336f-4b00-9e95-8e0f56b3f8b6)
]

