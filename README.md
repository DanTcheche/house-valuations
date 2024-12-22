# house-valuations
Full stack application to compare house valuations.


## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/compose/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. Generate `.env` files:
    ```sh
    cp frontend/.env.example frontend/.env
    cp backend/.env.example backend/.env
    ```

2. Start Docker containers:
    ```sh
    docker compose up -d
    ```

### Usage

Once the Docker containers are up and running, you can access the application via your web browser at `http://localhost:5173`.

### Architecture Improvements

- Provider data such as API keys and endpoints could be stored in a database. Due to time constraints, they are currently stored in environment variables.
