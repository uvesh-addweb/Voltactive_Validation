  Scenario: Test submenu and button on the BSS page
    Given The user is on the Home page

    When The user hovers over the "use_cases" menu
    And The user clicks on the "bss" submenu link and verify the redirection "bss" page

    When The user clicks on the "bss_framework" button
    Then The user should be redirected to the "bss_framework" page

    When The user clicks on the "bss_solution" button
    Then The user should be redirected to the "bss_solution" page

    When The user clicks on the "data_platform_2" button
    Then The user should be redirected to the "data_platform" page

    When The user clicks on the "edge_iot_2" button
    Then The user should be redirected to the "edge_iot" page

    When The user clicks on the "kafka_challange_2" button
    Then The user should be redirected to the "kafka_challange" page
