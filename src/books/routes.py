from fastapi import APIRouter, status, Header, Depends
from fastapi.exceptions import HTTPException
from typing import Optional, List

# from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel, BookModel
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.service import BookService
from src.books.models import Book

book_router = APIRouter()
book_service = BookService()


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
async def get_all_books(session: AsyncSession = Depends(get_session)) -> List[Book]:
    books = await book_service.get_all_books(session)
    return books


@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(
    book_data: Book, session: AsyncSession = Depends(get_session)
) -> dict:
    new_book = await book_service.create_book(book_data, session)

    return new_book


@book_router.get("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def get_book(book_id: str, session: AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.get_book(book_id, session)
    if book:
        return book
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )


@book_router.patch("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def update_book(
    book_id: str,
    book_update_data: BookUpdateModel,
    session: AsyncSession = Depends(get_session),
) -> dict:
    updated_book = await book_service.update_book(book_id, book_update_data, session)

    if updated_book:
        return updated_book
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )


@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def get_book(
    book_id: str,
    session: AsyncSession = Depends(get_session),
):
    book_to_delete = await book_service.delete_book(book_id, session)
    if book_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    else:
        return {}
