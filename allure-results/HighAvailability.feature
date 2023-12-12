  Scenario: Test submenu and button on the High Availability page
    Given The user is on the Home page

    When The user hovers over the "use_cases" menu
    And The user clicks on the "high_availability" submenu link and verify the redirection "high_availability" page

    When The user clicks on the "telco_provider" button
    Then The user should be redirected to the "telco_provider" page

    When The user clicks on the "fast_data_apps" button
    Then The user should be redirected to the "fast_data_apps" page

    When The user clicks on the "top-10-capabilites_2" button
    Then The user should be redirected to the "top-10-capabilites" page

    When The user clicks on the "avoid-it_4" button
    Then The user should be redirected to the "avoid-it" page

