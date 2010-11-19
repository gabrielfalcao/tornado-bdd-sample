# -*- coding: utf-8 -*-
Feature: Route my app at will
  As a tornado user
  I want to route my handlers in a easier way
  So that I can be more productive

  Scenario: Regular expression matching numbers
    Given I access the URL "/routing/numeral/0123456"
    Then I see the response is "number: 0123456"

  Scenario: Regular expression matching slugs
    Given I access the URL "/routing/slug/some-slug-here-123"
    Then I see the response is "slug: some-slug-here-123"

  Scenario: Regular expression matching anything
    Given I access the URL "/routing/anything/some-d546f7g87hyu45/@das.com/!#a$"
    Then I see the response is "some-d546f7g87hyu45/@das.com/!"
