#Day -11: data driven api testing
import requests
import pytest
import os 
import csv
import json
import allure

BASE_URL="https://6859658d138a18086dfe49a9.mockapi.io/api" #created a mockapi for testing purpose 

def read_api_data(): #function to accept the csv file 
    fp=os.path.join(os.path.dirname(__file__),"..","Csv_files","api_data.csv")
    with open (fp,newline='') as csvfile:
        reader=list(csv.DictReader(csvfile))
        return reader
    
@pytest.fixture(scope="session") #day-13: introduced pytest.fixture to maintain reusability of headers
def def_headers():
    return {"content-type":"application/json"}

@allure.title("MOCKAPI.IO automation testing")
@allure.description("Testing REST API on MOCKAPI.IO(designer- SHARATH R BHAT)")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("data",read_api_data())
def test_api(data,def_headers):
    url=BASE_URL+data["endpoint"] # url for method
    method=data["method"] #method
    payload=json.loads(data["payload"]) if data["payload"] else {}  #payload with json.loads (to convert data in to string to dict)

    if method=="GET": 
        try:
            res= requests.get(url,headers=def_headers)
            print(f"✅ Response:{res.json()}")
        except requests.exceptions.JSONDecodeError:
            print(f"❌ Exception caught:{res.text}")

    elif method=="DELETE":
        try:
            res=requests.delete(url,headers=def_headers)
            print(f"✅ Response:{res.json()}")
        except requests.exceptions.JSONDecodeError:
            print(f"❌ Exception caught:{res.text}")

    elif method =="POST":
        try:
            res= requests.post(url,json=payload,headers=def_headers)
            print(f"✅ Response:{res.json()}")
        except requests.exceptions.JSONDecodeError:
            print(f"❌ Exception caught:{res.text}")

    elif method =="PATCH":
        try:
            res= requests.patch(url,json=payload,headers=def_headers)
            print(f"✅ Response:{res.json()}")
        except requests.exceptions.JSONDecodeError:
            print(f"❌ Exception caught:{res.text}")

    elif method=="HEAD": #day-12: idempotent method check
        try:
            res= requests.head(url,headers=def_headers)
            print("✅ NO RESPONSE REQUIRED!")
        except requests.exceptions.JSONDecodeError:
            print(f"❌ Exception caught:{res.text}")
    else:
        pytest.skip(f"WRONG METHOD! {method}")
    
    assert res.status_code == int(data["expected_status"]), f"was expecting {data['expected_status']} but got {res.status_code}"


