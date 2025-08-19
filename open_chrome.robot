*** Settings ***
Library    AppiumLibrary

*** Variables ***
${REMOTE_URL}        http://localhost:4723
${PLATFORM_NAME}     Android
${PLATFORM_VERSION}  10
${DEVICE_NAME}       32007dd24e5e16cf
${AUTOMATION_NAME}   UiAutomator2
${APP_PACKAGE}       com.android.chrome
${APP_ACTIVITY}      com.google.android.apps.chrome.Main

*** Test Cases ***
Open Chrome Application
    Open Application    ${REMOTE_URL}    platformName=${PLATFORM_NAME}    platformVersion=${PLATFORM_VERSION}    deviceName=${DEVICE_NAME}    automationName=${AUTOMATION_NAME}    appPackage=${APP_PACKAGE}    appActivity=${APP_ACTIVITY}

    Sleep    3s
    Click Text    Continue as shweta
    Sleep    1s
    Click Text    Yes
    Sleep    2s
    Click Text    Got it

 # Click search bar
    Click Element    xpath=//android.widget.EditText[@text="Search or type web address"]

    # Wait a moment to ensure the keyboard is up
    Sleep    1s

    # Type "mountain"
    Input Text    xpath=//android.widget.EditText[@text="Search or type web address"]    mountain

    Sleep    2s

    Capture Page Screenshot

    Close Application
