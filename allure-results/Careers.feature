  Scenario: Test submenu and button on the Careers page
    Given The user is on the Home page

    When The user hovers over the "company" menu
    And The user clicks on the "careers" submenu link and verify the redirection "careers" page

    When The user clicks on the "linkedin_page_jobs" button
    Then The user should be redirected to the "linkedin_page_jobs" page
