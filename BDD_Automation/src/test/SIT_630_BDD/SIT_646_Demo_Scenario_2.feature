
Feature: Demo scenario
    #Contoh 1, dengan scenario outline
    @dynamic @SIT_507 @SIT_647
    Scenario Outline: <scenario_name>
      Given User execute the test scenario <scenario_id> <scenario_name>
        And with the MSISDN : <msisdn>
      When  User Hit the API with the payload
      Then  User successfully hit the API with status code 200

      Examples: Dynamic
      |scenario_id|scenario_name |msisdn |
      |.          |.             | .     |

    #Contoh 2, dengan regression  (static data)
#    @SIT_507
#    Scenario : SIT_507_Perform purchase package Xtra Combo 8GB 59rb (service id: 8211022) with xl prepaid subscriber
#      Given User execute the test scenario <scenario_name>
#        And with the MSISDN : "6287868381200"
#      When  User Hit the API with the payload
#      Then  User successfully hit the API with status code 200
#
#     @SIT_647
#     Scenario : SIT_647_Perform purchase package Xtra Combo 8GB 59rb (service id: 8211022) when balance is insufficient with xl prepaid subscriber
#      Given User execute the test scenario <scenario_name>
#        And with the MSISDN : "6287868381200"
#      When  User Hit the API with the payload
#      Then  User successfully hit the API with status code 200
