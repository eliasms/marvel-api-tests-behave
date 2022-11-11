Feature: GET Stories
    As a Marvel API consumer,
    I want to get stories.

    Background:
        Given I set Marvel API url
        And I have authorization keys to authenticate myself
    
    @positive
    Scenario: Get and list five stories on Marvel API
        Given I Set GET posts api endpoint "/v1/public/stories"
        And I Set param request with "limit" 5
        When Send GET HTTP request
        Then I receive valid HTTP response code 200
        And I get 5 titles returned from the request
