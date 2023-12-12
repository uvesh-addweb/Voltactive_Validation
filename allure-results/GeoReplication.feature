  Scenario: Test submenu and button on the Geo Replication page
    Given The user is on the Home page

    When The user hovers over the "use_cases" menu
    And The user clicks on the "geo_replication" submenu link and verify the redirection "geo_replication" page

    When The user clicks on the "learn-more_5" button
    Then The user should be redirected to the "learn-more_5" page

    When The user clicks on the "5g-monetization" button
    Then The user should be redirected to the "5g-monetization" page

    When The user clicks on the "avoid-it_3" button
    Then The user should be redirected to the "avoid-it" page

    When The user clicks on the "new_sql" button
    Then The user should be redirected to the "new_sql" page
