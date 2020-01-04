Feature: CreatePage

  As a user of the knowledge sharing platform
  I want to create a page
  So that I can share valuable, accurate and human-readable information

  Scenario: Navigate to the create page of the platform when logged in

    Given I have the url for the create page of the knowledge sharing platform
    And I am logged in
    When I enter the url into my web browser
    Then I am directed to the create page of the platform
    And I can edit the title, description, tags and contacts information
    And My user will be the default contact in the contacts section

  Scenario: Navigate to the create page of the platform when not logged in

    Given I have the url for the create page of the knowledge sharing platform
    And I am not logged in
    When I enter the url into my web browser
    Then I am directed to the sign-in page of the platform

  Scenario: Edit Title information before publishing

    Given I am on the create page
    When I click on the text box for the title of the page
    Then I can edit the text and update it to the title of my choice

  Scenario: Edit page description information before publishing

    Given I am on the create page
    When I click on the text box for the description of the page
    Then I can edit the text and update it to the description of my choice

  Scenario: Edit page tags before publishing

    Given I am on the create page
    When I click on the tags section of the page
    Then I can edit the tags and update it to the tags of my choice

  Scenario: Edit contacts before publishing

    Given I am on the create page
    When I click on the contacts section of the page
    Then I can edit the contact list and update it with the users of my choice
    And my user must always be on the list

  Scenario: Publish page

    Given I am on the create page
    And I am happy with the information on the page
    When I click on the publish button
    Then the page should be published on the platform
    And I am directed to the published page
