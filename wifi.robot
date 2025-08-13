*** Settings ***
Library    AppiumLibrary

*** Variables ***
${REMOTE_URL}       http://localhost:4723
${PLATFORM_NAME}    Android
${PLATFORM_VERSION}     10
${DEVICE_NAME}      32007dd24e5e16cf
${AUTOMATION_NAME}  UiAutomator2
${APP_PACKAGE}      com.android.settings
${APP_ACTIVITY}     .Settings

*** Test Cases ***
Toggle Wi-Fi On Samsung M20
	Open Application    ${REMOTE_URL}    platformName=${PLATFORM_NAME}    platformVersion=${PLATFORM_VERSION}    deviceName=${DEVICE_NAME}    automationName=${AUTOMATION_NAME}    appPackage=${APP_PACKAGE}    appActivity=${APP_ACTIVITY}
    Wait Until Page Contains     Connections
    Click Text    Connections
    Wait Until Page Contains    Wi-Fi    timeout=10s
    Click Text    Wi-Fi
    Wait Until Page Contains Element    xpath=//android.widget.Switch
    Click Element    xpath=//android.widget.Switch
    Sleep    2s
    Close Application
