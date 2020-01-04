Feature: SearchPage

  As a user of the knowledge sharing platform
  I want to search the platform for information
  So that I can find useful/relevant documentation that I can learn from

  Scenario: Navigate to the search page of the platform when logged in

    Given I have the url for the search page of the knowledge sharing platform
    And I am logged in
    When I enter the url into my web browser
    Then I can see the search box, most recent, my pages, top rated, upload document, create page and about tiles

  Scenario: Navigate to the search page of the platform when not logged in

    Given I have the url for the search page of the knowledge sharing platform
    And I am not logged in
    When I enter the url into my web browser
    Then I am directed to the sign-in page of the platform

  Scenario: Search for a keyword or sentence that has matches

    Given I am on the search page
    And I am logged in
    And there is a page published on the platform with the word 'amazon' in the description
    And I am presented with a way to search the platform
    And I enter the text 'amazon' in the search box
    When I click on the search button
    Then I am presented with the page results that match most closely to the text entered for my search

  Scenario: Search for a keyword or sentence that has no matches

    Given I am on the search page
    And I am logged in
    And I am presented with a way to search the platform
    And I enter the text 'machine learning' in the search box
    When I click on the search button
    Then I am presented with a message saying 'No results found for your search. Please try another search.'

  Scenario: Filter search on a tag

    Given I am on the search page
    And I am logged in
    And there is a page published on the platform with the word 'amazon' in the description
    And the same published page has a tag of 'AWS'
    And I am presented with a way to search the platform
    And I enter the text 'amazon' in the search box
    And I click on the advanced button
    And I apply a filter on a tag of 'AWS'
    When I click on the search button
    Then I am presented with the results that match most closely to my text for my search that have the tag 'AWS'

  Scenario: Filter search on multiple tags

    Given I am on the search page
    And I am logged in
    And there is a page published on the platform with the word 'amazon' in the description
    And the same published page has a tag of 'AWS'
    And the same published page has a contact of 'John Doe'
    And I am presented with a way to search the platform
    And I enter the text 'amazon' in the search box
    And I click on the advanced button
    And I apply a filter on a tag of 'AWS'
    And I apply a filter on a contact name of 'John Doe'
    When I click on the search button
    Then I am presented with the results that match most closely to my text for my search
    And the results must have the tag 'AWS' and must have a contact of 'John Doe'

  Scenario: Select a result/page to look at

    Given I am on the search page
    And I am logged in
    And I have run a search
    And I have had at least one result to my search
    When I click anywhere on the area of a result
    Then I am taken to the published page for the result I clicked on