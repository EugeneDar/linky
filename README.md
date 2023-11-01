## Description
A simple API for link shortening built on FastAPI, Redis, Nginx

## How to run servers, balancer and database

    docker-compose up -d --build

## How to test

    curl -X POST "http://localhost:8000/create?url=https://example.com"

    curl -X GET http://localhost:8000/link/KBQuX7qs
