*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://example.com    

*** Test Cases ***
Open Browser and Verify Title    
    [Documentation]    This test case opens the browser and verifies the page title.
    Open Browser    ${URL}    chrome
    Title Should Be    Example Domain
    Close Browser                                                                                    