# User Management API

A simple REST API for managing users built with FastAPI.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### 1. Create User
- **POST** `/users/`
- Request Body:
```json
{
    "id": 1,
    "name": "John Doe",
    "phone_no": "1234567890",
    "address": "123 Main St"
}
```

### 2. Get User by ID
- **GET** `/users/{id}`

### 3. Search Users by Name
- **GET** `/users/search?name={name}`

### 4. Update User
- **PUT** `/users/{id}`
- Request Body:
```json
{
    "name": "John Updated",
    "phone_no": "9876543210",
    "address": "456 Updated St"
}
```

### 5. Delete User
- **DELETE** `/users/{id}`

## API Documentation

Once the server is running, you can access:
- Interactive API docs (Swagger UI): `http://localhost:8000/docs`
- Alternative API docs (ReDoc): `http://localhost:8000/redoc` 
