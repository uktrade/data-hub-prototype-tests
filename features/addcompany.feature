Feature: Add new company

  Background: The user is on the company add page
    Given the user is on the add company page

  Scenario: Create UK Company with minimal fields
    When the user enters values into the form
      | name                        | Freds bakery     |
      | uk_based                    | Yes              |
      | business_type               | Charity          |
      | uk_sector                   | Retail           |
      | registered_address_country  | United Kingdom   |
      | registered_address_1        | 10 Green drive   |
      | registered_address_town     | Green town       |
      | registered_address_county   | Surrey           |
      | registered_address_postcode | GT4 4TT          |
      | uk_region                   | South East       |
      | description                 | Test description |
    And the user clicks save
    Then the user should see the company details screen
    And the screen should show the following data
      | Title                       | Freds bakery   |
      | Registered address          | 10 Green drive, Green town, Surrey, GT4 4TT |
      | Company type                | Charity                                     |
      | Sector                      | Retail                                      |
      | Region                      | South East                                  |
      | Description                 | Test description                            |
