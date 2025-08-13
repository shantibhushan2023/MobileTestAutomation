*** Settings ***
Library    AppiumLibrary

*** Variables ***
${REMOTE_URL}        http://127.0.0.1:4723
${PLATFORM_NAME}     Android
${DEVICE_NAME}       32007dd24e5e16cf
${APP_PACKAGE}       com.google.android.calculator
${APP_ACTIVITY}      com.android.calculator2.Calculator
${AUTOMATION_NAME}   UiAutomator2
${NO_RESET}          true

*** Test Cases ***
Multiply 7 And 3 In Calculator
    [Documentation]    Performs 7 × 3 = 21 in Google Calculator

    Open Application    ${REMOTE_URL}
    ...    platformName=${PLATFORM_NAME}
    ...    deviceName=${DEVICE_NAME}
    ...    automationName=${AUTOMATION_NAME}
    ...    appPackage=${APP_PACKAGE}
    ...    appActivity=${APP_ACTIVITY}
    ...    noReset=${NO_RESET}

    Sleep    2s
    Run Keyword And Ignore Error    Click Element    id=com.google.android.calculator:id/clr
    Run Keyword And Ignore Error    Click Element    id=com.google.android.calculator:id/del

    Wait Until Element Is Visible    id=com.google.android.calculator:id/digit_7    5s
    Click Element    id=com.google.android.calculator:id/digit_7

    Wait Until Element Is Visible    id=com.google.android.calculator:id/op_mul    5s
    Click Element    id=com.google.android.calculator:id/op_mul

    Wait Until Element Is Visible    id=com.google.android.calculator:id/digit_3    5s
    Click Element    id=com.google.android.calculator:id/digit_3

    Wait Until Element Is Visible    id=com.google.android.calculator:id/eq    5s
    Click Element    id=com.google.android.calculator:id/eq

    Sleep    2s
    Wait Until Element Is Visible    id=com.google.android.calculator:id/result_final    5s
    ${result}=    Get Text    id=com.google.android.calculator:id/result_final
    Log    Multiplication Result: ${result}
    Should Match Regexp    ${result}    ^21(\.0)?$

    Capture Page Screenshot    multiplication_result.png

    [Teardown]    Close Application