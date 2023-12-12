Feature: Sitemap URL Verification

  Scenario: Verify URLs from sitemap
    Given The user is on the Sitemap page
    When The user verifies all URLs
    Then All URLs should be redirected correctly
