*** Settings ***
Library    MyLibrary

*** Test Cases ***
Open And Close Chrome
    Open Chrome Browser
    Sleep    5s
    Close Chrome Browser