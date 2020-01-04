Feature: MostRecent

  As a user of the knowledge sharing platform
  I want to view the most recent published pages
  So that I quickly view examples of published pages

  Scenario: Navigate to the most recent page of the platform when logged in and pages have been published

    Given I have the url for the most recent page of the knowledge sharing platform
    And I am logged in
    When I enter the url into my web browser
    Then I can see the most recent pages published on the platform

  Scenario: Navigate to the most recent page of the knowledge sharing platform when logged in and no pages have been published

    Given I have the url for the most recent page of the knowledge sharing platform
    And I am logged in
    When I enter the url into my web browser
    Then I should see a message saying 'There have not been any pages published.'

  Scenario: Navigate to the most recent page of the platform when not logged in

    Given I have the url for the most recent page of the knowledge sharing platform
    And I am not logged in
    When I enter the url into my web browser
    Then I am directed to the sign-in page of the platform

  Scenario: Select a most recent page to view

    Given I am on the most recent page
    And I am logged in
    And I am presented with a view of the most recent published pages
    When I click anywhere on the area of a most recent page
    Then I am directed to the published page for the page I clicked on
