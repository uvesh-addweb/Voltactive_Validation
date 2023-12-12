  Scenario: Test submenu and button on the No Compromises page
    Given The user is on the Home page

    When The user hovers over the "why-volt" menu
    And The user clicks on the "no-compromises-menu" submenu link and verify the redirection "no-compromises-menu" page

    When The user clicks on the "learn-more" button
    Then The user should be redirected to the "learn-more" page

    When The user clicks on the "real-time" button
    Then The user should be redirected to the "real-time" page

    When The user clicks on the "streaming-data" button
    Then The user should be redirected to the "streaming-data" page

    When The user clicks on the "avoid-it" button
    Then The user should be redirected to the "avoid-it" page
