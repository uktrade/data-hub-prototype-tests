Feature: Allow a user to archive a company

  Scenario: The user can archive a company
    Given a company exists with
      | registered_name | uk_based | business_type | sectors  | region |
      | Test company    | True     | Sole trader   | Creative | London |

    When the user searches for "Test company"
    And the user selects a result containing the title "Test company"
    Then the user presses the "Archive company" button
    And the user selects 'The company has shut down' as a reason to archive
    Then the user presses the "Archive now" button
    Then the "Archived" badge is displayed


  Scenario: The search results screen indicates an archived company
    Given a company exists with
      | registered_name | uk_based | business_type | sectors  | region | archive_date | archived_by  | archive_reason    |
      | Test company    | True     | Sole trader   | Creative | London | 2016-01-10   | Fred Smith   | Company dissolved |

    When the user searches for "Test company"


  Scenario: Company archive details are shown in the detail screen
    Given a company exists with
      | registered_name | uk_based | business_type | sectors  | region | archive_date | archived_by  | archive_reason    |
      | Test company    | True     | Sole trader   | Creative | London | 2016-01-10   | Fred Smith   | Company dissolved |

    When the user searches for "Test company"
    And the user selects a result containing the title "Test company"
    Then the "Archived" badge is displayed
    And "This company has been archived on 10 January 2016 by Fred Smith" is displayed
    And "Reason: Company dissolved" is displayed


  Scenario: An archived company and be un-archived
    Given a company exists with
      | registered_name | uk_based | business_type | sectors  | region | archive_date | archived_by  | archive_reason    |
      | Test company    | True     | Sole trader   | Creative | London | 2016-01-10   | Fred Smith   | Company dissolved |

    When the user searches for "Test company"
    And the user selects a result containing the title "Test company"
    Then the user presses the "Unarchive now" button
