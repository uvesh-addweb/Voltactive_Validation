Feature: Verification of Logo and Menu links

  Scenario: Logo presence on Voltactive Home page
    Given The browser is launched
    When Open Voltactive homepage
    Then Verify that the logo present on the page

  Scenario: Menu links verification on home page
    Given The user is on home page
    When Get the menu Links
    Then Verify that the links are enable and clickable

#  Scenario: Links and Buttons verification on home page.
#    Given The user is on the home page
#    When Get the Buttons and links from the page
#    Then Verify that the links and buttons are enable and clickable

#  Scenario: Links and Buttons verification on No Compromises page.
#    Given The user is on the No Compromises page
#    When Get the Buttons and links from the No Compromises page
#    Then Verify that the links and buttons are enable and clickable on No Compromises page

#  Scenario: Links and Buttons verification on Volt for 5g page.
#    Given The user is on the Volt for 5g page
#    When Get the Buttons and links from the Volt for 5g page
#    Then Verify that the links and buttons are enable and clickable on Volt for 5g page
#
