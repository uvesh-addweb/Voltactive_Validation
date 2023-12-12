  Scenario: Test submenu and button on the Partner Program page
    Given The user is on the Home page

    When The user hovers over the "resources" menu
    And The user clicks on the "partner_program" submenu link and verify the redirection "partner_program" page

    When The user clicks on the "top-10-capabilites_7" button
    Then The user should be redirected to the "top-10-capabilites" page

    When The user clicks on the "decisioning_5" button
    Then The user should be redirected to the "decisioning" page

    When The user clicks on the "advantage_streaming_4" button
    Then The user should be redirected to the "advantage_streaming" page

    When The user clicks on the "avoid-it_10" button
    Then The user should be redirected to the "avoid-it" page
