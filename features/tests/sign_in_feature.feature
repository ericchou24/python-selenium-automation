# Created by ericc at 2/20/2021
Feature: Amazon Sign In Tests
  # Enter feature description here

  Scenario: Sign in page can be opened from Sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify Sign In page opens