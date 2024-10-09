# Inventory Management System API

This project is a backend API for a simple Inventory Management System built using Django Rest Framework. It supports CRUD operations on inventory items, integrated with JWT-based authentication for secure access. The system uses PostgreSQL for the database and Redis for caching.

## Features

- User registration and authentication using JWT
- CRUD operations for inventory items
- Redis caching for improved performance
- PostgreSQL database for data storage
- Comprehensive logging system
- Unit tests for API endpoints

## Prerequisites

- Python 3.8+
- PostgreSQL
- Redis

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/inventory-management-system.git
   cd inventory-management-system
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the PostgreSQL database:
   - Create a new database named `inventory_db`
   - Update the database configuration in `inventory_management/settings.py` with your PostgreSQL credentials

5. Set up Redis:
   - Ensure Redis is running on localhost:6379
   - If your Redis configuration is different, update the CACHES setting in `inventory_management/settings.py`

6. Apply migrations:
   ```
   python manage.py migrate
   ```

7. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```

## Running the Server

To start the development server, run:

```
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`.

## API Endpoints

### Authentication

- `POST /api/auth/register/`: Register a new user
- `POST /api/auth/login/`: Login and receive JWT tokens
- `POST /api/auth/token/`: Obtain JWT tokens
- `POST /api/auth/token/refresh/`: Refresh JWT token

### Inventory Items

- `GET /api/items/`: List all inventory items
- `POST /api/items/`: Create a new inventory item
- `GET /api/items/{id}/`: Retrieve a specific inventory item
- `PUT /api/items/{id}/`: Update a specific inventory item
- `DELETE /api/items/{id}/`: Delete a specific inventory item

## Usage Examples

### Register a New User

```bash
curl -X POST http://localhost:8000/api/auth/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "newuser", "email": "newuser@example.com", "password": "securepassword"}'
```

### Login and Obtain Tokens

```bash
curl -X POST http://localhost:8000/api/auth/login/ \
     -H "Content-Type: application/json" \
     -d '{"username": "newuser", "password": "securepassword"}'
```

### Create an Inventory Item

```bash
curl -X POST http://localhost:8000/api/items/ \
     -H "Authorization: Bearer <your_access_token>" \
     -H "Content-Type: application/json" \
     -d '{"name": "New Item", "description": "Description of the new item", "quantity": 10}'
```

### Retrieve an Inventory Item

```bash
curl -X GET http://localhost:8000/api/items/1/ \
     -H "Authorization: Bearer <your_access_token>"
```

## Running Tests

To run the unit tests, use the following command:

```
python manage.py test
```

## Logging

Logs are stored in the `debug.log` file in the project root directory. You can configure the logging settings in `inventory_management/settings.py`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
