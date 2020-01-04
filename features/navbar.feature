Feature: NavBar

  As a user of the knowledge sharing platform
  I want to navigate around the platform
  So that I can quickly get to the page I want

  Scenario: Visible pages when not logged in

    Given I am on the log-in page
    And I am not logged in
    When I click on the navbar menu
    Then I am only shown links to the sign-up, log-in, forgotten password and about pages

  Scenario: Visible pages when logged in

    Given I am on the search page
    And I am logged in
    When I click on the navbar menu
    Then I am shown links to the search, create, upload document, top rated, most recent, my pages, about page and a sign-out option.

  Scenario: Search from any page

    Given I am on the top rated page
    And I am logged in
    And I enter some text to search for
    When I submit my search
    Then I am directed to the results page with the page results that match most closely to the text entered for my search

  Scenario: Sign out when logged in and on any page

    Given I am on any page of the platform
    And I am logged in
    When I click on the navbar sign-out link
    Then I am logged out of my current session
    And I am directed to the log-in page of the platform

  Scenario: Navigate to sign-up page

    Given I am on the log-in page of the platform
    And I am not logged in
    When I click on the sign-up link in the navbar
    Then I am directed to the sign-up page

  Scenario: Navigate to log-in page

    Given I am on the sign-up page of the platform
    And I am not logged in
    When I click on the log-in link in the navbar
    Then I am directed to the log-in page

  Scenario: Navigate to forgotten password page

    Given I am on the log-in page of the platform
    And I am not logged in
    When I click on the forgotten password link in the navbar
    Then I am directed to the forgotten password page

  Scenario: Navigate to about page

    Given I am on the log-in page of the platform
    And I am not logged in
    When I click on the about link in the navbar
    Then I am directed to the about page

  Scenario: Navigate to search page

    Given I am on the about page of the platform
    And I am logged in
    When I click on the search link in the navbar
    Then I am directed to the search page

  Scenario: Navigate to create page

    Given I am on the about page of the platform
    And I am logged in
    When I click on the create link in the navbar
    Then I am directed to the create page

  Scenario: Navigate to upload document page

    Given I am on the about page of the platform
    And I am logged in
    When I click on the upload document link in the navbar
    Then I am directed to the upload document page

  Scenario: Navigate to top rated page

    Given I am on the about page of the platform
    And I am logged in
    When I click on the top rated link in the navbar
    Then I am directed to the top rated page

  Scenario: Navigate to most recent page

    Given I am on the about page of the platform
    And I am logged in
    When I click on the search most recent in the navbar
    Then I am directed to the most recent page

  Scenario: Navigate to my pages page

    Given I am on the about page of the platform
    And I am logged in
    When I click on the my pages link in the navbar
    Then I am directed to the my pages page

  Scenario: Sign-out of platform

    Given I am on the about page of the platform
    And I am logged in
    When I click on the sign-out link in the navbar
    Then I am logged out of the platform
    And I am directed to the log-in page of the platform