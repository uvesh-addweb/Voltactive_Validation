  Scenario: Test submenu and button on the Press Release page
    Given The user is on the Home page

    When The user hovers over the "company" menu
    And The user clicks on the "press_release" submenu link and verify the redirection "press_release" page

    When The user clicks on the "telecom_certificate" button
    Then The user should be redirected to the "telecom_certificate" page

    When The user clicks on the "i2i_systems" button
    Then The user should be redirected to the "i2i_systems" page

    When The user clicks on the "explosive_growth" button
    Then The user should be redirected to the "explosive_growth" page
