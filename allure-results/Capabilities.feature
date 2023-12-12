  Scenario: Test submenu and button on the Capabilities page
    Given The user is on the Home page

    When The user hovers over the "why-volt" menu
    And The user clicks on the "capabilites_4" submenu link and verify the redirection "capabilities_2" page

    When The user clicks on the "top-10-capabilites" button
    Then The user should be redirected to the "top-10-capabilites" page

    When The user clicks on the "avoid-it_2" button
    Then The user should be redirected to the "avoid-it" page

    When The user clicks on the "monitize_5g" button
    Then The user should be redirected to the "monitize_5g" page
