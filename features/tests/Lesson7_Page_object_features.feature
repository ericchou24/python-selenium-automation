# Created by ericc at 3/6/2021
Feature: Checking Orders and Cart Page
  # Enter feature description here

Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazon home page
 When Click Amazon Orders link
 Then Verify Sign In page is opened

Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon Home Page
 When Click on cart icon
 Then Verify Your Amazon Cart is empty text present