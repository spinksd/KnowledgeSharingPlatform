Feature: SignUpPage

  As a user of the knowledge sharing platform
  I want to get access to the platform
  So that I can have access to useful information I can learn from

  Scenario: Navigate to the signup page of the platform when not logged in

    Given I have the url for the signup page of the platform
    And I am not logged in
    When I enter the url into my web browser
    Then the signup page of the platform is displayed with a form requesting my forename, surname, role, email and password

  Scenario: Navigate to the signup page of the platform when logged in

    Given I have the url for the signup page of the platform
    And I am logged in
    When I enter the url into my web browser
    Then I am directed to the search page of the platform

  Scenario: Enter valid details into signup form

    Given I am on the signup page of the platform
    And I am not logged in
    And I enter valid details into the signup form
    When I press submit
    Then I should have a user created with the details I entered
    And I should be directed to the login page
    And I should be presented with a message saying 'User succesfully created.'

  Scenario: Enter invalid details into signup form

    Given I am on the signup page of the platform
    And I am not logged in
    And I enter invalid details into the signup form
    When I press submit
    Then I should not have a user created
    And I should be presented with a message saying 'Your details are invalid, please try again.'

  Scenario: Enter email already in use into signup form

    Given I am on the signup page of the platform
    And I am not logged in
    And I enter valid details into the signup form
    And the email I have entered is already in use by an account
    When I press submit
    Then I should not have a duplicate user created
    And I should be presented with a message saying 'A user has already been created for this email. Please request a new password via the 'Forgotten Password?' link.'

  Scenario: Click on login button

    Given I am on the signup page of the platform
    And I am not logged in
    When I click on the login button
    Then I should be directed to the login page
