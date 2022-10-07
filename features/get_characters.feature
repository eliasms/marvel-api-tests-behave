Feature: GET Characters

    Background:
        Given I set Marvel API url
        And I have authorization keys to authenticate myself

    Scenario Outline: Get and list chracters by characterid on Marvel API
        Given I Set GET posts api endpoint "/v1/public/characters/"
        And I set the characterId <characterId> in Path
        And I Set param request
        When Send GET HTTP request
        Then I receive valid HTTP response code 200
        And I receive character <name> returned from the request

        Examples: Characters
            | characterId | name            |
            | 1011198     | Agents of Atlas |
            | 1011297     | Agent Brand     |
            | 1011456     | Balder          |

    Scenario: Get a nonexistent character by characterid on Marvel API
        Given I Set GET posts api endpoint "/v1/public/characters/"
        And I set the characterId 9000 in Path
        And I Set param request
        When Send GET HTTP request
        Then I receive valid HTTP response code 404
        And I receive the message error "We couldn't find that character"



