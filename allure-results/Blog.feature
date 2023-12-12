  Scenario: Test submenu and button on the Blog page
    Given The user is on the Home page

    When The user hovers over the "resources" menu
    And The user clicks on the "blog" submenu link and verify the redirection "blog" page
