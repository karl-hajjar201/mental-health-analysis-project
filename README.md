# Challenge 1: Data Scientist

This is an application to return insights about the 'university_mental_health_iot_dataset.csv'

## Frameworks Used

FastAPI – Used to build the API. It provides automatic Swagger documentation (/docs).

Pydantic – Used to define and validate request/response schemas and auto-generated OpenAPI docs.

SQLite – Lightweight relational database used for storing daily stress insights. 

SQLAlchemy – SQL ORM for managing database models and queries in Python.

Flake8 – Code linter that enforces Python style guidelines (PEP8) to maintain clean and readable code.

Pytest – Testing framework used to write and run automated tests for the API endpoints.


## Exploratory Data Analysis

EDA was performed in a jupyter notebook included in this repo titled 'EDA.ipynb'. Main insights were collected using a correlation matrix. The notebook makes use
of Python libraries such as Pandas, Seaborn, and Matplotlib for analysis. 

## Setup Instructions


### Create Virtual Environment in project directory
```bash
 python -m venv .venv
 source .venv/bin/activate
```

### Install dependencies
```bash
 pip install -r requirements.txt
 ```

### Run application. This will seed the database.
```bash
uvicorn main:app --reload
```


## Endpoints

- GET /mental-insights
- GET /daily-insight
- GET /docs


Documentation on expected use of the API can be found at /docs.

## Tests

Tests can be run with the command 
```bash
python -m pytest tests/
```

## Linting

Linting can be run with the command
```bash
 flake8 {file_name}
```

# Lambda Implementation
I completed this exercise using FastAPI because I am more comfortable with it. I implemented the first endpoint (GET /mental-insights) using Lambda in addition. To test this implentation, install AWS SAM.

Then run 
``` bash
sam local start-api
```

GET /mental-insights will now be available.