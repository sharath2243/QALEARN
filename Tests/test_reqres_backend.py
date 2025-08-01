# Day-9: Intro to Backend API Testing
import requests
import responses
import pytest
import allure 
BASE_URL = "https://reqres.in/api" #url

@allure.title("Reqres.in automation testing")
@allure.description("Testing LOGIN on reqres.in")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("payload,expected_status", [ #parameterized testing
    ({"email": "eve.holt@reqres.in", "password": "cityslicka"}, 200),
    ({"email": "eve.holt@reqres.in"}, 400),
    ({}, 400),
])

@allure.step("Trying login..")
@pytest.mark.smoke
@responses.activate() #wrote mock reposnes so we can mock backend!
def test_backend_post(payload, expected_status): #function to login (post method)
    if expected_status==200:
        responses.add(
            responses.POST,
            f"{BASE_URL}/login",
            json={"token":"mock123"},
            status=200
        )
    else:
        responses.add(
            responses.POST,
            f"{BASE_URL}/login",
            json={"error":"missing cred! or something went wrong!"},
            status=expected_status
        )

    headers = {"x-api-key": "reqres-free-v1"}  # free-api-key

    res = requests.post(f"{BASE_URL}/login", json=payload) #post -request

    assert res.status_code == expected_status, f"Expected {expected_status}, got {res.status_code}" #assertion for sataus-code

    if res.status_code == 200:
        assert "token" in res.json(), "Token missing!"
        print(f"[✅ PASS] Login success!| Response: {res.json()}")
    elif res.status_code in (400, 401):
        assert "error" in res.json(), "Error message missing!"
        print(f"[❌ FAIL] Login failed as expected!| Response: {res.json()}")
    else:
        pytest.fail(f"Unexpected status code: {res.status_code}")

@allure.title("Reqres.in automation testing")
@allure.description("Testing GET_SINGLE on reqres.in")
@allure.step("Reading single user data..")
@pytest.mark.parametrize("userid,status",[(2,200),(999,404)])
@pytest.mark.smoke
@pytest.mark.regression
def test_backend_get_one(userid,status): #function to get a user by his id (GET)

    headers={"x-api-key": "reqres-free-v1"}
    res=requests.get(f"{BASE_URL}/users/{userid}",headers=headers) #200 ok
    res2=requests.get(f"{BASE_URL}/users/{userid}") #401 or #404

    assert res.status_code==status,f"expected:{status},got {res.status_code}"

    if res.status_code == 200:
        assert "data" in res.json(), "DATA missing!"
        print(f"[✅ PASS] USER FETCHED!| Response: {res.json()}")
    elif res2.status_code in (400, 401, 404):
        assert {}== res2.json()or "error" in res2.json(), "Error message missing!"
        print(f"[❌ FAIL] USER DETAILS NOT FOUND as expected!| Response: {res2.json()}")
    else:
        pytest.fail(f"Unexpected status code: {res.status_code}")

@allure.title("Reqres.in automation testing")
@allure.description("Testing GET ALL USERS on reqres.in")
@allure.step("Reading single user data..")
@pytest.mark.parametrize("status",[200,400,401,404]) #function to get all users 
@pytest.mark.smoke
@pytest.mark.regression
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

@allure.title("Reqres.in automation testing")
@allure.description("Testing POST on reqres.in")
@allure.step("User creation..")
@pytest.mark.parametrize("payload",[({"email": "lord23@gmail.com", "password": "abracadabra"}),
    ({"name": "eve.holt@reqres.in"}),
    ({})])
@pytest.mark.smoke
def test_backend_create_one(payload): #Day-10: create a user temproarily
    headers={"x-api-key": "reqres-free-v1"}

    res=requests.post(f"{BASE_URL}/users",json=payload,headers=headers) #with headers retruns 201
    res2=requests.post(f"{BASE_URL}/users",json=payload) #without headers returns 401

    assert res.status_code==201
    print(f"[✅ PASS] USER CREATED TEMPROARILY!| Response: {res.json()}")

    assert res2.status_code==401 
    print(f"[❌ FAIL] USER CREATION FAILED as expected!| Response: {res2.json()}")

@allure.title("Reqres.in automation testing")
@allure.description("Testing DELETE on reqres.in")
@allure.step("User deletion..")
@pytest.mark.parametrize("userid",[2,300,400,878]) # delete a user temproarily
@pytest.mark.smoke
def test_backend_delete(userid):
    headers={"x-api-key": "reqres-free-v1"}

    res=requests.delete(f"{BASE_URL}/users/{userid}",headers=headers) #with headers retruns 204 (no content)
    res2=requests.delete(f"{BASE_URL}/users/{userid}") #without headers returns 401

    assert res.status_code==204
    print(f"[✅ PASS] USER DELETED TEMPROARILY!")

    assert res2.status_code==401 
    print(f"[❌ FAIL] USER DELETION FAILED as expected!")

