# FatAPI Project

## Overview

FatAPI is a FastAPI-based web application that provides a RESTful API for managing a collection of books and includes various endpoints for greetings and header information retrieval. This project demonstrates the use of FastAPI to create a simple yet functional API with CRUD operations for books and additional utility endpoints.

## Features

- **Greeting Endpoints**: Multiple endpoints to return personalized greeting messages based on query parameters or path variables.
- **Book Management**: CRUD operations to create, read, update, and delete book records.
- **Header Retrieval**: Endpoint to retrieve and return HTTP request headers.
- **Data Validation**: Uses Pydantic models (`Book`, `BookUpdateModel`, `BookModel`) for request and response validation.
- **Error Handling**: Proper HTTP status codes and exception handling for invalid requests or missing resources.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn (for running the server)
- Pydantic (for data validation)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Mayejacob/fast-api-bookify.git
   cd fatapi

   fastapi dev src/
   ```
