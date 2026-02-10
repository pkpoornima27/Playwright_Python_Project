import logging

logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()

def test_get_one_record_api(playwright):
    request = playwright.request.new_context()
    response = request.get("https://dotesthere.com/api/users/1")
    mylogger.info(response)
    assert response.status == 200

def test_get_api(playwright):
    request = playwright.request.new_context()
    response = request.get("https://dotesthere.com/api/users?page=1&limit=10")
    mylogger.info(response)
    assert response.status ==200

