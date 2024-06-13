# Approach

## Overview

The goal of this project was to create a robust and scalable FastAPI application for managing a Configuration Management system that handles onboarding requirements for organizations from various countries. The API supports CRUD (Create, Read, Update, Delete) operations to manage configurations, catering to different country-specific requirements. 

## Steps I recollected after project conclusion

### 1. Project Setup

- **Initialize FastAPI Project**: 
   - Created a new FastAPI project structure.
   - Installed necessary dependencies: `fastapi`, `uvicorn`, `sqlalchemy`, `pydantic`, `psycopg2-binary`.

- **Database Configuration**:
   - Chose PostgreSQL as the database management system for its robustness and scalability.
   - Used SQLAlchemy as the ORM to interact with the PostgreSQL database in a Pythonic way.
   - Created a `config.py` file to manage configuration settings and used environment variables for database connection details to enhance security and flexibility.

### 2. Database Models

- **Define Models**:
   - Created an SQLAlchemy model `Configuration` representing the configurations required for onboarding organizations.
   - The model includes fields such as `country_code`, `business_name`, `registration_number`, and `extra_details`.

### 3. Schemas

- **Pydantic Schemas**:
   - Defined Pydantic models in `schemas.py` for request and response validation.
   - Created schemas for `ConfigurationCreate`, `ConfigurationUpdate`, and `Configuration` to ensure data validation and type safety.

### 4. CRUD Operations

- **CRUD Functions**:
   - Implemented CRUD functions in `crud.py` to interact with the database.
   - Functions include `get_configuration`, `create_configuration`, `update_configuration`, and `delete_configuration`.

### 5. API Endpoints

- **Create Endpoints**:
   - Defined API endpoints in `routes/configuration.py` for each CRUD operation.
   - Used dependency injection to manage database sessions with the help of FastAPI's `Depends`.

- **Error Handling**:
   - Implemented custom exception handlers for database-related errors and validation errors to ensure robust error handling.
   - Added `sqlalchemy_exception_handler`, `http_exception_handler` and `generic_exception_handler` to return informative error messages and appropriate HTTP status codes.

### 6. Modular Code Structure

- **Refactor Code**:
   - Organized code into separate modules to enhance readability and maintainability.
   - Moved route definitions to a dedicated module `routes/configuration.py`.
   - Included the router in the main application with a prefix and tags for better documentation and organization.

### 7. Testing

- **Endpoint Testing**:
   - Tested each endpoint using `curl` and Postman to ensure that CRUD operations work as expected.
   - Verified that partial updates work correctly with the PATCH method, ensuring only specified fields are updated.

