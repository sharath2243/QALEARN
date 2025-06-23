# Day-9: Intro to Backend API Testing
import requests
import pytest
import os 
import csv
import json

'''
BASE_URL = "https://reqres.in/api" #url

@pytest.mark.parametrize("payload,expected_status", [ #parameterized testing
    ({"email": "eve.holt@reqres.in", "password": "cityslicka"}, 200),
    ({"email": "eve.holt@reqres.in"}, 400),
    ({}, 400),
])

def test_backend_post(payload, expected_status): #function to login (post method)
    headers = {"x-api-key": "reqres-free-v1"}  # free-api-key

    res = requests.post(f"{BASE_URL}/login", json=payload, headers=headers) #post -request

    assert res.status_code == expected_status, f"Expected {expected_status}, got {res.status_code}" #assertion for sataus-code

    if res.status_code == 200:
        assert "token" in res.json(), "Token missing!"
        print(f"[✅ PASS] Login success!| Response: {res.json()}")
    elif res.status_code in (400, 401):
        assert "error" in res.json(), "Error message missing!"
        print(f"[❌ FAIL] Login failed as expected!| Response: {res.json()}")
    else:
        pytest.fail(f"Unexpected status code: {res.status_code}")

@pytest.mark.parametrize("userid,status",[(2,200),(999,404)])
def test_backend_get_one(userid,status): #function to get a user by his id (GET)

    headers={"x-api-key": "reqres-free-v1"}
    res=requests.get(f"{BASE_URL}/users/{userid}",headers=headers) #200 ok
    res2=requests.get(f"{BASE_URL}/users/{userid}") #401 or #404

    assert res.status_code==status,f"expected:{status},got {res.status_code}"

    if res.status_code == 200:
        assert "data" in res.json(), "DATA missing!"
        print(f"[✅ PASS] USER FETCHED!| Response: {res.json()}")
    elif res2.status_code in (400, 401,404):
        assert {}== res2.json()or "error" in res2.json(), "Error message missing!"
        print(f"[❌ FAIL] USER DETAILS NOT FOUND as expected!| Response: {res2.json()}")
    else:
        pytest.fail(f"Unexpected status code: {res.status_code}")


@pytest.mark.parametrize("status",[200,400,401,404]) #function to get all users 
def test_backend_get_all(status):
    headers={"x-api-key": "reqres-free-v1"}

    res=requests.get(f"{BASE_URL}/users",headers=headers) #returns 200
    res2=requests.get(f"{BASE_URL}/users") #without headers, returns 401
    if res.status_code==200:
        assert "data" in res.json(), "DATA missing!"

        print(f"[✅ PASS] USERS FETCHED!| Response: {res.json()}")
    else:
        assert {}== res2.json()or "error" in res2.json(), "Error message missing!"
        print(f"[❌ FAIL] USER DETAILS NOT FOUND as expected!| Response: {res2.json()}")

@pytest.mark.parametrize("payload",[({"email": "lord23@gmail.com", "password": "abracadabra"}),
    ({"name": "eve.holt@reqres.in"}),
    ({})])
def test_backend_create_one(payload): #Day-10: create a user temproarily
    headers={"x-api-key": "reqres-free-v1"}

    res=requests.post(f"{BASE_URL}/users",json=payload,headers=headers) #with headers retruns 201
    res2=requests.post(f"{BASE_URL}/users",json=payload) #without headers returns 401

    assert res.status_code==201
    print(f"[✅ PASS] USER CREATED TEMPROARILY!| Response: {res.json()}")

    assert res2.status_code==401 
    print(f"[❌ FAIL] USER CREATION FAILED as expected!| Response: {res2.json()}")

@pytest.mark.parametrize("userid",[2,300,400,878]) # delete a user temproarily
def test_backend_delete(userid):
    headers={"x-api-key": "reqres-free-v1"}

    res=requests.delete(f"{BASE_URL}/users/{userid}",headers=headers) #with headers retruns 204 (no content)
    res2=requests.delete(f"{BASE_URL}/users/{userid}") #without headers returns 401

    assert res.status_code==204
    print(f"[✅ PASS] USER DELETED TEMPROARILY!")

    assert res2.status_code==401 
    print(f"[❌ FAIL] USER DELETION FAILED as expected!")
'''
#day -11: data driven api testing

BASE_URL="https://6859658d138a18086dfe49a9.mockapi.io/api" #created a mockapi for testing purpose 

def read_api_data(): #function to accept the csv file 
    fp=os.path.join(os.path.dirname(__file__),"..","Csv_files","api_data.csv")
    with open (fp,newline='') as csvfile:
        reader=list(csv.DictReader(csvfile))
        return reader


@pytest.mark.parametrize("data",read_api_data())
def test_api(data):
    headers={"content-type":"application/json"}
    url=BASE_URL+data["endpoint"] # url for method
    method=data["method"] #method
    payload=json.loads(data["payload"]) if data["payload"] else {}  #payload with json.loads (to convert data in to string to dict)

    if method=="GET" or method=="DELETE": 
        try:
            res= requests.get(url,headers=headers)
            print(f"Response:{res.json()}")
        except requests.exceptions.JSONDecodeError:
            print(f"Exception caught:{res.text}")
    elif method =="POST" or method=="PUT" or method=="PATCH":
        try:
            res= requests.post(url,json=payload,headers=headers)
            print(f"Response:{res.json()}")
        except requests.exceptions.JSONDecodeError:
            print(f"Exception caught:{res.text}")
    else:
        pytest.skip(f"WRONG METHOD! {method}")
    
    assert res.status_code == int(data["expected_status"]), f"was expecting {data['expected_status']} but got {res.status_code}"


