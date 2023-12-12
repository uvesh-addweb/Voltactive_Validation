  Scenario: Test submenu and button on the OEM-Friendly page
    Given The user is on the Home page

    When The user hovers over the "use_cases" menu
    And The user clicks on the "oem" submenu link and verify the redirection "oem" page

    When The user clicks on the "framework" button
    Then The user should be redirected to the "framework" page

    When The user clicks on the "decisioning_2" button
    Then The user should be redirected to the "decisioning" page

    When The user clicks on the "fast_data_apps_3" button
    Then The user should be redirected to the "fast_data_apps" page

    When The user clicks on the "avoid-it_5" button
    Then The user should be redirected to the "avoid-it" page
