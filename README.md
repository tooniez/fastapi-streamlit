# FastAPI Streamlit Stack

This repository contains a full-stack application with a FastAPI backend and a Streamlit frontend.

## Features

### Backend (FastAPI)
- [ ] RESTful API routes
- [x] CORS (Cross-Origin Resource Sharing) support
- [ ] OAuth authentication
- [ ] ORM integration with a database

### Frontend (Streamlit)
- [ ] User authentication (login to server)
- [x] Demonstration of GET requests to the API backend
- [ ] Demonstration of POST requests to the API backend

## Setup

### Prerequisites
- Python 3.9+
- Streamlit
- FastAPI
- Pytest
- Black
- Docker

### Docker Setup

```shell
docker compose up
```


### Backend Setup
1. Navigate to the `api` directory
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Start the FastAPI server:
   ```
   uvicorn server:app --reload
   ```

### Frontend Setup
1. Navigate to the `app` directory
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```
   streamlit run streamlit_app.py
   ```

## Testing

- API and Streamlit tests: Run `make test`


## API Documentation
Once the backend server is running, you can access the API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

##  License

Copyright © 2024 [tooniez](https://github.com/tooniez). <br />
This project is [MIT](https://github.com/tooniez/fastapi-streamlit.git/blob/main/LICENSE) licensed.
