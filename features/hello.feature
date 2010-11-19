# -*- coding: utf-8 -*-
Feature: Hello World to greet
  As a Greet user
  I want see a Hello World
  So that I can see it is starting

  Scenario: Basic Hello
    Given I access the URL "/"
    Then I see the response is "Hello, world"
