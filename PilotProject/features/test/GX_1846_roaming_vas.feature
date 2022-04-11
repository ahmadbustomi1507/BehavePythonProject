#sample 1
Feature: roaming-vas-service

      @dynamic
      Scenario Outline: getSubscriberDetails
        Given User getting the MSISDN Target : <msisdn> with type : <type>
        When  User Hit the API with the payload
        Then  User successfully hit the API with status code 200

        Examples: Dynamic
        |msisdn        | type |
        |.             |.     |


