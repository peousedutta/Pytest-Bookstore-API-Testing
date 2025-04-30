import pytest
import requests
from utilities.ReadConfigurations import ReadConfig

class BookStore:
    def __init__(self):
        self.books_base_endpoint:str = '/BookStore/V1/Books'
        self.baseurl = ReadConfig.getApplicationUrl()

class AllBooks(BookStore):
    def perform_fetch_all_books(self):
        return requests.get(self.baseurl+self.books_base_endpoint)
    
    def check_status_code_200(self) -> bool:
        response = self.perform_fetch_all_books()
        if response.status_code == 200:
            return True
        else:
            return False
        
    def check_contentType(self) -> bool:
        raise NotImplementedError
    
    def check_response_jsonSchema() -> bool:
        raise NotImplementedError

    def check_responseTime(self) -> bool:
        response = self.perform_fetch_all_books()
        if response.elapsed.total_seconds < 1:
            return True
        else:
            return False

class BookByBookId(BookStore):
    def __init__(self):
        super().__init__()

    def perform_fetch_book_by_id(self,id:str):
        url : str = self.baseurl + '/BookStore/V1/Book?ISBN=' + id
        return requests.get(url)

    def check_get_book_by_id_responseTime(self, id:str) -> bool:
        raise NotImplementedError