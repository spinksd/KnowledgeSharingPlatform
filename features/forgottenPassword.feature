Feature: forgottenPassword

  As a user of the knowledge sharing platform
  I want to reset my password for my account
  So that I can regain access to the platform

  Scenario: Navigate to the forgotten password page of the website when not logged in

    Given I have the url for the forgotten password page of the knowledge sharing platform
    And I am not logged in
    When I enter the url into my web browser
    Then the forgotten password page of the website is displayed with a form requesting the email that's associated with the account

  Scenario: Navigate to the forgotten password page of the website when logged in

    Given I have the url for the forgotten password page of the knowledge sharing platform
    And I am logged in
    When I enter the url into my web browser
    Then I am directed to the search page of the platform
    And I should be presented with a message saying 'You need to be logged out to access that page.'

  Scenario: Enter valid email into forgotten password form
    Given I am on the forgotten password page
    and I am not logged in
    And I enter an email that is associated with an account into the form
    When I press submit
    Then I should be presented with a message saying 'An email has been sent to the user's email address if exists. Please follow the instructions on the email to reset your password.'
    And I should receive an email to the email address I entered with instructions on how to reset my password

  Scenario: Enter invalid email into forgotten password form
    Given I am on the forgotten password page
    And I am not logged in
    And I enter an email that is not associated with an account into the form
    When I press submit
    Then I should be presented with a message saying 'An email has been sent to the user's email address if exists. Please follow the instructions on the email to reset your password.'

  Scenario: Click on login button

    Given I am on the forgotten password page of the platform
    And I am not logged in
    When I click on the login button
    Then I should be directed to the login page