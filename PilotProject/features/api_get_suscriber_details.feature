#sample 1
Feature: API Test <insert name of the API here>

      @dynamic
      Scenario Outline: Get Voucher detils
        Given User getting the MSISDN Target : <MSISDN_Target>
        When  User Hit the API with the payload
        Then  User successfully hit the API with status code 200

        Examples: Dynamic
        |MSISDN_Target |
        |.             |
