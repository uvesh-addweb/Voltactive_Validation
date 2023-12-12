  Scenario: Test submenu and button on the Volt For 5g page
    Given The user is on the Home page

    When The user hovers over the "why-volt" menu
    And The user clicks on the "volt-for-5g" submenu link and verify the redirection "volt-for-5g" page

    When The user clicks on the "learn-more_1" button
    Then The user should be redirected to the "learn-more_1" page

    When The user clicks on the "learn-more_2" button
    Then The user should be redirected to the "learn-more_2" page

    When The user clicks on the "learn-more_3" button
    Then The user should be redirected to the "learn-more_3" page

    When The user clicks on the "learn-more_4" button
    Then The user should be redirected to the "learn-more_4" page

    When The user clicks on the "try-volt_2" button
    Then The user should be redirected to the "try-volt_2" page

    When The user clicks on the "5g-policy" button
    Then The user should be redirected to the "5g-policy" page

    When The user clicks on the "telcos" button
    Then The user should be redirected to the "telcos" page
