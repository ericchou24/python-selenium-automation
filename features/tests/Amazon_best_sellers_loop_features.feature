# Created by ericc at 2/27/2021
Feature: Loop through best sellers on Best Seller page
  # Enter feature description here

  Scenario: User is directed to correct Navigation in Best Sellers page
    Given Open Amazon Best Sellers Page
    When Verify there are five links
    Then Click through each link and verify that new page opens
    # Enter steps here