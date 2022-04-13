
Feature: GX_1846_roaming_vas
      Background: behave <feature_name> --tags=test1 --no-capture

      @test1 @dynamic
      Scenario Outline: getSubscriberDetails
        Given User getting the MSISDN Target : <msisdn> with type : <type>
          And get the test scenario name : <scenario_name>
        When  User Hit the API with the payload
        Then  User successfully hit the API with status code 200

        Examples: Dynamic
        | scenario_name |msisdn        | type |
        |.              |.             |.     |

      @test2 @putSubscriberDetails
      Scenario Outline: putSubscriberDetails
        Given User getting the MSISDN Target : <msisdn>
        When  User Hit the API with the payload
        Then  User successfully hit the API with status code 200

        Examples: Dynamic
        | scenario_name |msisdn        |
        |.              |.             |
