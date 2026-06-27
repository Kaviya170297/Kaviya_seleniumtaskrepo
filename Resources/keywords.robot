*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}    chrome
${url}    https://robotsparebinindustries.com/

*** Keywords ***
Open Application
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

LoginToApplication
    [Arguments]    ${username}    ${password}
    Input Text    id:username    ${username}
    Input Text    id:password    ${password}
    Click Element    xpath://button[normalize-space()='Log in']

VerifyLoginissuccessful
    Wait Until Page Contains Element    xpath://button[@id='logout']    10s

Logout
    Click Element    xpath://button[@id='logout']
    Close Browser
