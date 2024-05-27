# 0x05. AirBnB Clone - RESTful API

## Project Overview

This project is part of the curriculum for learning Python, Back-end development, APIs, and web server implementation using Flask. It aims to build a RESTful API for the AirBnB clone web application.

- **Project Duration:** May 23, 2024, 6:00 AM - May 28, 2024, 6:00 AM

## Concepts

For this project, we focused on the following concepts:

- REST API
- AirBnB clone

## Resources

We referred to the following resources to complete this project:

- [REST API concept page](https://example.com)
- [Learn REST: A RESTful Tutorial](https://example.com)
- [Designing a RESTful API with Python and Flask](https://example.com)
- [HTTP access control (CORS)](https://example.com)
- [Flask cheatsheet](https://example.com)
- [What are Flask Blueprints, exactly?](https://example.com)
- [Flask](https://example.com)
- [Modular Applications with Blueprints](https://example.com)
- [Flask tests](https://example.com)
- [Flask-CORS](https://example.com)

## Learning Objectives

By the end of this project, we aimed to be able to explain the following without external help:

### General Concepts

- **What REST means:** REST (Representational State Transfer) is an architectural style for designing networked applications. It relies on a stateless, client-server, cacheable communications protocol — the HTTP.
- **What API means:** An API (Application Programming Interface) is a set of rules that allows different software entities to communicate with each other.
- **What CORS means:** CORS (Cross-Origin Resource Sharing) is a mechanism that allows restricted resources on a web page to be requested from another domain outside the domain from which the first resource was served.
- **What is an API:** An API is a set of definitions and protocols for building and integrating application software.
- **What is a REST API:** A REST API is an API that conforms to the constraints of REST architectural style and allows for interaction with RESTful web services.
- **Other types of APIs:** Examples include SOAP APIs, GraphQL APIs, and RPC APIs.
- **HTTP methods:** 
  - **Retrieve resource(s):** GET
  - **Create a resource:** POST
  - **Update a resource:** PUT or PATCH
  - **Delete a resource:** DELETE
- **How to request REST API:** Using HTTP methods like GET, POST, PUT/PATCH, DELETE with appropriate endpoints and headers.

## Project Structure

The project structure is as follows:

```
.
├── api
│   ├── __init__.py
│   ├── v1
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── views
│   │   │   ├── __init__.py
│   │   │   ├── places.py
│   │   │   ├── users.py
│   │   │   ├── amenities.py
│   │   │   └── reviews.py
├── models
│   ├── __init__.py
│   ├── base_model.py
│   ├── place.py
│   ├── user.py
│   ├── amenity.py
│   └── review.py
├── tests
│   ├── test_models
│   │   ├── __init__.py
│   │   ├── test_place.py
│   │   ├── test_user.py
│   │   ├── test_amenity.py
│   │   └── test_review.py
│   ├── test_api
│   │   ├── __init__.py
│   │   ├── test_places.py
│   │   ├── test_users.py
│   │   ├── test_amenities.py
│   │   └── test_reviews.py
├── README.md
└── requirements.txt
```

## Installation

To install and run the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/airbnb-clone-restful-api.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd airbnb-clone-restful-api
   ```
3. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```
4. **Activate the virtual environment:**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
5. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

To run the API, execute the following command:

```bash
python3 api/v1/app.py
```

The API will be available at `http://localhost:5000`.

## Endpoints

The API has the following endpoints:

### Users

- `GET /api/v1/users` - Retrieve all users
- `GET /api/v1/users/<user_id>` - Retrieve a specific user
- `POST /api/v1/users` - Create a new user
- `PUT /api/v1/users/<user_id>` - Update a user
- `DELETE /api/v1/users/<user_id>` - Delete a user

### Places

- `GET /api/v1/places` - Retrieve all places
- `GET /api/v1/places/<place_id>` - Retrieve a specific place
- `POST /api/v1/places` - Create a new place
- `PUT /api/v1/places/<place_id>` - Update a place
- `DELETE /api/v1/places/<place_id>` - Delete a place

### Amenities

- `GET /api/v1/amenities` - Retrieve all amenities
- `GET /api/v1/amenities/<amenity_id>` - Retrieve a specific amenity
- `POST /api/v1/amenities` - Create a new amenity
- `PUT /api/v1/amenities/<amenity_id>` - Update an amenity
- `DELETE /api/v1/amenities/<amenity_id>` - Delete an amenity

### Reviews

- `GET /api/v1/reviews` - Retrieve all reviews
- `GET /api/v1/reviews/<review_id>` - Retrieve a specific review
- `POST /api/v1/reviews` - Create a new review
- `PUT /api/v1/reviews/<review_id>` - Update a review
- `DELETE /api/v1/reviews/<review_id>` - Delete a review

## Testing

To run the tests, execute the following command:

```bash
pytest
```

This will run all the test cases available in the `tests` directory.

## Conclusion

This project provided us with a comprehensive understanding of building a RESTful API using Flask. We learned how to structure a Flask application, create and manage endpoints, handle HTTP methods, and test our application.

For any questions or suggestions, please contact:

- Tom Nyabuto
