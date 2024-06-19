import requests


def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/621")
    assert response_body.status_code == 200
    data = response_body.json()
    #verification of keys
    assert 'firstname' in data, "incorect fisrstname"
    assert 'lastname' in data, "incorect lastname"
    #verification of data
    assert data["firstname"] == "Jim", "incorrect firstname"
    assert data["lastname"] == "Brown", "incorect lastname"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "incorrect message"


if __name__ == "__main__":
    main()
