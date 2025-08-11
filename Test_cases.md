# Test Cases - QALEARN

## 1. Saucedemo.com (UI)
- Test Case ID: TC_UI-001
- Title: *Verify Successful Login*
- Priority: High
- Severity: Critical
- Preconditions: 
  - user is on the Login page (https://www.saucedemo.com/)
- Steps:
  - Enter a valid username: standard_user
  - Enter a valid password: secret_sauce
  - Click the login button
- Expected Outcome:
  - user is navigated to /inventory.html (Home)
- Actual Outcome:
  - user is navigated to /inventory.html (Home)
- Status : PASS

## 2. Saucedemo.com (UI)
- Test Case ID: TC_UI_002
- Priority: High
- Severity: Critical
- Title: *Verify Unsuccessful login*
- Preconditions: 
  - user is on the Login page (https://www.saucedemo.com/)
- Steps:
  - Enter a valid username: standard_user
  - Enter a valid password: 12345678 
  - Click the login button
- Expected Outcome:
  - Error message stating `Epic sadface: Username and password do not match any user in this service` appears on the screen.
- Actual Outcome:
  - Error message stating `Epic sadface: Username and password do not match any user in this service` appears on the screen.
- Status : PASS

## 3. Saucedemo.com (UI)
- Test Case ID: TC_UI_003
- Priority: Medium
- Severity: Normal
- Title: *Verify the cart list functionality*
- Preconditions: 
  - User should be Logged-in.
  - User has added at least one product to the cart.
- Steps:
  - User clicks `cart-icon`, which is located in top right corner.
- Expected Outcome:
  - The products which are added by the user should be visible with it's description and price tag.
- Actual Outcome:
  - The products which are added by the user is visible with it's description and price tag.
- Status : PASS

## 4. Saucedemo.com (UI)
- Test Case ID: TC_UI-004
- Title: *Verify Remove button functionality*
- Priority: Medium
- Severity: Major
- Preconditions: 
  - user is successfuly logged in with username: `problem-user`
  - user has added at least one product to the cart
- Steps:
  - Clicks on the `Remove` button
- Expected Outcome: The prodcut has been removed.
- Actual Outcome: Clicking `Remove` does not remove the product.
- Status: FAIL

## 5. MOCKAPI (API):
- Test Case ID: TC_API_001
- Title: *Verify PATCH Request Updates User Data Successfully*
- Priority: Medium
- Severity: Normal
- Preconditions:
  - Given API Endpoint exists.( '/users/1' )
  - Header is included with `{"content-type":"application/json"}`
- Steps:
  - Send PATCH request to /users/1 with partial update data("{"username":"jarvis_69"}")
- Expected Outcome:
  - Response status code is 200 OK
  - Response body contains the updated user with the new username set to "jarvis_69"
  - Other fields remain unchanged
- Actual Outcome:
  - Response status code is 200 OK
  - Response body contains the updated user with the new username set to "jarvis_69"
  - Other fields remain unchanged
- Status: PASS

## 6. MOCKAPI (API):
- Test Case ID: TC_API_002
- Title: *Verify PATCH Request Updates Product Data (invalid)*
- Priority: Medium
- Severity: Normal
- Preconditions:
  - Given API Endpoint exists.( '/products/1' )
  - Header is included with `{"content-type":"application/json"}`
- Steps:
  - Send PATCH request to /products/87 with partial update data("{"name":"jug"}")
- Expected Outcome:
  - Response status code is 404 Not Found
- Actual Outcome:
  - Response status code is 400 Not Found
- Status: PASS

# 7. Reqres.in (API):
- Test Case ID: TC_API_003
- Title: *verify login functionality*
- Priority: High
- Severity: Critical
- Preconditions:
  - API Endpoint exists (`/api/login/`)
- Steps:
  - Send POST request to `/api/login` with valid mail and password and include the api key in the header.
- Expected Outcome:
  - Response status code is 201 Created
- Actual Outcome:
  - Response status code is 201 Created
- Status: PASS

