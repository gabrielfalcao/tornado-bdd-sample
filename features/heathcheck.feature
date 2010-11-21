# -*- coding: utf-8 -*-
Feature: Health Check
  As a deployment monitor
  I want make a health check on the application
  So that I can see if it is fine, or restart it

  Scenario: Health Check
    Given I access the URL "/_health-check"
    Then I see the response is "OK"
