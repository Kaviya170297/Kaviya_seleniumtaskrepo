*** Settings ***
Resource    ../Resources/keywords.robot
Test Teardown    Close Browser

*** Test Cases ***
Verify_Valid_Login
    Open Application
    LoginToApplication    maria    thoushallnotpass
    VerifyLoginissuccessful
    Sleep    3
    Logout