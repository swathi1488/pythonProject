import requests
def main():
    response_body=requests.get("https://restful-booker.herokuapp.com/booking/331")
    print(response_body.text)
    print(response_body.headers)()
#assertion(verify expected result with the actual result)
#request-header,statuscode ,authorization,body,json,file




if __name__=="__main__":
    main()