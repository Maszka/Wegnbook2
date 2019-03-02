*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary
Library           Process
Library           OperatingSystem


Suite Setup       Prepare Django
Suite Teardown    Terminate All Processes  kill=False

*** Variables ***
${BASE_URL}       http://127.0.0.1:8000/wegan/list
${BROWSER}        Chrome

${name_1}         Wegan1
${weight_1}       66
${height_1}       1,66
${sex_1}          Male
${tags_1}         Onion

*** Test Cases ***
User Can Add New Wegan
    [Setup]  Open Browser  ${BASE_URL}  ${BROWSER}
    Go To Add Wegan
    Fill Form
    Submit Form
    Veryfy If Success Page appeard
    Go To Wegans List
    Veryfy If wegan_1 Appears On List
    [Teardown]  Close Browser

BMI And Physique Should be countet Correctly
    [Setup]  Open Browser  ${BASE_URL}  ${BROWSER}
    Go To Wegans List
    BMI for WeganForBMI should equal 27.94
    Physique for WeganForBMI should equal Overweight
    [Teardown]  Close Browser

*** Keywords ***
Prepare Django
    Copy File  ../test_template.sqlite3  ../db.sqlite3
    Start Process  python  ../manage.py  runserver  127.0.0.1:8000  alias=django

Go To Add Wegan
    Click Link  link:Add

Go To Wegans List
  Click Link  link:List

Fill Form
  Input Text    id:id_name     ${name_1}
  Input Text    id:id_weight   ${weight_1}
  Input Text    id:id_height   ${height_1}
  Select From List By Label    id:id_sex    ${sex_1}
  Click Element  xpath=//select[@id="id_tags"]/option[.="${tags_1}"]

Go To Edit
  [Arguments]  name
   No operation

Veryfy If Success Page appeard
  Page Should Contain Element  xpath://p[@class="alert-success"]

Veryfy If wegan_1 Appears On List
  No operation

Veryfy If wegan_2 Appears On List
  No operation

Veryfy If wegan_1 not Appears On List
  No operation

BMI for ${WeganName} should equal ${value}
  Element Text Should Be  xpath://tr[td//text()[contains(., '${WeganName}')]]/td[4]  ${value}

Physique for ${WeganName} should equal ${value}
  Element Text Should Be  xpath://tr[td//text()[contains(., '${WeganName}')]]/td[5]  ${value}

