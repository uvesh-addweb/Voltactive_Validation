  Scenario: Test submenu and button on the IOT page
    Given The user is on the Home page

    When The user hovers over the "use_cases" menu
    And The user clicks on the "iot" submenu link and verify the redirection "iot" page

    When The user clicks on the "architects_2" button
    Then The user should be redirected to the "architects" page

    When The user clicks on the "advantage_streaming_3" button
    Then The user should be redirected to the "advantage_streaming" page

    When The user clicks on the "top-10-capabilites_6" button
    Then The user should be redirected to the "top-10-capabilites" page
