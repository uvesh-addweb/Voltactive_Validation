  Scenario: Test submenu and button on the Monetizing AI + ML page
    Given The user is on the Home page

    When The user hovers over the "use_cases" menu
    And The user clicks on the "ai_ml" submenu link and verify the redirection "ai_ml" page

    When The user clicks on the "16_faqs" button
    Then The user should be redirected to the "16_faqs" page

    When The user clicks on the "decisioning" button
    Then The user should be redirected to the "decisioning" page

    When The user clicks on the "top-10-capabilites_5" button
    Then The user should be redirected to the "top-10-capabilites" page

    When The user clicks on the "fast_data_apps_2" button
    Then The user should be redirected to the "fast_data_apps" page

