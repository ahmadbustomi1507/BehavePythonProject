
Feature: End to end gist.github
     The purpose of this scenario is end2end test, which steps are explained in the user story
     below:

     1.	As a user, I want to login to gist.github.com
     2.	As a user, I want to create a gist
     3.	As a user, I want to see the list of gists
     4.	As a user, I want to delete a gist
     5.	As a user, I want to edit a gist
     6.	As a user, I want to logout from gist.github.com

      Scenario: Sign in Gist
        Given User successfully open browser
        When  User access the website "https://gist.github.com/"
        When  User Sign in  using  username "enter username" and password "enter password"
        Then  User successfully login

      Scenario: Create Gist
        Given User successfully login
        When User check the list of the gist that has been created
        When  User create the gist, with filename "filename1", description "description" with content:
              """
                This is just a random content for automation #1
              """
        Then  New Gist has been created

      Scenario: Edit Gist
        Given User successfully login
        When User check the list of the gist that has been created
        When User choose one of the gist to edit "i edit this"
        Then The Gist has been edited

     Scenario: Delete Gist
       Given User successfully login
       When User check the list of the gist that has been created
       When User choose one of the gist to delete
       Then The gist has been deleted

     Scenario: Sign out from Gist
       Given User successfully login
       When User sign out from the web
       Then User successfully logout
