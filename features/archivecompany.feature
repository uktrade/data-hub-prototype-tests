Feature: Allow a user to archive a company
  Companies should never be deleted, but the user should be allowed to 'archive' companies, marking them as no
  longer active. Users also need to be able to un-archive a company if it becomes active again, to reduce duplication

  Background: Data hub contains a few companies, both active and non active
    Given companies exists with
      | registered_name | uk_based | business_type | sectors    | region | registered_address_1 | registered_address_town | registered_address_postcode | company_category        | company_status | archive_date | archived_by  | archive_reason       |
      | Test company A  | True     | Sole trader   | Creative   | London | 10 The Street Lane   | LONDON                  | SW1 1AA                     | Private Limited Company | Active         | 2016-01-10   | Fred Smith   | Company is dissolved |
      | Test company B  | True     | Sole trader   | Automotive | London | 20 The Street Lane   | LONDON                  | SW1 2AA                     | Sole Trader             | Active         |              |              |                      |
      | Test company C  | True     | Sole trader   | Aerospace  | London | 30 The Street Lane   | LONDON                  | SW1 3AA                     | Private Limited Company | Active         |              |              |                      |
      | Test company D  | True     | Sole trader   | Education  | London | 40 The Street Lane   | LONDON                  | SW1 4AA                     | Private Limited Company | Active         |              |              |                      |
      | Test company E  | True     | Sole trader   | Nuclear    | London | 50 The Street Lane   | LONDON                  | SW1 5AA                     | Private Limited Company | Active         |              |              |                      |
    And contacts exist with
      | company         | title | first_name | last_name | role     | email          | phone         |
      | Test company A  | Mr    | Fred       | Smith     | Director | fred@acme.com  | 07777 777 777 |
      | Test company B  | Mrs   | Julie      | Brown     | Director | julie@acme.com | 07777 777 777 |
    And interactions exist with
      | company         | contact      | interaction_type | subject                | date_of_interaction | advisor    | notes                    |
      | Test company A  | Fred Smith   | Face to face     | Had a chat about stuff | 2016-01-01          | Greg Green | Some test notes          |
      | Test company B  | Julie Brown  | Email            | Advised about exports  | 2016-02-01          | Greg Green | Docs requested by client |


  Scenario: The search results screen indicates an archived company
    When the user searches for "Test company A"
    Then the result for "Test company A" indicates the company is archived


  Scenario: The search results screen indicates an company is not archived
    When the user searches for "Test company B"
    Then the result for "Test company B" does not indicate the company is archived


  Scenario: The user is allowed to archive a company
    When the user views company "Test company B"
    Then the user can archive the company
    And the user selects 'Company is dissolved' as a reason to archive and archives the company
    Then the company detail screen indicates the company is archived
    And "This company has been archived" is displayed
    And "Reason: Company is dissolved" is displayed


  Scenario: An archived company can be un-archived
    When the user views company "Test company A"
    Then the user unarchives the company
    Then the company detail screen does not indicate the company is archived


  Scenario: Company archive details are shown in the detail screen
    When the user views company "Test company A"
    Then the company detail screen indicates the company is archived
    And "This company has been archived on 10 January 2016 by Fred Smith" is displayed
    And "Reason: Company is dissolved" is displayed


  Scenario: The user gets an error if no reason is given to unarchive
    When the user views company "Test company B"
    Then the user can archive the company
    And the user archives the company
    Then the user should see an error
    And the company detail screen does not indicate the company is archived


  Scenario: The user cannot archive a Companies House only result
    Given companies house entries exists with
      | company_number | company_name    | registered_address_address_1 | registered_address_town | registered_address_postcode | company_category        | company_status | incorporation_date |
      | 06768809       | zzz             | 10 The Street Lane           | LONDON                  | SW1 1AA                     | Private Limited Company | Active         | 2008-12-01         |
    And the user views a companies house record with company number "06768809"
    Then the user cannot archive the company


  Scenario: The user cannot edit an archived company
    When the user views company "Test company A"
    Then the user cannot edit the company


  Scenario: The user cannot add contacts to an archived company
    When the user views company "Test company A"
    Then the user selects the "Contacts" tab
    And the user cannot add a contact


  Scenario: The user cannot add interactions to an archived company
    When the user views company "Test company A"
    Then the user selects the "Interactions" tab
    And the user cannot add an interaction


  Scenario: Don't warn the user about not being able to add interactions
    When the user views company "Test company A"
    Then the user selects the "Interactions" tab
    And the user does not see an error summary


  Scenario: User can view but not Edit contacts
    When the user views the contact "Fred Smith"
    Then the user cannot edit the contact


  Scenario: User can view but not edit interactions
    When the user views the interaction "Had a chat about stuff"
    Then the user cannot edit the interaction