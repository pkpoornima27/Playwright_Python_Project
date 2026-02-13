import requests

base_url = "https://dotesthere.com/api"

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
    response_post = requests.post(f"{base_url}/users", json=payload, headers=headers)

    assert response_post.status_code == 201
    user =  response_post.json()["data"]
    assert user["email"] == "pk.poornima@gmail.com"



