# Day-9: Intro to Backend API Testing
import requests
import pytest

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
    res=requests.get(f"{BASE_URL}/users/{userid}",headers=headers)

    assert res.status_code==status,f"expected:{status},got {res.status_code}"

    if res.status_code == 200:
        assert "data" in res.json(), "DATA missing!"
        print(f"[✅ PASS] USER FETCHED!| Response: {res.json()}")
    elif res.status_code in (400, 401,404):
        assert {}== res.json()or "error" in res.json(), "Error message missing!"
        print(f"[❌ FAIL] USER DETAILS NOT FOUND as expected!| Response: {res.json()}")
    else:
        pytest.fail(f"Unexpected status code: {res.status_code}")


@pytest.mark.parametrize("status",[200,400,401,404]) #function to get all users 
def test_backend_get_all(status):
    headers={"x-api-key": "reqres-free-v1"}

    res=requests.get(f"{BASE_URL}/users",headers=headers)
    if res.status_code==200:
        assert "data" in res.json(), "DATA missing!"

        print(f"[✅ PASS] USERS FETCHED!| Response: {res.json()}")


