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
    **Make sure to set up the API Keys for the provider endpoints. The API container won't work if they are not set.** 

2. Start Docker containers:
    ```sh
    docker compose up -d
    ```

### Usage

Once the Docker containers are up and running, you can access the application via your web browser at `http://localhost:5173`.

**If the application in the frontend is being access from another port make sure to add that url to the BACKEND_CORS_ORIGINS array and restart the BE server or the API will fail**


### Docs

`http://localhost:8000/docs`

### Code Considerations and Architecture Improvements
- Provider data such as API keys and endpoints could be stored in a database. Due to time constraints, they are currently stored in environment variables.
- The list of provider adapters to be ran could also be retrieved from a database based on different conditions (like a provider being active) and that list could be used in the use case.
- Depending on the reliability of the providers we could cache the response in our own system, such as Redis, to improve response time and avoid third party errors. That cache would need to be cleared depending on the provider conditions or business rules.
