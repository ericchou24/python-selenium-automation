# Created by ericc at 2/13/2021
Feature: Verify Amazon Best Sellers Links
  # Enter feature description here

  Scenario: Verify There are 5 links in Amazon Best Sellers
  Given Open Amazon Best Sellers Page
  When Verify there are five links
    # Enter steps here