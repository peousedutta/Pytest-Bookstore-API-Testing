import requests
import pytest
import random
from utilities.ReadConfigurations import ReadConfig
from controller.bookstore import *

class Test_001_bookstore_get_call:
    baseurl = ReadConfig.getApplicationUrl()
    all_books = AllBooks()
    book_by_bookid = BookByBookId()

    @pytest.mark.smoke
    def test_fetch_all_books(self):
        allBooksResponse = self.all_books.perform_fetch_all_books()
        assert self.all_books.check_status_code_200(), f"Expected status code 200 but got {allBooksResponse.status_code}"
        # assert self.all_books.check_contentType(), f"Expected "
        # assert self.all_books.check_response_jsonSchema(), f"Expected"
        assert self.all_books.check_responseTime, f"Expected status code 200 but got {allBooksResponse.elapsed.total_seconds()}"

    @pytest.mark.dev
    @pytest.mark.smoke
    def test_fetch_book_by_bookid(self):
        allBooksData = self.all_books.perform_fetch_all_books().json()
        idList = [data["isbn"] for data in allBooksData["books"]]
        index = random.randint(0, len(idList) - 1)
        id = idList[index]

        bookData = self.book_by_bookid.perform_fetch_book_by_id(id)
        assert bookData.json()["isbn"] == id, "Error in i fetching"
        assert bookData.status_code == 200, f"Expected status code 200 but got {bookData.status_code}"
