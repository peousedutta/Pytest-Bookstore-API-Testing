import requests
import pytest
from utilities.ReadConfigurations import ReadConfig
from controller.bookstore import *

class Test_001_bookstore_get_call:
    baseurl = ReadConfig.getApplicationUrl()
    all_books = AllBooks()
    book_by_bookid = BookByBookId('abc')
    
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
        id = 'abc'
        response = requests.get(self.baseurl+self.get_all_books_path+'?ISBN='+id)