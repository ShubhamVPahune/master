*** Settings ***
Library    SeleniumLibrary
Library    operations.py

Test Teardown    Close Browser

*** Variables ***
${ipl_pointstable_url}    https://www.iplt20.com/points-table/men/2021
${goolge_url}    https://www.google.com/
${search_text}    IPL points table 2021

*** Test Cases ***

TC_1 Search ipl points table
    launch browser and maximize    ${goolge_url}
    Wait Until Element Is Visible    locator=//textarea[@title='Search']
    Input Text    locator=//textarea[@title='Search']    text=${search_text}
    Sleep    2s
    ${suggestions}    Get WebElements    locator=//*[@data-attrid='AutocompletePrediction']//ancestor::ul[@role='listbox']//li
    ${suggestion_text}    get_suggestions    ${suggestions}
    Log    message=suggestions are ${suggestion_text}
    Click Element    locator=//*[@aria-label='ipl points table 2021']
    Capture Page Screenshot

TC_2 save points table in csv
    # launch browser and maximize    ${ipl_pointstable_url}
    # ${table_element}    Get WebElement    locator=//div[@class='points-table-page']//table[@class="ih-td-tab"]
    # read_all_table_details    ${table_element}
    ${sqr_gen}    sqr_generator
    FOR    ${sqr_}    IN    ${sqr_gen}
        Log    message="generator object = ${sqr_}"
    END

*** Keywords ***
launch browser and maximize
    [Arguments]    ${url} 
    Open Browser    ${url}    browser=chrome
    Maximize Browser Window

