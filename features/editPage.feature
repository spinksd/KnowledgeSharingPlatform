Feature: EditPage

  As a user of the knowledge sharing platform
  I want to edit my published pages
  So that I can keep the information up to date

  Scenario: Attempt to edit page by accessing edit URL when logged in

    Given I have the url for the edit page of a published page that was created by my user
    And I am logged in
    When I enter the url into my web browser
    Then I am directed to the search page of the platform

  Scenario: Attempt to edit page by accessing edit URL when not logged in

    Given I have the url for the edit page of a published page that was created by my user
    And I am not logged in
    When I enter the url into my web browser
    Then I am directed to the sign-in page of the platform

  Scenario: View all editable items

    Given I am editing a published page that was created by my user
    And I am logged in
    When the editing page has loaded
    Then I can edit the title, description, tags and contacts information

  Scenario: Update Title

    Given I am editing a published page that was created by my user
    And I am logged in
    And I click on the text box for the title of the page
    When I remove the current title and type in the title to be 'test title - edited'
    Then the title on my edit page is set to 'test title - edited'

  Scenario: Update Description

    Given I am editing a published page that was created by my user
    And I am logged in
    And I click on the text box for the description of the page
    When I remove the current description and type in the description to be 'test description - edited'
    Then the description on my edit page is set to 'test description - edited'

  Scenario: Update Tags

    Given I am editing a published page that was created by my user
    And I am logged in
    And I click on the tags section of the page
    When I remove the current tags and add a tag 'test tag - edited'
    Then the only tag on my edit page is set to 'test tag - edited'

  Scenario: Update Contacts

    Given I am editing a published page that was created by my user
    And I am logged in
    And I click on the contacts section of the page
    When I remove any current additional contacts and add a contact 'test contact - edited'
    Then the contacts on my edit page should be my user and the 'test contact - edited' user

  Scenario: Publish my edits of my updated page

    Given I am editing a published page that was created by my user
    And I am logged in
    And I am happy with the information on the page
    And I am provided with a button to publish the page
    When I click on the publish button
    Then I am directed to the published page
    And the published page is updated with the information I have entered
