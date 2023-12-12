  Scenario: Test submenu and button on the Kafks + Streaming Data page
    Given The user is on the Home page

    When The user hovers over the "use_cases" menu
    And The user clicks on the "kafka" submenu link and verify the redirection "kafka" page

    When The user clicks on the "streaming_data" button
    Then The user should be redirected to the "streaming_data" page

    When The user clicks on the "architects" button
    Then The user should be redirected to the "architects" page

    When The user clicks on the "advantage_streaming" button
    Then The user should be redirected to the "advantage_streaming" page

    When The user clicks on the "top-10-capabilites_3" button
    Then The user should be redirected to the "top-10-capabilites" page
