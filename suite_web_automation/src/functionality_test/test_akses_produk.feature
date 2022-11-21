Feature: i want to access list produk from shipper
  as user i want to make sure to see shipper have 4 main product
  in the mainpage, as below:
  1. Aggregator Logistik Domestik
  2. Aggregator Logistik Internasional
  3. Manajemen Pergudangan
  4. Atoor by Shipper

  Scenario: clicking dropdown "Produk"
    Given user is in homepage
    When user click produk
    Then user will see 4 main products

    When user click "Aggregator Logistik Domestik"
    Then user will be redirected to shipping page

    When user back to previous page
    And user click "Aggregator Logistik Internasional"
    Then user will be redirected to international shipping page

    When user back to previous page
    And user click "Manajemen Pergudangan""
    Then user will be redirected to warehouse page

    When user back to previous page
    And user click "Atoor by Shipper""
    Then user will be redirected to atoor page



