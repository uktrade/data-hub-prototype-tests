Feature: Search allows people to look for things

  Background: Data hub contains some example data
    Given companies house entries exists with
        | company_number | company_name    | registered_address_address_1 | registered_address_town | registered_address_postcode | company_category        | company_status | incorporation_date |
        | 06768809       | Test company    | 10 The Street Lane           | LONDON                  | SW1 1AA                     | Private Limited Company | Active         | 2008-12-01         |

  Scenario: The user can search and see results
    Given the user searches for "test"
    Then the user should see a list of search results
    And the 1st result should contain the word "test" in it's title
