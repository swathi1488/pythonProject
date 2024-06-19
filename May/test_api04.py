import pytest
import requests


def test_sample():
    assert 4==4
def test_sample2():
    assert  5==6

def test_getrequest():
    response_body=requests.get("https://restful-booker.herokuapp.com/booking/621")
    assert response_body.status_code==200
    data=response_body.json()
    assert 'firstname' in data,"incorect firstname"
    assert 'lastname' in data,"incorect lastname"

    assert data["firstname"]=="Josh","incorect firstname"
    assert  data["lastname"]=="Allen","incorect lastname"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "incorrect message"

