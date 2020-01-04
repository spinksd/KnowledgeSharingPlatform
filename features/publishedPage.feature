Feature: PublishedPage

  As a user of the knowledge sharing platform
  I want to view published pages
  So that I edit my own or view others to learn and gain valuable information from them

  Scenario: Navigate to a published page of the platform when logged in

    Given I have the url for a published page of the knowledge sharing platform
    And I am logged in
    When I enter the url into my web browser
    Then I am directed to the published page
    And I can see the title, description, tags, document (if exists) and contact information for the page

  Scenario: Navigate to a published page of the platform when not logged in

    Given I have the url for a published page of the knowledge sharing platform
    And I am not logged in
    When I enter the url into my web browser
    Then I am directed to the sign-in page of the platform

  Scenario: Edit my published pages

    Given I am on a published page that was created by my user
    And I am logged in
    And I am provided with a button to edit the page
    When I click on the edit button
    Then I am directed to the editing view for the page
