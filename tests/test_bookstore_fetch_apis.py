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
        response = requests.get(self.baseurl+self.all_books.books_base_endpoint)
        assert self.all_books.check_status_code_200(), f"Expected status code 200 but got {response.status_code}"
        assert self.all_books.check_contentType(), f"Expected "
        assert self.all_books.check_response_jsonSchema(), f"Expected"
        assert self.all_books.check_responseTime, f"Expected status code 200 but got {response.elapsed.total_seconds()}"

    @pytest.mark.dev
    @pytest.mark.smoke
    def test_fetch_book_by_bookid(self):
        allBooksData = self.all_books.perform_fetch_all_books()
        idList = [data["isbn"] for data in allBooksData["books"]]
        index = random.randint(0, len(idList))

        id = idList[index]
        print(f"[DEBUG] -- {id}")
        bookData = self.book_by_bookid.perform_fetch_book_by_id(id)
        print(f"[DEBUG] -- {bookData}")

