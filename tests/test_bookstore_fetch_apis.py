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
        assert self.bookstore.check_status_code_200(allBooksResponse), f"[ERROR] Expected status code 200 but got {allBooksResponse.status_code}"
        assert self.all_books.timeElapsed < 1, f"[ERROR] Expected response time 1sec but got {allBooksResponse.elapsed.total_seconds()}"

    # @pytest.mark.parametrize("id", datafromCi)
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
        assert bookData.json()["isbn"] == id, "[ERROR] Error in fetching"
        assert self.bookstore.check_status_code_200(bookData), f"[ERROR] Expected status code 200 but got {bookData.status_code}"
        assert self.book_by_bookid.timeElapsed < 0.2, f"[ERROR] Expected response time 0.8s but got {bookData.elapsed.total_seconds()}"

    @pytest.mark.dev
    @pytest.mark.regression
    @pytest.mark.asyncio
    @pytest.mark.fail_case
    async def test_fetch_book_by_bookId_with_invalidData(self):
        id:str = "dummy"
        bookData = await self.book_by_bookid.perform_fetch_book_by_id(id)
        assert bookData.status_code == 400, f"[ERROR] Expected status code 400 but got {bookData.status_code}"