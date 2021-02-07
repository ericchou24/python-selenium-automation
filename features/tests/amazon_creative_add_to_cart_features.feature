# Created by ericc at 2/6/2021
Feature: Open and Add items into Amazon cart

  Scenario: User can add and verify item is in cart
  Given Open Amazon Product search page
  When Input Legos into search page and enter
  And Add first result into cart
  Then Verify item is in cart
    # Enter steps here