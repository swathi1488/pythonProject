import pytest
import requests

def test_sample():
    assert 4==4
def test_sample2():
    assert 5==5
def test_getrequests():
    response_body=requests.get("https://restful-booker.herokuapp.com/booking/699")
    assert response_body.status_code==200
    data=response_body.json()
    #verify keys
    assert "firstname" in data,"incorect firstname"
    assert "lastname" in data,"incorect lastname"

    assert  data["firstname"]=="Jim","incorect first name"
    assert  data["lastname"]=="Brown","incorect last name"
    assert data["clearbookingdates"]["checkin"] == "2018-01-01", "incorrect message"