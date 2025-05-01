import httpx
from utilities.ReadConfigurations import ReadConfig

class BookStore:
    def __init__(self):
        self.books_base_endpoint:str = '/BookStore/V1/Books'
        self.baseurl = ReadConfig.getApplicationUrl()
    
    def check_status_code_200(self, response) -> bool:
        if response.status_code == 200:
            return True
        else:
            return False
        
    def check_responseTime(self, response, time) -> bool:
        if response.elapsed.total_seconds < time:
            return True
        else:
            return False
        
    def check_contentType(self) -> bool:
        raise NotImplementedError


class AllBooks(BookStore):
    async def perform_fetch_all_books(self):
        async with httpx.AsyncClient() as client:
            return await client.get(self.baseurl+self.books_base_endpoint)
    
    def check_response_jsonSchema() -> bool:
        raise NotImplementedError


class BookByBookId(BookStore):
    def __init__(self):
        super().__init__()

    async def perform_fetch_book_by_id(self,id:str):
        async with httpx.AsyncClient() as client:
            url : str = self.baseurl + '/BookStore/V1/Book?ISBN=' + id
            return await client.get(url)

    def check_response_jsonSchema() -> bool:
        raise NotImplementedError