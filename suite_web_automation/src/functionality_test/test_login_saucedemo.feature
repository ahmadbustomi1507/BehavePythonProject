Feature: Test login feature of saucedemo

  Scenario: standard_user
      Given user successfully access login page of saucedemo
      When user fill in username "standard_user" and password "secret_sauce"
      Then  user successfully redirect to homepage
        And user will get correct image in the items

  Scenario: locked_out_user
      Given user successfully access login page of saucedemo
      When user fill in username "locked_out_user" and password "secret_sauce"
      Then  user will get message error as "Epic sadface: Sorry, this user has been locked out."

  Scenario: problem_user
      Given user successfully access login page of saucedemo
      When user fill in username "problem_user" and password "secret_sauce"
      Then  user successfully redirect to homepage
        And user will get wrong image in the items

  Scenario: performance_glitch_user
      Given user successfully access login page of saucedemo
      When user fill in username "performance_glitch_user" and password "secret_sauce"
      Then  user will redirect to homepage after timeout "5" sec

