  Scenario: Test submenu and button on the News page
    Given The user is on the Home page

    When The user hovers over the "company" menu
    And The user clicks on the "news" submenu link and verify the redirection "news" page
