  Scenario: Test the Link Redirection on Footer
    Given The user is on the Home page

    When The user clicks on the "privacy_statment" button
    Then The user should be redirected to the "privacy_statment" page

    When The user clicks on the "licennse_agreement" button
    Then The user should be redirected to the "licennse_agreement" page

    When The user clicks on the "contributor_agreement" button
    Then The user should be redirected to the "contributor_agreement" page

    When The user clicks on the "sitemap" button
    Then The user should be redirected to the "sitemap" page

    When The user clicks on the "contact_us" button
    Then The user should be redirected to the "contact" page
