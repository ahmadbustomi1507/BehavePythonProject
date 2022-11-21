Feature: Sample API test from mock api

    This is a test to check if the backend return correct
    registered users
    path : /api/v1/users

  @regression @test_1
  Scenario: Get user data
    Given user have an access to the API
    When user send request with payload
        """
        {
          "property_1":12346,
          "property_2": true,
          "property_3":"this is a value of property 3"
        }
        """
    Then user will get response status code "200"
    And user get list of the users

