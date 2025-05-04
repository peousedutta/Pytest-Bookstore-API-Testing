import time
import httpx
from utilities.ReadConfigurations import ReadConfig

class BookStore:
    def __init__(self):
        self.books_base_endpoint:str = '/BookStore/V1/Books'
    
    def check_status_code_200(self, response) -> bool:
        if response.status_code == 200:
            return True
        else:
            return False
        
    def check_contentType(self) -> bool:
        raise NotImplementedError


class AllBooks(BookStore):
    def __init__(self):
        super().__init__()
        self.timeElapsed : float = 0.0


    async def perform_fetch_all_books(self, baseurl:str):
        async with httpx.AsyncClient() as client:
            startTime = time.perf_counter()
            response =  await client.get(baseurl+self.books_base_endpoint)
            endTime = time.perf_counter()
            self.timeElapsed = endTime - startTime
            return response
    
    def check_response_jsonSchema(self) -> bool:
        raise NotImplementedError


class BookByBookId(BookStore):
    def __init__(self):
        super().__init__()
        self.timeElapsed : float = 0.0

    async def perform_fetch_book_by_id(self,id:str, baseurl:str):
        async with httpx.AsyncClient() as client:
            url : str = baseurl + '/BookStore/V1/Book?ISBN=' + id
            startTime = time.perf_counter()
            response = await client.get(url)
            endTime = time.perf_counter()
            self.timeElapsed = endTime - startTime
            return response

    def check_response_jsonSchema(self) -> bool:
        raise NotImplementedError