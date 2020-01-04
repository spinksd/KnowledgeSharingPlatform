Feature: SignInPage

  As a user of the knowledge sharing platform
  I want to access the platform
  So that I can have access to useful information I can learn from

  Scenario: Navigate to the sign-in page of the platform when not logged in

    Given I have the url for the sign-in page of the knowledge sharing platform
    And I am not logged in
    When I enter the url into my web browser
    Then the sign-in page of the platform is displayed asking me to log in or sign up

  Scenario: Navigate to the sign-in page of the platform when logged in

    Given I have the url for the sign-in page of the knowledge sharing platform
    And I am logged in
    When I enter the url into my web browser
    Then I am directed to the search page of the platform

  Scenario: Enter valid credentials into sign-in form

     Given I am on the sign-in page of the platform
     And I am not logged in
     And I enter valid credentials into the sign-in form
     When I press submit
     Then I should be logged in
     And I am directed to the search page of the platform

  Scenario: Enter invalid credentials into sign-in form

    Given I am on the sign-in page of the platform
    And I am not logged in
    And I enter invalid credentials into the sign-in form
    When I press submit
    Then I should not be logged in
    And I should be presented with a message saying 'Your credentials are invalid, please try again.'

  Scenario: Click on sign-up button

    Given I am on the sign-in page of the platform
    And I am not logged in
    When I click on the sign-up button
    Then I should be directed to the sign-up page

 Scenario: Click on 'forgotten password?' button

   Given I am on the sign-in page of the platform
   And I am not logged in
   When I click on the 'forgotten password' button
   Then I should be directed to the forgotten password page