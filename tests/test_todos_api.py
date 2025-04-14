import requests
import pytest
from utilities.ReadConfigurations import ReadConfig

class Test_todos_api:
    baseurl = ReadConfig.getApplicationUrl()
    def test_get_call(self):
        response = requests.get(self.baseurl)
        assert response.status_code == 200, 'Error in fetching the api call'
