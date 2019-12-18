Feature: SignUpPage

  As a user of the knowledge sharing platform
  I want to get access to the platform
  So that I can have access to useful information I can learn from

  Scenario: Navigate to the sign-up page of the website when not logged in

    Given I have the url for the sign-up page of the knowledge sharing platform website
    And I have not logged in
    When I enter the url into my web browser
    Then the sign-up page of the website is displayed with a form requesting my forename, surname, role, email and password

