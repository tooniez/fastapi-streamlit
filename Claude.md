# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Development Commands
- **Install all dependencies**: `make install`
- **Start FastAPI backend server**: `make run-api` (or `fastapi dev api/server.py`)
- **Start Streamlit frontend**: `make run-streamlit` (or `streamlit run app/streamlit_app.py`)
- **Format code**: `make format` (runs `black .`)
- **Run tests**: `make test` (runs `pytest`)

## Code Architecture
- **Backend (FastAPI)**: `api/server.py` - Contains RESTful API routes, CORS support, with planned OAuth authentication and ORM database integration.
- **Frontend (Streamlit)**: `app/streamlit_app.py` - Contains the Streamlit application with user authentication flow and API request demonstrations.
- **Testing**: `tests/` directory contains `test_api.py` and `test_streamlit_app.py`, run with `pytest`.
- **Pre-commit hooks**: `.pre-commit-config.yaml` configured with basic pre-commit hooks for code quality.
- **Docker**: Dockerfiles in `api/` and `app/` directories for containerized deployment.

## Setup Instructions
1. Install dependencies: `make install`
2. Start the FastAPI backend: `make run-api`
   - API docs available at `http://localhost:8000/docs` (Swagger UI)
   - ReDoc at `http://localhost:8000/redoc`
3. In a separate terminal, start the Streamlit app: `make run-streamlit`
4. Run tests: `make test`

## Notes
- The project uses `black` for code formatting
- Tests cover both the FastAPI backend and Streamlit frontend components