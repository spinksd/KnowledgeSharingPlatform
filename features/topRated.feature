Feature: TopRated

  As a user of the knowledge sharing platform
  I want to view the top rated published pages
  So that I quickly find the most useful information

  Scenario: Navigate to the top rated page of the website when logged in and pages have been published

    Given I have the url for the top rated page of the knowledge sharing platform
    And I am logged in
    When I enter the url into my web browser
    Then the top rated page of the website is displayed

  Scenario: Navigate to the top rated page of the website when logged in and no pages have been published

    Given I have the url for the top rated page of the knowledge sharing platform
    And I am logged in
    When I enter the url into my web browser
    Then I should see a message saying 'There have not been any published pages liked.'

  Scenario: Navigate to the top rated page of the website when not logged in

    Given I have the url for the top rated page of the knowledge sharing platform
    And I am not logged in
    When I enter the url into my web browser
    Then I am directed to the sign-in page of the website

  Scenario: Select a top rated page to view

    Given I am on the top rated page
    And I am logged in
    And I am presented with a view of the top rated pages
    When I click anywhere on the area of a top rated page
    Then I am directed to the published page for the page I clicked on
