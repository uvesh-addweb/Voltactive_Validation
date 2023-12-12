  Scenario: Test submenu and button on the About page
    Given The user is on the Home page

    When The user hovers over the "company" menu
    And The user clicks on the "about" submenu link and verify the redirection "about" page
