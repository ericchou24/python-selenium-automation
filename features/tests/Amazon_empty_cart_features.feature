# Created by ericc at 2/6/2021
Feature: Open Amazon Cart
  # Enter feature description here

  Scenario: User sees empty cart when cart button is clicked
  Given Opens Amazon Home page
  When Cart is clicked on navigation
  Then Verify Cart is empty
    # Enter steps here