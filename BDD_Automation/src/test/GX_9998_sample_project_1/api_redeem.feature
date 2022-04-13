#sample 1
Feature: API Test <insert name of the API here>

      @dynamic
      Scenario Outline: Redeem the voucher SA (Functionality Test)
        Given User getting the MSISDN RO : <MSISDN_RO>, MSISDN Target :<MSISDN_Target>, Voucher : <Voucher>, HRN : <HRN> from Releng
        When  User Hit the API with the payload
        Then  User successfully hit the API with status code 200

        Examples: Dynamic
        |MSISDN_RO | MSISDN_Target | Voucher | HRN |
        |.         |.              |.        |.    |

#sample 2
#Feature: Redeem voucher with Valid XL Number
#
#      Scenario: Prepare the MSISDN RO
#        Given Ready to used MSISDN number as "123"
#        When  User reset balance of the MSISDN to be "123"
#        Then  The balance is successfully reset to be "123"

#      Scenario: Prepare the MSISDN Target
#        Given Ready to used MSISDN number as "321"
#        When  User reset balance of the MSISDN to be "321"
#        Then  The balance is successfully reset to be "321"
#
#      Scenario: Prepare the Voucher
#        Given Ready to used VOUCHER_SERIAL_NUMBER as "12678125" and HRN "HRN_92138327"
#        When  User query update the Denom to "3", Expired date "05-04-2022T05:10:20",
#        Then VOUCHER_SERIAL_NUMBER is in the table voucher
#
#      Scenario: Redeem the voucher to target
#        Given User able to hit the API "<API endpoint>"
#        When  Access the API with payload 123 , 321 and HRN_92138327
#        Then  User successfully redeem the voucher
