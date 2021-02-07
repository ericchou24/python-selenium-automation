# Created by ericc at 2/5/2021
Feature: Amazon Help Center Cancel Orders
  # Enter feature description here

  Scenario: User is taken to Cancel order page when submitting "Cancel Order" in Help Center
  Given Open Amazon help center page
  When Cancel Orders inputted into Help Center input page
  Then Verify correct Cancel Items or Orders page
