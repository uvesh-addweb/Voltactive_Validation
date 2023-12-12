  Scenario: Test submenu and button on the Edge page
    Given The user is on the Home page

    When The user hovers over the "use_cases" menu
    And The user clicks on the "edge" submenu link and verify the redirection "edge" page

    When The user clicks on the "edge_computing" button
    Then The user should be redirected to the "edge_computing" page

    When The user clicks on the "rcr_weireless" button
    Then The user should be redirected to the "rcr_weireless" page

    When The user clicks on the "avoid-it_7" button
    Then The user should be redirected to the "avoid-it" page

    When The user clicks on the "vanilla_plus" button
    Then The user should be redirected to the "vanilla_plus" page
