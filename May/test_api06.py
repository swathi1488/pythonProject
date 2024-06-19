import pytest
import requests


@pytest.mark.positive
def test_creat_booking_positive():
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


@pytest.mark.negative
def test_creat_booking_negative():
    headers = {"content_type": "application/json"}
    json_payload = {}
    URL = "https://restful-booker.herokuapp.com/booking"
    response_body = requests.post(url=URL, headers=headers, json=json_payload)
    assert response_body.status_code ==500

