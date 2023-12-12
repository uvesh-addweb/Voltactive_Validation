  Scenario: Test submenu and button on the Real-Time Decisioning page
    Given The user is on the Home page

    When The user hovers over the "use_cases" menu
    And The user clicks on the "real_time_desisoning" submenu link and verify the redirection "real_time_desisoning" page

    When The user clicks on the "mediation_for_telcos" button
    Then The user should be redirected to the "mediation_for_telcos" page

    When The user clicks on the "real_time_personalization" button
    Then The user should be redirected to the "real_time_personalization" page
