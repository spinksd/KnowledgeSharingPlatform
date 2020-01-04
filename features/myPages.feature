Feature: MyPages

  As a user of the knowledge sharing platform
  I want to view the pages I have created and published
  So that I edit them or share them

  Scenario: Navigate to the my pages page of the platform when logged in and have published a page

    Given I have the url for the 'my pages' page of the knowledge sharing platform
    And I am logged in
    And I have previously published a page
    When I enter the url into my web browser
    Then I should see a collection of the pages that I have published

  Scenario: Navigate to the 'my pages' page of the platform when logged in and have not published a page

    Given I have the url for the 'my pages' page of the knowledge sharing platform
    And I am logged in
    When I enter the url into my web browser
    Then I should see a message saying 'You have not published any pages.'

  Scenario: Navigate to the 'my pages' page of the platform when not logged in

    Given I have the url for the 'my pages' page of the knowledge sharing platform
    And I am not logged in
    When I enter the url into my web browser
    Then I am directed to the sign-in page of the platform

  Scenario: Select a 'my pages' page to view when I have published a page

    Given I am on the 'my pages' page of the platform
    And I am logged in
    And I have previously published a page
    When I click anywhere on the area of one of my published pages
    Then I am directed to the published page for the page I clicked on