# Created by ericc at 1/30/2021
Feature: Open Amazon orders
  # Enter feature description here

  Scenario: User is taken to Sign in when checking Orders
  Given Open Amazon home page
  When Orders is clicked on navigation
  Then Verify Sign in page Opened
    # Enter steps here