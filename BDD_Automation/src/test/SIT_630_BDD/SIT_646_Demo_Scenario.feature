
Feature: amdocs-cm
    @dynamic @SIT_507 @SIT_647
    Scenario Outline: Getting msisdn info
      Given User execute the test scenario <scenario_name>
        And with the MSISDN : <MSISDN>
      When  User Hit the API with the payload
      Then  User successfully hit the API with status code 200

      Examples: Dynamic
      |scenario_name |MSISDN |
      |.             | .     |
