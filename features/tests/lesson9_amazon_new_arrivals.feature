# Created by ericc at 3/20/2021
Feature: Test for new arrivals page
  # Enter feature description here

  Scenario: Dropdown selection for an item in a different Amazon Department
    Given Open Amazon home page
    When grocery category is selected
    And Chips is searched
    Then Verify grocery department is selected


  Scenario: User can select item colors
    Given Open Amazon ProductID B074TBCSC8 page
    Then Hovers over New Arrivals
    And Verifies user sees the deals
