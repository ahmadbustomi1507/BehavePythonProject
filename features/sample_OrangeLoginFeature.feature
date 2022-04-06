Feature: OrangeHRM Login
#    Scenario: Logo presence on orange
#        Given i launch Chrome browser
#        When i Open Orange HRM Homepage
#        And Enter username "admin" and password "admin123"
#        And Click on login button
#        Then user must successfully login to the dashboard page

    Scenario Outline: Logo presence on orange
        Given i launch Chrome browser
        When i Open Orange HRM Homepage
        And Enter username "<username>" and password "<password>"
        And Click on login button
        Then user must successfully login to the dashboard page

        Examples:
        | username | password |
        | admin    | admin123 |
        | admin123 | admin    |
        | adminxyz | admin123 |
        | admin    | adminxyz |
