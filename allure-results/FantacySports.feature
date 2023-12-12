  Scenario: Test submenu and button on the Data Platform for Fantasy Sports page
    Given The user is on the Home page

    When The user hovers over the "use_cases" menu
    And The user clicks on the "fantasy_sports" submenu link and verify the redirection "fantasy_sports" page

    When The user clicks on the "sports_apps" button
    Then The user should be redirected to the "sports_apps" page

    When The user clicks on the "decisioning_4" button
    Then The user should be redirected to the "decisioning" page

    When The user clicks on the "top-10-capabilites_4" button
    Then The user should be redirected to the "top-10-capabilites" page

    When The user clicks on the "fast_data_apps_4" button
    Then The user should be redirected to the "fast_data_apps" page
