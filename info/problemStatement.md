## Objective:

Develop a robust and scalable FastAPI application to manage a Configuration Management system for onboarding Organisations from each country. The API will provide functionalities for CRUD (Create, Read, Update, Delete) operations for managing configurations.

## Implementation Requirements:

We are an international logistics company which deals with international transactions. To smoothly conduct international transactions we need to have a robust system which is able to handle onboarding requirements of each and every country. For e.g. When we onboard a country in India we need their Business Name, PAN, GSTIN numbers but for USA the requirements might be different as onboarding a company in USA may require Business Name, some other type of registration number and other extra details.

You as a developer should design a solution which is capable of handling following requirements

1. `/create_configuration [POST]` - This API is responsible for creating a configuration of a country onboarding requirements

2. `/get_configuration/{country_code}  [GET]`- This API will  provide a configuration requirements of a country

3. `/update_configuration/ [POST]` - This API will update a configuration requirements of a country

4. `/delete_configuration/ [DELETE]` -  This API will delete a configuration requirements of a country

Database and ORM:

1. Utilize PostgreSQL as the relational database management system.
2. Employ SQLAlchemy as the Object-Relational Mapper (ORM) to interact with the database in a Pythonic way.
3. Define SQLAlchemy models for above requirements
4. Design FastAPI endpoints for CRUD operations on both Book and Category entities
5. Employ Pydantic data models (schemas) to define the request and response data structures for each endpoint, ensuring data validation and type safety.
6. Implement comprehensive error handling using FastAPI's built-in exception handling mechanisms. This should include handling potential database errors, validation errors, and other application-specific exceptions.
Evaluation Criteria:

1. Functionality (Correctness of CRUD operations, data validation, etc.)
2. Code Structure (Readability, maintainability, modularity)
3. Error Handling (Robustness, informative error messages)
4. Documentation (Clear, concise API documentation)
5. Database Schema Design and its understanding
6. Product requirements and what are all different scenarios you have handled

## Additional Notes:

1. Consider using environment variables for database connection details to enhance security and flexibility.
2. Include comments and docstrings in your code to explain its purpose and behavior.