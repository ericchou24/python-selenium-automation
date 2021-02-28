# Created by ericc at 2/26/2021
Feature: Open Amazon Application Page on Terms and Condition
  # Enter feature description here

  Scenario: User can open and close Amazon Applications
   Given Open Amazon T&C page
   When Store original windows
   And Click on Amazon applications link (*see image below)
   And Switch to the newly opened window
   Then Amazon app page is opened
   And User can close new window and switch back to original

    # Enter steps here
