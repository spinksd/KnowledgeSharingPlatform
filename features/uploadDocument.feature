Feature: UploadDocument

  As a user of the knowledge sharing platform
  I want to upload a document to the platform
  So that I can share valuable information within my company

  Scenario: Navigate to the upload document page of the website when logged in

    Given I have the url for the upload document page of the knowledge sharing platform
    And I am logged in
    When I enter the url into my web browser
    Then I should be presented with a way to upload a document to the platform

  Scenario: Navigate to the upload document page of the website when not logged in

    Given I have the url for the upload document page of the knowledge sharing platform
    And I am not logged in
    When I enter the url into my web browser
    Then I am directed to the sign-in page of the website

  Scenario: Upload a valid document to the platform

    Given I am on the upload document page
    And I am logged in
    And I provide a valid document to upload in the upload form
    When I press submit
    Then I should be directed to the create page with the title, description and tags automatically generated and populated
    And I can review and edit the generated information before publishing the page

  Scenario: Attempt to upload an invalid document to the website

    Given I am on the upload document page
    And I am logged in
    And I provide an invalid document to upload
    When I press submit
    Then I should be presented with a message saying 'Invalid document selected, please upload a valid document.'