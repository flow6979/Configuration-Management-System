# Configuration Management System
The project involves creating a scalable FastAPI application for managing a Configuration Management system to handle onboarding requirements for organizations from various countries. It supports CRUD operations for country-specific configurations using PostgreSQL and SQLAlchemy, ensuring strong error handling, data validation, and a modular code structure for maintainability and readability.

## Getting Started

Follow these instructions to set up and run the project on your local machine.


### Prerequisites

Ensure you have the following installed:
- Python 3.8+
- PostgreSQL
- Git

### Installation

1. **Clone the repository**

   ```bash
   git clone 
   ```

   ```bash
   cd configuration-management-system
   ```

2. **Create a Virtual Environment**:

    ```bash
    python -m venv venv

    source venv/bin/activate   # Linux (my os)

            OR

    venv\Scripts\activate      # Windows
    ```

3. **Install the Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

### Database Setup

1. **Install PostgreSQL**:
    ```bash
    # for ubuntu (my os)
    sudo apt update

    sudo apt install postgresq

    ```
2. **Creating PostgreSQL user**:
    ```bash
    sudo -u postgres psql # log in as a superuser initially

    CREATE USER <username> WITH PASSWORD '<password>'; # creating PostgreSQL username and password
    ```

3. **Create a Database**:
    ```bash
    CREATE DATABASE <dbname>; 
    ```

4. **Grant Privileges**:
    ```bash
    GRANT ALL PRIVILEGES ON DATABASE <dbname> TO <username>;
    ```

5. **Set Up Environment Variables**:
    </br>
    Create a `.env` file in the project root and add your database connection URL:
    ```bash
    DATABASE_URL=postgresql://username:password@localhost/dbname
    ```

6. **Login as user to our db**:

    ```bash
    psql -U <username> -h localhost -d <dbname>

    ```

6. **To see table content**:
    ```bash
    SELECT * FROM <table_name>;
    ```

**IMPORTANT COMMANDS**
 - To check list of our db, we can use `\l`
 - To connecting with our database, we can use `\c <dbname>`
 - To list all tables in our db, we can use `\dt`

### Running the Application

1. **Apply Database Migrations**:
    </br>
    Ensure the database is up-to-date with the latest schema:
    ```bash
    alembic upgrade head
    ```

2. **Start the FastAPI Server**:
    </br>
    uvicorn app.main:app --reload
    ```bash
    uvicorn app.main:app --reload
    ```
    The application will be available at http://127.0.0.1:8000.
 