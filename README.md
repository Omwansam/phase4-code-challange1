# Heroes and Powers Code API

This project is a Flask-based API for managing heroes and their associated powers. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on heroes, powers, and their associations.

## Features

- Retrieve a list of heroes and their details.
- Retrieve a specific hero by ID.
- Retrieve a list of powers and their details.
- Retrieve a specific power by ID.
- Update power descriptions.
- Create associations between heroes and powers with strength attributes.

## Technologies Used

- Python
- Flask
- SQLAlchemy
- SQLite (or your preferred database)
- Alembic (for migrations)

## Prerequisites

Before running the project, ensure you have the following installed on your machine:

- Python 3.6 or later
- pip (Python package installer)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Omwansam/phase4-code-challange1.git
   cd  phase4-code-challange1

2. **Create the virtual environment**:

    ```bash
   pipenv install

3. **Activate the virtual environment**:

    ```bash
   pipenv shell

4. **Install the required packages**:

    ```bash
   pip install -r requirements.txt 

5. **Move the set up directory**:

    ```bash
   cd server   

6. **Set up the database**:

    ```bash
   flask db upgrade

7. **Seed the Database**:

    ```bash
   python3 seed.py

8. **Set up flask environment variable**:

    ```bash
   export FLASK_APP=app.py
   export FLASK_RUN_PORT=5555

9. **Run the application**:

    ```bash
   python3 app.py

This will start the Flask development server. By default, it runs on http://127.0.0.1:5555/
