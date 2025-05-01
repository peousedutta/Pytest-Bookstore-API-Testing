import pytest
import random
from utilities.ReadConfigurations import ReadConfig
from serviceObject.bookstore import *

class Test_001_bookstore_get_call:
    baseurl = ReadConfig.getApplicationUrl()
    bookstore = BookStore()
    all_books = AllBooks()
    book_by_bookid = BookByBookId()

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.asyncio
    async def test_fetch_all_books(self):
        allBooksResponse = await self.all_books.perform_fetch_all_books()
        assert self.bookstore.check_status_code_200(allBooksResponse), f"Expected status code 200 but got {allBooksResponse.status_code}"
        assert self.bookstore.check_responseTime(allBooksResponse, 1), f"Expected status code 200 but got {allBooksResponse.elapsed.total_seconds()}"

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.asyncio
    async def test_fetch_book_by_bookid(self):
        allBooksData = await self.all_books.perform_fetch_all_books()
        allBooksData = allBooksData.json()
        idList = [data["isbn"] for data in allBooksData["books"]]
        index = random.randint(0, len(idList) - 1)
        id = idList[index]

        bookData = await self.book_by_bookid.perform_fetch_book_by_id(id)
        assert bookData.json()["isbn"] == id, "Error in fetching"
        assert self.bookstore.check_responseTime(bookData, 0.5), f"Expected status code 200 but got {bookData.elapsed.total_seconds()}"
        assert self.bookstore.check_status_code_200(bookData), f"Expected status code 200 but got {bookData.status_code}"

    @pytest.mark.dev
    @pytest.mark.regression
    @pytest.mark.asyncio
    @pytest.mark.fail_case
    async def test_fetch_book_by_bookId_with_invalidData(self):
        id:str = "dummy"
        bookData = await self.book_by_bookid.perform_fetch_book_by_id(id)
        assert bookData.status_code == 400, f"Expected status code 400 but got {bookData.status_code}"