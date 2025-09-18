from fastapi import APIRouter, status, Header
from fastapi.exceptions import HTTPException
from typing import Optional, List
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel, BookModel

book_router = APIRouter()


@book_router.get("/message")
async def read_root():
    return {"message": "Hello world"}


@book_router.get("/greet/{name}")
async def greet_name(name: str) -> dict:
    return {"message": f"Hello {name} welcome to fastapi"}


@book_router.get("/greet/user")
async def greet_name(name: str) -> dict:
    return {"message": f"Hello {name} welcome to fastapi"}


@book_router.get("/greet/user/{type}")
async def greet_name(type: str, age: int) -> dict:
    return {"message": f"Hello {type} welcome to fastapi, your age is {age}"}


# optional
@book_router.get("/greet")
async def greet_name(name: Optional[str] = "customer", age: Optional[int] = 30) -> dict:
    return {"message": f"Hello {name} welcome to fastapi, your age is {age}"}


@book_router.post("/create_book")
async def create_book(book_data: BookModel):
    return {
        "title": book_data.title,
        "author": book_data.author,
    }


@book_router.get("/get_headers", status_code=200)
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None),
):
    request_headers = {}

    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["Agent"] = user_agent
    request_headers["host"] = host

    return request_headers


@book_router.get("/", response_model=List[Book])
async def get_all_books():
    return books


@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    newBook = book_data.model_dump()

    books.append(newBook)

    return newBook


@book_router.get("/{book_id}")
async def update_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.patch("/{book_id}", status_code=status.HTTP_200_OK)
async def get_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update_data.title
            book["publisher"] = book_update_data.publisher
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language

            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
