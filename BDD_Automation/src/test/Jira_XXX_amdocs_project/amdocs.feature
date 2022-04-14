Feature: amdocs-cm

  Scenario Outline:
      Scenario Outline: Redeem the voucher SA (Functionality Test)
        Given User getting the MSISDN : <MSISDN>
        When  User Hit the API with the payload
        Then  User successfully hit the API with status code 200

        Examples: Dynamic
        |MSISDN |
        |6287877244027|
        |6287877244036|
        |6287879346682|
        |6287879550484|
        |6287880570611|
        |6287880570613|
