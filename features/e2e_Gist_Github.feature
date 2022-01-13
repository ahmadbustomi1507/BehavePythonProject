
Feature: End to end gist.github
     The purpose of this scenario is end2end test, which steps are explained in the user story
     below:

     1.	As a user, I want to login to gist.github.com
     2.	As a user, I want to create a gist
     3.	As a user, I want to see the list of gists
     4.	As a user, I want to delete a gist
     5.	As a user, I want to edit a gist
     6.	As a user, I want to logout from gist.github.com

      Scenario: Create, Delete and Edit a gist
        Given User successfully open browser
        When  User open the "https://www.google.com" homepage
        When  User Sign in  using  username "username" and password "password"
        When  User create the gist, with filename "filename1", description "description" with content:
              """
                This is just a random content for automation #1
              """
        When  User create the gist, with filename "filename1", description "description" with content:
              """
                This is just a random content for automation #2
              """
        When  User check the list of gists
        When  User delete a gist, with filename "filename1"
        When  User edit a gist, with filename "filename2"
        Then  User sucessfully logout
