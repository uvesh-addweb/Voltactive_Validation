  Scenario: Test submenu and button on the Documentation page
    Given The user is on the Home page

    When The user hovers over the "resources" menu
    And The user clicks on the "documentation" submenu link and verify the redirection "documentation" page
