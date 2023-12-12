  Scenario: Test submenu and button on the Fraud Prevention page
    Given The user is on the Home page

    When The user hovers over the "use_cases" menu
    And The user clicks on the "fraud_prevention" submenu link and verify the redirection "fraud_prevention" page

    When The user clicks on the "litsen_to_podcast" button
    Then The user should be redirected to the "litsen_to_podcast" page

    When The user clicks on the "sakura" button
    Then The user should be redirected to the "sakura" page

    When The user clicks on the "age_of_5g" button
    Then The user should be redirected to the "age_of_5g" page

    When The user clicks on the "growth_engine" button
    Then The user should be redirected to the "growth_engine" page

    When The user clicks on the "avoid-it_8" button
    Then The user should be redirected to the "avoid-it" page

    When The user clicks on the "new_sql_2" button
    Then The user should be redirected to the "new_sql" page
