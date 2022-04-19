
Feature: amdocs-cm
    @normal @dynamic @method @automation @test_id
    Scenario Outline: Getting msisdn info
      Given User getting the MSISDN : <MSISDN>
      When  User Hit the API with the payload
      Then  User successfully hit the API with status code 200

      Examples: Dynamic
      |scenario_name |MSISDN |
      |scenario_1    |6287877244027|
      |scenario_2    |6287877244036|
      |scenario_3    |6287879346682|
      |scenario_4    |6287879550484|
      |scenario_5    |6287880570611|
      |scenario_6    |6287880570613|

#      @method @regression @test_id
#      Scenario: Redeem the voucher SA (Functionality Test)
#        Given User getting the MSISDN : <MSISDN>
#        When  User Hit the API with the payload
#        Then  User successfully hit the API with status code 200

#      @method @regression
#      Scenario: Redeem the voucher SA (Functionality Test)
#        Given User getting the MSISDN : <MSISDN>
#        When  User Hit the API with the payload
#        Then  User successfully hit the API with status code 200
#
#      @method @regression
#      Scenario: Redeem the voucher SA (Functionality Test)
#        Given User getting the MSISDN : <MSISDN>
#        When  User Hit the API with the payload
#        Then  User successfully hit the API with status code 200