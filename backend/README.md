# House Valuations Backend

This are the instructions to only run the BE locally without using Docker.

- [Poetry](https://python-poetry.org/docs/)

### Installation

1. Install Poetry:
    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2. Generate `.env` files:
    ```sh
    cp frontend/.env.example frontend/.env
    cp backend/.env.example backend/.env
    ```

3. Install dependencies using Poetry:
    ```sh
    cd backend
    poetry shell
    poetry install
    ```

### Running the FastAPI Application

1. Start the FastAPI application:
    ```sh
    poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

2. Access the application in your web browser at `http://localhost:8000`.
