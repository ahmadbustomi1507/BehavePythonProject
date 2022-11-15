Feature: API test https://gorest.co.in/public/v1/posts
     The purpose of this scenario is simple api test, which steps are explained in the user story
     below:
     created user info:
        "id": 1769,
        "name": "Tomi",
        "email": "somerandomemail.@gmail.com",
        "gender": "male",
        "status": "active"

     1. As a user, I want to create a post with data:
         {
          "id": 10,
          "user_id": 8,
          "title": "Automation test 15/01/2022",
          "body": "This is just a random post for an automation with BDD approach"
         }
         created User
     2. As a user, I want to see the details of a post that I recently create.
     3. As a user, I want to update the products that I recently created to update body {"body": "[modified]This is just a random post for an automation with BDD approach"}
     4. As a user, I want to delete the products that I recently updated.

      Scenario: create a post
        Given Successfully registered new user_id "1769"
        When  User create a new post
        Then POST success with reponse code "201"

      Scenario: get the post
         Given Successfully registered new user_id "1769"
         When User get the created post
         Then GET success with response code "200"

       Scenario: update the post
         Given Successfully registered new user_id "1769"
         When User update the created post
         Then PUT success with response "200"

       Scenario: Delete the post
         Given Successfully registered new user_id "1769"
         When User delete the created post
         Then DELETE success with response "204"
http://redeem-voucher-sa-sit.api.devgcp.excelcom.co.id/umb/menu/business/transferSa?DEALERMSISDN=628176677807&HRN=4678009180739283&MSISDN=628176677807&USERINPUT=6281808030805
http://10.24.139.15:9997/custom-action
{
	"action": "RESETBALANCE",
	"param": [
		{
			"paramname": "MSISDN",
			"paramvalue": "6281808030805"
		},
		{
			"paramname": "BALANCE",
			"paramvalue": "50000"
		},
		{
			"paramname": "TYPE",
			"paramvalue": "MO"
		}
	]

}
{
	"action": "RESETBALANCE",
	"param": [
		{
			"paramname": "MSISDN",
			"paramvalue": "628176677807"
		},
		{
			"paramname": "BALANCE",
			"paramvalue": "1000000"
		},
		{
			"paramname": "TYPE",
			"paramvalue": "PO"
		}
	]

}
