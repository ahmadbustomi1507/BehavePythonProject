
Feature: Demo scenario
    #Contoh 1, dengan scenario outline,flownya sama
    @dynamic @SIT_507 @SIT_647
    Scenario Outline: <scenario_id> <scenario_name>
      Given User execute the test scenario <scenario_id> <scenario_name>
        And with the MSISDN : <msisdn>
      When  User Hit the API with the payload
      Then  User successfully hit the API with status code 200

      Examples: Dynamic
      |scenario_id|scenario_name |msisdn |
      |.          |.             | .     |

#    #Contoh 2,  regression , asumsikan nomor msisdn sudah otomatis
#    @SIT_507
#    Scenario : SIT_507_Perform purchase package Xtra Combo 8GB 59rb with multiple request
#      Given User prepared the data test automated as
#          |scenario_id|scenario_name |msisdn |
#          |.          |.             | .     |
#      When  User Hit the API with the payload
#        And User Hit the API with the payload
#      Then  User successfully hit the API with status code 200
#
#     @SIT_647
#     Scenario : SIT_647_Perform purchase package Xtra Combo 8GB 59rb (service id: 8211022) with wrong payload
#      Given User execute the test scenario <scenario_name>
#          |scenario_id|scenario_name |msisdn |
#          |.          |.             | .     |
#        And with the MSISDN : "6287868381200"
#      When  User Hit the API with the payload
#      Then  User successfully hit the API with status code 200
