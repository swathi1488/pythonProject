import requests


def create_token():
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response_body = requests.post("https://restful-booker.herokuapp.com/auth", headers=headers, json=json_payload)
    data = response_body.json()
    token = data["token"]
    print(token)
    return token

def creat_booking():
    headers = {"content_type": "application/json"}
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    URL = "https://restful-booker.herokuapp.com/booking"
    response_body = requests.post(url=URL, headers=headers, json=json_payload)
    assert response_body.status_code == 200
    data = response_body.json()
    booking_id=data["bookingid"]
    print(booking_id)
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "Jim", "incorect first name"
    assert data["booking"]["lastname"] == "Brown", "incorect last name"
    return booking_id



def test_put_request():
    # bookingid,token
    url= "https://restful-booker.herokuapp.com/booking/"
    booking_id =str(creat_booking())
    url_path = url + booking_id
    cookie_value = "token=" +(create_token())
    headers = {
        "Content-Type": "application/json",
        "cookie": cookie_value
    }
    print(headers)
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_body = requests.put(url=url_path, headers=headers, json=json_payload)
    assert response_body.status_code == 200,"incorect status code"
    data=response_body.json()
    assert data["firstname"] == "Jim", "incorect first name"
    assert data["lastname"] == "Brown", "incorect last name"

def test_delete():
    # bookingid,token
    try:
        url = "https://restful-booker.herokuapp.com/booking/"
        booking_id = str(creat_booking())
        url_path = url + booking_id
        cookie_value = "token=" + (create_token())
        headers = {
            "Content-Type": "application/json",
            "cookie": cookie_value
        }
        print(headers)

        response_body = requests.delete(url=url_path, headers=headers)
        assert response_body.status_code == 201
    except Exception as error:
      print(error)



