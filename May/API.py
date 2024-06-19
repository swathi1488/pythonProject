import requests

def main():
    response_body=requests.get("https://restful-booker.herokuapp.com/booking/331")
    print(response_body.text)
    print(response_body.status_code)
    print(response_body.json())
    if response_body==200:
        print("TC#1 get request suscessfull")
    else:
        print("TC#1 get request not successfull")



if __name__=="__main__":
    main()