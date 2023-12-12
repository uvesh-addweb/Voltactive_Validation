  Scenario: Test submenu and button on the Webinars and Events page
    Given The user is on the Home page

    When The user hovers over the "resources" menu
    And The user clicks on the "webinar" submenu link and verify the redirection "webinar" page

    When The user clicks on the "register_now" button
    Then The user should be redirected to the "register_now" page

    When The user clicks on the "view_now_1" button
    Then The user should be redirected to the "view_now_1" page

    When The user clicks on the "view_now_2" button
    Then The user should be redirected to the "view_now_2" page

    When The user clicks on the "view_now_3" button
    Then The user should be redirected to the "view_now_3" page
