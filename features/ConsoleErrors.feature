Feature: Verification of Console Errors

  Scenario: Check for console errors in sitemap pages
    Given The sitemap URL is "https://voltSTG:oI5L!YKmQ@1gOvqQ@stg.voltactivedata.com/sitemap"
    When I check for console errors in sitemap pages
    Then I should see the console errors for each page, if any