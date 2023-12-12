  Scenario: Test submenu and button on the Billing Mediation Data page
    Given The user is on the Home page

    When The user hovers over the "use_cases" menu
    And The user clicks on the "billing_mediation" submenu link and verify the redirection "billing_mediation" page

    When The user clicks on the "telco_mediation" button
    Then The user should be redirected to the "telco_mediation" page

    When The user clicks on the "data_platform" button
    Then The user should be redirected to the "data_platform" page

    When The user clicks on the "edge_iot" button
    Then The user should be redirected to the "edge_iot" page

    When The user clicks on the "kafka_challange" button
    Then The user should be redirected to the "kafka_challange" page
