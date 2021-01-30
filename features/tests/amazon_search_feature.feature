# Created by ericc at 1/28/2021
Feature: Amazon Search Test
  # Enter feature description here

  Scenario: User can search for a product
  Given Open Amazon Page
  When Input Watches into Amazon search field
  And Click on Amazon search icon
  Then Product results for Watches are shown on Amazon
    # Enter steps here