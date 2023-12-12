  Scenario: Test submenu and button on the Cloud page
    Given The user is on the Home page

    When The user hovers over the "use_cases" menu
    And The user clicks on the "cloud" submenu link and verify the redirection "cloud" page

    When The user clicks on the "microservices" button
    Then The user should be redirected to the "microservices" page

    When The user clicks on the "tech_stacks" button
    Then The user should be redirected to the "tech_stacks" page

    When The user clicks on the "decisioning_3" button
    Then The user should be redirected to the "decisioning" page

    When The user clicks on the "avoid-it_6" button
    Then The user should be redirected to the "avoid-it" page
