import requests

base_url = "https://dotesthere.com/api/"

headers = {
         "Content-Type": "application/json"
     }

def test_get_api_all_records():
    response = requests.get(f"{base_url}/users", params={"page": 1, "limit": 10})
    assert response.status_code == 200
    data = response.json()['data']
    assert len(data)>0
    first_user = data[0]
    assert first_user['id'] == 1
    assert first_user['first_name'] == 'Ankur'
    assert first_user['last_name'] == 'Autoamtion'
    assert first_user['email'] == 'ankur.automation@dotesthere.com'
    assert first_user['avatar'] == 'https://dotesthere.com/img/faces/1-image.jpg'


def test_get_api_one_records():
    response = requests.get(f"{base_url}/users/2")
    assert response.status_code == 200
    data = response.json()['data']
    assert data['id'] == 2
    assert data['email'] == 'janet.weaver@dotesthere.com'
    assert data['first_name'] == 'Janet'
    assert data['last_name'] == 'Weaver'

def test_create_update_delete_api():
    payload = {
            "email": "pk.poornima@gmail.com",
            "first_name": "Poornima",
            "last_name": "Kemparaju",
            "job": "Test Automation Engineer"
        }
    response = requests.post()

# def test_post_api():
#     url = "https://dotesthere.com/api/users"
#     payload = {
#         "email": "pk.poornima@gmail.com",
#         "first_name": "Poornima",
#         "last_name": "Kemparaju",
#         "job": "Test Automation Engineer"
#     }
#     headers = {
#         "Content-Type": "application/json"
#     }
#     response = requests.post(url, json=payload, headers=headers)
#     assert response.status_code == 201
#     assert (response.json()['data']['id']) == 3
#     assert (response.json()['data']['email']) == "pk.poornima@gmail.com"
#     assert (response.json()['data']['first_name']) == "Poornima"
#     assert (response.json()['data']['last_name']) == "Kemparaju"
#     assert (response.json()['data']['job']) == "Test Automation Engineer"
#
# def test_put_api():
#     url = "https://dotesthere.com/api/users/1"
#     payload = {
#         "email": "natarajmb@gmail.com",
#         "first_name": "Nataraj",
#         "last_name": "Basappa",
#         "job": "CTO"
#     }
#     headers = {
#         "Content-Type": "application/json"
#     }
#     response = requests.put(url, json=payload, headers=headers)
#     assert response.status_code == 200
#     assert (response.json()['data']['id']) == 1
#     assert (response.json()['data']['email']) == "natarajmb@gmail.com"
#     assert (response.json()['data']['first_name']) == "Nataraj"
#     assert (response.json()['data']['last_name']) == "Basappa"
#     assert (response.json()['data']['avatar']) == "https://dotesthere.com/img/faces/1-image.jpg"
#     assert (response.json()['data']['job']) == "CTO"
#
# def test_delete_api():
#     url = "https://dotesthere.com/api/users/1"
#     response = requests.delete(url)
#     assert  response.status_code == 204
