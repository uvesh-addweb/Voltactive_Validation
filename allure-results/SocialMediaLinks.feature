  Scenario: Test the Social Media Links Redirection on Footer
    Given The user is on the Home page

    When The user clicks on the "linked_in" button
    Then The user should be redirected to the "linked_in" page
