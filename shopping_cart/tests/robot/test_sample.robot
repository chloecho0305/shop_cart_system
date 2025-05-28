*** Settings ***
Library    RequestsLibrary
Suite Setup    Create Session    shopping_cart    http://127.0.0.1:8000/

*** Test Cases ***
Homepage Should Return 200
    ${response}=    Get Request   shopping_cart    /
    Should Be Equal As Integers    ${response.status_code}    200
